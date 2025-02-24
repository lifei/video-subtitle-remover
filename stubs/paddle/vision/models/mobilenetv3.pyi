from ..ops import ConvNormActivation as ConvNormActivation
from _typeshed import Incomplete
from paddle import nn as nn
from paddle.utils.download import get_weights_path_from_url as get_weights_path_from_url

model_urls: Incomplete

class SqueezeExcitation(nn.Layer):
    avgpool: Incomplete
    fc1: Incomplete
    fc2: Incomplete
    activation: Incomplete
    scale_activation: Incomplete
    def __init__(self, input_channels, squeeze_channels, activation=..., scale_activation=...) -> None: ...
    def forward(self, input): ...

class InvertedResidualConfig:
    in_channels: Incomplete
    kernel: Incomplete
    expanded_channels: Incomplete
    out_channels: Incomplete
    use_se: Incomplete
    activation_layer: Incomplete
    stride: Incomplete
    def __init__(self, in_channels, kernel, expanded_channels, out_channels, use_se, activation, stride, scale: float = 1.0) -> None: ...
    @staticmethod
    def adjust_channels(channels, scale: float = 1.0): ...

class InvertedResidual(nn.Layer):
    use_res_connect: Incomplete
    use_se: Incomplete
    expand: Incomplete
    expand_conv: Incomplete
    bottleneck_conv: Incomplete
    mid_se: Incomplete
    linear_conv: Incomplete
    def __init__(self, in_channels, expanded_channels, out_channels, filter_size, stride, use_se, activation_layer, norm_layer) -> None: ...
    def forward(self, x): ...

class MobileNetV3(nn.Layer):
    config: Incomplete
    scale: Incomplete
    last_channel: Incomplete
    num_classes: Incomplete
    with_pool: Incomplete
    firstconv_in_channels: Incomplete
    lastconv_in_channels: Incomplete
    lastconv_out_channels: Incomplete
    conv: Incomplete
    blocks: Incomplete
    lastconv: Incomplete
    avgpool: Incomplete
    classifier: Incomplete
    def __init__(self, config, last_channel, scale: float = 1.0, num_classes: int = 1000, with_pool: bool = True) -> None: ...
    def forward(self, x): ...

class MobileNetV3Small(MobileNetV3):
    def __init__(self, scale: float = 1.0, num_classes: int = 1000, with_pool: bool = True) -> None: ...

class MobileNetV3Large(MobileNetV3):
    def __init__(self, scale: float = 1.0, num_classes: int = 1000, with_pool: bool = True) -> None: ...

def mobilenet_v3_small(pretrained: bool = False, scale: float = 1.0, **kwargs): ...
def mobilenet_v3_large(pretrained: bool = False, scale: float = 1.0, **kwargs): ...
