from _typeshed import Incomplete
from paddle.base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_mode as in_dynamic_mode
from paddle.utils import deprecated as deprecated

def graph_sample_neighbors(row, colptr, input_nodes, eids: Incomplete | None = None, perm_buffer: Incomplete | None = None, sample_size: int = -1, return_eids: bool = False, flag_perm_buffer: bool = False, name: Incomplete | None = None): ...
