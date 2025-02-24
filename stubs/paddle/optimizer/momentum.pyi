from ..base import core as core, framework as framework
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete
from paddle.framework import in_dynamic_or_pir_mode as in_dynamic_or_pir_mode
from paddle.regularizer import L2Decay as L2Decay

class Momentum(Optimizer):
    type: str
    def __init__(self, learning_rate: float = 0.001, momentum: float = 0.9, parameters: Incomplete | None = None, use_nesterov: bool = False, weight_decay: Incomplete | None = None, grad_clip: Incomplete | None = None, multi_precision: bool = False, rescale_grad: float = 1.0, use_multi_tensor: bool = False, name: Incomplete | None = None) -> None: ...
