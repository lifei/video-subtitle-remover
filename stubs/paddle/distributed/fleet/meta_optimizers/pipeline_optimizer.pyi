from .common import CollectiveHelper as CollectiveHelper, OP_ROLE_KEY as OP_ROLE_KEY, OP_ROLE_VAR_KEY as OP_ROLE_VAR_KEY, OpRole as OpRole, is_backward_op as is_backward_op, is_loss_grad_op as is_loss_grad_op
from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from _typeshed import Incomplete

class PipelineOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    meta_optimizers_black_list: Incomplete
    global_ring_id: int
    dp_ring_id: int
    start_pipeline_ring_id: int
    def __init__(self, optimizer) -> None: ...
    endpoints: Incomplete
    current_endpoint: Incomplete
    rank: Incomplete
    nranks: Incomplete
    wrapped_opt: Incomplete
    startup_program: Incomplete
    inner_parallelism: Incomplete
    pipeline_num: Incomplete
    main_program_list: Incomplete
    main_program: Incomplete
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
