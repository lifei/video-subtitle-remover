from .layers import Layer as Layer
from _typeshed import Incomplete

class PairwiseDistance(Layer):
    p: Incomplete
    epsilon: Incomplete
    keepdim: Incomplete
    name: Incomplete
    def __init__(self, p: float = 2.0, epsilon: float = 1e-06, keepdim: bool = False, name: Incomplete | None = None) -> None: ...
    def forward(self, x, y): ...
    def extra_repr(self): ...
