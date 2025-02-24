from .pass_base import PassBase as PassBase, register_pass as register_pass
from .pass_utils import AutoParallelStreamType as AutoParallelStreamType
from _typeshed import Incomplete
from paddle.distributed.auto_parallel.static.operators.common import ParallelMode as ParallelMode, is_data_parallel_reduce_op as is_data_parallel_reduce_op, is_parameter_related as is_parameter_related
from paddle.distributed.auto_parallel.static.process_group import new_process_group as new_process_group
from paddle.distributed.auto_parallel.static.utils import get_logger as get_logger, get_var_numel as get_var_numel, insert_dependencies_for_vars as insert_dependencies_for_vars, is_backward_op as is_backward_op, is_dep_skip_op as is_dep_skip_op, is_forward_op as is_forward_op, is_loss_grad_op as is_loss_grad_op, is_optimize_op as is_optimize_op, naive_set_dist_op_attr_for_program_by_mesh_and_mapping as naive_set_dist_op_attr_for_program_by_mesh_and_mapping, set_var_dist_attr as set_var_dist_attr
from paddle.distributed.fleet.meta_optimizers.sharding.utils import get_var_size as get_var_size
from paddle.framework import core as core
from paddle.static import default_main_program as default_main_program, default_startup_program as default_startup_program
from paddle.utils import unique_name as unique_name

OpRole: Incomplete
OP_ROLE_KEY: Incomplete

class ShardingPass(PassBase):
    dp_groups: Incomplete
    sharding_infos: Incomplete
    varname_to_sharding_info: Incomplete
    sharding_hybrid_dp: bool
    outer_dp_group: Incomplete
    shared_params_grads: Incomplete
    def __init__(self) -> None: ...

def is_sharding_param_broadcast_op(op): ...
def partition_by_use_order(params, group_size): ...
def partition_by_greedy_even(params, group_size): ...
def partition_parameters(params, group_size, algor: str = 'greedy_even'): ...
def re_order_program(block, param_grads, dist_context): ...
def group_param(sharding_info, fuse_size): ...

class ShardingInfo:
    group: Incomplete
    params_grads: Incomplete
    params: Incomplete
    param_names: Incomplete
    group_size: Incomplete
    global_rank: Incomplete
    local_rank: Incomplete
    partition_algor: Incomplete
    rank_to_params: Incomplete
    param_to_rank: Incomplete
    def __init__(self, group, rank, params_grads, partition_algor) -> None: ...
    def get_var_rank(self, varname): ...
    def is_in_local_shard(self, param_name): ...
    def get_broadcast_vars_and_param_usage(self, block): ...
    def get_param_grad(self, param_name): ...

class VarGroup:
    max_siez: Incomplete
    dtype: Incomplete
    rank: int
    numel: int
    vars: Incomplete
    coalesce_var: Incomplete
    coalesce_dep_varname: Incomplete
    coalesce_op_idx: Incomplete
    reduce_op_indices: Incomplete
    allreduce_op_indices: Incomplete
    is_in_local_shard: bool
    def __init__(self, max_size) -> None: ...
    def acceptable(self, param, rank): ...
    def collect(self, param, rank) -> None: ...
    def __len__(self) -> int: ...
