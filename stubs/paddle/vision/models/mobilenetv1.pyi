from ..ops import ConvNormActivation as ConvNormActivation
from _typeshed import Incomplete
from paddle import nn as nn
from paddle.utils.download import get_weights_path_from_url as get_weights_path_from_url

model_urls: Incomplete

class DepthwiseSeparable(nn.Layer):
    def __init__(self, in_channels, out_channels1, out_channels2, num_groups, stride, scale) -> None: ...
    def forward(self, x): ...

class MobileNetV1(nn.Layer):
    scale: Incomplete
    dwsl: Incomplete
    num_classes: Incomplete
    with_pool: Incomplete
    conv1: Incomplete
    pool2d_avg: Incomplete
    fc: Incomplete
    def __init__(self, scale: float = 1.0, num_classes: int = 1000, with_pool: bool = True) -> None: ...
    def forward(self, x): ...

def mobilenet_v1(pretrained: bool = False, scale: float = 1.0, **kwargs): ...
