from .pass_base import PassBase as PassBase, register_pass as register_pass
from _typeshed import Incomplete
from paddle.base import core as core
from paddle.base.framework import Program as Program
from paddle.distributed.auto_parallel.static.process_group import remove_process_group as remove_process_group
from paddle.distributed.auto_parallel.static.utils import is_backward_op as is_backward_op, is_forward_op as is_forward_op, is_lr_sched_op as is_lr_sched_op, is_optimize_op as is_optimize_op
from paddle.distributed.fleet.fleet_executor_utils import TaskNode as TaskNode

__not_shape_var_type__: Incomplete

def is_reshard_op(op): ...

class PipelinePass(PassBase):
    def __init__(self) -> None: ...
