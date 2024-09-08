"""The following classes provide wrappers for data being transmitted via ROS topics. These classes form the inputs and outputs of [Components](agents.components.md)."""

from typing import Union, Any
import numpy as np
from attrs import define, field, Factory

# FROM AUTOROS
from ros_sugar.supported_types import (
    SupportedType,
    Audio,
    Image,
    MapMetaData,
    Odometry,
    String,
    ROSImage,
)
from ros_sugar.topic import (
    BaseTopic,
    QoSConfig,
    _normalize_topic_name,
    supported_types,
    get_all_msg_types,
    get_msg_type,
)

# FROM ROS_SUGAR
from ros_sugar import base_validators
from ros_sugar.base_attrs import BaseAttrs
from ros_sugar.config import BaseComponentConfig, ComponentRunType
from ros_sugar.component import BaseComponent
from ros_sugar.launcher import Launcher
from ros_sugar.utils import component_action

# LEIBNIZ TYPES
from agents_interfaces.msg import Point2D, Bbox2D, Detection2D, Detections2D
from agents_interfaces.msg import (
    Video as ROSVideo,
    Tracking as ROSTracking,
    Trackings as ROSTrackings,
)
from .callbacks import ObjectDetectionCallback, VideoCallback

__all__ = [
    "String",
    "Audio",
    "Image",
    "MapMetaData",
    "Odometry",
    "Topic",
    "FixedInput",
    "base_validators",
    "BaseAttrs",
    "BaseComponent",
    "BaseComponentConfig",
    "ComponentRunType",
    "Launcher",
    "component_action",
    "MapLayer",
    "Route",
]


def get_msg_type_extra(
    type_name: Union[type[supported_types.SupportedType], str],
) -> Union[type[supported_types.SupportedType], str]:
    """Closure around verification function in ros_sugar to provide additional types."""
    return get_msg_type(
        type_name, additional_types=[Video, Detection, Detections, Tracking, Trackings]
    )


class Video(SupportedType):
    """Video."""

    _ros_type = ROSVideo
    callback = VideoCallback

    @classmethod
    def convert(cls, output: Union[list[ROSImage], list[np.ndarray]], **_) -> ROSVideo:
        """
        Takes an list of images and retunrs a video message (Image Array)
        :return: Video
        """
        frames = [Image.convert(frame) for frame in output]
        msg = ROSVideo()
        msg.frames = frames
        return msg


class Detection(SupportedType):
    """Detection."""

    _ros_type = Detection2D
    callback = None  # not defined

    @classmethod
    def convert(cls, output: dict, img: np.ndarray, **_) -> Detection2D:
        """
        Takes object detection data and converts it into a ROS message
        of type Detection2D
        :return: Detection2D
        """
        msg = Detection2D()
        msg.scores = output["scores"]
        msg.labels = output["labels"]
        boxes = []
        for bbox in output["bboxes"]:
            box = Bbox2D()
            box.top_left_x = bbox[0]
            box.top_left_y = bbox[1]
            box.bottom_right_x = bbox[2]
            box.bottom_right_y = bbox[3]
            boxes.append(box)

        msg.boxes = boxes
        msg.image = Image.convert(img)
        return msg


class Detections(SupportedType):
    """Detections."""

    _ros_type = Detections2D
    callback = ObjectDetectionCallback

    @classmethod
    def convert(cls, output: list, images: list, **_) -> Detections2D:
        """
        Takes object detections data and converts it into a ROS message
        of type Detections2D
        :return: Detections2D
        """
        msg = Detections2D()
        detections = []
        for img, detection in zip(images, output):
            detections.append(Detection.convert(detection, img))
        msg.detections = detections
        return msg


class Tracking(SupportedType):
    """Tracking."""

    _ros_type = ROSTracking
    callback = None  # Not defined

    @classmethod
    def convert(cls, output: dict, img: np.ndarray, **_) -> ROSTracking:
        """
        Takes tracking data and converts it into a ROS message
        of type Tracking
        :return: ROSTracking
        """
        msg = ROSTracking()
        msg.ids = output.get("ids") or []
        msg.labels = output.get("tracked_labels") or []
        centroids = []
        estimated_velocities = []
        # assumes centroids and estimated_velocities would be of equal length
        if o_centroids := output.get("centroids") and (
            o_estimated_velocities := output.get("estimated_velocities")
        ):
            for obj_centroids, obj_vels in zip(o_centroids, o_estimated_velocities):
                for obj_instance_c, obj_instance_v in zip(obj_centroids, obj_vels):
                    centroid = Point2D()
                    centroid.x = obj_instance_c[0]
                    centroid.y = obj_instance_c[1]
                    centroids.append(centroid)
                    estimated_velocity = Point2D()
                    estimated_velocity.x = obj_instance_v[0]
                    estimated_velocity.y = obj_instance_v[1]
                    estimated_velocities.append(estimated_velocity)

        msg.centroids = centroids
        msg.estimated_velocities = estimated_velocities
        msg.image = Image.convert(img)
        return msg


class Trackings(SupportedType):
    """Trackings."""

    _ros_type = ROSTrackings
    callback = None  # Not defined

    @classmethod
    def convert(cls, output: list, images: list, **_) -> ROSTrackings:
        """
        Takes trackings data and converts it into a ROS message
        of type ROSTrackings
        :return: ROSTrackings
        """
        msg = ROSTrackings()
        trackings = []
        for img, tracking in zip(images, output):
            trackings.append(Tracking.convert(tracking, img))
        msg.trackings = trackings
        return msg


@define(kw_only=True)
class Topic(BaseTopic):
    """
    A topic is an idomatic wrapper for a ROS topic, which is essentially a pub/sub queue. Topics can be given as inputs or outputs to components. When given as inputs, components automatically create listeners for the topics upon their activation. And when given as outputs, components create publishers for publishing to the topic.

    :param name: Name of the topic
    :type name: str
    :param msg_type: One of the SupportedTypes. This parameter can be set by passing the SupportedType data-type name as a string
    :type msg_type: Union[type[supported_types.SupportedType], str]
    :param qos_profile: QoS profile for the topic
    :type qos_profile: QoSConfig

    Example usage:
    ```python
    position = Topic(name="odom", msg_type="Odometry")
    map_meta_data = Topic(name="map_meta_data", msg_type="MapMetaData")
    ```
    """

    name: str = field(converter=_normalize_topic_name)
    msg_type: Union[type[supported_types.SupportedType], str] = field(
        converter=get_msg_type_extra,
        validator=base_validators.in_(
            get_all_msg_types(
                additional_types=[Video, Detection, Detections, Tracking, Trackings]
            )
        ),
    )
    qos_profile: QoSConfig = Factory(QoSConfig)
    ros_msg_type: Any = field(init=False)

    @msg_type.validator
    def _update_ros_type(self, _, value):
        """_update_ros_type.

        :param _:
        :param value:
        """
        self.ros_msg_type = value._ros_type


@define(kw_only=True)
class FixedInput(BaseAttrs):
    """
    A FixedInput can be provided to components as input and is similar to a Topic except components do not create a subscriber to it and whenever they _read_ it, they always get the same data. The nature of the data depends on the _msg_type_ specified.

    :param name: Name of the topic
    :type name: str
    :param msg_type: One of the SupportedTypes. This parameter can be set by passing the SupportedType data-type name as a string
    :type msg_type: Union[type[supported_types.SupportedType], str]
    :param fixed: Fixed input string or path to a file. Various SupportedTypes implement FixedInput processing differently.
    :type fixed: str | Path

    Example usage:
    ```python
    text0 = FixedInput(
        name="text2",
        msg_type="String",
        fixed="What kind of a room is this? Is it an office, a bedroom or a kitchen? Give a one word answer, out of the given choices")
    ```
    """

    name: str = field(converter=_normalize_topic_name)
    msg_type: Union[type[supported_types.SupportedType], str] = field(
        converter=get_msg_type_extra,
        validator=base_validators.in_(
            get_all_msg_types(
                additional_types=[Video, Detection, Detections, Tracking, Trackings]
            )
        ),
    )
    fixed: Any = field()


@define(kw_only=True)
class MapLayer(BaseAttrs):
    """A MapLayer represents a single input for a MapEncoding component. It can subscribe to a specific text topic.

    :param subscribes_to: The topic that this map layer is subscribed to.
    :type subscribes_to: Topic
    :param temporal_change: Indicates whether the map should store changes over time for the same position. Defaults to False.
    :type temporal_change: bool
    :param resolution_multiple: A positive multiplication factor for the base resolution of the map grid, for fine or coarse graining the map. Defaults to 1.
    :type resolution_multiple: int
    :param pre_defined: An optional list of pre-defined data points in the layer. Each datapoint is a tuple of [position, text], where position is a numpy array of coordinates.
    :type pre_defined: list[tuple[np.ndarray, str]]

    Example of usage:
    ```python
    my_map_layer = MapLayer(subscribes_to='my_topic', temporal_change=True)
    ```
    """

    subscribes_to: Topic = field()
    temporal_change: bool = field(default=False)
    resolution_multiple: int = field(
        default=1, validator=base_validators.in_range(min_value=0.1, max_value=10)
    )
    pre_defined: list[tuple[np.ndarray, str]] = Factory(list)


@define(kw_only=True)
class Route(BaseAttrs):
    """
    A Route defines a topic to be routed to by the SemanticRouter, along with samples of similar text that the input must match to for the route to be used.

    :param routes_to: The topic that the input to the SemanticRouter is routed to.
    :type routes_to: Topic
    :param samples: A list of sample text strings associated with this route.
    :type samples: list[str]

    Example of usage:
    ```python
    goto_route = Route(routes_to='goto', samples=['Go to the door', 'Go to the kitchen'])
    ```
    """

    routes_to: Topic = field()
    samples: list[str] = field()
