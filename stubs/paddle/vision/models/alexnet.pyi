from _typeshed import Incomplete
from paddle import nn as nn
from paddle.base.param_attr import ParamAttr as ParamAttr
from paddle.nn import Conv2D as Conv2D, Dropout as Dropout, Linear as Linear, MaxPool2D as MaxPool2D, ReLU as ReLU
from paddle.nn.initializer import Uniform as Uniform
from paddle.utils.download import get_weights_path_from_url as get_weights_path_from_url

model_urls: Incomplete

class ConvPoolLayer(nn.Layer):
    relu: Incomplete
    def __init__(self, input_channels, output_channels, filter_size, stride, padding, stdv, groups: int = 1, act: Incomplete | None = None) -> None: ...
    def forward(self, inputs): ...

class AlexNet(nn.Layer):
    num_classes: Incomplete
    def __init__(self, num_classes: int = 1000) -> None: ...
    def forward(self, inputs): ...

def alexnet(pretrained: bool = False, **kwargs): ...
