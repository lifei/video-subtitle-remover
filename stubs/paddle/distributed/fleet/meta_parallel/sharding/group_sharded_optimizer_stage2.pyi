from .group_sharded_storage import GradStorage as GradStorage, ParamStorage as ParamStorage
from .group_sharded_utils import GroupShardedClipGrad as GroupShardedClipGrad, Type as Type, device_guard as device_guard
from _typeshed import Incomplete
from paddle.distributed import ParallelMode as ParallelMode, fleet as fleet
from paddle.distributed.collective import new_group as new_group
from paddle.framework import core as core
from paddle.nn import ClipGradByGlobalNorm as ClipGradByGlobalNorm
from paddle.optimizer import Optimizer as Optimizer

HybridParallelClipGrad = fleet.meta_optimizers.dygraph_optimizer.hybrid_parallel_optimizer.HybridParallelClipGrad
alignment: Incomplete
align: Incomplete

class GroupShardedOptimizerStage2(Optimizer):
    use_main_grad: Incomplete
    world_size: Incomplete
    param_storages: Incomplete
    offload: Incomplete
    offload_device: str
    offload_buffer_size: int
    offload_param2align: Incomplete
    offload_params: Incomplete
    offload_grads: Incomplete
    dev_id: Incomplete
    def __init__(self, params, optim, group: Incomplete | None = None, offload: bool = False, device: str = 'gpu', pertrain_sync_models: bool = True, dp_group: Incomplete | None = None, **kw) -> None: ...
    @property
    def local_params(self): ...
    @property
    def param2rank(self): ...
    @property
    def dtype_rank_params(self): ...
    @property
    def rank_buffer_size(self): ...
    def step(self) -> None: ...
    def minimize(self) -> None: ...
    def set_state_dict(self, state_dict) -> None: ...
    def state_dict(self): ...
    def set_lr(self, lr) -> None: ...
    def get_lr(self): ...
