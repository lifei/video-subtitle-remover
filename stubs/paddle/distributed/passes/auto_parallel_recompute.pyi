from ..auto_parallel.static.dist_attribute import OperatorDistAttr as OperatorDistAttr
from ..auto_parallel.static.utils import get_loss_op as get_loss_op, insert_dependencies_for_two_ops as insert_dependencies_for_two_ops, is_backward_op as is_backward_op, is_recompute_exclude_op as is_recompute_exclude_op, is_recompute_op as is_recompute_op, naive_set_dist_op_attr_for_program_by_mesh_and_mapping as naive_set_dist_op_attr_for_program_by_mesh_and_mapping, set_dist_op_desc_original_id as set_dist_op_desc_original_id, set_var_dist_attr as set_var_dist_attr
from ..utils.log_utils import get_logger as get_logger
from .pass_base import PassBase as PassBase, register_pass as register_pass
from _typeshed import Incomplete
from paddle.base.backward import ProgramStats as ProgramStats
from paddle.distributed.fleet.meta_optimizers.common import OP_ROLE_KEY as OP_ROLE_KEY, OpRole as OpRole
from paddle.framework import core as core
from paddle.utils import unique_name as unique_name

logger: Incomplete

class RecomputeState(ProgramStats):
    seg_op_deps: Incomplete
    def __init__(self, block, ops) -> None: ...
    @property
    def checkpoints(self): ...
    @property
    def reserved_vars(self): ...
    def is_recompute(self): ...
    def build_states(self) -> None: ...
    def get_recompute_segments(self, no_recompute_segments=[]): ...
    def modify_forward_desc_for_recompute(self, dist_context) -> None: ...

class RecomputePass(PassBase):
    def __init__(self) -> None: ...
    def get_ops_per_device(self, ops, all_ops_process_meshs, sr: int = 0): ...
    def reset_op_dist_attr(self, op, var_name_dict) -> None: ...
    def set_op_dist_attr(self, op, old_dist_attr, var_name_dict) -> None: ...
