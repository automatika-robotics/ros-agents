from abc import abstractmethod
from copy import deepcopy
from typing import Optional, Sequence, Union, List, Dict

from ..callbacks import GenericCallback
from ..ros import (
    BaseComponent,
    ComponentRunType,
    FixedInput,
    SupportedType,
    Topic,
)
from ..config import ComponentConfig


class Component(BaseComponent):
    """Component."""

    def __init__(
        self,
        inputs: Optional[Sequence[Union[Topic, FixedInput]]] = None,
        outputs: Optional[Sequence[Topic]] = None,
        config: Optional[ComponentConfig] = None,
        trigger: Union[Topic, List[Topic], float] = 1.0,
        callback_group=None,
        component_name: str = "agents_component",
        **kwargs,
    ):
        self.config: ComponentConfig = deepcopy(config) if config else ComponentConfig()  # type: ignore
        self.allowed_inputs: Dict[str, List[type[SupportedType]]]
        self.allowed_outputs: Dict[str, List[type[SupportedType]]]

        # setup inputs and outputs
        if inputs:
            self.validate_topics(inputs)

        if outputs:
            self.validate_topics(outputs)

        # Initialize Parent Component
        super().__init__(
            component_name=component_name,
            inputs=inputs,
            outputs=outputs,
            config=self.config,
            callback_group=callback_group,
            enable_health_broadcast=False,
            **kwargs,
        )

        # setup component run type and triggers
        self.trigger(trigger)

    def activate(self):
        """
        Create required subscriptions, publications and timers.
        """
        # Setup trigger based callback or frequency based timer
        if self.run_type is ComponentRunType.EVENT:
            self.create_component_triggers()

        super().activate()

    def __add_subscriber_to_callback(self, callback: GenericCallback) -> None:
        # Creates subscriber and attaches it to input callback object
        callback.set_node_name(self.node_name)
        if hasattr(callback.input_topic, "fixed"):
            self.get_logger().debug(
                f"Fixed input specified for topic: {callback.input_topic} of type {callback.input_topic.msg_type}"
            )
        else:
            callback.set_subscriber(self._add_ros_subscriber(callback))

    def create_all_subscribers(self):
        """
        Override to handle fixed inputs
        """
        self.get_logger().info("STARTING ALL SUBSCRIBERS")
        # Create subscribers
        for callback in self.callbacks.values():
            self.__add_subscriber_to_callback(callback)

    def _add_callback_to_trigger(self, trig_name: str) -> None:
        callback = self.callbacks[trig_name]
        self.trig_callbacks[trig_name] = callback
        # remove trigger inputs from in_topics
        del self.callbacks[trig_name]
        self.__add_subscriber_to_callback(callback)
        # Add execution step of the node as a post callback function
        callback.on_callback_execute(self._execution_step)

    def create_component_triggers(self) -> None:
        """
        Creates component triggers for events specified as triggers
        """
        self.get_logger().info("STARTING SUBSCRIBERS FOR TRIGGER TOPICS")
        self.trig_callbacks = {}
        if isinstance(self.config._trigger, list):
            for t in self.config._trigger:
                self._add_callback_to_trigger(t)
        elif isinstance(self.config._trigger, str):
            self._add_callback_to_trigger(self.config._trigger)

    def destroy_all_subscribers(self) -> None:
        """
        Destroys all node subscribers
        """
        self.get_logger().info("DESTROYING ALL SUBSCRIBERS")
        all_callbacks = (
            self.callbacks.values()
            if self.run_type is not ComponentRunType.EVENT
            else list(self.callbacks.values()) + list(self.trig_callbacks.values())
        )
        for callback in all_callbacks:
            if callback._subscriber:
                self.destroy_subscription(callback._subscriber)

    def trigger(self, trigger: Union[Topic, List[Topic], float]) -> None:
        """
        Set component trigger
        """
        if isinstance(trigger, list):
            triggers = []
            for t in trigger:
                if t.name not in self.callbacks:
                    raise TypeError(
                        f"Invalid configuration for component trigger {t.name} - A trigger needs to be one of the inputs already defined in component inputs."
                    )
                triggers.append(t.name)
            self.config.run_type = ComponentRunType.EVENT
            self.config._trigger = triggers

        elif isinstance(trigger, Topic):
            if trigger.name not in self.callbacks:
                raise TypeError(
                    f"Invalid configuration for component trigger {trigger.name} - A trigger needs to be one of the inputs already defined in component inputs."
                )
            self.run_type = ComponentRunType.EVENT
            self.config._trigger = trigger.name

        else:
            self.run_type = ComponentRunType.TIMED
            # Set component loop_rate (Hz)
            self.config.loop_rate = 1 / trigger

    def validate_topics(
        self,
        topics: Sequence[Union[Topic, FixedInput]],
        allowed_topics: Optional[Dict[str, List[type[SupportedType]]]] = None,
        topics_direction: str = "Topics",
    ):
        """
        Verify component specific inputs or outputs using allowed topics if provided
        """
        # type validation
        correct_type = all(isinstance(i, (Topic, FixedInput)) for i in topics)
        if not correct_type:
            raise TypeError(
                f"{topics_direction} to a component can only be of type Topic"
            )

        # message type validation based on allowed types
        if not allowed_topics:
            return

        all_msg_types = [topic.msg_type for topic in topics]
        all_topics_types = allowed_topics["Required"] + (
            allowed_topics.get("Optional") or []
        )
        correct_topics = all(
            allowed_t in all_msg_types for allowed_t in allowed_topics["Required"]
        )
        correct_msgtypes = all(
            msg_type in all_topics_types for msg_type in all_msg_types
        )
        if not correct_topics:
            raise TypeError(
                f"The component should be given at least one input of each datatype: {allowed_topics['Required']}"
            )
        if not correct_msgtypes:
            raise TypeError(
                f"{topics_direction} to the component can only be of the allowed datatypes: {all_topics_types}"
            )

    @abstractmethod
    def _execution_step(self, **kwargs):
        """_execution_step.

        :param args:
        :param kwargs:
        """
        raise NotImplementedError(
            "This method needs to be implemented by child components."
        )
