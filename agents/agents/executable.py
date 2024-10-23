import argparse
from typing import List

import rclpy
import setproctitle
from rclpy.executors import MultiThreadedExecutor
from rclpy.utilities import try_shutdown

from . import config as all_configs
from . import components as all_components
from . import clients
from .ros import Topic, FixedInput, MapLayer, Route


def _parse_args() -> tuple[argparse.Namespace, List[str]]:
    """Parse arguments."""
    parser = argparse.ArgumentParser(description="Component Executable Config")
    parser.add_argument(
        "--config_type", type=str, help="Component configuration class name"
    )
    parser.add_argument("--component_type", type=str, help="Component class name")
    parser.add_argument(
        "--node_name",
        type=str,
        help="Component ROS2 node name",
    )
    parser.add_argument("--config", type=str, help="Component configuration object")
    parser.add_argument(
        "--inputs",
        type=str,
        help="Component input topics",
    )
    parser.add_argument(
        "--outputs",
        type=str,
        help="Component output topics",
    )
    parser.add_argument(
        "--routes",
        type=str,
        help="Semantic router routes",
    )
    parser.add_argument(
        "--layers",
        type=str,
        help="Map Encoding layers",
    )
    parser.add_argument(
        "--config_file", type=str, help="Path to configuration YAML file"
    )
    parser.add_argument(
        "--events", type=str, help="Events to be monitored by the component"
    )
    parser.add_argument(
        "--actions", type=str, help="Actions associated with the component Events"
    )
    parser.add_argument(
        "--external_processors",
        type=str,
        help="External processors associated with the component input and output topics",
    )
    return parser.parse_known_args()


def _parse_component_config(args: argparse.Namespace) -> all_configs.ComponentConfig:
    """Parse the component config object

    :param args: Command line arguments
    :type args: argparse.Namespace

    :return: Component config object
    :rtype: object
    """
    config_type = args.config_type or None
    if not config_type:
        raise ValueError("config_type must be provided")

    # Get config type and update from json arg
    config_class = getattr(all_configs, config_type)
    if not config_class:
        raise TypeError(
            f"Unknown config_type '{config_type}'. Known types are {all_configs.__all__}"
        )

    config = config_class()
    config.from_json(args.config)

    return config


def _parse_ros_args(args_names: List[str]) -> List[str]:
    """Parse ROS arguments from command line arguments

    :param args_names: List of all parsed arguments
    :type args_names: list[str]

    :return: List ROS parsed arguments
    :rtype: list[str]
    """
    # Look for --ros-args in ros_args
    ros_args_start = None
    if "--ros-args" in args_names:
        ros_args_start = args_names.index("--ros-args")

    if ros_args_start is not None:
        ros_specific_args = args_names[ros_args_start:]
    else:
        ros_specific_args = []
    return ros_specific_args


def main():
    """Executable main function to run a component as a ROS2 node in a new process.
    Used to start a node using ROS Sugar Launcher. Extends functionality from ROS Sugar

    :param list_of_components: List of all known Component classes in the package
    :type list_of_components: List[Type]
    :param list_of_configs: List of all known ComponentConfig classes in the package
    :type list_of_configs: List[Type]
    :raises ValueError: If component or component config are unknown classes
    :raises ValueError: If component cannot be started with provided arguments
    """
    args, args_names = _parse_args()

    # Initialize rclpy with the ros-specific arguments
    rclpy.init(args=_parse_ros_args(args_names))

    component_type = args.component_type or None

    if not component_type:
        raise ValueError("Cannot launch without providing a component_type")

    comp_class = getattr(all_components, component_type)

    if not comp_class:
        raise ValueError(
            f"Cannot launch unknown component type '{component_type}'. Known types are: '{all_components.__all__}'"
        )

    # Get name
    component_name = args.node_name or None

    if not component_name:
        raise ValueError("Cannot launch component without specifying a name")

    # SET PROCESS NAME
    setproctitle.setproctitle(component_name)

    config = _parse_component_config(args)

    # Get Yaml config file if provided
    config_file = args.config_file or None

    # Get inputs/outputs
    inputs = (
        [FixedInput(**i) if i.get("fixed") else Topic(**i) for i in args.inputs]
        if args.inputs
        else None
    )
    outputs = [Topic(**o) for o in args.outputs] if args.outputs else None
    layers = [MapLayer(**i) for i in args.layers] if args.layers else None
    routes = [Route(**r) for r in args.routes] if args.routes else None

    # Init the component
    # Semantic Router Component
    if comp_class == all_components.SemanticRouter.__name__:
        db_client = getattr(clients, config._db_client["client_type"])(
            **config._db_client
        )
        component = comp_class(
            inputs=inputs,
            routes=routes,
            db_client=db_client,
            config=config,
            component_name=component_name,
            config_file=config_file,
        )
    # Map Encoding Component
    elif comp_class == all_components.MapEncoding.__name__:
        db_client = getattr(clients, config._db_client["client_type"])(
            **config._db_client
        )
        component = comp_class(
            layers=layers,
            position=config._position,
            map_topic=config._map_topic,
            db_client=db_client,
            config=config,
            component_name=component_name,
            config_file=config_file,
        )

    # All other components
    else:
        model_client = (
            getattr(clients, config._model_client["client_type"])(
                **config._model_client
            )
            if config._model_client
            else None
        )
        db_client = (
            getattr(clients, config._db_client["client_type"])(**config._db_client)
            if config._db_client
            else None
        )

        component = comp_class(
            inputs=inputs,
            outputs=outputs,
            model_client=model_client,
            db_client=db_client,
            config=config,
            component_name=component_name,
            config_file=config_file,
        )

    # Init the node with rclpy
    component.rclpy_init_node()

    # Set events/actions
    events_json = args.events or None
    actions_json = args.actions or None

    if events_json and actions_json:
        component._events_json = events_json
        component._actions_json = actions_json

    # Set external processors
    external_processors = args.external_processors or None
    if external_processors:
        component._external_processors_json = external_processors

    executor = MultiThreadedExecutor()

    executor.add_node(component)

    try:
        executor.spin()

    except KeyboardInterrupt:
        pass

    finally:
        executor.remove_node(component)
        try_shutdown()