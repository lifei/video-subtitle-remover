from ..base import framework as framework
from ..base.dygraph import no_grad as no_grad
from ..framework import in_dynamic_mode as in_dynamic_mode
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete

class Adadelta(Optimizer):
    type: str
    def __init__(self, learning_rate: float = 0.001, epsilon: float = 1e-06, rho: float = 0.95, parameters: Incomplete | None = None, weight_decay: Incomplete | None = None, grad_clip: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
