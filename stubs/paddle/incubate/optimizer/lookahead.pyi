from _typeshed import Incomplete
from paddle.base import framework as framework, unique_name as unique_name
from paddle.base.framework import Variable as Variable
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.optimizer import Optimizer as Optimizer

class LookAhead(Optimizer):
    inner_optimizer: Incomplete
    alpha: Incomplete
    k: Incomplete
    type: str
    helper: Incomplete
    def __init__(self, inner_optimizer, alpha: float = 0.5, k: int = 5, name: Incomplete | None = None) -> None: ...
    def step(self) -> None: ...
    def minimize(self, loss, startup_program: Incomplete | None = None, parameters: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
