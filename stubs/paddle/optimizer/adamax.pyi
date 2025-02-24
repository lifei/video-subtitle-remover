from ..base import core as core, framework as framework
from ..base.dygraph import no_grad as no_grad
from ..base.framework import name_scope as name_scope
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete

class Adamax(Optimizer):
    type: str
    def __init__(self, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, parameters: Incomplete | None = None, weight_decay: Incomplete | None = None, grad_clip: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
