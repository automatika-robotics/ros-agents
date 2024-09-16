from typing import Optional, Union

import numpy as np

from ..clients.db_base import DBClient
from ..config import MapConfig
from ..ros import (
    MapMetaData,
    Odometry,
    String,
    Topic,
    Detections,
    MapLayer,
    component_action,
)
from ..utils import validate_func_args
from .component_base import Component, ComponentRunType


class MapEncoding(Component):
    """Map encoding component that encodes text information as a semantic map based on the robots localization.
    It takes in map layers, position topic, map meta data topic, and a vector database client.
    Map layers can be arbitrary text based outputs from other components such as MLLMs or Vision.

    :param layers: A list of map layer objects to be encoded.
    :type layers: list[MapLayer]
    :param position: The topic for the current robot position.
    :type position: Topic
    :param map_meta_data: The topic for storing and retrieving map metadata.
    :type map_meta_data: Topic
    :param config: The configuration for the map encoding component.
    :type config: MapConfig
    :param db_client: A database client to store and retrieve map data.
    :type db_client: DBClient
    :param trigger: An optional trigger value or topic that triggers the map encoding process.
    :type trigger: Union[Topic, list[Topic], float]
    :param callback_group: An optional callback group for the map encoding component.
    :param kwargs: Additional keyword arguments.

    Example usage:
    ```python
    position_topic = Topic(name="position", msg_type="Odometry")
    map_meta_data_topic = Topic(name="map_meta_data", msg_type="MapMetaData")
    config = MapConfig(map_name="map")
    db_client = DBClient(db=ChromaDB("database_name"))
    layers = [MapLayer(subscribes_to=text1, resolution_multiple=3),
              MapLayer(subscribes_to=detections1, temporal_change=True)]  # text1 and detections1 are String topics that are being published on by other components
    map_encoding_component = MapEncoding(
        layers=layers,
        position=position_topic,
        map_meta_data=map_meta_data_topic,
        config=config,
        db_client=db_client,
    )
    ```
    """

    @validate_func_args
    def __init__(
        self,
        *,
        layers: list[MapLayer],
        position: Topic,
        map_meta_data: Topic,
        config: MapConfig,
        db_client: DBClient,
        trigger: Union[Topic, list[Topic], float] = 10.0,
        callback_group=None,
        component_name="map_encoder_component",
        **kwargs,
    ):
        self.config: MapConfig = config
        self.allowed_inputs = {
            "Required": [String, Odometry, MapMetaData],
            "Optional": [Detections],
        }
        self.db_client = db_client
        self.position = position
        self.map_meta_data = map_meta_data
        super().__init__(
            None,
            None,
            config,
            trigger,
            callback_group,
            component_name,
            **kwargs,
        )

        # create layers
        self._layers(layers)

    def activate(self):
        """activate."""
        self.get_logger().debug(f"Current Status: {self.health_status.value}")
        # initialize db client
        self.db_client.check_connection()
        self.db_client.initialize()

        # activate the rest
        super().activate()

        # fill out pre-defined points in layers
        for layer in self.layers_dict.values():
            if layer.pre_defined and len(layer.pre_defined) > 0:
                self._fill_out_pre_defined(layer, layer.pre_defined)

    def deactivate(self):
        """deactivate."""
        # deactivate the rest
        super().deactivate()

        # deactivate db client
        self.db_client.check_connection()
        self.db_client.deinitialize()

    def _fill_out_pre_defined(
        self,
        layer: MapLayer,
        points: Union[list[tuple[np.ndarray, str]], tuple[np.ndarray, str]],
    ) -> None:
        """Fill out any pre-defined points in the MapLayer.

        :param layer:
        :type layer: MapLayer
        :param points:
        :type points: list[tuple[np.ndarray, str]] | tuple[np.ndarray, str]
        :rtype: None
        """
        self.get_logger().info(
            f"Adding points to map colletion: {self.config.map_name}"
        )

        time_stamp = self.get_ros_time().sec
        layer_name = layer.subscribes_to.name

        to_be_added = {
            "collection_name": self.config.map_name,
            "distance_func": self.config.distance_func,
            "ids": [],
            "documents": [],
            "metadatas": [],
        }

        # create a list in case of one point
        if not isinstance(points, list):
            points = [points]

        # add pre_defined points
        for data in points:
            coordinates_string = np.array2string(data[0], separator=",")[1:-1]
            # Create metadata
            metadata = {
                "layer_name": layer_name,
                "coordinates": coordinates_string,
                "timestamp": time_stamp,
                "temporal_change": layer.temporal_change,
            }

            id = (
                f"{layer_name}:{data[0]}:0"
                if not layer.temporal_change
                else f"{layer_name}:{data[0]}:{time_stamp}"
            )
            to_be_added["ids"].append(id)
            to_be_added["documents"].append(data[1])
            to_be_added["metadatas"].append(metadata)

        self.db_client.add(to_be_added)

    def _get_layer_data(
        self, time_stamp, map_coordinates
    ) -> tuple[Optional[dict[str, list]], Optional[dict[str, list]]]:
        """
        Gathers data from listeners and creates input for a map DB
        :param agg_obj: The aggregator object
        :param kwargs:  Additional keyword arguments
        :returns: DB input formatted data
        :rtype: dict
        """

        to_be_added = {
            "collection_name": self.config.map_name,
            "distance_func": self.config.distance_func,
            "ids": [],
            "documents": [],
            "metadatas": [],
        }
        to_be_checked = {
            "collection_name": self.config.map_name,
            "distance_func": self.config.distance_func,
            "ids": [],
            "documents": [],
            "metadatas": [],
        }

        for name, layer in self.layers_dict.items():
            if item := self.callbacks[name].get_output():
                # create layer metadata
                metadata = {}
                metadata["layer_name"] = name
                # set layer specific space coordinate based on resolution multiple
                relative_coordinates = map_coordinates // layer.resolution_multiple
                # convert ndarray to string for serialization and vectordb storage
                coordinates_string = np.array2string(
                    relative_coordinates, separator=","
                )[1:-1]
                metadata["coordinates"] = coordinates_string
                # set time_stamp and temporal_change flag
                metadata["temporal_change"] = layer.temporal_change
                metadata["time_stamp"] = time_stamp

                # create ids and assign to appropriate dict based on temporal_change
                if layer.temporal_change:
                    to_be_added["ids"].append(
                        f"{name}:{relative_coordinates}:{time_stamp}"
                    )
                    to_be_added["metadatas"].append(metadata)
                    to_be_added["documents"].append(item)
                else:
                    # time value remains 0 if layer assumed to be temporaly static
                    to_be_checked["ids"].append(f"{name}:{relative_coordinates}:0")
                    to_be_checked["metadatas"].append(metadata)
                    to_be_checked["documents"].append(item)

        # check for null
        if not to_be_added["ids"]:
            to_be_added = None
        if not to_be_checked["ids"]:
            to_be_checked = None

        return to_be_added, to_be_checked

    def _execution_step(self, **kwargs):
        """Execution step for Map component.
        :param args:
        :param kwargs:
        """
        time_stamp = self.get_ros_time().sec
        if self.run_type is ComponentRunType.EVENT:
            trigger = kwargs.get("topic")
            if not trigger:
                return
            self.get_logger().info(f"Received trigger of {trigger.name}")
        else:
            self.get_logger().info(f"Sending at {time_stamp}")

        # process position and meta data inputs
        position = self.callbacks[self.position.name].get_output()
        map_meta_data = self.callbacks[self.map_meta_data.name].get_output()

        # if position or map meta data is not received, do nothing
        if position is None or map_meta_data is None:
            self.get_logger().warning(
                f"Received position: {position}, map_meta_data: {map_meta_data}. Not sending data to map DB."
            )
            return

        # calculate relative coordinates (using configuration elements of position)
        map_coordinates = self._get_map_coordinates(position[:3], map_meta_data)

        # create input dict
        to_be_added, to_be_checked = self._get_layer_data(time_stamp, map_coordinates)

        if not to_be_added and not to_be_checked:
            self.get_logger().warning("Data not received on any layer")
            return

        if to_be_added:
            self.db_client.add(to_be_added)
        if to_be_checked:
            self.db_client.conditional_add(to_be_checked)

    def _get_map_coordinates(
        self, position: np.ndarray, map_meta_data: dict
    ) -> np.ndarray | None:
        """
        Get coordinates from position and map meta data
        :param position: relative position in meters
        :type position: np.ndarray | None
        :param map_meta_data: Dict with resolution, height and width of map
        :type map_meta_data: dict | None
        :rtype: np.ndarray | None
        """
        # get coordinates from position and map meta data
        if resolution := map_meta_data.get("resolution"):
            return position // resolution
        else:
            return None

    def _layers(self, layers: list[MapLayer]):
        """
        Set component layers.

        :param layers: List of layers
        :type layers: list[MapLayer]
        """
        self.layers_dict = {layer.subscribes_to.name: layer for layer in layers}
        layer_topics = [layer.subscribes_to for layer in layers]
        all_inputs = [*layer_topics, self.position, self.map_meta_data]
        self.validate_topics(all_inputs, self.allowed_inputs, "Inputs")
        self.callbacks = {
            input.name: input.msg_type.callback(input) for input in all_inputs
        }

    @component_action
    def add_point(self, layer: MapLayer, point: tuple[np.ndarray, str]) -> None:
        """Component action to add a user defined point to the map collection.
        This action can be executed on an event.

        :param layer: Layer to which the point should be added
        :type layer: MapLayer
        :param point: A tuple of position (numpy array) and text data (str)
        :type point: tuple[np.ndarray, str]
        :rtype: None
        """
        self._fill_out_pre_defined(layer, point)
