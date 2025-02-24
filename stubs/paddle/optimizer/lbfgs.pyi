from ..base import framework as framework
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete

class LBFGS(Optimizer):
    learning_rate: Incomplete
    max_iter: Incomplete
    max_eval: Incomplete
    tolerance_grad: Incomplete
    tolerance_change: Incomplete
    history_size: Incomplete
    line_search_fn: Incomplete
    state: Incomplete
    def __init__(self, learning_rate: float = 1.0, max_iter: int = 20, max_eval: Incomplete | None = None, tolerance_grad: float = 1e-07, tolerance_change: float = 1e-09, history_size: int = 100, line_search_fn: Incomplete | None = None, parameters: Incomplete | None = None, weight_decay: Incomplete | None = None, grad_clip: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def state_dict(self): ...
    def step(self, closure): ...
    def minimize(self, loss, startup_program: Incomplete | None = None, parameters: Incomplete | None = None, no_grad_set: Incomplete | None = None) -> None: ...
