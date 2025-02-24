from .pass_base import PassBase as PassBase, PassType as PassType, register_pass as register_pass
from paddle.distributed.auto_parallel.static.utils import naive_set_dist_op_attr_for_program_by_mesh as naive_set_dist_op_attr_for_program_by_mesh
from paddle.distributed.fleet.meta_optimizers.common import OP_ROLE_KEY as OP_ROLE_KEY
from paddle.static import default_main_program as default_main_program

class SequenceParallelOptimizationPass(PassBase):
    def __init__(self) -> None: ...
