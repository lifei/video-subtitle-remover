from ...base.data_feeder import check_type as check_type, check_variable_and_dtype as check_variable_and_dtype
from ...base.layer_helper import LayerHelper as LayerHelper
from _typeshed import Incomplete
from paddle.framework import in_dynamic_or_pir_mode as in_dynamic_or_pir_mode

def pairwise_distance(x, y, p: float = 2.0, epsilon: float = 1e-06, keepdim: bool = False, name: Incomplete | None = None): ...
