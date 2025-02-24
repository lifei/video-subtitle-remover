from .dist_attribute import OperatorDistAttr as OperatorDistAttr
from .operators.common import BACKWARD_ONLY_DIST_OPS as BACKWARD_ONLY_DIST_OPS
from .utils import __no_shape_var_type__ as __no_shape_var_type__, is_backward_op as is_backward_op, is_forward_op as is_forward_op, is_loss_op as is_loss_op, is_optimize_op as is_optimize_op
from _typeshed import Incomplete
from paddle.distributed.auto_parallel.static.dist_context import DistributedContext as DistributedContext
from paddle.distributed.auto_parallel.static.operators.common import get_distributed_operator_impl_container as get_distributed_operator_impl_container
from paddle.framework import Program as Program, core as core
from paddle.static import Parameter as Parameter

__varname_not_in_block__: Incomplete

class Partitioner:
    def __init__(self, dist_context, rank_id: int = 0) -> None: ...
    def partition(self, serial_main_program, serial_startup_program, params_grads): ...
    def partition_startup_program(self, serial_main_program, serial_startup_program): ...
    def partition_main_program(self, serial_main_program, params_and_grads): ...
    def partition_block(self, ref_block, target_block) -> None: ...
