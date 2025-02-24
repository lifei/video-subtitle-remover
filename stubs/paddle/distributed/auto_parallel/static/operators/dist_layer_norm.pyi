from ..completion import get_phi_spmd_rule as get_phi_spmd_rule
from ..utils import get_dist_tensor_spec as get_dist_tensor_spec, is_dim_shard as is_dim_shard
from .common import DistributedOperatorImplContainer as DistributedOperatorImplContainer, get_default_distributed_operator_impl as get_default_distributed_operator_impl, register_distributed_operator_impl_container as register_distributed_operator_impl_container, update_op_dims_mapping as update_op_dims_mapping
from paddle.base.log_helper import get_logger as get_logger

class DistributedLayerNorm(DistributedOperatorImplContainer):
    def __init__(self, op_type) -> None: ...
    @staticmethod
    def update_dims_mapping(dist_op): ...
    @staticmethod
    def mapping_to_dist_operator_impl(dist_op, original_op_dist_attr): ...
