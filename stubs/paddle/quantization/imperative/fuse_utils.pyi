from . import utils as utils
from _typeshed import Incomplete
from paddle import nn as nn

class Identity(nn.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def forward(self, input): ...

def fuse_conv_bn(model) -> None: ...
def fuse_layers(model, layers_to_fuse, inplace: bool = False): ...

types_to_fusion_method: Incomplete
