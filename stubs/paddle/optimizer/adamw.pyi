from ..base import core as core, framework as framework
from ..base.framework import Parameter as Parameter, Variable as Variable, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode, in_pir_mode as in_pir_mode
from ..nn.clip import GradientClipBase as GradientClipBase
from .lr import LRScheduler as LRScheduler
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete
from paddle import pir as pir
from paddle.base.libpaddle import DataType as DataType
from paddle.pir import OpResult as OpResult

class AdamW(Optimizer):
    helper: Incomplete
    clear_gradients: Incomplete
    type: str
    regularization: Incomplete
    def __init__(self, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, parameters: Incomplete | None = None, weight_decay: float = 0.01, lr_ratio: Incomplete | None = None, apply_decay_param_fun: Incomplete | None = None, grad_clip: Incomplete | None = None, lazy_mode: bool = False, multi_precision: bool = False, name: Incomplete | None = None) -> None: ...
    def step(self): ...
