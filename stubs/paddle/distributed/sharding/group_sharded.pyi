from _typeshed import Incomplete
from paddle.distributed.fleet.meta_parallel.sharding.group_sharded_optimizer_stage2 import GroupShardedOptimizerStage2 as GroupShardedOptimizerStage2
from paddle.distributed.fleet.meta_parallel.sharding.group_sharded_stage2 import GroupShardedStage2 as GroupShardedStage2
from paddle.distributed.fleet.meta_parallel.sharding.group_sharded_stage3 import GroupShardedStage3 as GroupShardedStage3
from paddle.distributed.fleet.meta_parallel.sharding.group_sharded_utils import GroupShardedScaler as GroupShardedScaler
from paddle.distributed.fleet.utils.mix_precision_utils import MixPrecisionOptimizer as MixPrecisionOptimizer
from paddle.distributed.utils.log_utils import get_logger as get_logger
from paddle.optimizer import Optimizer as Optimizer

logger_: Incomplete

def group_sharded_parallel(model, optimizer, level, scaler: Incomplete | None = None, group: Incomplete | None = None, offload: bool = False, sync_buffers: bool = False, buffer_max_size=..., segment_size=..., sync_comm: bool = False, dp_group: Incomplete | None = None, exclude_layer: Incomplete | None = None): ...
def save_group_sharded_model(model, output, optimizer: Incomplete | None = None) -> None: ...
