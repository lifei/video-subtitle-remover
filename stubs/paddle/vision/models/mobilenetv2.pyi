from ..ops import ConvNormActivation as ConvNormActivation
from _typeshed import Incomplete
from paddle import nn as nn
from paddle.utils.download import get_weights_path_from_url as get_weights_path_from_url

model_urls: Incomplete

class InvertedResidual(nn.Layer):
    stride: Incomplete
    use_res_connect: Incomplete
    conv: Incomplete
    def __init__(self, inp, oup, stride, expand_ratio, norm_layer=...) -> None: ...
    def forward(self, x): ...

class MobileNetV2(nn.Layer):
    num_classes: Incomplete
    with_pool: Incomplete
    last_channel: Incomplete
    features: Incomplete
    pool2d_avg: Incomplete
    classifier: Incomplete
    def __init__(self, scale: float = 1.0, num_classes: int = 1000, with_pool: bool = True) -> None: ...
    def forward(self, x): ...

def mobilenet_v2(pretrained: bool = False, scale: float = 1.0, **kwargs): ...
