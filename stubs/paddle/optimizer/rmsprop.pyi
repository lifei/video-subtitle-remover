from ..base import framework as framework
from ..base.framework import in_dygraph_mode as in_dygraph_mode
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete

class RMSProp(Optimizer):
    type: str
    def __init__(self, learning_rate, rho: float = 0.95, epsilon: float = 1e-06, momentum: float = 0.0, centered: bool = False, parameters: Incomplete | None = None, weight_decay: Incomplete | None = None, grad_clip: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
