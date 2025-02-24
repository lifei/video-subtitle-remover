from ...base import core as core, framework as framework
from ...base.framework import in_dygraph_mode as in_dygraph_mode, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode
from .initializer import Initializer as Initializer
from _typeshed import Incomplete

class ConstantInitializer(Initializer):
    def __init__(self, value: float = 0.0, force_cpu: bool = False) -> None: ...
    def forward(self, var, block: Incomplete | None = None): ...

class Constant(ConstantInitializer):
    def __init__(self, value: float = 0.0) -> None: ...
