from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from _typeshed import Incomplete
from paddle.base import framework as framework
from paddle.common_ops_import import LayerHelper as LayerHelper
from paddle.framework import core as core, in_dynamic_mode as in_dynamic_mode
from paddle.nn.clip import ClipGradByNorm as ClipGradByNorm, append_gradient_clip_ops as append_gradient_clip_ops
from paddle.optimizer import Momentum as Momentum, Optimizer as Optimizer
from paddle.regularizer import L1Decay as L1Decay, L2Decay as L2Decay
from paddle.static import create_global_var as create_global_var

class DGCMomentumOptimizer(Optimizer):
    type: str
    def __init__(self, learning_rate, momentum, rampup_begin_step, rampup_step: int = 1, sparsity=[0.999], parameter_list: Incomplete | None = None, use_nesterov: bool = False, num_trainers: Incomplete | None = None, regularization: Incomplete | None = None, grad_clip: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def apply_gradients(self, params_grads): ...

class DGCOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    dgc_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    meta_optimizers_black_list: Incomplete
    def __init__(self, optimizer) -> None: ...
    def backward(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None, callbacks: Incomplete | None = None): ...
    def apply_gradients(self, params_grads): ...
    def apply_optimize(self, loss, startup_program, params_grads): ...
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
