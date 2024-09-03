from typing import Optional
import numpy as np
from .utils import VADStatus

try:
    import torch
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "VAD in SpeechToText components requires torchaudio and onnxruntime to be installed. Please install them with `pip install torchaudio onnxruntime`"
    ) from e

# VAD Model Singleton
model, _ = torch.hub.load("snakers4/silero-vad", "silero_vad", onnx=True)


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
        model,
        threshold: float = 0.5,
        sample_rate: int = 16000,
        min_silence_duration_ms: int = 500,
        speech_pad_ms: int = 30,
    ):
        self.model = model
        self.threshold = threshold
        self.sample_rate = sample_rate

        if sample_rate not in [8000, 16000]:
            raise ValueError(
                "VADIterator does not support sampling rates other than [8000, 16000]"
            )

        self.min_silence_samples = sample_rate * min_silence_duration_ms / 1000
        self.speech_pad_samples = sample_rate * speech_pad_ms / 1000
        self.reset_states()
        self.audio_chunks = []

    def reset_states(self):
        self.model.reset_states()
        self.triggered = False
        self.temp_end = 0
        self.current_sample = 0

    @torch.no_grad()
    def __call__(self, x: bytes) -> Optional[VADStatus]:
        """
        x: bytes
            audio chunks
        """
        # convert bytes to np.float32 and normalize
        x_np_f32 = (
            np.frombuffer(x, dtype=np.int16).astype(np.float32, order="C") / 32768
        )

        x_tensor = torch.from_numpy(x_np_f32)

        x_tensor = x_tensor.squeeze(1) if x_tensor.dim() == 2 else x_tensor

        window_size_samples = len(x_tensor)
        self.current_sample += window_size_samples

        speech_prob = self.model(x_tensor, self.sample_rate).item()

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
