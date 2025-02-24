from ..ops import ConvNormActivation as ConvNormActivation
from _typeshed import Incomplete
from paddle import nn as nn
from paddle.base.param_attr import ParamAttr as ParamAttr
from paddle.nn import AdaptiveAvgPool2D as AdaptiveAvgPool2D, AvgPool2D as AvgPool2D, Dropout as Dropout, Linear as Linear, MaxPool2D as MaxPool2D
from paddle.nn.initializer import Uniform as Uniform
from paddle.utils.download import get_weights_path_from_url as get_weights_path_from_url

model_urls: Incomplete

class InceptionStem(nn.Layer):
    conv_1a_3x3: Incomplete
    conv_2a_3x3: Incomplete
    conv_2b_3x3: Incomplete
    max_pool: Incomplete
    conv_3b_1x1: Incomplete
    conv_4a_3x3: Incomplete
    def __init__(self) -> None: ...
    def forward(self, x): ...

class InceptionA(nn.Layer):
    branch1x1: Incomplete
    branch5x5_1: Incomplete
    branch5x5_2: Incomplete
    branch3x3dbl_1: Incomplete
    branch3x3dbl_2: Incomplete
    branch3x3dbl_3: Incomplete
    branch_pool: Incomplete
    branch_pool_conv: Incomplete
    def __init__(self, num_channels, pool_features) -> None: ...
    def forward(self, x): ...

class InceptionB(nn.Layer):
    branch3x3: Incomplete
    branch3x3dbl_1: Incomplete
    branch3x3dbl_2: Incomplete
    branch3x3dbl_3: Incomplete
    branch_pool: Incomplete
    def __init__(self, num_channels) -> None: ...
    def forward(self, x): ...

class InceptionC(nn.Layer):
    branch1x1: Incomplete
    branch7x7_1: Incomplete
    branch7x7_2: Incomplete
    branch7x7_3: Incomplete
    branch7x7dbl_1: Incomplete
    branch7x7dbl_2: Incomplete
    branch7x7dbl_3: Incomplete
    branch7x7dbl_4: Incomplete
    branch7x7dbl_5: Incomplete
    branch_pool: Incomplete
    branch_pool_conv: Incomplete
    def __init__(self, num_channels, channels_7x7) -> None: ...
    def forward(self, x): ...

class InceptionD(nn.Layer):
    branch3x3_1: Incomplete
    branch3x3_2: Incomplete
    branch7x7x3_1: Incomplete
    branch7x7x3_2: Incomplete
    branch7x7x3_3: Incomplete
    branch7x7x3_4: Incomplete
    branch_pool: Incomplete
    def __init__(self, num_channels) -> None: ...
    def forward(self, x): ...

class InceptionE(nn.Layer):
    branch1x1: Incomplete
    branch3x3_1: Incomplete
    branch3x3_2a: Incomplete
    branch3x3_2b: Incomplete
    branch3x3dbl_1: Incomplete
    branch3x3dbl_2: Incomplete
    branch3x3dbl_3a: Incomplete
    branch3x3dbl_3b: Incomplete
    branch_pool: Incomplete
    branch_pool_conv: Incomplete
    def __init__(self, num_channels) -> None: ...
    def forward(self, x): ...

class InceptionV3(nn.Layer):
    num_classes: Incomplete
    with_pool: Incomplete
    layers_config: Incomplete
    inception_stem: Incomplete
    inception_block_list: Incomplete
    avg_pool: Incomplete
    dropout: Incomplete
    fc: Incomplete
    def __init__(self, num_classes: int = 1000, with_pool: bool = True) -> None: ...
    def forward(self, x): ...

def inception_v3(pretrained: bool = False, **kwargs): ...
