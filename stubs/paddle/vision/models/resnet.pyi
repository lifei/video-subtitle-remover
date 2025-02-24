from _typeshed import Incomplete
from paddle import nn as nn
from paddle.utils.download import get_weights_path_from_url as get_weights_path_from_url

model_urls: Incomplete

class BasicBlock(nn.Layer):
    expansion: int
    conv1: Incomplete
    bn1: Incomplete
    relu: Incomplete
    conv2: Incomplete
    bn2: Incomplete
    downsample: Incomplete
    stride: Incomplete
    def __init__(self, inplanes, planes, stride: int = 1, downsample: Incomplete | None = None, groups: int = 1, base_width: int = 64, dilation: int = 1, norm_layer: Incomplete | None = None) -> None: ...
    def forward(self, x): ...

class BottleneckBlock(nn.Layer):
    expansion: int
    conv1: Incomplete
    bn1: Incomplete
    conv2: Incomplete
    bn2: Incomplete
    conv3: Incomplete
    bn3: Incomplete
    relu: Incomplete
    downsample: Incomplete
    stride: Incomplete
    def __init__(self, inplanes, planes, stride: int = 1, downsample: Incomplete | None = None, groups: int = 1, base_width: int = 64, dilation: int = 1, norm_layer: Incomplete | None = None) -> None: ...
    def forward(self, x): ...

class ResNet(nn.Layer):
    groups: Incomplete
    base_width: Incomplete
    num_classes: Incomplete
    with_pool: Incomplete
    inplanes: int
    dilation: int
    conv1: Incomplete
    bn1: Incomplete
    relu: Incomplete
    maxpool: Incomplete
    layer1: Incomplete
    layer2: Incomplete
    layer3: Incomplete
    layer4: Incomplete
    avgpool: Incomplete
    fc: Incomplete
    def __init__(self, block, depth: int = 50, width: int = 64, num_classes: int = 1000, with_pool: bool = True, groups: int = 1) -> None: ...
    def forward(self, x): ...

def resnet18(pretrained: bool = False, **kwargs): ...
def resnet34(pretrained: bool = False, **kwargs): ...
def resnet50(pretrained: bool = False, **kwargs): ...
def resnet101(pretrained: bool = False, **kwargs): ...
def resnet152(pretrained: bool = False, **kwargs): ...
def resnext50_32x4d(pretrained: bool = False, **kwargs): ...
def resnext50_64x4d(pretrained: bool = False, **kwargs): ...
def resnext101_32x4d(pretrained: bool = False, **kwargs): ...
def resnext101_64x4d(pretrained: bool = False, **kwargs): ...
def resnext152_32x4d(pretrained: bool = False, **kwargs): ...
def resnext152_64x4d(pretrained: bool = False, **kwargs): ...
def wide_resnet50_2(pretrained: bool = False, **kwargs): ...
def wide_resnet101_2(pretrained: bool = False, **kwargs): ...
