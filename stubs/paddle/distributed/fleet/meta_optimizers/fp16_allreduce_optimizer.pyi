from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from _typeshed import Incomplete
from paddle.framework import core as core
from paddle.utils import unique_name as unique_name

class FP16AllReduceOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    meta_optimizers_black_list: Incomplete
    def __init__(self, optimizer) -> None: ...
    @staticmethod
    def fp16_compression(param_and_grads): ...
    def apply_optimize(self, loss, startup_program, params_grads): ...
