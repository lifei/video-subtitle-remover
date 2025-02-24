from ...base import core as core, framework as framework, unique_name as unique_name
from ...base.framework import in_dygraph_mode as in_dygraph_mode, in_pir_mode as in_pir_mode
from .initializer import Initializer as Initializer, calculate_gain as calculate_gain
from _typeshed import Incomplete

class MSRAInitializer(Initializer):
    def __init__(self, uniform: bool = True, fan_in: Incomplete | None = None, seed: int = 0, negative_slope: int = 0, nonlinearity: str = 'relu') -> None: ...
    def forward(self, var, block: Incomplete | None = None): ...

class KaimingNormal(MSRAInitializer):
    def __init__(self, fan_in: Incomplete | None = None, negative_slope: float = 0.0, nonlinearity: str = 'relu') -> None: ...

class KaimingUniform(MSRAInitializer):
    def __init__(self, fan_in: Incomplete | None = None, negative_slope: float = 0.0, nonlinearity: str = 'relu') -> None: ...
