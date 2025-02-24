from .auto_parallel_sharding import ShardingPass as ShardingPass
from .pass_base import PassBase as PassBase, register_pass as register_pass
from paddle.distributed.auto_parallel.static.operators.common import is_amp_flag_sync_op as is_amp_flag_sync_op, is_data_parallel_reduce_op as is_data_parallel_reduce_op, is_global_norm_sync_op as is_global_norm_sync_op
from paddle.distributed.auto_parallel.static.utils import OpRole as OpRole, insert_dependencies_for_vars as insert_dependencies_for_vars, is_comm_op as is_comm_op

class AutoParalSupplementDepPass(PassBase):
    def __init__(self) -> None: ...
