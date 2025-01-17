from typing import Any, Union, Optional, List, Dict
import queue
import threading

from ..clients.model_base import ModelClient
from ..config import SpeechToTextConfig
from ..ros import Audio, String, Topic
from ..utils import validate_func_args, VADStatus
from .model_component import ModelComponent
from .component_base import ComponentRunType


class SpeechToText(ModelComponent):
    """
    This component takes in audio input and outputs a text representation of the audio using Speech-to-Text models (e.g. Whisper).

    :param inputs: The input topics for the STT.
        This should be a list of Topic objects, limited to Audio type.
    :type inputs: list[Topic]
    :param outputs: The output topics for the STT.
        This should be a list of Topic objects, String type is handled automatically.
    :type outputs: list[Topic]
    :param model_client: The model client for the STT.
        This should be an instance of ModelClient.
    :type model_client: ModelClient
    :param config: The configuration for the STT.
        This should be an instance of SpeechToTextConfig. If not provided, defaults to SpeechToTextConfig().
    :type config: Optional[SpeechToTextConfig]
    :param trigger: The trigger value or topic for the STT.
        This can be a single Topic object, a list of Topic objects.
    :type trigger: Union[Topic, list[Topic], float]
    :param callback_group: An optional callback group for the STT.
        If provided, this should be a string. Otherwise, it defaults to None.
    :type callback_group: str
    :param component_name: The name of the STT component.
        This should be a string and defaults to "speechtotext_component".
    :type component_name: str

    Example usage:
    ```python
    audio_topic = Topic(name="audio", msg_type="Audio")
    text_topic = Topic(name="text", msg_type="String")
    config = SpeechToTextConfig(enable_vad=True)
    model = Whisper(name="whisper")
    model_client = ModelClient(model=model)
    stt_component = SpeechToText(
        inputs=[audio_topic],
        outputs=[text_topic],
        model_client=model_client,
        config=config,
        component_name='stt_component'
    )
    ```
    """

    @validate_func_args
    def __init__(
        self,
        *,
        inputs: List[Topic],
        outputs: List[Topic],
        model_client: ModelClient,
        config: Optional[SpeechToTextConfig] = None,
        trigger: Union[Topic, List[Topic]],
        component_name: str,
        callback_group=None,
        **kwargs,
    ):
        self.config: SpeechToTextConfig = config or SpeechToTextConfig()
        self.allowed_inputs = {"Required": [Audio]}
        self.handled_outputs = [String]

        if isinstance(trigger, float):
            raise TypeError(
                "SpeechToText component cannot be started as a timed component"
            )

        super().__init__(
            inputs,
            outputs,
            model_client,
            self.config,
            trigger,
            callback_group,
            component_name,
            **kwargs,
        )

    def custom_on_activate(self):
        """Custom activation"""
        # NOTE: Custom activate to ensure creation of separate thread if VAD is enabled
        # happens after activation as VAD starts sending received voice to execution
        # step right away

        # Activate component
        super().custom_on_activate()

        # If VAD is enabled, start a listening stream on a separate thread
        if self.config.enable_vad:
            from ..utils.vad import VADIterator

            self.event = threading.Event()
            self.queue = queue.Queue()
            self.vad_iterator = VADIterator(
                threshold=self.config.threshold,
                sample_rate=self.config.sample_rate,
                min_silence_duration_ms=self.config.min_silence_duration_ms,
                speech_pad_ms=self.config.speech_pad_ms,
            )
            self.listening_thread = threading.Thread(target=self._process_audio).start()

    def custom_on_deactivate(self):
        # If VAD is enabled, stop the listening stream thread
        if self.config.enable_vad:
            self.event.set()
            if self.listening_thread:
                self.listening_thread.join()

        # Deactivate component
        super().custom_on_deactivate()

    def _create_input(self, *_, **kwargs) -> Optional[Dict[str, Any]]:
        """Create inference input for SpeechToText models
        :param args:
        :param kwargs:
        :rtype: dict[str, Any]
        """

        if self.config.enable_vad and kwargs.get("vad") is not None:
            query = kwargs["vad"]
        else:
            # set query as trigger
            trigger = kwargs.get("topic")
            if not trigger:
                return None
            query = self.trig_callbacks[trigger.name].get_output()
            if query is None or len(query) == 0:
                return None

        return {"query": query, **self.config._get_inference_params()}

    def _stream_callback(
        self, indata: bytes, frames: int, _, status
    ) -> tuple[bytes, int]:
        """Stream callback function for processing audio

        :param indata:
        :type indata: np.ndarray
        :param frames:
        :type frames: int
        :param _:
        :param status:
        :type status: sd.CallbackFlags
        :rtype: None
        """
        assert frames == self.config.block_size
        if status:
            self.get_logger().warn(f"Status: {status}")
        try:
            import pyaudio
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "enable_vad configuration for SpeechToText component requires pyaudio module to be installed. Please install it with `pip install pyaudio`"
            ) from e
        vad_output = self.vad_iterator(indata)
        if vad_output:
            self.queue.put_nowait(vad_output)
        return indata, pyaudio.paContinue

    def _process_audio(self) -> None:
        """Creates a stream to process audio from device"""

        # clear event and queue
        self.queue.queue.clear()
        self.event.clear()

        try:
            import pyaudio
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "enable_vad configuration for SpeechToText component requires pyaudio module to be installed. Please install it with `pip install pyaudio`"
            ) from e
        # Create an interface to PortAudio
        audio_interface = pyaudio.PyAudio()

        stream = audio_interface.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.config.sample_rate,
            frames_per_buffer=self.config.block_size,
            input=True,
            start=True,
            stream_callback=self._stream_callback,  # type: ignore
        )

        while True:
            vad_output = self.queue.get()
            if vad_output is VADStatus.START:
                # Do stuff when someone starts speaking
                self.get_logger().debug("Speech started")
            if vad_output is VADStatus.END:
                # Send audio when speech finishes
                self.get_logger().debug("Speech ended")
                self._execution_step(vad=True)
            if self.event.is_set():
                stream.stop_stream()
                stream.close()
                audio_interface.terminate()
                break
        self.event.wait()

    def _execution_step(self, *args, **kwargs):
        """_execution_step.

        :param args:
        :param kwargs:
        """
        # Check for vad before checking for triggers
        if self.config.enable_vad and kwargs.get("vad"):
            self.get_logger().debug("Received speech from vad")
            kwargs["vad"] = self.vad_iterator.get_chunks()
        elif self.run_type is ComponentRunType.EVENT:
            trigger = kwargs.get("topic")
            if not trigger:
                return
            self.get_logger().debug(f"Received trigger on topic {trigger.name}")
        else:
            time_stamp = self.get_ros_time().sec
            self.get_logger().debug(f"Sending at {time_stamp}")

        # create inference input
        inference_input = self._create_input(*args, **kwargs)
        # call model inference
        if not inference_input:
            self.get_logger().warning("Input not received, not calling model inference")
            return

        # conduct inference
        if self.model_client:
            result = self.model_client.inference(inference_input)
            if result:
                # publish inference result
                if self.publishers_dict:
                    for publisher in self.publishers_dict.values():
                        publisher.publish(**result)
            else:
                # raise a fallback trigger via health status
                self.health_status.set_failure()

    def _warmup(self):
        """Warm up and stat check"""
        import time
        from pathlib import Path

        with open(
            str(Path(__file__).parents[1] / Path("resources/test.wav")), "rb"
        ) as file:
            file_bytes = file.read()

        inference_input = {"query": file_bytes, **self.config._get_inference_params()}

        # Run inference once to warm up and once to measure time
        self.model_client.inference(inference_input)

        start_time = time.time()
        result = self.model_client.inference(inference_input)
        elapsed_time = time.time() - start_time

        self.get_logger().warning(f"Model Output: {result}")
        self.get_logger().warning(f"Approximate Inference time: {elapsed_time} seconds")
        self.get_logger().warning(
            f"RTF: {elapsed_time / 2}"  # audio length, 2 seconds
        )
