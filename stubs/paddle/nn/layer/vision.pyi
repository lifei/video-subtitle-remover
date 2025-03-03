from .. import functional as functional
from .layers import Layer as Layer
from _typeshed import Incomplete

class PixelShuffle(Layer):
    def __init__(self, upscale_factor, data_format: str = 'NCHW', name: Incomplete | None = None) -> None: ...
    def forward(self, x): ...
    def extra_repr(self): ...

class PixelUnshuffle(Layer):
    def __init__(self, downscale_factor, data_format: str = 'NCHW', name: Incomplete | None = None) -> None: ...
    def forward(self, x): ...
    def extra_repr(self): ...

class ChannelShuffle(Layer):
    def __init__(self, groups, data_format: str = 'NCHW', name: Incomplete | None = None) -> None: ...
    def forward(self, x): ...
    def extra_repr(self): ...
