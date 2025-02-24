from _typeshed import Incomplete
from paddle.base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_mode as in_dynamic_mode

def graph_khop_sampler(row, colptr, input_nodes, sample_sizes, sorted_eids: Incomplete | None = None, return_eids: bool = False, name: Incomplete | None = None): ...
