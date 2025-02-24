from paddle.base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_mode as in_dynamic_mode

def identity_loss(x, reduction: str = 'none'): ...
