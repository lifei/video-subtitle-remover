from _typeshed import Incomplete
from paddle.optimizer import Optimizer as Optimizer
from paddle.utils import deprecated as deprecated

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
