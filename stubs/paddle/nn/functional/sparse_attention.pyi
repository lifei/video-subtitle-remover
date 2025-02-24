from _typeshed import Incomplete
from paddle import in_dynamic_mode as in_dynamic_mode
from paddle.base.layer_helper import LayerHelper as LayerHelper

def sparse_attention(query, key, value, sparse_csr_offset, sparse_csr_columns, key_padding_mask: Incomplete | None = None, attn_mask: Incomplete | None = None, name: Incomplete | None = None): ...
