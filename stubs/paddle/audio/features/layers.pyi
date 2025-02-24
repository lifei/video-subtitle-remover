from ..functional import compute_fbank_matrix as compute_fbank_matrix, create_dct as create_dct, power_to_db as power_to_db
from ..functional.window import get_window as get_window
from _typeshed import Incomplete
from paddle import Tensor as Tensor, nn as nn

class Spectrogram(nn.Layer):
    power: Incomplete
    fft_window: Incomplete
    def __init__(self, n_fft: int = 512, hop_length: int | None = 512, win_length: int | None = None, window: str = 'hann', power: float = 1.0, center: bool = True, pad_mode: str = 'reflect', dtype: str = 'float32') -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...

class MelSpectrogram(nn.Layer):
    n_mels: Incomplete
    f_min: Incomplete
    f_max: Incomplete
    htk: Incomplete
    norm: Incomplete
    fbank_matrix: Incomplete
    def __init__(self, sr: int = 22050, n_fft: int = 2048, hop_length: int | None = 512, win_length: int | None = None, window: str = 'hann', power: float = 2.0, center: bool = True, pad_mode: str = 'reflect', n_mels: int = 64, f_min: float = 50.0, f_max: float | None = None, htk: bool = False, norm: str | float = 'slaney', dtype: str = 'float32') -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...

class LogMelSpectrogram(nn.Layer):
    ref_value: Incomplete
    amin: Incomplete
    top_db: Incomplete
    def __init__(self, sr: int = 22050, n_fft: int = 512, hop_length: int | None = None, win_length: int | None = None, window: str = 'hann', power: float = 2.0, center: bool = True, pad_mode: str = 'reflect', n_mels: int = 64, f_min: float = 50.0, f_max: float | None = None, htk: bool = False, norm: str | float = 'slaney', ref_value: float = 1.0, amin: float = 1e-10, top_db: float | None = None, dtype: str = 'float32') -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...

class MFCC(nn.Layer):
    dct_matrix: Incomplete
    def __init__(self, sr: int = 22050, n_mfcc: int = 40, n_fft: int = 512, hop_length: int | None = None, win_length: int | None = None, window: str = 'hann', power: float = 2.0, center: bool = True, pad_mode: str = 'reflect', n_mels: int = 64, f_min: float = 50.0, f_max: float | None = None, htk: bool = False, norm: str | float = 'slaney', ref_value: float = 1.0, amin: float = 1e-10, top_db: float | None = None, dtype: str = 'float32') -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
