from _typeshed import Incomplete
from paddle.framework import LayerHelper as LayerHelper, in_dynamic_mode as in_dynamic_mode

def masked_multihead_attention(x, cache_kv: Incomplete | None = None, bias: Incomplete | None = None, src_mask: Incomplete | None = None, cum_offsets: Incomplete | None = None, sequence_lengths: Incomplete | None = None, rotary_tensor: Incomplete | None = None, beam_cache_offset: Incomplete | None = None, qkv_out_scale: Incomplete | None = None, out_shift: Incomplete | None = None, out_smooth: Incomplete | None = None, seq_len: int = 1, rotary_emb_dims: int = 0, use_neox_rotary_style: bool = False, compute_dtype: str = 'default', out_scale: int = -1, quant_round_type: int = 1, quant_max_bound: float = 127.0, quant_min_bound: float = -127.0): ...
