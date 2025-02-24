from _typeshed import Incomplete
from paddle.base import core as core
from paddle.base.data_feeder import check_type as check_type, check_variable_and_dtype as check_variable_and_dtype
from paddle.base.framework import Variable as Variable, in_dygraph_mode as in_dygraph_mode
from paddle.base.layer_helper import LayerHelper as LayerHelper

def check_finite_and_unscale(x, scale, name: Incomplete | None = None, float_status: Incomplete | None = None): ...
def update_loss_scaling(x, found_inf, prev_loss_scaling, num_good_steps, num_bad_steps, incr_every_n_steps, decr_every_n_nan_or_inf, incr_ratio, decr_ratio, stop_update: bool = False, name: Incomplete | None = None): ...
