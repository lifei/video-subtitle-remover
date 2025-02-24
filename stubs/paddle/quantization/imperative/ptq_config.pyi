from .ptq_quantizer import KLQuantizer as KLQuantizer, PerChannelAbsmaxQuantizer as PerChannelAbsmaxQuantizer, SUPPORT_ACT_QUANTIZERS as SUPPORT_ACT_QUANTIZERS, SUPPORT_WT_QUANTIZERS as SUPPORT_WT_QUANTIZERS
from _typeshed import Incomplete

class PTQConfig:
    in_act_quantizer: Incomplete
    out_act_quantizer: Incomplete
    wt_quantizer: Incomplete
    quant_hook_handle: Incomplete
    enable_in_act_quantizer: bool
    def __init__(self, activation_quantizer, weight_quantizer) -> None: ...

default_ptq_config: Incomplete
