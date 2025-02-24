from .utils import convert_out_size_to_list as convert_out_size_to_list, get_out_size_tensor_inputs as get_out_size_tensor_inputs, reshape_lhs_rhs as reshape_lhs_rhs
from _typeshed import Incomplete
from paddle.base.data_feeder import check_dtype as check_dtype, check_type as check_type, check_variable_and_dtype as check_variable_and_dtype
from paddle.base.framework import Variable as Variable
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_or_pir_mode as in_dynamic_or_pir_mode

def send_u_recv(x, src_index, dst_index, reduce_op: str = 'sum', out_size: Incomplete | None = None, name: Incomplete | None = None): ...
def send_ue_recv(x, y, src_index, dst_index, message_op: str = 'add', reduce_op: str = 'sum', out_size: Incomplete | None = None, name: Incomplete | None = None): ...
def send_uv(x, y, src_index, dst_index, message_op: str = 'add', name: Incomplete | None = None): ...
