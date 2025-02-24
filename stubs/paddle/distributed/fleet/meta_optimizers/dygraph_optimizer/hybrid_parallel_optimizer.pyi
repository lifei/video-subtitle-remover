from ...base.topology import ParallelMode as ParallelMode
from ...utils.hybrid_parallel_util import fused_allreduce_gradients as fused_allreduce_gradients, unwrap_optimizer as unwrap_optimizer
from ...utils.log_util import logger as logger
from ...utils.mix_precision_utils import MixPrecisionOptimizer as MixPrecisionOptimizer
from _typeshed import Incomplete
from paddle import framework as framework
from paddle.autograd import no_grad as no_grad
from paddle.distributed import fleet as fleet
from paddle.distributed.fleet.meta_optimizers.dygraph_optimizer.dygraph_sharding_optimizer import DygraphShardingOptimizer as DygraphShardingOptimizer, DygraphShardingOptimizerV2 as DygraphShardingOptimizerV2
from paddle.distributed.fleet.utils.hybrid_parallel_util import obtain_optimizer_parameters_list as obtain_optimizer_parameters_list
from paddle.framework import core as core
from paddle.nn import ClipGradByGlobalNorm as ClipGradByGlobalNorm, clip as clip

g_shard_norm_align_dp: Incomplete

class HybridParallelClipGrad:
    not_sharding_stage1: bool
    def __init__(self, clip, hcg) -> None: ...
    def __getattr__(self, item): ...
    def __call__(self, params_grads): ...

class HybridParallelOptimizer:
    def __init__(self, optimizer, hcg, strategy) -> None: ...
    def step(self) -> None: ...
    def minimize(self, loss, startup_program: Incomplete | None = None, parameters: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
    def __getattr__(self, item): ...
