from ...random import determinate_rng as determinate_rng, is_enable_auto_rand_ctrl as is_enable_auto_rand_ctrl
from ..completion import get_phi_spmd_rule as get_phi_spmd_rule
from ..utils import get_dist_tensor_spec as get_dist_tensor_spec, naive_set_dist_op_attr_for_program_by_mesh_and_mapping as naive_set_dist_op_attr_for_program_by_mesh_and_mapping, set_var_dist_attr as set_var_dist_attr
from .common import DistributedOperatorImplContainer as DistributedOperatorImplContainer, merge_forward_backward_dims_mapping as merge_forward_backward_dims_mapping, register_distributed_operator_impl as register_distributed_operator_impl, register_distributed_operator_impl_container as register_distributed_operator_impl_container, update_op_dims_mapping as update_op_dims_mapping
from .dist_eltwise import DistributedDefaultImpl0 as DistributedDefaultImpl0, DistributedElementwiseImpl0 as DistributedElementwiseImpl0
from paddle.base.log_helper import get_logger as get_logger
from paddle.framework import core as core
from paddle.utils import unique_name as unique_name

class DistributedDropout(DistributedOperatorImplContainer):
    def __init__(self, op_type) -> None: ...
    @staticmethod
    def update_dims_mapping(dist_op): ...
    @staticmethod
    def mapping_to_dist_operator_impl(dist_op, original_op_dist_attr): ...

class DistributedDropoutImpl0(DistributedElementwiseImpl0):
    def __init__(self, name) -> None: ...
    @staticmethod
    def forward(ctx, *args, **kwargs) -> None: ...
    @staticmethod
    def backward(ctx, *args, **kwargs) -> None: ...
