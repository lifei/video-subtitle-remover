import paddle
from _typeshed import Incomplete
from pathlib import Path

class AudioInfo:
    sample_rate: Incomplete
    num_samples: Incomplete
    num_channels: Incomplete
    bits_per_sample: Incomplete
    encoding: Incomplete
    def __init__(self, sample_rate: int, num_samples: int, num_channels: int, bits_per_sample: int, encoding: str) -> None: ...

def info(filepath: str) -> AudioInfo: ...
def load(filepath: str | Path, frame_offset: int = 0, num_frames: int = -1, normalize: bool = True, channels_first: bool = True) -> tuple[paddle.Tensor, int]: ...
def save(filepath: str, src: paddle.Tensor, sample_rate: int, channels_first: bool = True, encoding: str | None = None, bits_per_sample: int | None = 16): ...
