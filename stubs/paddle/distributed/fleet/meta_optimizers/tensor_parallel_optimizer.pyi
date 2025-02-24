from .common import CollectiveHelper as CollectiveHelper, OP_ROLE_KEY as OP_ROLE_KEY, OP_ROLE_VAR_KEY as OP_ROLE_VAR_KEY, OpRole as OpRole, is_backward_op as is_backward_op, is_loss_grad_op as is_loss_grad_op, is_optimizer_op as is_optimizer_op
from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from _typeshed import Incomplete
from paddle import static as static

class TensorParallelOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    meta_optimizers_black_list: Incomplete
    mp_ring_id: int
    global_ring_id: int
    dp_ring_id: int
    def __init__(self, optimizer) -> None: ...
    endpoints: Incomplete
    current_endpoint: Incomplete
    startup_program: Incomplete
    main_program: Incomplete
    nranks: Incomplete
    rank: Incomplete
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
