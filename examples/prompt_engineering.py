from agents.components import Vision, MLLM
from agents.models import VisionModel, Idefics2
from agents.clients.roboml import RESPModelClient, HTTPModelClient
from agents.ros import Topic, Launcher
from agents.config import VisionConfig

image0 = Topic(name="image_raw", msg_type="Image")
detections_topic = Topic(name="detections", msg_type="Detections")

object_detection = VisionModel(
    name="object_detection", checkpoint="dino-4scale_r50_8xb2-12e_coco"
)
roboml_detection = RESPModelClient(object_detection)

detection_config = VisionConfig(threshold=0.5)
vision = Vision(
    inputs=[image0],
    outputs=[detections_topic],
    trigger=image0,
    config=detection_config,
    model_client=roboml_detection,
    component_name="detection_component",
)

text_query = Topic(name="text0", msg_type="String")
text_answer = Topic(name="text1", msg_type="String")

idefics = Idefics2(name="idefics_model")
idefics_client = HTTPModelClient(idefics)

mllm = MLLM(
    inputs=[text_query, image0, detections_topic],
    outputs=[text_answer],
    model_client=idefics_client,
    trigger=text_query,
)

mllm.set_component_prompt(
    template="""Imagine you are a robot.
    This image has following items: {{ detections }}.
    Answer the following about this image: {{ text0 }}"""
)
launcher = Launcher()
launcher.add_pkg(components=[vision, mllm])
launcher.bringup()
