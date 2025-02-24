from ..fp16_lists import gray_list as gray_list_fp16
from _typeshed import Incomplete
from paddle.amp.amp_lists import BF16_WHITE_LIST as BF16_WHITE_LIST
from paddle.base import core as core

class AutoMixedPrecisionListsBF16:
    bf16_list: Incomplete
    fp32_list: Incomplete
    gray_list: Incomplete
    bf16_initializer_list: Incomplete
    unsupported_list: Incomplete
    fp32_varnames: Incomplete
    def __init__(self, custom_bf16_list: Incomplete | None = None, custom_fp32_list: Incomplete | None = None, custom_fp32_varnames: Incomplete | None = None) -> None: ...

bf16_initializer_list: Incomplete
bf16_list = BF16_WHITE_LIST
gray_list = gray_list_fp16
_: Incomplete
unsupported_list: Incomplete
fp32_list: Incomplete
