from _typeshed import Incomplete
from paddle.base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_mode as in_dynamic_mode, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode

def sample_neighbors(row, colptr, input_nodes, sample_size: int = -1, eids: Incomplete | None = None, return_eids: bool = False, perm_buffer: Incomplete | None = None, name: Incomplete | None = None): ...
def weighted_sample_neighbors(row, colptr, edge_weight, input_nodes, sample_size: int = -1, eids: Incomplete | None = None, return_eids: bool = False, name: Incomplete | None = None): ...
