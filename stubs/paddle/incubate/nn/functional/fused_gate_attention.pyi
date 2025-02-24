from _typeshed import Incomplete
from paddle.framework import in_dynamic_mode as in_dynamic_mode

def fused_gate_attention(query, key: Incomplete | None = None, query_weight: Incomplete | None = None, key_weight: Incomplete | None = None, value_weight: Incomplete | None = None, qkv_weight: Incomplete | None = None, gate_linear_weight: Incomplete | None = None, gate_linear_bias: Incomplete | None = None, out_linear_weight: Incomplete | None = None, out_linear_bias: Incomplete | None = None, nonbatched_bias: Incomplete | None = None, attn_mask: Incomplete | None = None, has_gating: bool = True, merge_qkv: bool = True, use_flash_attn: bool = False): ...
