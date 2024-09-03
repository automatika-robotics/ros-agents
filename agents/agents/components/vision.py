from typing import Any, Union, Optional

from ..models import VisionModel

from ..clients.model_base import ModelClient
from ..config import VisionConfig
from ..ros import Detections, FixedInput, Image, Topic, Trackings
from ..utils import validate_func_args
from .model_component import ModelComponent


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
        inputs: list[Union[Topic, FixedInput]],
        outputs: list[Topic],
        model_client: ModelClient,
        config: Optional[VisionConfig] = None,
        trigger: Union[Topic, list[Topic], float] = 1,
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
            config,
            trigger,
            callback_group,
            component_name,
            **kwargs,
        )
        # check for correct model and setup number of trackers to be initialized if any
        if self.model_client and not isinstance(self.model_client.model, VisionModel):
            raise TypeError(
                "A vision component can only be started with a Vision Model"
            )
        if self.model_client.model.setup_trackers:  # type: ignore
            model_client.model._num_trackers = len(inputs)

    def _create_input(self, *_, **kwargs) -> Optional[dict[str, Any]]:
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
