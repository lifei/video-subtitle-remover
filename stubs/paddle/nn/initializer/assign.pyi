from ...base import core as core, framework as framework, unique_name as unique_name
from ...base.data_feeder import check_type as check_type
from ...base.framework import in_dygraph_mode as in_dygraph_mode
from .initializer import Initializer as Initializer
from _typeshed import Incomplete

class NumpyArrayInitializer(Initializer):
    def __init__(self, value) -> None: ...
    def forward(self, var, block: Incomplete | None = None): ...

class Assign(NumpyArrayInitializer):
    def __init__(self, value, name: Incomplete | None = None) -> None: ...
