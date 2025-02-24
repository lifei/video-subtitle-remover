from _typeshed import Incomplete
from paddle.base import framework as framework
from paddle.base.framework import in_dygraph_mode as in_dygraph_mode
from paddle.optimizer import Optimizer as Optimizer

class LarsMomentumOptimizer(Optimizer):
    type: str
    def __init__(self, learning_rate, momentum, lars_coeff: float = 0.001, lars_weight_decay: float = 0.0005, parameter_list: Incomplete | None = None, regularization: Incomplete | None = None, grad_clip: Incomplete | None = None, name: Incomplete | None = None, exclude_from_weight_decay: Incomplete | None = None, epsilon: int = 0, multi_precision: bool = False, rescale_grad: float = 1.0) -> None: ...
