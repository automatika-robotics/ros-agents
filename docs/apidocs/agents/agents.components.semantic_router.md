---
orphan: true
---

# {py:mod}`agents.components.semantic_router`

```{py:module} agents.components.semantic_router
```

```{autodoc2-docstring} agents.components.semantic_router
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SemanticRouter <agents.components.semantic_router.SemanticRouter>`
  - ```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter
    :summary:
    ```
````

### API

`````{py:class} SemanticRouter(*, inputs: list[agents.ros.Topic], routes: list[agents.ros.Route], default_route: typing.Optional[agents.ros.Route] = None, config: agents.config.SemanticRouterConfig, db_client: agents.clients.db_base.DBClient, callback_group=None, component_name: str = 'router_component', **kwargs)
:canonical: agents.components.semantic_router.SemanticRouter

Bases: {py:obj}`agents.components.component_base.Component`

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter
```

````{py:method} activate()
:canonical: agents.components.semantic_router.SemanticRouter.activate

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.activate
```

````

````{py:method} deactivate()
:canonical: agents.components.semantic_router.SemanticRouter.deactivate

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.deactivate
```

````

````{py:method} outputs(outputs: list[agents.ros.Topic])
:canonical: agents.components.semantic_router.SemanticRouter.outputs
:abstractmethod:

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.outputs
```

````

````{py:method} create_all_subscribers()
:canonical: agents.components.semantic_router.SemanticRouter.create_all_subscribers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_all_subscribers
```

````

````{py:method} create_all_publishers()
:canonical: agents.components.semantic_router.SemanticRouter.create_all_publishers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_all_publishers
```

````

````{py:method} create_component_triggers()
:canonical: agents.components.semantic_router.SemanticRouter.create_component_triggers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_component_triggers
```

````

````{py:method} destroy_all_subscribers()
:canonical: agents.components.semantic_router.SemanticRouter.destroy_all_subscribers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_all_subscribers
```

````

````{py:method} destroy_all_publishers()
:canonical: agents.components.semantic_router.SemanticRouter.destroy_all_publishers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_all_publishers
```

````

````{py:method} inputs(inputs: typing.Sequence[typing.Union[agents.ros.Topic, agents.ros.FixedInput]])
:canonical: agents.components.semantic_router.SemanticRouter.inputs

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.inputs
```

````

````{py:method} trigger(trigger: typing.Union[agents.ros.Topic, list[agents.ros.Topic], float]) -> None
:canonical: agents.components.semantic_router.SemanticRouter.trigger

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.trigger
```

````

````{py:method} validate_topics(topics: typing.Sequence[typing.Union[agents.ros.Topic, agents.ros.FixedInput]], allowed_topics: typing.Optional[dict[str, list[type[agents.ros.SupportedType]]]] = None, topics_direction: str = 'Topics')
:canonical: agents.components.semantic_router.SemanticRouter.validate_topics

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.validate_topics
```

````

````{py:method} got_all_inputs() -> bool
:canonical: agents.components.semantic_router.SemanticRouter.got_all_inputs

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.got_all_inputs
```

````

````{py:method} get_missing_inputs() -> typing.Union[list[str], None]
:canonical: agents.components.semantic_router.SemanticRouter.get_missing_inputs

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_missing_inputs
```

````

````{py:method} attach_custom_callback(input_topic: agents.ros.Topic, callable: typing.Callable) -> None
:canonical: agents.components.semantic_router.SemanticRouter.attach_custom_callback

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.attach_custom_callback
```

````

````{py:method} add_callback_postprocessor(input_topic: agents.ros.Topic, func: typing.Callable) -> None
:canonical: agents.components.semantic_router.SemanticRouter.add_callback_postprocessor

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.add_callback_postprocessor
```

````

````{py:method} add_publisher_preprocessor(output_topic: agents.ros.Topic, func: typing.Callable) -> None
:canonical: agents.components.semantic_router.SemanticRouter.add_publisher_preprocessor

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.add_publisher_preprocessor
```

````

````{py:method} create_all_timers()
:canonical: agents.components.semantic_router.SemanticRouter.create_all_timers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_all_timers
```

````

````{py:method} create_all_action_servers()
:canonical: agents.components.semantic_router.SemanticRouter.create_all_action_servers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_all_action_servers
```

````

````{py:method} create_all_services()
:canonical: agents.components.semantic_router.SemanticRouter.create_all_services

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_all_services
```

````

````{py:method} destroy_all_timers()
:canonical: agents.components.semantic_router.SemanticRouter.destroy_all_timers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_all_timers
```

````

````{py:method} destroy_all_services()
:canonical: agents.components.semantic_router.SemanticRouter.destroy_all_services

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_all_services
```

````

````{py:method} destroy_all_action_servers()
:canonical: agents.components.semantic_router.SemanticRouter.destroy_all_action_servers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_all_action_servers
```

````

````{py:method} configure(config_file: str)
:canonical: agents.components.semantic_router.SemanticRouter.configure

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.configure
```

````

````{py:method} rclpy_init_node(*args, **kwargs)
:canonical: agents.components.semantic_router.SemanticRouter.rclpy_init_node

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.rclpy_init_node
```

````

````{py:property} run_type
:canonical: agents.components.semantic_router.SemanticRouter.run_type
:type: ros_sugar.config.ComponentRunType

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.run_type
```

````

````{py:property} fallback_rate
:canonical: agents.components.semantic_router.SemanticRouter.fallback_rate
:type: float

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.fallback_rate
```

````

````{py:property} loop_rate
:canonical: agents.components.semantic_router.SemanticRouter.loop_rate
:type: float

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.loop_rate
```

````

````{py:method} update_cmd_args_list()
:canonical: agents.components.semantic_router.SemanticRouter.update_cmd_args_list

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.update_cmd_args_list
```

````

````{py:property} inputs_json
:canonical: agents.components.semantic_router.SemanticRouter.inputs_json
:abstractmethod:
:type: typing.Union[str, bytes]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.inputs_json
```

````

````{py:property} outputs_json
:canonical: agents.components.semantic_router.SemanticRouter.outputs_json
:abstractmethod:
:type: typing.Union[str, bytes]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.outputs_json
```

````

````{py:method} main_action_callback(goal_handle)
:canonical: agents.components.semantic_router.SemanticRouter.main_action_callback
:abstractmethod:

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.main_action_callback
```

````

````{py:property} main_action_name
:canonical: agents.components.semantic_router.SemanticRouter.main_action_name
:type: typing.Optional[str]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.main_action_name
```

````

````{py:property} main_srv_name
:canonical: agents.components.semantic_router.SemanticRouter.main_srv_name
:type: typing.Optional[str]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.main_srv_name
```

````

````{py:method} main_service_callback(request, response)
:canonical: agents.components.semantic_router.SemanticRouter.main_service_callback
:abstractmethod:

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.main_service_callback
```

````

````{py:method} get_change_parameters_msg_from_config(config: ros_sugar.config.BaseComponentConfig) -> ros_sugar_interfaces.srv.ChangeParameters.Request
:canonical: agents.components.semantic_router.SemanticRouter.get_change_parameters_msg_from_config
:classmethod:

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_change_parameters_msg_from_config
```

````

````{py:method} is_topic_of_type(input, msg_type: type) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.is_topic_of_type

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.is_topic_of_type
```

````

````{py:method} attach_callbacks()
:canonical: agents.components.semantic_router.SemanticRouter.attach_callbacks

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.attach_callbacks
```

````

````{py:property} available_actions
:canonical: agents.components.semantic_router.SemanticRouter.available_actions
:type: typing.List[str]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.available_actions
```

````

````{py:method} start() -> bool
:canonical: agents.components.semantic_router.SemanticRouter.start

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.start
```

````

````{py:method} stop() -> bool
:canonical: agents.components.semantic_router.SemanticRouter.stop

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.stop
```

````

````{py:method} reconfigure(new_config: typing.Any, keep_alive: bool = False) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.reconfigure

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.reconfigure
```

````

````{py:method} restart(wait_time: typing.Optional[float] = None) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.restart

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.restart
```

````

````{py:method} set_param(param_name: str, new_value: typing.Any, keep_alive: bool = True) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.set_param

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.set_param
```

````

````{py:method} set_params(params_names: typing.List[str], new_values: typing.List, keep_alive: bool = True) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.set_params

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.set_params
```

````

````{py:property} fallbacks
:canonical: agents.components.semantic_router.SemanticRouter.fallbacks
:type: typing.List[str]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.fallbacks
```

````

````{py:method} on_fail(action: typing.Union[typing.List[ros_sugar.action.Action], ros_sugar.action.Action], max_retries: typing.Optional[int] = None) -> None
:canonical: agents.components.semantic_router.SemanticRouter.on_fail

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_fail
```

````

````{py:method} on_system_fail(action: typing.Union[typing.List[ros_sugar.action.Action], ros_sugar.action.Action], max_retries: typing.Optional[int] = None) -> None
:canonical: agents.components.semantic_router.SemanticRouter.on_system_fail

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_system_fail
```

````

````{py:method} on_component_fail(action: typing.Union[typing.List[ros_sugar.action.Action], ros_sugar.action.Action], max_retries: typing.Optional[int] = None) -> None
:canonical: agents.components.semantic_router.SemanticRouter.on_component_fail

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_component_fail
```

````

````{py:method} on_plugin_fail(action: typing.Union[typing.List[ros_sugar.action.Action], ros_sugar.action.Action], max_retries: typing.Optional[int] = None) -> None
:canonical: agents.components.semantic_router.SemanticRouter.on_plugin_fail

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_plugin_fail
```

````

````{py:method} broadcast_status() -> None
:canonical: agents.components.semantic_router.SemanticRouter.broadcast_status

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.broadcast_status
```

````

````{py:method} custom_on_configure() -> None
:canonical: agents.components.semantic_router.SemanticRouter.custom_on_configure

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.custom_on_configure
```

````

````{py:method} custom_on_activate() -> None
:canonical: agents.components.semantic_router.SemanticRouter.custom_on_activate

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.custom_on_activate
```

````

````{py:method} custom_on_deactivate() -> None
:canonical: agents.components.semantic_router.SemanticRouter.custom_on_deactivate

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.custom_on_deactivate
```

````

````{py:method} custom_on_shutdown() -> None
:canonical: agents.components.semantic_router.SemanticRouter.custom_on_shutdown

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.custom_on_shutdown
```

````

````{py:method} custom_on_error() -> None
:canonical: agents.components.semantic_router.SemanticRouter.custom_on_error

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.custom_on_error
```

````

````{py:property} lifecycle_state
:canonical: agents.components.semantic_router.SemanticRouter.lifecycle_state
:type: int

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.lifecycle_state
```

````

````{py:method} custom_on_cleanup()
:canonical: agents.components.semantic_router.SemanticRouter.custom_on_cleanup

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.custom_on_cleanup
```

````

````{py:method} on_configure(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.semantic_router.SemanticRouter.on_configure

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_configure
```

````

````{py:method} on_activate(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.semantic_router.SemanticRouter.on_activate

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_activate
```

````

````{py:method} on_deactivate(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.semantic_router.SemanticRouter.on_deactivate

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_deactivate
```

````

````{py:method} on_shutdown(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.semantic_router.SemanticRouter.on_shutdown

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_shutdown
```

````

````{py:method} on_cleanup(state: rclpy.lifecycle.State) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.semantic_router.SemanticRouter.on_cleanup

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_cleanup
```

````

````{py:method} on_error(state: rclpy.lifecycle.LifecycleState) -> rclpy.lifecycle.TransitionCallbackReturn
:canonical: agents.components.semantic_router.SemanticRouter.on_error

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.on_error
```

````

````{py:method} add_execute_once(method: typing.Callable)
:canonical: agents.components.semantic_router.SemanticRouter.add_execute_once

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.add_execute_once
```

````

````{py:method} add_execute_in_loop(method: typing.Callable)
:canonical: agents.components.semantic_router.SemanticRouter.add_execute_in_loop

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.add_execute_in_loop
```

````

````{py:method} get_ros_time() -> builtin_interfaces.msg.Time
:canonical: agents.components.semantic_router.SemanticRouter.get_ros_time

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_ros_time
```

````

````{py:method} get_secs_time() -> float
:canonical: agents.components.semantic_router.SemanticRouter.get_secs_time

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_secs_time
```

````

````{py:property} launch_cmd_args
:canonical: agents.components.semantic_router.SemanticRouter.launch_cmd_args
:type: typing.List[str]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.launch_cmd_args
```

````

````{py:property} config_json
:canonical: agents.components.semantic_router.SemanticRouter.config_json
:type: typing.Union[str, bytes]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.config_json
```

````

````{py:method} setup_qos(qos_policy: ros_sugar.config.QoSConfig) -> rclpy.qos.QoSProfile
:canonical: agents.components.semantic_router.SemanticRouter.setup_qos

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.setup_qos
```

````

````{py:method} init_flags()
:canonical: agents.components.semantic_router.SemanticRouter.init_flags

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.init_flags
```

````

````{py:method} init_variables()
:canonical: agents.components.semantic_router.SemanticRouter.init_variables

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.init_variables
```

````

````{py:method} create_tf_listener(tf_config: ros_sugar.tf.TFListenerConfig) -> ros_sugar.tf.TFListener
:canonical: agents.components.semantic_router.SemanticRouter.create_tf_listener

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_tf_listener
```

````

````{py:method} create_client(*args, **kwargs) -> rclpy.client.Client
:canonical: agents.components.semantic_router.SemanticRouter.create_client

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_client
```

````

````{py:method} create_all_service_clients()
:canonical: agents.components.semantic_router.SemanticRouter.create_all_service_clients

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_all_service_clients
```

````

````{py:method} create_all_action_clients()
:canonical: agents.components.semantic_router.SemanticRouter.create_all_action_clients

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_all_action_clients
```

````

````{py:method} destroy_all_action_clients()
:canonical: agents.components.semantic_router.SemanticRouter.destroy_all_action_clients

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_all_action_clients
```

````

````{py:method} destroy_all_service_clients()
:canonical: agents.components.semantic_router.SemanticRouter.destroy_all_service_clients

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_all_service_clients
```

````

````{py:attribute} PARAM_REL_TOL
:canonical: agents.components.semantic_router.SemanticRouter.PARAM_REL_TOL
:value: >
   1e-06

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.PARAM_REL_TOL
```

````

````{py:property} publishers
:canonical: agents.components.semantic_router.SemanticRouter.publishers
:type: typing.Iterator[rclpy.publisher.Publisher]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.publishers
```

````

````{py:property} subscriptions
:canonical: agents.components.semantic_router.SemanticRouter.subscriptions
:type: typing.Iterator[rclpy.subscription.Subscription]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.subscriptions
```

````

````{py:property} clients
:canonical: agents.components.semantic_router.SemanticRouter.clients
:type: typing.Iterator[rclpy.client.Client]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.clients
```

````

````{py:property} services
:canonical: agents.components.semantic_router.SemanticRouter.services
:type: typing.Iterator[rclpy.service.Service]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.services
```

````

````{py:property} timers
:canonical: agents.components.semantic_router.SemanticRouter.timers
:type: typing.Iterator[rclpy.timer.Timer]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.timers
```

````

````{py:property} guards
:canonical: agents.components.semantic_router.SemanticRouter.guards
:type: typing.Iterator[rclpy.guard_condition.GuardCondition]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.guards
```

````

````{py:property} waitables
:canonical: agents.components.semantic_router.SemanticRouter.waitables
:type: typing.Iterator[rclpy.waitable.Waitable]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.waitables
```

````

````{py:property} executor
:canonical: agents.components.semantic_router.SemanticRouter.executor
:type: typing.Optional[rclpy.executors.Executor]

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.executor
```

````

````{py:property} context
:canonical: agents.components.semantic_router.SemanticRouter.context
:type: rclpy.context.Context

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.context
```

````

````{py:property} default_callback_group
:canonical: agents.components.semantic_router.SemanticRouter.default_callback_group
:type: rclpy.callback_groups.CallbackGroup

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.default_callback_group
```

````

````{py:property} handle
:canonical: agents.components.semantic_router.SemanticRouter.handle

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.handle
```

````

````{py:method} get_name() -> str
:canonical: agents.components.semantic_router.SemanticRouter.get_name

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_name
```

````

````{py:method} get_namespace() -> str
:canonical: agents.components.semantic_router.SemanticRouter.get_namespace

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_namespace
```

````

````{py:method} get_clock() -> rclpy.clock.Clock
:canonical: agents.components.semantic_router.SemanticRouter.get_clock

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_clock
```

````

````{py:method} get_logger()
:canonical: agents.components.semantic_router.SemanticRouter.get_logger

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_logger
```

````

````{py:method} declare_parameter(name: str, value: typing.Any = None, descriptor: typing.Optional[rcl_interfaces.msg.ParameterDescriptor] = None, ignore_override: bool = False) -> rclpy.parameter.Parameter
:canonical: agents.components.semantic_router.SemanticRouter.declare_parameter

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.declare_parameter
```

````

````{py:method} declare_parameters(namespace: str, parameters: typing.List[typing.Union[typing.Tuple[str], typing.Tuple[str, rclpy.parameter.Parameter.Type], typing.Tuple[str, typing.Any, rcl_interfaces.msg.ParameterDescriptor]]], ignore_override: bool = False) -> typing.List[rclpy.parameter.Parameter]
:canonical: agents.components.semantic_router.SemanticRouter.declare_parameters

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.declare_parameters
```

````

````{py:method} undeclare_parameter(name: str)
:canonical: agents.components.semantic_router.SemanticRouter.undeclare_parameter

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.undeclare_parameter
```

````

````{py:method} has_parameter(name: str) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.has_parameter

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.has_parameter
```

````

````{py:method} get_parameter_types(names: typing.List[str]) -> typing.List[rclpy.parameter.Parameter.Type]
:canonical: agents.components.semantic_router.SemanticRouter.get_parameter_types

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_parameter_types
```

````

````{py:method} get_parameter_type(name: str) -> rclpy.parameter.Parameter.Type
:canonical: agents.components.semantic_router.SemanticRouter.get_parameter_type

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_parameter_type
```

````

````{py:method} get_parameters(names: typing.List[str]) -> typing.List[rclpy.parameter.Parameter]
:canonical: agents.components.semantic_router.SemanticRouter.get_parameters

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_parameters
```

````

````{py:method} get_parameter(name: str) -> rclpy.parameter.Parameter
:canonical: agents.components.semantic_router.SemanticRouter.get_parameter

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_parameter
```

````

````{py:method} get_parameter_or(name: str, alternative_value: typing.Optional[rclpy.parameter.Parameter] = None) -> rclpy.parameter.Parameter
:canonical: agents.components.semantic_router.SemanticRouter.get_parameter_or

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_parameter_or
```

````

````{py:method} get_parameters_by_prefix(prefix: str) -> typing.Dict[str, typing.Optional[typing.Union[bool, int, float, str, bytes, typing.Sequence[bool], typing.Sequence[int], typing.Sequence[float], typing.Sequence[str]]]]
:canonical: agents.components.semantic_router.SemanticRouter.get_parameters_by_prefix

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_parameters_by_prefix
```

````

````{py:method} set_parameters(parameter_list: typing.List[rclpy.parameter.Parameter]) -> typing.List[rcl_interfaces.msg.SetParametersResult]
:canonical: agents.components.semantic_router.SemanticRouter.set_parameters

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.set_parameters
```

````

````{py:method} set_parameters_atomically(parameter_list: typing.List[rclpy.parameter.Parameter]) -> rcl_interfaces.msg.SetParametersResult
:canonical: agents.components.semantic_router.SemanticRouter.set_parameters_atomically

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.set_parameters_atomically
```

````

````{py:method} add_pre_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], typing.List[rclpy.parameter.Parameter]]) -> None
:canonical: agents.components.semantic_router.SemanticRouter.add_pre_set_parameters_callback

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.add_pre_set_parameters_callback
```

````

````{py:method} add_on_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], rcl_interfaces.msg.SetParametersResult]) -> None
:canonical: agents.components.semantic_router.SemanticRouter.add_on_set_parameters_callback

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.add_on_set_parameters_callback
```

````

````{py:method} add_post_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], None]) -> None
:canonical: agents.components.semantic_router.SemanticRouter.add_post_set_parameters_callback

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.add_post_set_parameters_callback
```

````

````{py:method} remove_pre_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], typing.List[rclpy.parameter.Parameter]]) -> None
:canonical: agents.components.semantic_router.SemanticRouter.remove_pre_set_parameters_callback

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.remove_pre_set_parameters_callback
```

````

````{py:method} remove_on_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], rcl_interfaces.msg.SetParametersResult]) -> None
:canonical: agents.components.semantic_router.SemanticRouter.remove_on_set_parameters_callback

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.remove_on_set_parameters_callback
```

````

````{py:method} remove_post_set_parameters_callback(callback: typing.Callable[[typing.List[rclpy.parameter.Parameter]], None]) -> None
:canonical: agents.components.semantic_router.SemanticRouter.remove_post_set_parameters_callback

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.remove_post_set_parameters_callback
```

````

````{py:method} describe_parameter(name: str) -> rcl_interfaces.msg.ParameterDescriptor
:canonical: agents.components.semantic_router.SemanticRouter.describe_parameter

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.describe_parameter
```

````

````{py:method} describe_parameters(names: typing.List[str]) -> typing.List[rcl_interfaces.msg.ParameterDescriptor]
:canonical: agents.components.semantic_router.SemanticRouter.describe_parameters

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.describe_parameters
```

````

````{py:method} set_descriptor(name: str, descriptor: rcl_interfaces.msg.ParameterDescriptor, alternative_value: typing.Optional[rcl_interfaces.msg.ParameterValue] = None) -> rcl_interfaces.msg.ParameterValue
:canonical: agents.components.semantic_router.SemanticRouter.set_descriptor

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.set_descriptor
```

````

````{py:method} add_waitable(waitable: rclpy.waitable.Waitable) -> None
:canonical: agents.components.semantic_router.SemanticRouter.add_waitable

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.add_waitable
```

````

````{py:method} remove_waitable(waitable: rclpy.waitable.Waitable) -> None
:canonical: agents.components.semantic_router.SemanticRouter.remove_waitable

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.remove_waitable
```

````

````{py:method} resolve_topic_name(topic: str, *, only_expand: bool = False) -> str
:canonical: agents.components.semantic_router.SemanticRouter.resolve_topic_name

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.resolve_topic_name
```

````

````{py:method} resolve_service_name(service: str, *, only_expand: bool = False) -> str
:canonical: agents.components.semantic_router.SemanticRouter.resolve_service_name

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.resolve_service_name
```

````

````{py:method} create_publisher(msg_type, topic: str, qos_profile: typing.Union[rclpy.qos.QoSProfile, int], *, callback_group: typing.Optional[rclpy.callback_groups.CallbackGroup] = None, event_callbacks: typing.Optional[rclpy.event_handler.PublisherEventCallbacks] = None, qos_overriding_options: typing.Optional[rclpy.qos_overriding_options.QoSOverridingOptions] = None, publisher_class: typing.Type[rclpy.publisher.Publisher] = Publisher) -> rclpy.publisher.Publisher
:canonical: agents.components.semantic_router.SemanticRouter.create_publisher

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_publisher
```

````

````{py:method} create_subscription(msg_type, topic: str, callback: typing.Callable[[rclpy.node.MsgType], None], qos_profile: typing.Union[rclpy.qos.QoSProfile, int], *, callback_group: typing.Optional[rclpy.callback_groups.CallbackGroup] = None, event_callbacks: typing.Optional[rclpy.event_handler.SubscriptionEventCallbacks] = None, qos_overriding_options: typing.Optional[rclpy.qos_overriding_options.QoSOverridingOptions] = None, raw: bool = False) -> rclpy.subscription.Subscription
:canonical: agents.components.semantic_router.SemanticRouter.create_subscription

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_subscription
```

````

````{py:method} create_service(srv_type, srv_name: str, callback: typing.Callable[[rclpy.node.SrvTypeRequest, rclpy.node.SrvTypeResponse], rclpy.node.SrvTypeResponse], *, qos_profile: rclpy.qos.QoSProfile = qos_profile_services_default, callback_group: rclpy.callback_groups.CallbackGroup = None) -> rclpy.service.Service
:canonical: agents.components.semantic_router.SemanticRouter.create_service

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_service
```

````

````{py:method} create_timer(timer_period_sec: float, callback: typing.Callable, callback_group: rclpy.callback_groups.CallbackGroup = None, clock: rclpy.clock.Clock = None) -> rclpy.timer.Timer
:canonical: agents.components.semantic_router.SemanticRouter.create_timer

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_timer
```

````

````{py:method} create_guard_condition(callback: typing.Callable, callback_group: rclpy.callback_groups.CallbackGroup = None) -> rclpy.guard_condition.GuardCondition
:canonical: agents.components.semantic_router.SemanticRouter.create_guard_condition

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_guard_condition
```

````

````{py:method} create_rate(frequency: float, clock: rclpy.clock.Clock = None) -> rclpy.timer.Rate
:canonical: agents.components.semantic_router.SemanticRouter.create_rate

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.create_rate
```

````

````{py:method} destroy_publisher(publisher: rclpy.publisher.Publisher) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.destroy_publisher

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_publisher
```

````

````{py:method} destroy_subscription(subscription: rclpy.subscription.Subscription) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.destroy_subscription

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_subscription
```

````

````{py:method} destroy_client(client: rclpy.client.Client) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.destroy_client

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_client
```

````

````{py:method} destroy_service(service: rclpy.service.Service) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.destroy_service

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_service
```

````

````{py:method} destroy_timer(timer: rclpy.timer.Timer) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.destroy_timer

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_timer
```

````

````{py:method} destroy_guard_condition(guard: rclpy.guard_condition.GuardCondition) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.destroy_guard_condition

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_guard_condition
```

````

````{py:method} destroy_rate(rate: rclpy.timer.Rate) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.destroy_rate

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_rate
```

````

````{py:method} destroy_node()
:canonical: agents.components.semantic_router.SemanticRouter.destroy_node

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.destroy_node
```

````

````{py:method} get_publisher_names_and_types_by_node(node_name: str, node_namespace: str, no_demangle: bool = False) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.semantic_router.SemanticRouter.get_publisher_names_and_types_by_node

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_publisher_names_and_types_by_node
```

````

````{py:method} get_subscriber_names_and_types_by_node(node_name: str, node_namespace: str, no_demangle: bool = False) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.semantic_router.SemanticRouter.get_subscriber_names_and_types_by_node

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_subscriber_names_and_types_by_node
```

````

````{py:method} get_service_names_and_types_by_node(node_name: str, node_namespace: str) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.semantic_router.SemanticRouter.get_service_names_and_types_by_node

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_service_names_and_types_by_node
```

````

````{py:method} get_client_names_and_types_by_node(node_name: str, node_namespace: str) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.semantic_router.SemanticRouter.get_client_names_and_types_by_node

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_client_names_and_types_by_node
```

````

````{py:method} get_topic_names_and_types(no_demangle: bool = False) -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.semantic_router.SemanticRouter.get_topic_names_and_types

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_topic_names_and_types
```

````

````{py:method} get_service_names_and_types() -> typing.List[typing.Tuple[str, typing.List[str]]]
:canonical: agents.components.semantic_router.SemanticRouter.get_service_names_and_types

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_service_names_and_types
```

````

````{py:method} get_node_names() -> typing.List[str]
:canonical: agents.components.semantic_router.SemanticRouter.get_node_names

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_node_names
```

````

````{py:method} get_fully_qualified_node_names() -> typing.List[str]
:canonical: agents.components.semantic_router.SemanticRouter.get_fully_qualified_node_names

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_fully_qualified_node_names
```

````

````{py:method} get_node_names_and_namespaces() -> typing.List[typing.Tuple[str, str]]
:canonical: agents.components.semantic_router.SemanticRouter.get_node_names_and_namespaces

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_node_names_and_namespaces
```

````

````{py:method} get_node_names_and_namespaces_with_enclaves() -> typing.List[typing.Tuple[str, str, str]]
:canonical: agents.components.semantic_router.SemanticRouter.get_node_names_and_namespaces_with_enclaves

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_node_names_and_namespaces_with_enclaves
```

````

````{py:method} get_fully_qualified_name() -> str
:canonical: agents.components.semantic_router.SemanticRouter.get_fully_qualified_name

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_fully_qualified_name
```

````

````{py:method} count_publishers(topic_name: str) -> int
:canonical: agents.components.semantic_router.SemanticRouter.count_publishers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.count_publishers
```

````

````{py:method} count_subscribers(topic_name: str) -> int
:canonical: agents.components.semantic_router.SemanticRouter.count_subscribers

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.count_subscribers
```

````

````{py:method} get_publishers_info_by_topic(topic_name: str, no_mangle: bool = False) -> typing.List[rclpy.topic_endpoint_info.TopicEndpointInfo]
:canonical: agents.components.semantic_router.SemanticRouter.get_publishers_info_by_topic

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_publishers_info_by_topic
```

````

````{py:method} get_subscriptions_info_by_topic(topic_name: str, no_mangle: bool = False) -> typing.List[rclpy.topic_endpoint_info.TopicEndpointInfo]
:canonical: agents.components.semantic_router.SemanticRouter.get_subscriptions_info_by_topic

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.get_subscriptions_info_by_topic
```

````

````{py:method} wait_for_node(fully_qualified_node_name: str, timeout: float) -> bool
:canonical: agents.components.semantic_router.SemanticRouter.wait_for_node

```{autodoc2-docstring} agents.components.semantic_router.SemanticRouter.wait_for_node
```

````

`````
