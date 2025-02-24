from ..base import framework as framework
from ..base.dygraph import no_grad as no_grad
from ..base.framework import in_dynamic_or_pir_mode as in_dynamic_or_pir_mode
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete

class SGD(Optimizer):
    type: str
    def __init__(self, learning_rate: float = 0.001, parameters: Incomplete | None = None, weight_decay: Incomplete | None = None, grad_clip: Incomplete | None = None, multi_precision: bool = False, name: Incomplete | None = None) -> None: ...
