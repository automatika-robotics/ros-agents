from abc import abstractmethod
import inspect
from typing import Any, Optional, Sequence, Union

from ..clients.model_base import ModelClient
from ..config import BaseComponentConfig
from ..ros import FixedInput, Topic, SupportedType
from .component_base import Component


class ModelComponent(Component):
    """ModelComponent."""

    def __init__(
        self,
        inputs: Optional[Sequence[Union[Topic, FixedInput]]] = None,
        outputs: Optional[Sequence[Topic]] = None,
        model_client: Optional[ModelClient] = None,
        config: Optional[BaseComponentConfig] = None,
        trigger: Union[Topic, list[Topic], float] = 1.0,
        callback_group=None,
        component_name: str = "model_component",
        **kwargs,
    ):
        # setup model client
        self.model_client = model_client if model_client else None
        self.handled_outputs: list[type[SupportedType]]

        # Initialize Component
        super().__init__(
            inputs,
            outputs,
            config,
            trigger,
            callback_group,
            component_name,
            **kwargs,
        )

    def activate(self):
        """
        Create required subscriptions, publications, timers and initilize a model if provided.
        """
        self.get_logger().debug(f"Current Status: {self.health_status.value}")

        # validate output topics if handled_outputs exist
        self.get_logger().info("Validating Model Component Output Topics")
        self._validate_output_topics()

        # Initialize model
        if self.model_client:
            self.model_client.check_connection()
            self.model_client.initialize()

        # Activate component
        super().activate()

    def deactivate(self):
        """
        Destroy all declared subscriptions, publications, timers, ... etc. to deactivate the node
        """
        # deactivate component
        super().deactivate()

        # Deinitialize model
        if self.model_client:
            self.model_client.check_connection()
            self.model_client.deinitialize()

    def _validate_output_topics(self) -> None:
        """
        Verify that output topics that are not handled, have pre-processing functions provided
        """

        if hasattr(self, "publishers_dict") and hasattr(self, "handled_outputs"):
            for name, pub in self.publishers_dict.items():
                if pub.output_topic.msg_type not in self.handled_outputs and (
                    not pub._pre_processors
                ):
                    func_body = inspect.getsource(pub.output_topic.msg_type.convert)
                    raise TypeError(f"""{type(self).__name__} components can only handle output topics of type(s) {self.handled_outputs} automatically. {name} is of type {pub.output_topic.msg_type}. Please provide a pre-processing function for this topic and attach it to the topic by calling the `add_publisher_preprocessor` on the component {self.node_name}. Make sure the output of the pre-processor function can be passed as parameter output to the following function:
{func_body}""")

    @abstractmethod
    def _create_input(self, *args, **kwargs) -> Union[dict[str, Any], None]:
        """_create_input.

        :param args:
        :param kwargs:
        :rtype: dict[str, Any] | None
        """
        raise NotImplementedError(
            "This method needs to be implemented by child components."
        )

    @abstractmethod
    def _execution_step(self, *args, **kwargs):
        """_execution_step.

        :param args:
        :param kwargs:
        """
        raise NotImplementedError(
            "This method needs to be implemented by child components."
        )
