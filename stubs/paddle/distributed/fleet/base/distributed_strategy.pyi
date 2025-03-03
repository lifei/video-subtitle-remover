from _typeshed import Incomplete
from paddle.base.wrapped_decorator import wrap_decorator as wrap_decorator
from paddle.distributed.fleet.proto import distributed_strategy_pb2 as distributed_strategy_pb2
from paddle.distributed.fleet.utils.log_util import logger as logger

non_auto_func_called: bool

def __non_auto_func_called__(func): ...

is_strict_auto: Incomplete

def get_repeated_msg_dict(msg): ...
def get_msg_dict(msg): ...
def assign_repeated_msg(msg, config) -> None: ...
def assign_configs_value(msg, config) -> None: ...
def check_configs_key(msg, config, field_name) -> None: ...

class DistributedJobInfo:
    job_info: Incomplete
    def __init__(self) -> None: ...
ReduceStrategyFleet = int

class DistributedStrategy:
    strategy: Incomplete
    hybrid_parallel_order: Incomplete
    sync_param_name: Incomplete
    def __init__(self) -> None: ...
    def __setattr__(self, key, value) -> None: ...
    def save_to_prototxt(self, output) -> None: ...
    def load_from_prototxt(self, pb_file) -> None: ...
    @property
    def execution_strategy(self): ...
    @execution_strategy.setter
    def execution_strategy(self, strategy) -> None: ...
    @property
    def build_strategy(self): ...
    @build_strategy.setter
    def build_strategy(self, strategy) -> None: ...
    @property
    def gradient_scale_configs(self): ...
    @gradient_scale_configs.setter
    def gradient_scale_configs(self, config) -> None: ...
    @property
    def a_sync(self): ...
    @a_sync.setter
    def a_sync(self, flag) -> None: ...
    @property
    def a_sync_configs(self): ...
    @a_sync_configs.setter
    def a_sync_configs(self, configs) -> None: ...
    @property
    def trainer_desc_configs(self): ...
    @property
    def adam_d2sum(self): ...
    @adam_d2sum.setter
    def adam_d2sum(self, flag) -> None: ...
    @trainer_desc_configs.setter
    def trainer_desc_configs(self, configs) -> None: ...
    @property
    def fs_client_param(self): ...
    @fs_client_param.setter
    def fs_client_param(self, configs) -> None: ...
    @property
    def sparse_table_configs(self): ...
    @sparse_table_configs.setter
    def sparse_table_configs(self, configs) -> None: ...
    @sparse_table_configs.setter
    def fleet_desc_configs(self, configs) -> None: ...
    @property
    def amp(self): ...
    @amp.setter
    def amp(self, flag) -> None: ...
    @property
    def amp_configs(self): ...
    @amp_configs.setter
    def amp_configs(self, configs) -> None: ...
    @property
    def asp(self): ...
    @asp.setter
    def asp(self, flag) -> None: ...
    @property
    def qat(self): ...
    @qat.setter
    def qat(self, flag) -> None: ...
    @property
    def qat_configs(self): ...
    @qat_configs.setter
    def qat_configs(self, configs) -> None: ...
    @property
    def recompute(self): ...
    @property
    def sync_nccl_allreduce(self): ...
    @sync_nccl_allreduce.setter
    def sync_nccl_allreduce(self, flag) -> None: ...
    @property
    def use_hierarchical_allreduce(self): ...
    @use_hierarchical_allreduce.setter
    def use_hierarchical_allreduce(self, flag) -> None: ...
    @property
    def hierarchical_allreduce_inter_nranks(self): ...
    @hierarchical_allreduce_inter_nranks.setter
    def hierarchical_allreduce_inter_nranks(self, value) -> None: ...
    @property
    def sync_batch_norm(self): ...
    @sync_batch_norm.setter
    def sync_batch_norm(self, flag) -> None: ...
    @property
    def fuse_all_reduce_ops(self): ...
    @fuse_all_reduce_ops.setter
    def fuse_all_reduce_ops(self, flag) -> None: ...
    @property
    def fuse_grad_size_in_MB(self): ...
    @fuse_grad_size_in_MB.setter
    def fuse_grad_size_in_MB(self, value) -> None: ...
    @property
    def last_comm_group_size_MB(self): ...
    @last_comm_group_size_MB.setter
    def last_comm_group_size_MB(self, value) -> None: ...
    @property
    def find_unused_parameters(self): ...
    @find_unused_parameters.setter
    def find_unused_parameters(self, flag) -> None: ...
    @property
    def nccl_comm_num(self): ...
    @nccl_comm_num.setter
    def nccl_comm_num(self, value) -> None: ...
    @recompute.setter
    def recompute(self, flag) -> None: ...
    @property
    def recompute_configs(self): ...
    @recompute_configs.setter
    def recompute_configs(self, configs) -> None: ...
    @property
    def sharding(self): ...
    @sharding.setter
    def sharding(self, flag) -> None: ...
    @property
    def sharding_configs(self): ...
    @sharding_configs.setter
    def sharding_configs(self, configs) -> None: ...
    @property
    def without_graph_optimization(self): ...
    @without_graph_optimization.setter
    def without_graph_optimization(self, flag) -> None: ...
    @property
    def fuse_grad_merge(self): ...
    @fuse_grad_merge.setter
    def fuse_grad_merge(self, fuse_grad_merge) -> None: ...
    @property
    def fuse_grad_size_in_num(self): ...
    @fuse_grad_size_in_num.setter
    def fuse_grad_size_in_num(self, num) -> None: ...
    @property
    def pipeline(self): ...
    @property
    def is_fl_ps_mode(self): ...
    @is_fl_ps_mode.setter
    def is_fl_ps_mode(self, flag) -> None: ...
    @property
    def is_with_coordinator(self): ...
    @is_with_coordinator.setter
    def is_with_coordinator(self, flag) -> None: ...
    @pipeline.setter
    def pipeline(self, flag) -> None: ...
    @property
    def pipeline_configs(self): ...
    @pipeline_configs.setter
    def pipeline_configs(self, configs) -> None: ...
    @property
    def tensor_parallel(self): ...
    @tensor_parallel.setter
    def tensor_parallel(self, flag) -> None: ...
    @property
    def tensor_parallel_configs(self): ...
    @tensor_parallel_configs.setter
    def tensor_parallel_configs(self, configs) -> None: ...
    @property
    def hybrid_configs(self): ...
    @hybrid_configs.setter
    def hybrid_configs(self, configs) -> None: ...
    @property
    def localsgd(self): ...
    @localsgd.setter
    def localsgd(self, flag) -> None: ...
    @property
    def localsgd_configs(self): ...
    @localsgd_configs.setter
    def localsgd_configs(self, configs) -> None: ...
    @property
    def adaptive_localsgd(self): ...
    @adaptive_localsgd.setter
    def adaptive_localsgd(self, flag) -> None: ...
    @property
    def adaptive_localsgd_configs(self): ...
    @adaptive_localsgd_configs.setter
    def adaptive_localsgd_configs(self, configs) -> None: ...
    @property
    def dgc(self): ...
    @dgc.setter
    def dgc(self, flag) -> None: ...
    @property
    def dgc_configs(self): ...
    @dgc_configs.setter
    def dgc_configs(self, configs) -> None: ...
    @property
    def fp16_allreduce(self): ...
    @fp16_allreduce.setter
    def fp16_allreduce(self, flag) -> None: ...
    @property
    def gradient_merge(self): ...
    @gradient_merge.setter
    def gradient_merge(self, flag) -> None: ...
    @property
    def gradient_merge_configs(self): ...
    @gradient_merge_configs.setter
    def gradient_merge_configs(self, configs) -> None: ...
    @property
    def lars(self): ...
    @lars.setter
    def lars(self, flag) -> None: ...
    @property
    def lars_configs(self): ...
    @lars_configs.setter
    def lars_configs(self, configs) -> None: ...
    @property
    def lamb(self): ...
    @lamb.setter
    def lamb(self, flag) -> None: ...
    @property
    def lamb_configs(self): ...
    @lamb_configs.setter
    def lamb_configs(self, configs) -> None: ...
    @property
    def elastic(self): ...
    @elastic.setter
    def elastic(self, flag) -> None: ...
    @property
    def auto(self): ...
    @auto.setter
    def auto(self, flag) -> None: ...
    @property
    def semi_auto(self): ...
    @semi_auto.setter
    def semi_auto(self, flag) -> None: ...
    @property
    def auto_search(self): ...
    @auto_search.setter
    def auto_search(self, flag) -> None: ...
    @property
    def split_data(self): ...
    @split_data.setter
    def split_data(self, flag) -> None: ...
    @property
    def qat(self): ...
    @qat.setter
    def qat(self, flag) -> None: ...
    @property
    def qat_configs(self): ...
    @qat_configs.setter
    def qat_configs(self, configs) -> None: ...
    @property
    def heter_ccl_mode(self): ...
    @heter_ccl_mode.setter
    def heter_ccl_mode(self, flag) -> None: ...
    @property
    def cudnn_exhaustive_search(self): ...
    @cudnn_exhaustive_search.setter
    def cudnn_exhaustive_search(self, flag) -> None: ...
    @property
    def conv_workspace_size_limit(self): ...
    @conv_workspace_size_limit.setter
    def conv_workspace_size_limit(self, value) -> None: ...
    @property
    def cudnn_batchnorm_spatial_persistent(self): ...
    @cudnn_batchnorm_spatial_persistent.setter
    def cudnn_batchnorm_spatial_persistent(self, flag) -> None: ...
