from ..auto_parallel.process_mesh import ProcessMesh as ProcessMesh
from .auto_parallel_amp import AMPPass as AMPPass
from .pass_base import register_pass as register_pass
from _typeshed import Incomplete
from paddle.common_ops_import import check_type as check_type, check_variable_and_dtype as check_variable_and_dtype
from paddle.distributed.auto_parallel.static.dist_attribute import OperatorDistAttr as OperatorDistAttr
from paddle.distributed.auto_parallel.static.process_group import get_world_process_group as get_world_process_group
from paddle.distributed.auto_parallel.static.utils import is_backward_op as is_backward_op, is_forward_op as is_forward_op, naive_set_dist_op_attr_for_program_by_mesh_and_mapping as naive_set_dist_op_attr_for_program_by_mesh_and_mapping, set_var_dist_attr as set_var_dist_attr
from paddle.distributed.fleet.meta_optimizers.common import OP_ROLE_KEY as OP_ROLE_KEY, OpRole as OpRole
from paddle.framework import core as core
from paddle.static import default_main_program as default_main_program, default_startup_program as default_startup_program
from paddle.utils import unique_name as unique_name

world_process_group: Incomplete
__amp_skip_ops__: Incomplete
__target_dtype__: Incomplete
__amp_utils__: Incomplete

def set_op_dtype_to_fp16(op) -> None: ...

class FP16State:
    program: Incomplete
    amp_list: Incomplete
    use_fp16_guard: Incomplete
    dist_context: Incomplete
    grad_op_to_op_map: Incomplete
    input_data_var_names: Incomplete
    forward_non_leaf_tensors: Incomplete
    forward_input_cast_ops: Incomplete
    is_train: bool
    out_var_op_deps: Incomplete
    def __init__(self, program, amp_list, dist_context, use_fp16_guard, input_data_var_names: Incomplete | None = None) -> None: ...
    def set_var_to_fp16(self, var_name, block) -> None: ...
    def resolute_tensor_dtype(self, block) -> None: ...
    def cast_block(self, block) -> None: ...

def cast_startup_program(): ...

class FP16Pass(AMPPass):
    def __init__(self) -> None: ...
