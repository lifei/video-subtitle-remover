from _typeshed import Incomplete
from paddle.framework import LayerHelper as LayerHelper, in_dynamic_mode as in_dynamic_mode, in_pir_mode as in_pir_mode

def fused_rms_norm(x, norm_weight, norm_bias, epsilon, begin_norm_axis, bias: Incomplete | None = None, residual: Incomplete | None = None, quant_scale: int = -1, quant_round_type: int = 0, quant_max_bound: int = 0, quant_min_bound: int = 0): ...
