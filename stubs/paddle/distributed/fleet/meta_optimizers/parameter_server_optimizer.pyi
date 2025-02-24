from ..base.private_helper_function import wait_server_ready as wait_server_ready
from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from _typeshed import Incomplete
from paddle.framework import core as core

class ParameterServerOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    def __init__(self, optimizer) -> None: ...
    def get_dist_env(self): ...
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
