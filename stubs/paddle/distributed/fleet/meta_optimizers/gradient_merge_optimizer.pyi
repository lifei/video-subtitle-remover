from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from _typeshed import Incomplete

class GradientMergeOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    wrapped_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    meta_optimizers_black_list: Incomplete
    def __init__(self, optimizer) -> None: ...
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
