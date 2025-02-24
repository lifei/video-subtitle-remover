from _typeshed import Incomplete
from paddle import nn as nn

class IntermediateLayerGetter(nn.LayerDict):
    __annotations__: Incomplete
    return_layers: Incomplete
    def __init__(self, model: nn.Layer, return_layers: dict[str, str]) -> None: ...
    def forward(self, x): ...
