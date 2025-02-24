from ..framework import core as core
from _typeshed import Incomplete
from paddle.base.data_feeder import check_type as check_type, convert_dtype as convert_dtype

class PrintOptions:
    precision: int
    threshold: int
    edgeitems: int
    linewidth: int
    sci_mode: bool

DEFAULT_PRINT_OPTIONS: Incomplete

def set_printoptions(precision: Incomplete | None = None, threshold: Incomplete | None = None, edgeitems: Incomplete | None = None, sci_mode: Incomplete | None = None, linewidth: Incomplete | None = None) -> None: ...
def to_string(var, prefix: str = 'Tensor'): ...
def sparse_tensor_to_string(tensor, prefix: str = 'Tensor'): ...
def dist_tensor_to_string(tensor, prefix: str = 'Tensor'): ...
def tensor_to_string(tensor, prefix: str = 'Tensor'): ...
