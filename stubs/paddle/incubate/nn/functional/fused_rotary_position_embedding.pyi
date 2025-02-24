from _typeshed import Incomplete
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_or_pir_mode as in_dynamic_or_pir_mode

def fused_rotary_position_embedding(q, k: Incomplete | None = None, v: Incomplete | None = None, sin: Incomplete | None = None, cos: Incomplete | None = None, position_ids: Incomplete | None = None, use_neox_rotary_style: bool = True): ...
