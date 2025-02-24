from ..auto_parallel.process_mesh import ProcessMesh as ProcessMesh
from ..auto_parallel.static.utils import is_backward_op as is_backward_op, is_forward_op as is_forward_op, is_loss_grad_op as is_loss_grad_op, is_loss_op as is_loss_op, is_optimize_op as is_optimize_op
from .pass_base import PassBase as PassBase, register_pass as register_pass
from _typeshed import Incomplete
from paddle.base.data_feeder import check_type as check_type, check_variable_and_dtype as check_variable_and_dtype
from paddle.distributed.auto_parallel.static.dist_attribute import OperatorDistAttr as OperatorDistAttr
from paddle.distributed.auto_parallel.static.process_group import get_world_process_group as get_world_process_group
from paddle.distributed.auto_parallel.static.utils import naive_set_dist_op_attr_for_program_by_mesh_and_mapping as naive_set_dist_op_attr_for_program_by_mesh_and_mapping, set_var_dist_attr as set_var_dist_attr
from paddle.distributed.fleet.meta_optimizers.common import OP_ROLE_KEY as OP_ROLE_KEY, OpRole as OpRole
from paddle.framework import core as core
from paddle.static.amp.bf16.amp_utils import AutoMixedPrecisionListsBF16 as AutoMixedPrecisionListsBF16
from paddle.static.amp.fp16_utils import AutoMixedPrecisionLists as AutoMixedPrecisionLists, find_op_index as find_op_index, find_true_post_op as find_true_post_op, find_true_prev_op as find_true_prev_op
from paddle.utils import unique_name as unique_name

world_process_group: Incomplete
__amp_skip_ops__: Incomplete

class AMPLists:
    def __init__(self, white_list: Incomplete | None = None, black_list: Incomplete | None = None, black_varnames: Incomplete | None = None, dtype: str = 'float16') -> None: ...
    @property
    def white_list(self): ...
    @property
    def black_list(self): ...
    @property
    def gray_list(self): ...
    @property
    def black_varnames(self): ...
    @property
    def is_fp16(self): ...
    @property
    def dtype(self): ...
    @property
    def amp_list(self): ...

class AMPState:
    program: Incomplete
    dist_context: Incomplete
    amp_lists: Incomplete
    amp_dtype: Incomplete
    grad_op_to_op_map: Incomplete
    out_var_op_deps: Incomplete
    def __init__(self, program, amp_lists, amp_dtype, dist_context) -> None: ...
    def build_state(self): ...

class AMPPass(PassBase):
    def __init__(self) -> None: ...
    def get_loss(self): ...
