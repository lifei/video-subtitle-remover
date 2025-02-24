from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from _typeshed import Incomplete
from paddle.distributed.passes import PassContext as PassContext
from paddle.distributed.ps.utils.ps_factory import PsProgramBuilderFactory as PsProgramBuilderFactory
from paddle.distributed.ps.utils.public import TrainerRuntimeConfig as TrainerRuntimeConfig, build_var_distributed as build_var_distributed, dtype_to_size as dtype_to_size, get_dist_env as get_dist_env, get_var_mem_size as get_var_mem_size, logger as logger
from paddle.framework import core as core

class ParameterServerOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    def __init__(self, optimizer) -> None: ...
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
    def minimize_losses_impl(self, losses, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
