from ... import base as base
from ...base import framework as framework
from ...base.core import VarDesc as VarDesc
from ...base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from .initializer import Initializer as Initializer
from _typeshed import Incomplete
from paddle import in_dynamic_mode as in_dynamic_mode
from paddle.utils import unique_name as unique_name

class Dirac(Initializer):
    def __init__(self, groups: int = 1, name: Incomplete | None = None) -> None: ...
    def __call__(self, var, block: Incomplete | None = None): ...
