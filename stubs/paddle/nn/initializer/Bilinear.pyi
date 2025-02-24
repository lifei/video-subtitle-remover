from ...base import core as core, framework as framework, unique_name as unique_name
from ...base.framework import in_dygraph_mode as in_dygraph_mode
from .initializer import Initializer as Initializer
from _typeshed import Incomplete

class Bilinear(Initializer):
    def __init__(self) -> None: ...
    def forward(self, var, block: Incomplete | None = None): ...
