from _typeshed import Incomplete
from paddle.base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from paddle.base.framework import Variable as Variable
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_mode as in_dynamic_mode

def reindex_graph(x, neighbors, count, value_buffer: Incomplete | None = None, index_buffer: Incomplete | None = None, name: Incomplete | None = None): ...
def reindex_heter_graph(x, neighbors, count, value_buffer: Incomplete | None = None, index_buffer: Incomplete | None = None, name: Incomplete | None = None): ...
