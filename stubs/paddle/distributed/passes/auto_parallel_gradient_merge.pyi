from .pass_base import PassBase as PassBase, PassType as PassType, register_pass as register_pass
from _typeshed import Incomplete
from paddle.distributed.auto_parallel.process_mesh import ProcessMesh as ProcessMesh
from paddle.distributed.auto_parallel.static.process_group import get_world_process_group as get_world_process_group
from paddle.distributed.auto_parallel.static.utils import is_forward_op as is_forward_op, is_optimize_op as is_optimize_op, naive_set_dist_op_attr_for_program_by_mesh_and_mapping as naive_set_dist_op_attr_for_program_by_mesh_and_mapping, set_var_dist_attr as set_var_dist_attr
from paddle.distributed.fleet.meta_optimizers.common import OP_ROLE_KEY as OP_ROLE_KEY, OP_ROLE_VAR_KEY as OP_ROLE_VAR_KEY, OpRole as OpRole
from paddle.framework import core as core
from paddle.static import device_guard as device_guard

world_process_group: Incomplete

def parse_program(main_program, startup_program, params_grads, k_steps, avg, dist_context) -> None: ...

class GradientMergePass(PassBase):
    def __init__(self) -> None: ...
