from _typeshed import Incomplete
from paddle.framework import LayerHelper as LayerHelper, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode

def variable_length_memory_efficient_attention(query, key, value, seq_lens, kv_seq_lens, mask: Incomplete | None = None, scale: Incomplete | None = None, causal: bool = False, pre_cache_length: int = 0): ...
