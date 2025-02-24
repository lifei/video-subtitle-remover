from ...base import framework as framework
from ...base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from ...base.dygraph import no_grad as no_grad
from .initializer import Initializer as Initializer
from _typeshed import Incomplete
from paddle.utils import unique_name as unique_name

class Orthogonal(Initializer):
    def __init__(self, gain: float = 1.0, name: Incomplete | None = None) -> None: ...
    def __call__(self, var, block: Incomplete | None = None): ...
