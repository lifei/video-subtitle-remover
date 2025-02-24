import paddle
from ..features import LogMelSpectrogram as LogMelSpectrogram, MFCC as MFCC, MelSpectrogram as MelSpectrogram, Spectrogram as Spectrogram
from _typeshed import Incomplete

feat_funcs: Incomplete

class AudioClassificationDataset(paddle.io.Dataset):
    files: Incomplete
    labels: Incomplete
    feat_type: Incomplete
    sample_rate: Incomplete
    feat_config: Incomplete
    def __init__(self, files: list[str], labels: list[int], feat_type: str = 'raw', sample_rate: int = None, **kwargs) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
