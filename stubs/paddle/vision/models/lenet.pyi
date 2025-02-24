from _typeshed import Incomplete
from paddle import nn as nn

class LeNet(nn.Layer):
    num_classes: Incomplete
    features: Incomplete
    fc: Incomplete
    def __init__(self, num_classes: int = 10) -> None: ...
    def forward(self, inputs): ...
