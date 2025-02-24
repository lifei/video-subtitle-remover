from ...base import core as core, framework as framework, unique_name as unique_name
from ...base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from ...base.framework import in_dygraph_mode as in_dygraph_mode, in_pir_mode as in_pir_mode
from .initializer import Initializer as Initializer
from _typeshed import Incomplete

class XavierInitializer(Initializer):
    def __init__(self, uniform: bool = True, fan_in: Incomplete | None = None, fan_out: Incomplete | None = None, seed: int = 0) -> None: ...
    def forward(self, var, block: Incomplete | None = None): ...

class XavierNormal(XavierInitializer):
    def __init__(self, fan_in: Incomplete | None = None, fan_out: Incomplete | None = None, name: Incomplete | None = None) -> None: ...

class XavierUniform(XavierInitializer):
    def __init__(self, fan_in: Incomplete | None = None, fan_out: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
