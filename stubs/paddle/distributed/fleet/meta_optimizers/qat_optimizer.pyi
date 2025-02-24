from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from _typeshed import Incomplete
from paddle.static.quantization.quanter import quant_aware as quant_aware

class QATOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    meta_optimizers_black_list: Incomplete
    def __init__(self, optimizer) -> None: ...
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
    def qat_init(self, place, scope: Incomplete | None = None, test_program: Incomplete | None = None) -> None: ...
