from typing import Any, Union, Optional, List, Dict

from ..clients.model_base import ModelClient
from ..config import VisionConfig
from ..ros import Detections, FixedInput, Image, Topic, Trackings
from ..utils import validate_func_args
from .model_component import ModelComponent
from .component_base import ComponentRunType


class Vision(ModelComponent):
    """
    This component performs object detection and tracking on input images and outputs a list of detected objects, along with their bounding boxes and confidence scores.

    :param inputs: The input topics for the object detection.
        This should be a list of Topic objects or FixedInput objects, limited to Image type.
    :type inputs: list[Union[Topic, FixedInput]]
    :param outputs: The output topics for the object detection.
        This should be a list of Topic objects, Detection and Tracking types are handled automatically.
    :type outputs: list[Topic]
    :param model_client: The model client for the vision component.
        This should be an instance of ModelClient.
    :type model_client: ModelClient
    :param config: The configuration for the vision component.
        This should be an instance of VisionConfig. If not provided, defaults to VisionConfig().
    :type config: VisionConfig
    :param trigger: The trigger value or topic for the vision component.
        This can be a single Topic object, a list of Topic objects, or a float value for timed components.
    :type trigger: Union[Topic, list[Topic], float]
    :param callback_group: An optional callback group for the vision component.
        If provided, this should be a string. Otherwise, it defaults to None.
    :type callback_group: str
    :param component_name: The name of the vision component.
        This should be a string and defaults to "vision_component".
    :type component_name: str

    Example usage:
    ```python
    image_topic = Topic(name="image", msg_type="Image")
    detections_topic = Topic(name="detections", msg_type="Detections")
    config = VisionConfig()
    model_client = ModelClient(model=DetectionModel(name='yolov5'))
    vision_component = Vision(
        inputs=[image_topic],
        outputs=[detections_topic],
        model_client=model_client
        config=config,
    )
    ```
    """

    @validate_func_args
    def __init__(
        self,
        *,
        inputs: List[Union[Topic, FixedInput]],
        outputs: List[Topic],
        model_client: ModelClient,
        config: Optional[VisionConfig] = None,
        trigger: Union[Topic, List[Topic], float] = 1.0,
        callback_group=None,
        component_name: str = "vision_component",
        **kwargs,
    ):
        self.config: VisionConfig = config or VisionConfig()
        self.allowed_inputs = {"Required": [Image]}
        self.handled_outputs = [Detections, Trackings]

        super().__init__(
            inputs,
            outputs,
            model_client,
            self.config,
            trigger,
            callback_group,
            component_name,
            **kwargs,
        )
        # check for correct model and setup number of trackers to be initialized if any
        if model_client.model_type != "VisionModel":
            raise TypeError(
                "A vision component can only be started with a Vision Model"
            )
        if hasattr(model_client, "_model") and self.model_client._model.setup_trackers:  # type: ignore
            model_client._model._num_trackers = len(inputs)

    def _create_input(self, *_, **kwargs) -> Optional[Dict[str, Any]]:
        """Create inference input for ObjectDetection models
        :param args:
        :param kwargs:
        :rtype: dict[str, Any]
        """
        # set one image topic as query for event based trigger
        if trigger := kwargs.get("topic"):
            images = [self.trig_callbacks[trigger.name].get_output()]
        else:
            images = []

            for i in self.callbacks.values():
                if (item := i.get_output()) is not None:
                    images.append(item)

        if not images:
            return None

        return {"images": images, **self.config._get_inference_params()}

    def _execution_step(self, *args, **kwargs):
        """_execution_step.

        :param args:
        :param kwargs:
        """

        if self.run_type is ComponentRunType.EVENT:
            trigger = kwargs.get("topic")
            if not trigger:
                return
            self.get_logger().info(f"Received trigger on topic {trigger.name}")
        else:
            time_stamp = self.get_ros_time().sec
            self.get_logger().info(f"Sending at {time_stamp}")

        # create inference input
        inference_input = self._create_input(*args, **kwargs)
        # call model inference
        if not inference_input:
            self.get_logger().warning("Input not received, not calling model inference")
            return

        # conduct inference
        if self.model_client:
            result = self.model_client.inference(inference_input)
            # raise a fallback trigger via health status
            if not result:
                self.health_status.set_failure()
            else:
                # publish inference result
                if result["output"] and hasattr(self, "publishers_dict"):
                    for publisher in self.publishers_dict.values():
                        publisher.publish(
                            **result,
                            frame_id=self.trig_callbacks[trigger.name].frame_id,
                            time_stamp=self.get_ros_time(),
                        )
