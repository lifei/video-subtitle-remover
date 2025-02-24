from ..base import core as core, framework as framework
from ..base.framework import Variable as Variable, in_dygraph_mode as in_dygraph_mode, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode, in_pir_mode as in_pir_mode
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete
from paddle import pir as pir
from paddle.base.libpaddle import DataType as DataType
from paddle.pir import OpResult as OpResult

GRAD_TYPES: Incomplete

class Adam(Optimizer):
    type: str
    def __init__(self, learning_rate: float = 0.001, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-08, parameters: Incomplete | None = None, weight_decay: Incomplete | None = None, grad_clip: Incomplete | None = None, lazy_mode: bool = False, multi_precision: bool = False, use_multi_tensor: bool = False, name: Incomplete | None = None) -> None: ...
    def step(self): ...
