from _typeshed import Incomplete
from paddle.amp.amp_lists import EXTRA_BLACK_LIST as EXTRA_BLACK_LIST, FP16_BLACK_LIST as FP16_BLACK_LIST, FP16_WHITE_LIST as FP16_WHITE_LIST
from paddle.base import core as core
from paddle.base.log_helper import get_logger as get_logger

black_list = FP16_BLACK_LIST
white_list = FP16_WHITE_LIST

def check_amp_dtype(dtype): ...
def get_low_precision_vartype(dtype): ...
def get_low_precision_dtypestr(dtype): ...

class AutoMixedPrecisionLists:
    amp_dtype: Incomplete
    white_list: Incomplete
    black_list: Incomplete
    gray_list: Incomplete
    unsupported_list: Incomplete
    all_list: Incomplete
    black_varnames: Incomplete
    def __init__(self, custom_white_list: Incomplete | None = None, custom_black_list: Incomplete | None = None, custom_black_varnames: Incomplete | None = None, dtype: str = 'float16') -> None: ...

gray_list: Incomplete
CustomOpLists = AutoMixedPrecisionLists
