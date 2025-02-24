from ...base import core as core, framework as framework, unique_name as unique_name
from ...base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from ...base.framework import in_dygraph_mode as in_dygraph_mode, in_pir_mode as in_pir_mode
from .initializer import Initializer as Initializer
from _typeshed import Incomplete
from paddle import pir as pir

class UniformInitializer(Initializer):
    def __init__(self, low: float = -1.0, high: float = 1.0, seed: int = 0, diag_num: int = 0, diag_step: int = 0, diag_val: float = 1.0) -> None: ...
    def forward(self, var, block: Incomplete | None = None): ...

class Uniform(UniformInitializer):
    def __init__(self, low: float = -1.0, high: float = 1.0, name: Incomplete | None = None) -> None: ...
