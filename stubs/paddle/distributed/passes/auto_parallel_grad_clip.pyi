from ..auto_parallel.process_mesh import ProcessMesh as ProcessMesh
from ..auto_parallel.static.dist_attribute import OperatorDistAttr as OperatorDistAttr, TensorDistAttr as TensorDistAttr
from ..auto_parallel.static.operators.common import SyncMode as SyncMode, is_data_parallel_reduce_op as is_data_parallel_reduce_op
from ..auto_parallel.static.process_group import get_all_process_groups as get_all_process_groups, get_world_process_group as get_world_process_group
from ..auto_parallel.static.reshard import Resharder as Resharder
from ..auto_parallel.static.utils import insert_dependencies_for_vars as insert_dependencies_for_vars, is_gradient_clip_op as is_gradient_clip_op, is_optimize_op as is_optimize_op
from .auto_parallel_sharding import ShardingPass as ShardingPass
from .pass_base import PassBase as PassBase, register_pass as register_pass
from _typeshed import Incomplete
from paddle.distributed.fleet.meta_optimizers.common import OP_ROLE_KEY as OP_ROLE_KEY, OpRole as OpRole

class ClipHelper:
    params: Incomplete
    params_name: Incomplete
    rank_id: Incomplete
    block: Incomplete
    dist_context: Incomplete
    pass_context: Incomplete
    sharding_group: Incomplete
    world_ranks: Incomplete
    world_nranks: Incomplete
    pure_data_parallel: Incomplete
    rank_to_params: Incomplete
    def __init__(self, params_grads, rank_id, block, dist_context, pass_context) -> None: ...
    def is_calcuate_norm(self, name): ...
    def is_local_param(self, name): ...
    def is_local_var_with_dist_attr(self, name): ...

class ClipGradByGloblNormPass(PassBase):
    def __init__(self) -> None: ...
