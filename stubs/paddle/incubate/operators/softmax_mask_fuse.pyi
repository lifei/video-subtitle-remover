from _typeshed import Incomplete
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_mode as in_dynamic_mode

def softmax_mask_fuse(x, mask, name: Incomplete | None = None): ...
