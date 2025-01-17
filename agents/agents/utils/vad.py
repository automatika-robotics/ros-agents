from typing import Optional
import numpy as np
from .utils import VADStatus, load_model

try:
    import onnxruntime as ort
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "VAD in SpeechToText components requires onnxruntime to be installed. Please install them with `pip install onnxruntime`"
    ) from e

# VAD Model Singleton
vad_model_url = "https://raw.githubusercontent.com/snakers4/silero-vad/refs/heads/master/src/silero_vad/data/silero_vad.onnx"


class VADIterator:
    """Adapted from https://github.com/snakers4/silero-vad/blob/master/src/silero_vad/utils_vad.py
    Check out https://github.com/snakers4/silero-vad
    Citation:
        @misc{Silero VAD,
          author = {Silero Team},
          title = {Silero VAD: pre-trained enterprise-grade Voice Activity Detector (VAD), Number Detector and Language Classifier},
          year = {2024},
          publisher = {GitHub},
          journal = {GitHub repository},
          howpublished = {https://github.com/snakers4/silero-vad},
          commit = {insert_some_commit_here},
          email = {hello@silero.ai}
        }

    """

    def __init__(
        self,
        model_path: str = load_model("silero_vad", vad_model_url),
        threshold: float = 0.5,
        sample_rate: int = 16000,
        min_silence_duration_ms: int = 500,
        speech_pad_ms: int = 30,
    ):
        self.threshold = threshold

        if sample_rate not in [8000, 16000]:
            raise ValueError(
                "VADIterator does not support sampling rates other than [8000, 16000]"
            )
        self.sample_rate = np.array(sample_rate).astype(np.int64)

        # Initialize the ONNX model
        sessionOptions = ort.SessionOptions()
        sessionOptions.inter_op_num_threads = 1
        sessionOptions.intra_op_num_threads = 1

        self.model = ort.InferenceSession(
            model_path, sess_options=sessionOptions, providers=["CPUExecutionProvider"]
        )

        self._state = np.zeros((2, 1, 128)).astype("float32")

        self.min_silence_samples = sample_rate * min_silence_duration_ms / 1000
        self.speech_pad_samples = sample_rate * speech_pad_ms / 1000

        self.reset_states()
        self.audio_chunks = []

    def reset_states(self):
        self.triggered = False
        self.temp_end = 0
        self.current_sample = 0

    def __call__(self, x: bytes) -> Optional[VADStatus]:
        """
        x: bytes
            audio chunks
        """
        # convert bytes to np.float32 and normalize
        x_np_f32 = (
            np.frombuffer(x, dtype=np.int16).astype(np.float32, order="C") / 32768
        )
        window_size_samples = x_np_f32.shape[0]
        self.current_sample += window_size_samples

        ort_inputs = {
            "input": x_np_f32[None,],
            "state": self._state,
            "sr": self.sample_rate,
        }

        out, self._state = self.model.run(None, ort_inputs)

        speech_prob = out[0][0]

        if (speech_prob >= self.threshold) and self.temp_end:
            self.temp_end = 0

        if (speech_prob >= self.threshold) and not self.triggered:
            self.triggered = True
            return VADStatus.START

        if (speech_prob < self.threshold - 0.15) and self.triggered:
            if not self.temp_end:
                self.temp_end = self.current_sample
            if self.current_sample - self.temp_end < self.min_silence_samples:
                return None
            else:
                self.temp_end = 0
                self.triggered = False
                return VADStatus.END

        if self.triggered:
            self.audio_chunks.append(x)

        return None

    def get_chunks(self) -> Optional[bytes]:
        """Get detected speech chunks"""
        if len(self.audio_chunks) > 0:
            _audio = b"".join(self.audio_chunks)
            self.audio_chunks = []
            return _audio
