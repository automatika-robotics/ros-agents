---
orphan: true
---

# {py:mod}`agents.components.llm`

```{py:module} agents.components.llm
```

```{autodoc2-docstring} agents.components.llm
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`LLM <agents.components.llm.LLM>`
  - ```{autodoc2-docstring} agents.components.llm.LLM
    :summary:
    ```
````

### API

`````{py:class} LLM(*, inputs: list[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], outputs: list[agents.ros.Topic], model_client: agents.clients.model_base.ModelClient, config: typing.Optional[agents.config.LLMConfig] = None, db_client: typing.Optional[agents.clients.db_base.DBClient] = None, trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float] = 1, callback_group=None, component_name: str = 'llm_component', **kwargs)
:canonical: agents.components.llm.LLM

Bases: {py:obj}`agents.components.model_component.ModelComponent`

```{autodoc2-docstring} agents.components.llm.LLM
```

````{py:method} activate()
:canonical: agents.components.llm.LLM.activate

```{autodoc2-docstring} agents.components.llm.LLM.activate
```

````

````{py:method} deactivate()
:canonical: agents.components.llm.LLM.deactivate

```{autodoc2-docstring} agents.components.llm.LLM.deactivate
```

````

````{py:method} add_documents(ids: list[str], metadatas: list[dict], documents: list[str]) -> None
:canonical: agents.components.llm.LLM.add_documents

```{autodoc2-docstring} agents.components.llm.LLM.add_documents
```

````

````{py:method} set_topic_prompt(input_topic: agents.ros.Topic, template: typing.Union[str, pathlib.Path]) -> None
:canonical: agents.components.llm.LLM.set_topic_prompt

```{autodoc2-docstring} agents.components.llm.LLM.set_topic_prompt
```

````

````{py:method} set_component_prompt(template: typing.Union[str, pathlib.Path]) -> None
:canonical: agents.components.llm.LLM.set_component_prompt

```{autodoc2-docstring} agents.components.llm.LLM.set_component_prompt
```

````

````{py:method} create_all_subscribers()
:canonical: agents.components.llm.LLM.create_all_subscribers

```{autodoc2-docstring} agents.components.llm.LLM.create_all_subscribers
```

````

````{py:method} create_all_publishers()
:canonical: agents.components.llm.LLM.create_all_publishers

```{autodoc2-docstring} agents.components.llm.LLM.create_all_publishers
```

````

````{py:method} create_component_triggers()
:canonical: agents.components.llm.LLM.create_component_triggers

```{autodoc2-docstring} agents.components.llm.LLM.create_component_triggers
```

````

````{py:method} destroy_all_subscribers()
:canonical: agents.components.llm.LLM.destroy_all_subscribers

```{autodoc2-docstring} agents.components.llm.LLM.destroy_all_subscribers
```

````

````{py:method} destroy_all_publishers()
:canonical: agents.components.llm.LLM.destroy_all_publishers

```{autodoc2-docstring} agents.components.llm.LLM.destroy_all_publishers
```

````

````{py:method} inputs(inputs: typing.Sequence[typing.Union[agents.ros.Topic, agents.ros.FixedInput]])
:canonical: agents.components.llm.LLM.inputs

```{autodoc2-docstring} agents.components.llm.LLM.inputs
```

````

````{py:method} outputs(outputs: typing.Sequence[agents.ros.Topic])
:canonical: agents.components.llm.LLM.outputs

```{autodoc2-docstring} agents.components.llm.LLM.outputs
```

````

````{py:method} trigger(trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float]) -> None
:canonical: agents.components.llm.LLM.trigger

```{autodoc2-docstring} agents.components.llm.LLM.trigger
```

````

````{py:method} validate_topics(topics: typing.Sequence[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], allowed_topics: typing.Optional[dict[str, list[type[agents.ros.SupportedType]]]] = None, topics_direction: str = 'Topics')
:canonical: agents.components.llm.LLM.validate_topics

```{autodoc2-docstring} agents.components.llm.LLM.validate_topics
```

````

````{py:method} got_all_inputs() -> bool
:canonical: agents.components.llm.LLM.got_all_inputs

```{autodoc2-docstring} agents.components.llm.LLM.got_all_inputs
```

````

````{py:method} get_missing_inputs() -> typing.Union[list[str], None]
:canonical: agents.components.llm.LLM.get_missing_inputs

```{autodoc2-docstring} agents.components.llm.LLM.get_missing_inputs
```

````

````{py:method} attach_custom_callback(input_topic: agents.ros.Topic, callable: typing.Callable) -> None
:canonical: agents.components.llm.LLM.attach_custom_callback

```{autodoc2-docstring} agents.components.llm.LLM.attach_custom_callback
```

````

````{py:method} add_callback_postprocessor(input_topic: agents.ros.Topic, func: typing.Callable) -> None
:canonical: agents.components.llm.LLM.add_callback_postprocessor

```{autodoc2-docstring} agents.components.llm.LLM.add_callback_postprocessor
```

````

````{py:method} add_publisher_preprocessor(output_topic: agents.ros.Topic, func: typing.Callable) -> None
:canonical: agents.components.llm.LLM.add_publisher_preprocessor

```{autodoc2-docstring} agents.components.llm.LLM.add_publisher_preprocessor
```

````

````{py:method} create_all_timers()
:canonical: agents.components.llm.LLM.create_all_timers

```{autodoc2-docstring} agents.components.llm.LLM.create_all_timers
```

````

````{py:method} create_all_action_servers()
:canonical: agents.components.llm.LLM.create_all_action_servers

```{autodoc2-docstring} agents.components.llm.LLM.create_all_action_servers
```

````

````{py:method} create_all_services()
:canonical: agents.components.llm.LLM.create_all_services

```{autodoc2-docstring} agents.components.llm.LLM.create_all_services
```

````

````{py:method} destroy_all_timers()
:canonical: agents.components.llm.LLM.destroy_all_timers

```{autodoc2-docstring} agents.components.llm.LLM.destroy_all_timers
```

````

````{py:method} destroy_all_services()
:canonical: agents.components.llm.LLM.destroy_all_services

```{autodoc2-docstring} agents.components.llm.LLM.destroy_all_services
```

````

````{py:method} destroy_all_action_servers()
:canonical: agents.components.llm.LLM.destroy_all_action_servers

```{autodoc2-docstring} agents.components.llm.LLM.destroy_all_action_servers
```

````

````{py:method} configure(config_file: str)
:canonical: agents.components.llm.LLM.configure

```{autodoc2-docstring} agents.components.llm.LLM.configure
```

````

````{py:method} rclpy_init_node(*args, **kwargs)
:canonical: agents.components.llm.LLM.rclpy_init_node

```{autodoc2-docstring} agents.components.llm.LLM.rclpy_init_node
```

````

````{py:property} run_type
:canonical: agents.components.llm.LLM.run_type
:type: ros_sugar.config.ComponentRunType

```{autodoc2-docstring} agents.components.llm.LLM.run_type
```

````

````{py:property} fallback_rate
:canonical: agents.components.llm.LLM.fallback_rate
:type: float

```{autodoc2-docstring} agents.components.llm.LLM.fallback_rate
```

````

````{py:property} loop_rate
:canonical: agents.components.llm.LLM.loop_rate
:type: float

```{autodoc2-docstring} agents.components.llm.LLM.loop_rate
```

````

````{py:method} update_cmd_args_list()
:canonical: agents.components.llm.LLM.update_cmd_args_list

```{autodoc2-docstring} agents.components.llm.LLM.update_cmd_args_list
```

````

````{py:property} inputs_json
:canonical: agents.components.llm.LLM.inputs_json
:abstractmethod:
:type: typing.Union[str, bytes]

```{autodoc2-docstring} agents.components.llm.LLM.inputs_json
```

````

````{py:property} outputs_json
:canonical: agents.components.llm.LLM.outputs_json
:abstractmethod:
:type: typing.Union[str, bytes]

```{autodoc2-docstring} agents.components.llm.LLM.outputs_json
```

````

````{py:method} main_action_callback(goal_handle)
:canonical: agents.components.llm.LLM.main_action_callback
:abstractmethod:

```{autodoc2-docstring} agents.components.llm.LLM.main_action_callback
```

````

````{py:property} main_action_name
:canonical: agents.components.llm.LLM.main_action_name
:type: typing.Optional[str]

```{autodoc2-docstring} agents.components.llm.LLM.main_action_name
```

````

````{py:property} main_srv_name
:canonical: agents.components.llm.LLM.main_srv_name
:type: typing.Optional[str]

```{autodoc2-docstring} agents.components.llm.LLM.main_srv_name
```

````

````{py:method} main_service_callback(request, response)
:canonical: agents.components.llm.LLM.main_service_callback
:abstractmethod:

```{autodoc2-docstring} agents.components.llm.LLM.main_service_callback
```

````

````{py:method} get_change_parameters_msg_from_config(config: ros_sugar.config.BaseComponentConfig) -> ros_sugar_interfaces.srv.ChangeParameters.Request
:canonical: agents.components.llm.LLM.get_change_parameters_msg_from_config
:classmethod:

```{autodoc2-docstring} agents.components.llm.LLM.get_change_parameters_msg_from_config
```

````

````{py:method} is_topic_of_type(input, msg_type: type) -> bool
:canonical: agents.components.llm.LLM.is_topic_of_type

```{autodoc2-docstring} agents.components.llm.LLM.is_topic_of_type
```

````

````{py:method} attach_callbacks()
:canonical: agents.components.llm.LLM.attach_callbacks

```{autodoc2-docstring} agents.components.llm.LLM.attach_callbacks
```

````

````{py:property} available_actions
:canonical: agents.components.llm.LLM.available_actions
:type: typing.List[str]

```{autodoc2-docstring} agents.components.llm.LLM.available_actions
```

````

````{py:method} start() -> bool
:canonical: agents.components.llm.LLM.start

```{autodoc2-docstring} agents.components.llm.LLM.start
```

````

````{py:method} stop() -> bool
:canonical: agents.components.llm.LLM.stop

```{autodoc2-docstring} agents.components.llm.LLM.stop
```

````

````{py:method} reconfigure(new_config: typing.Any, keep_alive: bool = False) -> bool
:canonical: agents.components.llm.LLM.reconfigure

```{autodoc2-docstring} agents.components.llm.LLM.reconfigure
```

````

````{py:method} restart(wait_time: typing.Optional[float] = None) -> bool
:canonical: agents.components.llm.LLM.restart

```{autodoc2-docstring} agents.components.llm.LLM.restart
```

````

````{py:method} set_param(param_name: str, new_value: typing.Any, keep_alive: bool = True) -> bool
:canonical: agents.components.llm.LLM.set_param

```{autodoc2-docstring} agents.components.llm.LLM.set_param
```

````

````{py:method} set_params(params_names: typing.List[str], new_values: typing.List, keep_alive: bool = True) -> bool
:canonical: agents.components.llm.LLM.set_params

```{autodoc2-docstring} agents.components.llm.LLM.set_params
```

````

````{py:property} fallbacks
:canonical: agents.components.llm.LLM.fallbacks
:type: typing.List[str]

```{autodoc2-docstring} agents.components.llm.LLM.fallbacks
```

````

````{py:method} on_fail(action: typing.Union[typing.List[ros_sugar.action.Action], ros_sugar.action.Action], max_retries: typing.Optional[int] = None) -> None
:canonical: agents.components.llm.LLM.on_fail

```{autodoc2-docstring} agents.components.llm.LLM.on_fail
```

````

````{py:method} on_system_fail(action: typing.Union[typing.List[ros_sugar.action.Action], ros_sugar.action.Action], max_retries: typing.Optional[int] = None) -> None
:canonical: agents.components.llm.LLM.on_system_fail

```{autodoc2-docstring} agents.components.llm.LLM.on_system_fail
```

````

````{py:method} on_component_fail(action: typing.Union[typing.List[ros_sugar.action.Action], ros_sugar.action.Action], max_retries: typing.Optional[int] = None) -> None
:canonical: agents.components.llm.LLM.on_component_fail

```{autodoc2-docstring} agents.components.llm.LLM.on_component_fail
```

````

````{py:method} on_plugin_fail(action: typing.Union[typing.List[ros_sugar.action.Action], ros_sugar.action.Action], max_retries: typing.Optional[int] = None) -> None
:canonical: agents.components.llm.LLM.on_plugin_fail

```{autodoc2-docstring} agents.components.llm.LLM.on_plugin_fail
```

````

````{py:method} broadcast_status() -> None
:canonical: agents.components.llm.LLM.broadcast_status

```{autodoc2-docstring} agents.components.llm.LLM.broadcast_status
```

````

````{py:method} custom_on_configure() -> None
:canonical: agents.components.llm.LLM.custom_on_configure

```{autodoc2-docstring} agents.components.llm.LLM.custom_on_configure
```

````

````{py:method} custom_on_activate() -> None
:canonical: agents.components.llm.LLM.custom_on_activate

```{autodoc2-docstring} agents.components.llm.LLM.custom_on_activate
```

````

````{py:method} custom_on_deactivate() -> None
:canonical: agents.components.llm.LLM.custom_on_deactivate

```{autodoc2-docstring} agents.components.llm.LLM.custom_on_deactivate
```

````

````{py:method} custom_on_shutdown() -> None
:canonical: agents.components.llm.LLM.custom_on_shutdown

```{autodoc2-docstring} agents.components.llm.LLM.custom_on_shutdown
```

````

````{py:method} custom_on_error() -> None
:canonical: agents.components.llm.LLM.custom_on_error

```{autodoc2-docstring} agents.components.llm.LLM.custom_on_error
```

````

````{py:property} lifecycle_state
:canonical: agents.components.llm.LLM.lifecycle_state
:type: int

```{autodoc2-docstring} agents.components.llm.LLM.lifecycle_state
```

````

````{py:method} custom_on_cleanup()
:canonical: agents.components.llm.LLM.custom_on_cleanup

```{autodoc2-docstring} agents.components.llm.LLM.custom_on_cleanup
```

````

````{py:method} on_configure(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.llm.LLM.on_configure

```{autodoc2-docstring} agents.components.llm.LLM.on_configure
```

````

````{py:method} on_activate(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.llm.LLM.on_activate

```{autodoc2-docstring} agents.components.llm.LLM.on_activate
```

````

````{py:method} on_deactivate(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.llm.LLM.on_deactivate

```{autodoc2-docstring} agents.components.llm.LLM.on_deactivate
```

````

````{py:method} on_shutdown(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.llm.LLM.on_shutdown

```{autodoc2-docstring} agents.components.llm.LLM.on_shutdown
```

````

````{py:method} on_cleanup(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.llm.LLM.on_cleanup

```{autodoc2-docstring} agents.components.llm.LLM.on_cleanup
```

````

````{py:method} on_error(state: rclpy.lifecycle.LifecycleState) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.llm.LLM.on_error

```{autodoc2-docstring} agents.components.llm.LLM.on_error
```

````

````{py:method} add_execute_once(method: typing.Callable)
:canonical: agents.components.llm.LLM.add_execute_once

```{autodoc2-docstring} agents.components.llm.LLM.add_execute_once
```

````

````{py:method} add_execute_in_loop(method: typing.Callable)
:canonical: agents.components.llm.LLM.add_execute_in_loop

```{autodoc2-docstring} agents.components.llm.LLM.add_execute_in_loop
```

````

````{py:method} get_ros_time() -> builtin_interfaces.msg.Time
:canonical: agents.components.llm.LLM.get_ros_time

```{autodoc2-docstring} agents.components.llm.LLM.get_ros_time
```

````

````{py:method} get_secs_time() -> float
:canonical: agents.components.llm.LLM.get_secs_time

```{autodoc2-docstring} agents.components.llm.LLM.get_secs_time
```

````

````{py:property} launch_cmd_args
:canonical: agents.components.llm.LLM.launch_cmd_args
:type: typing.List[str]

```{autodoc2-docstring} agents.components.llm.LLM.launch_cmd_args
```

````

````{py:property} config_json
:canonical: agents.components.llm.LLM.config_json
:type: typing.Union[str, bytes]

```{autodoc2-docstring} agents.components.llm.LLM.config_json
```

````

````{py:method} setup_qos(qos_policy: ros_sugar.config.QoSConfig) -> rclpy.qos.QoSProfile
:canonical: agents.components.llm.LLM.setup_qos

```{autodoc2-docstring} agents.components.llm.LLM.setup_qos
```

````

````{py:method} init_flags()
:canonical: agents.components.llm.LLM.init_flags

```{autodoc2-docstring} agents.components.llm.LLM.init_flags
```

````

````{py:method} init_variables()
:canonical: agents.components.llm.LLM.init_variables

```{autodoc2-docstring} agents.components.llm.LLM.init_variables
```

````

````{py:method} create_tf_listener(tf_config: ros_sugar.tf.TFListenerConfig) -> ros_sugar.tf.TFListener
:canonical: agents.components.llm.LLM.create_tf_listener

```{autodoc2-docstring} agents.components.llm.LLM.create_tf_listener
```

````

````{py:method} create_client(*args, **kwargs) -> rclpy.client.Client
:canonical: agents.components.llm.LLM.create_client

```{autodoc2-docstring} agents.components.llm.LLM.create_client
```

````

````{py:method} create_all_service_clients()
:canonical: agents.components.llm.LLM.create_all_service_clients

```{autodoc2-docstring} agents.components.llm.LLM.create_all_service_clients
```

````

````{py:method} create_all_action_clients()
:canonical: agents.components.llm.LLM.create_all_action_clients

```{autodoc2-docstring} agents.components.llm.LLM.create_all_action_clients
```

````

````{py:method} destroy_all_action_clients()
:canonical: agents.components.llm.LLM.destroy_all_action_clients

```{autodoc2-docstring} agents.components.llm.LLM.destroy_all_action_clients
```

````

````{py:method} destroy_all_service_clients()
:canonical: agents.components.llm.LLM.destroy_all_service_clients

```{autodoc2-docstring} agents.components.llm.LLM.destroy_all_service_clients
```

````

````{py:attribute} PARAM_REL_TOL
:canonical: agents.components.llm.LLM.PARAM_REL_TOL
:value: >
   1e-06

```{autodoc2-docstring} agents.components.llm.LLM.PARAM_REL_TOL
```

````

````{py:property} publishers
:canonical: agents.components.llm.LLM.publishers
:type: typing.Iterator[rclpy.publisher.Publisher]

```{autodoc2-docstring} agents.components.llm.LLM.publishers
```

````

````{py:property} subscriptions
:canonical: agents.components.llm.LLM.subscriptions
:type: typing.Iterator[rclpy.subscription.Subscription]

```{autodoc2-docstring} agents.components.llm.LLM.subscriptions
```

````

````{py:property} clients
:canonical: agents.components.llm.LLM.clients
:type: typing.Iterator[rclpy.client.Client]

```{autodoc2-docstring} agents.components.llm.LLM.clients
```

````

````{py:property} services
:canonical: agents.components.llm.LLM.services
:type: typing.Iterator[rclpy.service.Service]

```{autodoc2-docstring} agents.components.llm.LLM.services
```

````

````{py:property} timers
:canonical: agents.components.llm.LLM.timers
:type: typing.Iterator[rclpy.timer.Timer]

```{autodoc2-docstring} agents.components.llm.LLM.timers
```

````

````{py:property} guards
:canonical: agents.components.llm.LLM.guards
:type: typing.Iterator[rclpy.guard_condition.GuardCondition]

```{autodoc2-docstring} agents.components.llm.LLM.guards
```

````

````{py:property} waitables
:canonical: agents.components.llm.LLM.waitables
:type: typing.Iterator[rclpy.waitable.Waitable]

```{autodoc2-docstring} agents.components.llm.LLM.waitables
```

````

````{py:property} executor
:canonical: agents.components.llm.LLM.executor
:type: typing.Optional[rclpy.executors.Executor]

```{autodoc2-docstring} agents.components.llm.LLM.executor
```

````

````{py:property} context
:canonical: agents.components.llm.LLM.context
:type: rclpy.context.Context

```{autodoc2-docstring} agents.components.llm.LLM.context
```

````

````{py:property} default_callback_group
:canonical: agents.components.llm.LLM.default_callback_group
:type: rclpy.callback_groups.CallbackGroup

```{autodoc2-docstring} agents.components.llm.LLM.default_callback_group
```

````

````{py:property} handle
:canonical: agents.components.llm.LLM.handle

```{autodoc2-docstring} agents.components.llm.LLM.handle
```

````

````{py:method} get_name() -> str
:canonical: agents.components.llm.LLM.get_name

```{autodoc2-docstring} agents.components.llm.LLM.get_name
```

````

````{py:method} get_namespace() -> str
:canonical: agents.components.llm.LLM.get_namespace

```{autodoc2-docstring} agents.components.llm.LLM.get_namespace
```

````

````{py:method} get_clock() -> rclpy.clock.Clock
:canonical: agents.components.llm.LLM.get_clock

```{autodoc2-docstring} agents.components.llm.LLM.get_clock
```

````

````{py:method} get_logger()
:canonical: agents.components.llm.LLM.get_logger

```{autodoc2-docstring} agents.components.llm.LLM.get_logger
```

````

````{py:method} declare_parameter(name: str, value: typing.Any = None, descriptor: typing.Optional[rcl_interfaces.msg.ParameterDescriptor] = None, ignore_override: bool = False) -> rclpy.parameter.Parameter
:canonical: agents.components.llm.LLM.declare_parameter

```{autodoc2-docstring} agents.components.llm.LLM.declare_parameter
```

````

````{py:method} declare_parameters(namespace: str, parameters: typing.List[typing.Union[typing.Tuple[str], typing.Tuple[str, rclpy.parameter.Parameter.Type], typing.Tuple[str, typing.Any, rcl_interfaces.msg.ParameterDescriptor]]], ignore_override: bool = False) -> typing.List[rclpy.parameter.Parameter]
:canonical: agents.components.llm.LLM.declare_parameters

```{autodoc2-docstring} agents.components.llm.LLM.declare_parameters
```

````

````{py:method} undeclare_parameter(name: str)
:canonical: agents.components.llm.LLM.undeclare_parameter

```{autodoc2-docstring} agents.components.llm.LLM.undeclare_parameter
```

````

````{py:method} has_parameter(name: str) -> bool
:canonical: agents.components.llm.LLM.has_parameter

```{autodoc2-docstring} agents.components.llm.LLM.has_parameter
```

````

````{py:method} get_parameter_types(names: typing.List[str]) -> typing.List[rclpy.parameter.Parameter.Type]
:canonical: agents.components.llm.LLM.get_parameter_types

```{autodoc2-docstring} agents.components.llm.LLM.get_parameter_types
```

````

````{py:method} get_parameter_type(name: str) -> rclpy.parameter.Parameter.Type
:canonical: agents.components.llm.LLM.get_parameter_type

```{autodoc2-docstring} agents.components.llm.LLM.get_parameter_type
```

````

````{py:method} get_parameters(names: typing.List[str]) -> typing.List[rclpy.parameter.Parameter]
:canonical: agents.components.llm.LLM.get_parameters

```{autodoc2-docstring} agents.components.llm.LLM.get_parameters
```

````

````{py:method} get_parameter(name: str) -> rclpy.parameter.Parameter
:canonical: agents.components.llm.LLM.get_parameter

```{autodoc2-docstring} agents.components.llm.LLM.get_parameter
```

````

````{py:method} get_parameter_or(name: str, alternative_value: typing.Optional[rclpy.parameter.Parameter] = None) -> rclpy.parameter.Parameter
:canonical: agents.components.llm.LLM.get_parameter_or

```{autodoc2-docstring} agents.components.llm.LLM.get_parameter_or
```

````

````{py:method} get_parameters_by_prefix(prefix: str) -> typing.Dict[str, typing.Optional[typing.Union[bool, int, float, str, bytes, typing.Sequence[bool], typing.Sequence[int], typing.Sequence[float], typing.Sequence[str]]]]
:canonical: agents.components.llm.LLM.get_parameters_by_prefix

```{autodoc2-docstring} agents.components.llm.LLM.get_parameters_by_prefix
```

````

````{py:method} set_parameters(parameter_list: typing.List[rclpy.parameter.Parameter]) -> typing.List[rcl_interfaces.msg.SetParametersResult]
:canonical: agents.components.llm.LLM.set_parameters

```{autodoc2-docstring} agents.components.llm.LLM.set_parameters
```

````

````{py:method} set_parameters_atomically(parameter_list: typing.List[rclpy.parameter.Parameter]) -> rcl_interfaces.msg.SetParametersResult
:canonical: agents.components.llm.LLM.set_parameters_atomically

```{autodoc2-docstring} agents.components.llm.LLM.set_parameters_atomically
```

````

````{py:method} add_pre_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], typing.List[rclpy.parameter.Parameter]]) -> None
:canonical: agents.components.llm.LLM.add_pre_set_parameters_callback

```{autodoc2-docstring} agents.components.llm.LLM.add_pre_set_parameters_callback
```

````

````{py:method} add_on_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], rcl_interfaces.msg.SetParametersResult]) -> None
:canonical: agents.components.llm.LLM.add_on_set_parameters_callback

```{autodoc2-docstring} agents.components.llm.LLM.add_on_set_parameters_callback
```

````

````{py:method} add_post_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], None]) -> None
:canonical: agents.components.llm.LLM.add_post_set_parameters_callback

```{autodoc2-docstring} agents.components.llm.LLM.add_post_set_parameters_callback
```

````

````{py:method} remove_pre_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], typing.List[rclpy.parameter.Parameter]]) -> None
:canonical: agents.components.llm.LLM.remove_pre_set_parameters_callback

```{autodoc2-docstring} agents.components.llm.LLM.remove_pre_set_parameters_callback
```

````

````{py:method} remove_on_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], rcl_interfaces.msg.SetParametersResult]) -> None
:canonical: agents.components.llm.LLM.remove_on_set_parameters_callback

```{autodoc2-docstring} agents.components.llm.LLM.remove_on_set_parameters_callback
```

````

````{py:method} remove_post_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], None]) -> None
:canonical: agents.components.llm.LLM.remove_post_set_parameters_callback

```{autodoc2-docstring} agents.components.llm.LLM.remove_post_set_parameters_callback
```

````

````{py:method} describe_parameter(name: str) -> rcl_interfaces.msg.ParameterDescriptor
:canonical: agents.components.llm.LLM.describe_parameter

```{autodoc2-docstring} agents.components.llm.LLM.describe_parameter
```

````

````{py:method} describe_parameters(names: typing.List[str]) -> typing.List[rcl_interfaces.msg.ParameterDescriptor]
:canonical: agents.components.llm.LLM.describe_parameters

```{autodoc2-docstring} agents.components.llm.LLM.describe_parameters
```

````

````{py:method} set_descriptor(name: str, descriptor: rcl_interfaces.msg.ParameterDescriptor, alternative_value: typing.Optional[rcl_interfaces.msg.ParameterValue] = None) -> rcl_interfaces.msg.ParameterValue
:canonical: agents.components.llm.LLM.set_descriptor

```{autodoc2-docstring} agents.components.llm.LLM.set_descriptor
```

````

````{py:method} add_waitable(waitable: rclpy.waitable.Waitable) -> None
:canonical: agents.components.llm.LLM.add_waitable

```{autodoc2-docstring} agents.components.llm.LLM.add_waitable
```

````

````{py:method} remove_waitable(waitable: rclpy.waitable.Waitable) -> None
:canonical: agents.components.llm.LLM.remove_waitable

```{autodoc2-docstring} agents.components.llm.LLM.remove_waitable
```

````

````{py:method} resolve_topic_name(topic: str, *, only_expand: bool = False) -> str
:canonical: agents.components.llm.LLM.resolve_topic_name

```{autodoc2-docstring} agents.components.llm.LLM.resolve_topic_name
```

````

````{py:method} resolve_service_name(service: str, *, only_expand: bool = False) -> str
:canonical: agents.components.llm.LLM.resolve_service_name

```{autodoc2-docstring} agents.components.llm.LLM.resolve_service_name
```

````

````{py:method} create_publisher(msg_type, topic: str, qos_profile: typing.Union[rclpy.qos.QoSProfile, int], *, callback_group: typing.Optional[rclpy.callback_groups.CallbackGroup] = None, event_callbacks: typing.Optional[rclpy.event_handler.PublisherEventCallbacks] = None, qos_overriding_options: typing.Optional[rclpy.qos_overriding_options.QoSOverridingOptions] = None, publisher_class: typing.Type[rclpy.publisher.Publisher] = Publisher) -> rclpy.publisher.Publisher
:canonical: agents.components.llm.LLM.create_publisher

```{autodoc2-docstring} agents.components.llm.LLM.create_publisher
```

````

````{py:method} create_subscription(msg_type, topic: str, callback: typing.Callable[[rclpy.node.MsgType], None], qos_profile: typing.Union[rclpy.qos.QoSProfile, int], *, callback_group: typing.Optional[rclpy.callback_groups.CallbackGroup] = None, event_callbacks: typing.Optional[rclpy.event_handler.SubscriptionEventCallbacks] = None, qos_overriding_options: typing.Optional[rclpy.qos_overriding_options.QoSOverridingOptions] = None, raw: bool = False) -> rclpy.subscription.Subscription
:canonical: agents.components.llm.LLM.create_subscription

```{autodoc2-docstring} agents.components.llm.LLM.create_subscription
```

````

````{py:method} create_service(srv_type, srv_name: str, callback: typing.Callable[[rclpy.node.SrvTypeRequest, rclpy.node.SrvTypeResponse], rclpy.node.SrvTypeResponse], *, qos_profile: rclpy.qos.QoSProfile = qos_profile_services_default, callback_group: rclpy.callback_groups.CallbackGroup = None) -> rclpy.service.Service
:canonical: agents.components.llm.LLM.create_service

```{autodoc2-docstring} agents.components.llm.LLM.create_service
```

````

````{py:method} create_timer(timer_period_sec: float, callback: typing.Callable, callback_group: rclpy.callback_groups.CallbackGroup = None, clock: rclpy.clock.Clock = None) -> rclpy.timer.Timer
:canonical: agents.components.llm.LLM.create_timer

```{autodoc2-docstring} agents.components.llm.LLM.create_timer
```

````

````{py:method} create_guard_condition(callback: typing.Callable, callback_group: rclpy.callback_groups.CallbackGroup = None) -> rclpy.guard_condition.GuardCondition
:canonical: agents.components.llm.LLM.create_guard_condition

```{autodoc2-docstring} agents.components.llm.LLM.create_guard_condition
```

````

````{py:method} create_rate(frequency: float, clock: rclpy.clock.Clock = None) -> rclpy.timer.Rate
:canonical: agents.components.llm.LLM.create_rate

```{autodoc2-docstring} agents.components.llm.LLM.create_rate
```

````

````{py:method} destroy_publisher(publisher: rclpy.publisher.Publisher) -> bool
:canonical: agents.components.llm.LLM.destroy_publisher

```{autodoc2-docstring} agents.components.llm.LLM.destroy_publisher
```

````

````{py:method} destroy_subscription(subscription: rclpy.subscription.Subscription) -> bool
:canonical: agents.components.llm.LLM.destroy_subscription

```{autodoc2-docstring} agents.components.llm.LLM.destroy_subscription
```

````

````{py:method} destroy_client(client: rclpy.client.Client) -> bool
:canonical: agents.components.llm.LLM.destroy_client

```{autodoc2-docstring} agents.components.llm.LLM.destroy_client
```

````

````{py:method} destroy_service(service: rclpy.service.Service) -> bool
:canonical: agents.components.llm.LLM.destroy_service

```{autodoc2-docstring} agents.components.llm.LLM.destroy_service
```

````

````{py:method} destroy_timer(timer: rclpy.timer.Timer) -> bool
:canonical: agents.components.llm.LLM.destroy_timer

```{autodoc2-docstring} agents.components.llm.LLM.destroy_timer
```

````

````{py:method} destroy_guard_condition(guard: rclpy.guard_condition.GuardCondition) -> bool
:canonical: agents.components.llm.LLM.destroy_guard_condition

```{autodoc2-docstring} agents.components.llm.LLM.destroy_guard_condition
```

````

````{py:method} destroy_rate(rate: rclpy.timer.Rate) -> bool
:canonical: agents.components.llm.LLM.destroy_rate

```{autodoc2-docstring} agents.components.llm.LLM.destroy_rate
```

````

````{py:method} destroy_node()
:canonical: agents.components.llm.LLM.destroy_node

```{autodoc2-docstring} agents.components.llm.LLM.destroy_node
```

````

````{py:method} get_publisher_names_and_types_by_node(node_name: str, node_namespace: str, no_demangle: bool = False) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.llm.LLM.get_publisher_names_and_types_by_node

```{autodoc2-docstring} agents.components.llm.LLM.get_publisher_names_and_types_by_node
```

````

````{py:method} get_subscriber_names_and_types_by_node(node_name: str, node_namespace: str, no_demangle: bool = False) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.llm.LLM.get_subscriber_names_and_types_by_node

```{autodoc2-docstring} agents.components.llm.LLM.get_subscriber_names_and_types_by_node
```

````

````{py:method} get_service_names_and_types_by_node(node_name: str, node_namespace: str) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.llm.LLM.get_service_names_and_types_by_node

```{autodoc2-docstring} agents.components.llm.LLM.get_service_names_and_types_by_node
```

````

````{py:method} get_client_names_and_types_by_node(node_name: str, node_namespace: str) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.llm.LLM.get_client_names_and_types_by_node

```{autodoc2-docstring} agents.components.llm.LLM.get_client_names_and_types_by_node
```

````

````{py:method} get_topic_names_and_types(no_demangle: bool = False) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.llm.LLM.get_topic_names_and_types

```{autodoc2-docstring} agents.components.llm.LLM.get_topic_names_and_types
```

````

````{py:method} get_service_names_and_types() -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.llm.LLM.get_service_names_and_types

```{autodoc2-docstring} agents.components.llm.LLM.get_service_names_and_types
```

````

````{py:method} get_node_names() -> typing.List[str]
:canonical: agents.components.llm.LLM.get_node_names

```{autodoc2-docstring} agents.components.llm.LLM.get_node_names
```

````

````{py:method} get_fully_qualified_node_names() -> typing.List[str]
:canonical: agents.components.llm.LLM.get_fully_qualified_node_names

```{autodoc2-docstring} agents.components.llm.LLM.get_fully_qualified_node_names
```

````

````{py:method} get_node_names_and_namespaces() -> typing.List[typing.Tuple[str, str]]
:canonical: agents.components.llm.LLM.get_node_names_and_namespaces

```{autodoc2-docstring} agents.components.llm.LLM.get_node_names_and_namespaces
```

````

````{py:method} get_node_names_and_namespaces_with_enclaves() -> typing.List[typing.Tuple[str, str, str]]
:canonical: agents.components.llm.LLM.get_node_names_and_namespaces_with_enclaves

```{autodoc2-docstring} agents.components.llm.LLM.get_node_names_and_namespaces_with_enclaves
```

````

````{py:method} get_fully_qualified_name() -> str
:canonical: agents.components.llm.LLM.get_fully_qualified_name

```{autodoc2-docstring} agents.components.llm.LLM.get_fully_qualified_name
```

````

````{py:method} count_publishers(topic_name: str) -> int
:canonical: agents.components.llm.LLM.count_publishers

```{autodoc2-docstring} agents.components.llm.LLM.count_publishers
```

````

````{py:method} count_subscribers(topic_name: str) -> int
:canonical: agents.components.llm.LLM.count_subscribers

```{autodoc2-docstring} agents.components.llm.LLM.count_subscribers
```

````

````{py:method} get_publishers_info_by_topic(topic_name: str, no_mangle: bool = False) -> typing.List[rclpy.topic_endpoint_info.TopicEndpointInfo]
:canonical: agents.components.llm.LLM.get_publishers_info_by_topic

```{autodoc2-docstring} agents.components.llm.LLM.get_publishers_info_by_topic
```

````

````{py:method} get_subscriptions_info_by_topic(topic_name: str, no_mangle: bool = False) -> typing.List[rclpy.topic_endpoint_info.TopicEndpointInfo]
:canonical: agents.components.llm.LLM.get_subscriptions_info_by_topic

```{autodoc2-docstring} agents.components.llm.LLM.get_subscriptions_info_by_topic
```

````

````{py:method} wait_for_node(fully_qualified_node_name: str, timeout: float) -> bool
:canonical: agents.components.llm.LLM.wait_for_node

```{autodoc2-docstring} agents.components.llm.LLM.wait_for_node
```

````

`````
