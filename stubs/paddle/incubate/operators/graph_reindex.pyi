from _typeshed import Incomplete
from paddle.base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_mode as in_dynamic_mode
from paddle.utils import deprecated as deprecated

def graph_reindex(x, neighbors, count, value_buffer: Incomplete | None = None, index_buffer: Incomplete | None = None, flag_buffer_hashtable: bool = False, name: Incomplete | None = None): ...
