from _typeshed import Incomplete
from paddle.base.data_feeder import check_dtype as check_dtype, check_type as check_type, check_variable_and_dtype as check_variable_and_dtype
from paddle.base.framework import Variable as Variable
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_or_pir_mode as in_dynamic_or_pir_mode
from paddle.geometric.message_passing.utils import convert_out_size_to_list as convert_out_size_to_list, get_out_size_tensor_inputs as get_out_size_tensor_inputs
from paddle.utils import deprecated as deprecated

def graph_send_recv(x, src_index, dst_index, pool_type: str = 'sum', out_size: Incomplete | None = None, name: Incomplete | None = None): ...
