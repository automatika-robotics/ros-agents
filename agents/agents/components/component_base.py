from abc import abstractmethod
from copy import deepcopy
from typing import Callable, Optional, Sequence, Union

from ..ros import (
    BaseComponent,
    ComponentRunType,
    FixedInput,
    SupportedType,
    Topic,
)
from ..callbacks import GenericCallback
from ..config import BaseComponentConfig
from ..publisher import Publisher


class Component(BaseComponent):
    """Component."""

    def __init__(
        self,
        inputs: Optional[Sequence[Union[Topic, FixedInput]]] = None,
        outputs: Optional[Sequence[Topic]] = None,
        config: Optional[BaseComponentConfig] = None,
        trigger: Union[Topic, list[Topic], float] = 1.0,
        callback_group=None,
        component_name: str = "leibniz_component",
        **kwargs,
    ):
        self.config = deepcopy(config) if config else BaseComponentConfig()
        self.allowed_inputs: dict[str, list[type[SupportedType]]]
        self.allowed_outputs: dict[str, list[type[SupportedType]]]

        # setup inputs and outputs
        if inputs:
            self.inputs(inputs)

        if outputs:
            self.outputs(outputs)

        # setup component run type and triggers
        self.trigger(trigger)

        # Initialize Node
        super().__init__(
            component_name,
            self.config,
            callback_group,
            enable_health_broadcast=False,
            **kwargs,
        )

    def activate(self):
        """
        Create required subscriptions, publications and timers.
        """
        # Setup trigger based callback or frequency based timer
        if self.run_type is ComponentRunType.EVENT:
            self.create_component_triggers()

        super().activate()

    def create_all_subscribers(self):
        """
        Creates all node subscribers from component inputs
        """
        self.get_logger().info("STARTING ALL SUBSCRIBERS")
        if hasattr(self, "callbacks"):
            # Create subscribers
            for callback in self.callbacks.values():
                # Creates subscriber and attaches it to input callback object
                callback.set_node_name(self.node_name)
                if hasattr(callback.input_topic, "fixed"):
                    self.get_logger().debug(
                        f"Fixed input specified for topic: {callback.input_topic} of type {callback.input_topic.msg_type}"
                    )
                else:
                    callback.set_subscriber(self._add_ros_subscriber(callback))
        super().create_all_subscribers()

    def create_all_publishers(self):
        """
        Creates all node publishers from component outputs
        """
        self.get_logger().info("STARTING ALL PUBLISHERS")
        if hasattr(self, "publishers_dict"):
            # Create publisher and attach it to output publisher object
            for publisher in self.publishers_dict.values():
                publisher.set_node_name(self.node_name)
                # Set ROS publisher for each output publisher
                publisher = publisher.set_publisher(self._add_ros_publisher(publisher))
        # create publishers for the base component (used for health broadcast)
        super().create_all_publishers()

    def create_component_triggers(self):
        """
        Creates component triggers for events specified as triggers
        """
        self.get_logger().info("STARTING SUBSCRIBERS FOR TRIGGER TOPICS")
        if hasattr(self, "trig_callbacks"):
            for callback in self.trig_callbacks.values():
                # Creates subscriber and attaches a callback object to the input
                callback.set_node_name(self.node_name)
                if hasattr(callback.input_topic, "fixed"):
                    self.get_logger().debug(
                        f"Fixed input specified for topic: {callback.input_topic} of type {callback.input_topic.msg_type}"
                    )
                else:
                    callback.set_subscriber(self._add_ros_subscriber(callback))
                # Add execution step of the node as a post callback function
                callback.on_callback_execute(self._execution_step)

    def destroy_all_subscribers(self):
        """
        Destroys all node subscribers
        """
        self.get_logger().info("DESTROYING ALL SUBSCRIBERS")
        if hasattr(self, "callbacks"):
            all_callbacks = (
                self.callbacks.values()
                if self.run_type is not ComponentRunType.EVENT
                else list(self.callbacks.values()) + list(self.trig_callbacks.values())
            )
            for callback in all_callbacks:
                if callback._subscriber:
                    self.destroy_subscription(callback._subscriber)
        super().destroy_all_subscribers()

    def destroy_all_publishers(self):
        """
        Destroys all node publishers
        """
        self.get_logger().info("DESTROYING ALL PUBLISHERS")
        if hasattr(self, "publishers_dict"):
            for publisher in self.publishers_dict.values():
                if publisher._publisher:
                    self.destroy_publisher(publisher._publisher)
        # destroy publishers in parent, if they exist
        super().destroy_all_publishers()

    def _add_ros_subscriber(self, callback: GenericCallback):
        """Creates a subscriber to be attached to an input message.

        :param msg:
        :type msg: Input
        :param callback:
        :type callback: GenericCallback
        """
        _subscriber = self.create_subscription(
            msg_type=callback.input_topic.ros_msg_type,
            topic=callback.input_topic.name,
            qos_profile=self.setup_qos(callback.input_topic.qos_profile),
            callback=callback.callback,
            callback_group=self.callback_group,
        )
        self.get_logger().debug(
            f"Started subscriber to topic: {callback.input_topic.name} of type {callback.input_topic.msg_type}"
        )
        return _subscriber

    def _add_ros_publisher(self, publisher: Publisher):
        """
        Sets the publisher attribute of a component for a given Topic
        """
        qos_profile = self.setup_qos(publisher.output_topic.qos_profile)
        return self.create_publisher(
            publisher.output_topic.ros_msg_type,
            publisher.output_topic.name,
            qos_profile,
        )

    def inputs(self, inputs: Sequence[Union[Topic, FixedInput]]):
        """
        Set component input streams (topics)
        """
        self.validate_topics(inputs, self.allowed_inputs, "Inputs")
        self.callbacks = {
            input.name: input.msg_type.callback(input) for input in inputs
        }

    def outputs(self, outputs: Sequence[Topic]):
        """
        Set component output streams (topics)
        """
        if hasattr(self, "allowed_outputs"):
            self.validate_topics(outputs, self.allowed_outputs, "Outputs")
        self.publishers_dict = {output.name: Publisher(output) for output in outputs}

    def trigger(self, trigger: Union[Topic, list[Topic], float]) -> None:
        """
        Set component trigger
        """
        if isinstance(trigger, list):
            for t in trigger:
                if t.name not in self.callbacks:
                    raise TypeError(
                        f"Invalid configuration for component trigger {t.name} - A trigger needs to be one of the inputs already defined in component inputs."
                    )
            self.run_type = ComponentRunType.EVENT
            self.trig_callbacks = {}
            for t in trigger:
                self.trig_callbacks[t.name] = self.callbacks[t.name]
                # remove trigger inputs from in_topics
                del self.callbacks[t.name]

        elif isinstance(trigger, Topic):
            if trigger.name not in self.callbacks:
                raise TypeError(
                    f"Invalid configuration for component trigger {trigger.name} - A trigger needs to be one of the inputs already defined in component inputs."
                )
            self.run_type = ComponentRunType.EVENT
            self.trig_callbacks = {trigger.name: self.callbacks[trigger.name]}
            del self.callbacks[trigger.name]

        else:
            self.run_type = ComponentRunType.TIMED
            # Set component loop_rate (Hz)
            self.config.loop_rate = 1 / trigger

    def validate_topics(
        self,
        topics: Sequence[Union[Topic, FixedInput]],
        allowed_topics: Optional[dict[str, list[type[SupportedType]]]] = None,
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

    def got_all_inputs(self) -> bool:
        """
        Check if all input topics are being published
        :return: If all inputs are published
        :rtype: bool
        """
        # Check if all callbacks of the selected topics got input messages
        if not self.callbacks:
            return False
        for callback in self.callbacks.values():
            if not callback.get_output():
                return False
        return True

    def get_missing_inputs(self) -> Union[list[str], None]:
        """
        Get a list of input topic names not being published
        :return: List of unpublished topics
        :rtype: list[str]
        """
        unpublished_topics = []
        if not self.callbacks:
            return None
        for callback in self.callbacks.values():
            if not callback.get_output():
                unpublished_topics.append(callback.input_topic.name)
        return unpublished_topics

    @abstractmethod
    def _execution_step(self, **kwargs):
        """_execution_step.

        :param args:
        :param kwargs:
        """
        raise NotImplementedError(
            "This method needs to be implemented by child components."
        )

    def attach_custom_callback(self, input_topic: Topic, callable: Callable) -> None:
        """
        Method to attach custom method to subscriber callbacks
        """
        if not callable(callable):
            raise TypeError("A custom callback must be a Callable")
        if callback := self.callbacks.get(input_topic.name):
            if not callback:
                raise TypeError("Specified input topic does not exist")
            callback.on_callback_execute(callable)

    def add_callback_postprocessor(self, input_topic: Topic, func: Callable) -> None:
        """Adds a callable as a post processor for topic callback.
        :param input_topic:
        :type input_topic: Topic
        :param callable:
        :type func: Callable
        """
        if not callable(callable):
            raise TypeError(
                "A postprocessor must be a Callable with input and output types the same as the topic."
            )
        if callback := self.callbacks.get(input_topic.name):
            if not callback:
                raise TypeError("Specified input topic does not exist")
            callback.add_post_processor(func)

    def add_publisher_preprocessor(self, output_topic: Topic, func: Callable) -> None:
        """Adds a callable as a pre processor for topic publisher.
        :param output_topic:
        :type output_topic: Topic
        :param callable:
        :type func: Callable
        """
        if not callable(callable):
            raise TypeError(
                "A preprocessor must be a Callable with input and output types the same as the topic."
            )
        if self.publishers_dict:
            if publisher := self.publishers_dict.get(output_topic.name):
                if not publisher:
                    raise TypeError("Specified output topic does not exist")
                publisher.add_pre_processor(func)
        else:
            raise TypeError(
                "The component does not have any output topics specified. Add output topics with Component.outputs method"
            )
