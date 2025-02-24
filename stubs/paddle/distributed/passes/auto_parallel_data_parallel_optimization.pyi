from .pass_base import PassBase as PassBase, PassType as PassType, register_pass as register_pass
from _typeshed import Incomplete
from paddle.distributed.auto_parallel.process_mesh import ProcessMesh as ProcessMesh
from paddle.distributed.auto_parallel.static.dist_attribute import OperatorDistAttr as OperatorDistAttr, TensorDistAttr as TensorDistAttr
from paddle.distributed.auto_parallel.static.operators.common import is_data_parallel_reduce_op as is_data_parallel_reduce_op, is_data_parallel_scale_op as is_data_parallel_scale_op
from paddle.distributed.auto_parallel.static.utils import find_higher_order_backward_op as find_higher_order_backward_op, get_var_numel as get_var_numel, insert_dependencies_for_vars as insert_dependencies_for_vars, is_forward_op as is_forward_op, is_loss_grad_op as is_loss_grad_op, is_optimize_op as is_optimize_op, ring_id_to_process_group as ring_id_to_process_group
from paddle.distributed.fleet.meta_optimizers.common import OP_ROLE_KEY as OP_ROLE_KEY, OpRole as OpRole
from paddle.static import default_main_program as default_main_program
from paddle.utils import unique_name as unique_name

__rescale_grad_supported_opts__: Incomplete
__max_stream_num_allow__: int

class DataParallelOptimizationPass(PassBase):
    def __init__(self) -> None: ...
    def is_data_parallel_applied(self): ...
    def summary(self, grad_groups=[]) -> None: ...

class GradientsGroup:
    max_group_size: Incomplete
    ops: Incomplete
    gradients: Incomplete
    numel: int
    dtype: Incomplete
    ring_id: Incomplete
    coalesce_var: Incomplete
    coalesce_op_idx: int
    allreduce_op_idx: int
    scale_op_idx: int
    remove_wait_op_indices: Incomplete
    remove_allreduce_op_indices: Incomplete
    remove_scale_op_indices: Incomplete
    def __init__(self, ops, max_group_size) -> None: ...
    def acceptable(self, grad_var, ring_id): ...
    def add(self, grad_var, ring_id, i) -> None: ...
    def finalize(self) -> None: ...
