from typing import Any, Union, Optional

from ..clients.model_base import ModelClient
from ..config import MLLMConfig
from ..ros import FixedInput, Image, String, Topic, Detections
from ..utils import validate_func_args
from .llm import LLM


class MLLM(LLM):
    """
    This component utilizes multi-modal large language models (e.g. Llava) that can be used to process text and image data.

    :param inputs: The input topics or fixed inputs for the MLLM component.
        This should be a list of Topic objects or FixedInput instances, limited to String and Image types.
    :type inputs: list[Topic | FixedInput]
    :param outputs: The output topics for the MLLM component.
        This should be a list of Topic objects. String type is handled automatically.
    :type outputs: list[Topic]
    :param model_client: The model client for the MLLM component.
        This should be an instance of ModelClient.
    :type model_client: ModelClient
    :param config: Optional configuration for the MLLM component.
        This should be an instance of MLLMConfig. If not provided, defaults to MLLMConfig().
    :type config: MLLMConfig
    :param trigger: The trigger value or topic for the MLLM component.
        This can be a single Topic object, a list of Topic objects, or a float value for a timed component. Defaults to 1.
    :type trigger: Union[Topic, list[Topic], float]
    :param callback_group: An optional callback group for the MLLM component.
        If provided, this should be a string. Otherwise, it defaults to None.
    :type callback_group: str
    :param component_name: The name of the MLLM component.
        This should be a string and defaults to "mllm_component".
    :type component_name: str

    Example usage:
    ```python
    text0 = Topic(name="text0", msg_type="String")
    image0 = Topic(name="image0", msg_type="Image")
    text0 = Topic(name="text1", msg_type="String")
    config = MLLMConfig()
    model = TransformersMLLM(name='idefics')
    model_client = ModelClient(model=model)
    mllm_component = MLLM(inputs=[text0, image0],
                          outputs=[text1],
                          model_client=model_client,
                          config=config,
                          component_name='mllm_component')
    ```
    """

    @validate_func_args
    def __init__(
        self,
        *,
        inputs: list[Union[Topic, FixedInput]],
        outputs: list[Topic],
        model_client: ModelClient,
        config: Optional[MLLMConfig] = None,
        trigger: Union[Topic, list[Topic], float] = 1,
        callback_group=None,
        component_name: str = "mllm_component",
        **kwargs,
    ):
        self.allowed_inputs = {"Required": [String, Image], "Optional": [Detections]}

        config = MLLMConfig() or config

        super().__init__(
            inputs=inputs,
            outputs=outputs,
            model_client=model_client,
            config=config,
            trigger=trigger,
            callback_group=callback_group,
            component_name=component_name,
            allowed_inputs=self.allowed_inputs,
            **kwargs,
        )

    def _create_input(self, *_, **kwargs) -> Optional[dict[str, Any]]:
        """Create inference input for MLLM models
        :param args:
        :param kwargs:
        :rtype: dict[str, Any]
        """
        images = []
        # context dict to gather all String inputs for use in system prompt
        context = {}
        # set mllm query as trigger
        if trigger := kwargs.get("topic"):
            query = self.trig_callbacks[trigger.name].get_output()
            context[trigger.name] = query

            # handle chat reset
            if self.chat_history and query.lower() == self.config.history_reset_phrase:
                self.chat_history = []
                return None

        else:
            query = None

        # aggregate all inputs that are available
        for i in self.callbacks.values():
            if (item := i.get_output()) is not None:
                # set trigger equal to a topic with type String if trigger not found
                if i.input_topic.msg_type is String:
                    if not query:
                        query = item
                    context[i.input_topic.name] = item
                elif i.input_topic.msg_type is Detections:
                    context[i.input_topic.name] = item
                # get images from image topics
                if i.input_topic.msg_type == Image:
                    images.append(item)

        if not query or not images:
            return None

        # set system prompt template
        query = (
            self._component_template.render(context)
            if self._component_template
            else query
        )
        # add rag docs to query if enabled in config and if docs retreived
        query = self._make_rag_query(query) if self.config.enable_rag else query

        message = {"role": "user", "content": query}

        messages = self._handle_chat_history(message)

        self.get_logger().debug(f"Input from component: {messages}")

        return {
            "query": messages,
            "images": images,
            **self.config._get_inference_params(),
        }
