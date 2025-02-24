from ...base import core as core, framework as framework, unique_name as unique_name
from ...base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from ...base.framework import in_dygraph_mode as in_dygraph_mode, in_pir_mode as in_pir_mode
from .initializer import Initializer as Initializer
from _typeshed import Incomplete
from paddle import pir as pir

class NormalInitializer(Initializer):
    def __init__(self, loc: float = 0.0, scale: float = 1.0, seed: int = 0) -> None: ...
    def forward(self, var, block: Incomplete | None = None): ...

class Normal(NormalInitializer):
    def __init__(self, mean: float = 0.0, std: float = 1.0, name: Incomplete | None = None) -> None: ...

class TruncatedNormalInitializer(Initializer):
    def __init__(self, loc: float = 0.0, scale: float = 1.0, seed: int = 0) -> None: ...
    def forward(self, var, block: Incomplete | None = None): ...

class TruncatedNormal(TruncatedNormalInitializer):
    def __init__(self, mean: float = 0.0, std: float = 1.0, name: Incomplete | None = None) -> None: ...
