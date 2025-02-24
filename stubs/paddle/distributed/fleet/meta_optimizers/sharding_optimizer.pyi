from ..utils.log_util import logger as logger
from .common import CollectiveHelper as CollectiveHelper, OP_ROLE_KEY as OP_ROLE_KEY, OP_ROLE_VAR_KEY as OP_ROLE_VAR_KEY, OpRole as OpRole, is_backward_op as is_backward_op, is_optimizer_op as is_optimizer_op, is_update_op as is_update_op
from .meta_optimizer_base import MetaOptimizerBase as MetaOptimizerBase
from .sharding import utils as utils
from .sharding.fp16_helper import FP16Utils as FP16Utils
from .sharding.gradient_clip_helper import GradientClipHelper as GradientClipHelper
from .sharding.offload_helper import OffloadHelper as OffloadHelper
from .sharding.prune import ProgramDeps as ProgramDeps
from .sharding.shard import ProgramSegment as ProgramSegment, Shard as Shard
from .sharding.utils import get_first_optimize_op_idx as get_first_optimize_op_idx, get_grad_device as get_grad_device, get_var_size as get_var_size, insert_allreduce_ops as insert_allreduce_ops, insert_broadcast_ops as insert_broadcast_ops, insert_cast_ops as insert_cast_ops, insert_fill_constant_ops as insert_fill_constant_ops, insert_reduce_ops as insert_reduce_ops, insert_scale_loss_grad_ops as insert_scale_loss_grad_ops, insert_sync_calc_op as insert_sync_calc_op, insert_sync_comm_ops as insert_sync_comm_ops
from .sharding.weight_decay_helper import WeightDecayHelper as WeightDecayHelper
from _typeshed import Incomplete
from paddle.base import core as core
from paddle.incubate.optimizer import PipelineOptimizer as PipelineOptimizer
from paddle.static import create_global_var as create_global_var, default_startup_program as default_startup_program, device_guard as device_guard
from paddle.utils import unique_name as unique_name

class ShardingOptimizer(MetaOptimizerBase):
    inner_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    meta_optimizers_black_list: Incomplete
    mp_degree: int
    def __init__(self, optimizer) -> None: ...
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
    def collect_segment(self, segment, op_idx, block): ...
    def create_persistable_gradients_and_insert_merge_ops(self, main_block, startup_block, insert_idx, grad_names, shard) -> None: ...

class ThreadShardingOptimizer(ShardingOptimizer):
    inner_opt: Incomplete
    meta_optimizers_white_list: Incomplete
    op_role_key: Incomplete
    def __init__(self, optimizer) -> None: ...
    def minimize_impl(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
