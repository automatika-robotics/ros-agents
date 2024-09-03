from typing import Optional

from agents.clients.ollama import OllamaClient
from agents.clients.roboml import HTTPDBClient, HTTPModelClient, RESPModelClient
from agents.components import (
    LLM,
    MLLM,
    MapEncoding,
    SemanticRouter,
    SpeechToText,
    TextToSpeech,
    VideoMessageMaker,
    Vision,
)
from agents.config import (
    VisionConfig,
    LLMConfig,
    MapConfig,
    MLLMConfig,
    SemanticRouterConfig,
    SpeechToTextConfig,
    TextToSpeechConfig,
    VideoMessageMakerConfig,
)
from agents.models import Idefics2, Llama3, Llava, SpeechT5, Whisper, VisionModel
from agents.vectordbs import ChromaDB
from agents.ros import FixedInput, Topic, Launcher, MapLayer, Route

# Make a regular VQA component

text0 = Topic(name="text0", msg_type="String")
image0 = Topic(name="image_raw", msg_type="Image")
text1 = Topic(name="text1", msg_type="String")
detections_topic = Topic(name="detections", msg_type="Detections")

config = MLLMConfig()
idefics = Idefics2(name="idefics")
idefics_client = HTTPModelClient(idefics, logging_level="debug")

mllm = MLLM(
    inputs=[text0, image0, detections_topic],
    outputs=[text1],
    config=config,
    model_client=idefics_client,
    trigger=[text0],
    component_name="vqa",
)

mllm.set_component_prompt(
    template="You are an amazing and funny robot. You answer all questions with short and concise answers. This image has following items: {{ detections }}. Please answer the following about this image: {{ text0 }}"
)

# Make an introspective timed component with fixed input
text2 = FixedInput(
    name="text2",
    msg_type="String",
    fixed="What kind of a room is this? Is it an office, a bedroom or a kitchen? Give a one word answer, out of the given choices",
)
text3 = Topic(name="text3", msg_type="String")

model = Llava(name="llava")
model_client = OllamaClient(model, logging_level="debug")
introspector = MLLM(
    inputs=[text2, image0],
    outputs=[text3],
    config=config,
    model_client=model_client,
    trigger=15.0,
    component_name="introspector",
)


def introspection_validation(output: str) -> Optional[str]:
    """Validates the output of the introspective component before publication.
    :param output:
    :type output: str
    :rtype: Optional[str]
    """
    for option in ["office", "bedroom", "kitchen"]:
        if option in output.lower():
            return option


introspector.add_publisher_preprocessor(text3, introspection_validation)

# Make a map encoder
chroma = ChromaDB(name="MainDB")
db_client = HTTPDBClient(db=chroma, logging_level="debug")
position = Topic(name="odom", msg_type="Odometry")
map_meta_data = Topic(name="map_meta_data", msg_type="MapMetaData")

layer1 = MapLayer(subscribes_to=text3, resolution_multiple=3)

map_conf = MapConfig(map_name="map")
map = MapEncoding(
    layers=[layer1],
    position=position,
    map_meta_data=map_meta_data,
    config=map_conf,
    db_client=db_client,
    trigger=15.0,
)

# Create a video maker component
video0 = Topic(name="video0", msg_type="Video")

vid_maker_config = VideoMessageMakerConfig(motion_estimation_func="optical_flow")
video_maker = VideoMessageMaker(
    inputs=[image0], outputs=[video0], config=vid_maker_config, trigger=image0
)

# Start an llm component using ollama
llama = Llama3(
    name="llama",
    system_prompt="You are an amazing and funny robot assistant. You answer all questions with short and concise answers.",
)

ollama_client = OllamaClient(llama, logging_level="debug")

text4 = Topic(name="text4", msg_type="String")
text5 = Topic(name="text5", msg_type="String")

llm_config = LLMConfig()
llm = LLM(
    inputs=[text4],
    outputs=[text1],
    config=llm_config,
    model_client=ollama_client,
    trigger=[text4],
    component_name="llama",
)

# Semantic router that publishes to a Go To Anything topic for relevant queries
question = Topic(name="question", msg_type="String")
goto = Topic(name="goto", msg_type="String")

goto_route = Route(
    routes_to=goto,
    samples=[
        "Go to the door",
        "Go to the kitchen",
        "Get me a glass",
        "Fetch a ball",
        "Go to hallway",
        "Go over there",
    ],
)
mllm_route = Route(
    routes_to=text0,
    samples=[
        "Are we indoors or outdoors",
        "What do you see?",
        "Whats in front of you?",
        "Where are we",
        "Do you see any people?",
        "How many things are infront of you?",
        "Is this room occupied?",
    ],
)
llm_route = Route(
    routes_to=text4,
    samples=[
        "What is the capital of France?",
        "Is there life on Mars?",
        "How many tablespoons in a cup?",
        "How are you today?",
        "Whats up?",
    ],
)

router_config = SemanticRouterConfig(router_name="go-to-router", distance_func="l2")
router = SemanticRouter(
    inputs=[question],
    routes=[llm_route, mllm_route, goto_route],
    default_route=llm_route,
    config=router_config,
    db_client=db_client,
)

## define text to speech and speech to text interfaces
audio_in = Topic(name="audio0", msg_type="Audio")
audio_out = Topic(name="audio1", msg_type="Audio")

whisper = Whisper(name="whisper")
roboml_whisper = HTTPModelClient(whisper, logging_level="debug")

speech_config = SpeechToTextConfig()
speech_to_text = SpeechToText(
    inputs=[audio_in],
    outputs=[question],
    config=speech_config,
    model_client=roboml_whisper,
    trigger=audio_in,
)

speecht5 = SpeechT5(name="speecht5")
roboml_speecht5 = HTTPModelClient(speecht5)
text_config = TextToSpeechConfig()
text_to_speech = TextToSpeech(
    inputs=[text1],
    outputs=[audio_out],
    config=text_config,
    trigger=text1,
    model_client=roboml_speecht5,
)

# Add an object detection model
object_detection = VisionModel(name="object_detection", setup_trackers=True)
roboml_detection = RESPModelClient(object_detection, logging_level="debug")
detection_config = VisionConfig(labels_to_track=["bottle"])
tracking_topic = Topic(name="tracking", msg_type="Trackings")
vision = Vision(
    inputs=[image0],
    outputs=[detections_topic, tracking_topic],
    config=detection_config,
    trigger=image0,
    model_client=roboml_detection,
    component_name="detection_component",
)


# Launch the components
launcher = Launcher(
    components=[
        mllm,
        llm,
        introspector,
        video_maker,
        map,
        router,
        speech_to_text,
        text_to_speech,
        vision,
    ],
    enable_monitoring=False,
    activate_all_components_on_start=True,
)
launcher.on_fail(action_name="restart")
launcher.fallback_rate = 1 / 10  # 0.1 Hz or 10 seconds
launcher.bringup(ros_log_level="debug")
