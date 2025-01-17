from typing import Optional, Union, Dict, List
from pathlib import Path

from attrs import define, field, Factory

from .ros import base_validators, BaseComponentConfig, Topic, Route
from .utils import validate_kwargs

__all__ = [
    "LLMConfig",
    "MLLMConfig",
    "SpeechToTextConfig",
    "TextToSpeechConfig",
    "SemanticRouterConfig",
    "MapConfig",
    "VideoMessageMakerConfig",
    "VisionConfig",
]


@define(kw_only=True)
class ModelComponentConfig(BaseComponentConfig):
    warmup: Optional[bool] = field(default=False)


@define(kw_only=True)
class LLMConfig(ModelComponentConfig):
    """
    Configuration for the Large Language Model (LLM) component.

    It defines various settings that control how the LLM component operates, including
    whether to enable chat history, retreival augmented generation (RAG) and more.

    :param enable_rag: Enables or disables Retreival Augmented Generation.
    :type enable_rag: bool
    :param collection_name: The name of the vectordb collection to use for RAG.
    :type collection_name: Optional[str]
    :param distance_func: The distance metric used for nearest neighbor search for RAG.
        Supported values are "l2", "ip", and "cosine".
    :type distance_func: str
    :param n_results: The maximum number of results to return for RAG. Defaults to 1.
        For numbers greater than 1, results will be concatenated together in a single string.
    :type n_results: int
    :param chat_history: Whether to include chat history in the LLM's prompt.
    :type chat_history: bool
    :param history_reset_phrase: Phrase to reset chat history. Defaults to 'chat reset'
    :type history_reset_phrase: str
    :param history_size: Number of user messages to keep in chat history. Defaults to 10
    :type history_size: int
    :param temperature: Temperature used for sampling tokens during generation.
        Default is 0.8 and must be greater than 0.0.
    :type temperature: float
    :param max_new_tokens: The maximum number of new tokens to generate.
        Default is 100 and must be greater than 0.

    Example of usage:
    ```python
    config = LLMConfig(enable_rag=True, collection_name="my_collection", distance_func="l2")
    ```
    """

    enable_rag: bool = field(default=False)
    collection_name: Optional[str] = field(default=None)
    distance_func: str = field(
        default="l2", validator=base_validators.in_(["l2", "ip", "cosine"])
    )
    n_results: int = field(default=1)
    add_metadata: bool = field(default=False)
    chat_history: bool = field(default=False)
    history_reset_phrase: str = "chat reset"
    history_size: int = 10  # number of user messages
    temperature: float = field(default=0.8, validator=base_validators.gt(0.0))
    max_new_tokens: int = field(default=100, validator=base_validators.gt(0))
    _component_prompt: Optional[Union[str, Path]] = field(
        default=None, alias="_component_prompt"
    )
    _topic_prompts: Dict[str, Union[str, Path]] = field(
        default=Factory(dict), alias="_topic_prompts"
    )
    _tool_descriptions: List[Dict] = field(
        default=Factory(list), alias="_tool_descriptions"
    )
    _tool_response_flags: Dict[str, bool] = field(
        default=Factory(dict), alias="_tool_response_flags"
    )

    def _get_inference_params(self) -> Dict:
        """get_inference_params.
        :rtype: dict
        """
        return {
            "chat_history": self.chat_history,
            "temperature": self.temperature,
            "max_new_tokens": self.max_new_tokens,
        }


@define(kw_only=True)
class MLLMConfig(LLMConfig):
    """
    Configuration for the Multi-Modal Large Language Model (MLLM) component.

    It defines various settings that control how the LLM component operates, including
    whether to enable chat history, retreival augmented generation (RAG) and more.

    :param enable_rag: Enables or disables Retreival Augmented Generation.
    :type enable_rag: bool
    :param collection_name: The name of the vectordb collection to use for RAG.
    :type collection_name: Optional[str]
    :param distance_func: The distance metric used for nearest neighbor search for RAG.
        Supported values are "l2", "ip", and "cosine".
    :type distance_func: str
    :param n_results: The maximum number of results to return for RAG.
    :type n_results: int
    :param chat_history: Whether to include chat history in the MLLM's prompt.
    :type chat_history: bool
    :param temperature: Temperature used for sampling tokens during generation.
        Default is 0.7 and must be greater than 0.0.
    :type temperature: float
    :param max_new_tokens: The maximum number of new tokens to generate.
        Default is 100 and must be greater than 0.

    Example of usage:
    ```python
    config = MLLMConfig(enable_rag=True, collection_name="my_collection", distance_func="l2")
    ```
    """

    pass


@define(kw_only=True)
class VisionConfig(ModelComponentConfig):
    """Configuration for a detection component.

    The config allows you to customize the detection and/or tracking process.

    :param threshold: The confidence threshold for object detection, ranging from 0.1 to 1.0 (default: 0.5).
    :type threshold: float
    :param get_data_labels: Whether to return data labels along with detections (default: True).
    :type get_data_labels: bool
    :param labels_to_track: A list of specific labels to track, when the model is used as a tracker (default: None).
    :type labels_to_track: Optional[list]

    Example of usage:
    ```python
    config = DetectionConfig(threshold=0.3)
    ```
    """

    threshold: float = field(
        default=0.5, validator=base_validators.in_range(min_value=0.1, max_value=1.0)
    )
    get_data_labels: bool = field(default=True)
    labels_to_track: Optional[List[str]] = field(default=None)
    enable_visualization: Optional[bool] = field(default=False)

    def _get_inference_params(self) -> Dict:
        """get_inference_params.
        :rtype: dict
        """
        return {
            "threshold": self.threshold,
            "get_data_labels": self.get_data_labels,
            "labels_to_track": self.labels_to_track,
        }


@define(kw_only=True)
class TextToSpeechConfig(ModelComponentConfig):
    """Configuration for a Text-To-Speech component.

    This class defines the configuration options for a Text-To-Speech component.

    :param play_on_device: Whether to play the audio on available audio device (default: False).
    :type play_on_device: bool
    :param device: Device id (int) or name (sub-string) for playing the audio. Only effective if play_on_device is True (default: 'default').
    :type play_on_device: bool
    :param buffer_size: Size of the buffer for playing audio on device. Only effective if play_on_device is True (default: 20).
    :type buffer_size: int
    :param block_size: Size of the audio block to be read for playing audio on device. Only effective if play_on_device is True (default: 1024).
    :type block_size: int
    :param get_bytes: Whether the model should return the speech data as bytes instead of base64 encoded string(default: False).
    :type get_bytes: bool

    Example of usage:
    ```python
    config = TextToSpeechConfig(play_on_device=True, get_bytes=False)
    ```
    """

    play_on_device: bool = field(default=False)
    device: Union[int, str] = field(default="default")
    buffer_size: int = field(default=20)
    block_size: int = field(default=1024)
    get_bytes: bool = field(default=False)

    def _get_inference_params(self) -> Dict:
        """get_inference_params.
        :rtype: dict
        """
        return {"get_bytes": self.get_bytes}


@define(kw_only=True)
class SpeechToTextConfig(ModelComponentConfig):
    """
    Configuration for a Speech-To-Text component.

    This class defines the configuration options for a Speech-To-Text component.

    :param enable_vad: Enable Voice Activity Detection (VAD) to identify when speech is present in continuous input stream from an input audio device. Uses silero-vad model and requires, PyTorch to be installed.
                       Defaults to False.
    :type enable_vad: bool
    :param device: Device id (int) or name (sub-string) to use for audio input.
                   Only effective if enable_vad is set to true. Defaults to 'default'.
    :type device: Union[int, str]
    :param sample_rate: Sample rate of the audio stream in Hz. Must be 8000 or 16000.
                        Only effective if enable_vad is set to true. Default is 16000.
    :type sample_rate: int
    :param threshold: Minimum threshold above which speech is considered present.
                      Only effective if enable_vad is set to true. Defaults to 0.5 (50%).
    :type threshold: float
    :param min_silence_duration_ms: Minimum duration of silence in milliseconds before
                                     considering it as a speaker pause. Only effective if enable_vad is set to true. Defaults to 500 ms.
    :type min_silence_duration_ms: int
    :param speech_pad_ms: Duration in milliseconds to pad silence at the start and end
                           of detected speech regions. Only effective if enable_vad is set to true. Defaults to 30 ms.

    Example of usage:
    ```python
    config = SpeechToTextConfig(
        enable_vad=True,
        device="my_device",
        sample_rate=16000,
        threshold=0.5,
        min_silence_duration_ms=500,
        speech_pad_ms=30,
    )
    ```
    """

    enable_vad: bool = field(default=False)
    device: Union[int, str] = field(default="default")
    sample_rate: int = field(
        default=16000, validator=base_validators.in_([8000, 16000])
    )
    threshold: float = field(default=0.5)
    min_silence_duration_ms: int = field(default=500)
    speech_pad_ms: int = field(default=30)
    block_size: int = field(init=False)

    def __attrs_post_init__(self):
        self.block_size = 640 if self.sample_rate == 16000 else 320

    def _get_inference_params(self) -> Dict:
        """get_inference_params.
        :rtype: dict
        """
        return {}


def _get_optional_topic(topic: Union[Topic, Dict]) -> Optional[Topic]:
    if not topic:
        return
    if isinstance(topic, Topic):
        return topic
    return Topic(**topic)


@define(kw_only=True)
class MapConfig(BaseComponentConfig):
    """Configuration for a MapEncoding component.

    :param map_name: The name of the map.
    :type map_name: str
    :param distance_func: The function used to calculate distance when retreiving information from the map collection. Can be one of "l2" (L2 distance), "ip" (Inner Product), or "cosine" (Cosine similarity). Default is "l2".
    :type distance_func: str

    Example of usage:
    ```python
    config = MapConfig(map_name="my_map", distance_func="ip")
    ```
    """

    map_name: str = field()
    distance_func: str = field(
        default="l2", validator=base_validators.in_(["l2", "ip", "cosine"])
    )
    _position: Optional[Union[Topic, Dict]] = field(
        default=None, converter=_get_optional_topic, alias="_position"
    )
    _map_topic: Optional[Union[Topic, Dict]] = field(
        default=None, converter=_get_optional_topic, alias="_map_topic"
    )


def _get_optional_route(route: Union[Route, Dict]) -> Optional[Route]:
    if not route:
        return
    if isinstance(route, Route):
        return route
    return Route(**route)


@define(kw_only=True)
class SemanticRouterConfig(BaseComponentConfig):
    """Configuration parameters for a semantic router component.

    :param router_name: The name of the router.
    :type router_name: str
    :param distance_func: The function used to calculate distance from route samples in vectordb. Can be one of "l2" (L2 distance), "ip" (Inner Product), or "cosine" (Cosine similarity). Default is "l2".
    :type distance_func: str
    :param maximum_distance: The maximum distance threshold for routing. A value between 0.1 and 1.0. Defaults to 0.4
    :type maximum_distance: float

    Example of usage:
    ```python
    config = SemanticRouterConfig(router_name="my_router")
    # or
    config = SemanticRouterConfig(router_name="my_router", distance_func="ip", maximum_distance=0.7)
    ```
    """

    router_name: str = field()
    distance_func: str = field(
        default="l2", validator=base_validators.in_(["l2", "ip", "cosine"])
    )
    maximum_distance: float = field(
        default=0.4, validator=base_validators.in_range(min_value=0.1, max_value=1.0)
    )
    _default_route: Optional[Union[Route, Dict]] = field(
        default=None, converter=_get_optional_route, alias="_default_route"
    )


@define(kw_only=True)
class VideoMessageMakerConfig(BaseComponentConfig):
    """Configuration parameters for a video message maker component.

    :param min_video_frames: The minimum number of frames in a video segment. Default is 15, assuming a 0.5 second video at 30 fps.
    :type min_video_frames: int
    :param max_video_frames: The maximum number of frames in a video segment. Default is 600, assuming a 20 second video at 30 fps.
    :type max_video_frames: int
    :param motion_estimation_func: The function used for motion estimation. Can be one of "frame_difference" or "optical_flow". Default is None.
    :type motion_estimation_func: Optional[str]
    :param threshold: The threshold value for motion detection. A float between 0.1 and 5.0. Default is 0.3.
    :type threshold: float
    :param flow_kwargs: Additional keyword arguments for the optical flow algorithm. Default is a dictionary with reasonable values.

    Example of usage:
    ```python
    config = VideoMessageMakerConfig()
    # or
    config = VideoMessageMakerConfig(min_video_frames=30, motion_estimation_func="optical_flow", threshold=0.5)
    ```
    """

    min_video_frames: int = field(default=15)  # assuming 0.5 second video at 30 fps
    max_video_frames: int = field(default=600)  # assuming 20 second video at 30 fps
    motion_estimation_func: Optional[str] = field(
        default=None,
        validator=base_validators.in_(["frame_difference", "optical_flow"]),
    )
    threshold: float = field(
        default=0.3, validator=base_validators.in_range(min_value=0.1, max_value=5.0)
    )
    flow_kwargs: Dict = field(
        default={
            "pyr_scale": 0.5,
            "levels": 3,
            "winsize": 15,
            "iterations": 3,
            "poly_n": 5,
            "poly_sigma": 1.1,
            "flags": 0,
        },
        validator=validate_kwargs,
    )
