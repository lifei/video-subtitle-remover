from ..utils.log_utils import get_logger as get_logger
from .auto_parallel_sharding import is_forward_op as is_forward_op
from .pass_base import PassBase as PassBase, register_pass as register_pass
from _typeshed import Incomplete
from paddle.distributed.auto_parallel.static.utils import is_optimize_op as is_optimize_op, is_recompute_op as is_recompute_op, naive_set_dist_op_attr_for_program_by_mesh_and_mapping as naive_set_dist_op_attr_for_program_by_mesh_and_mapping, set_var_dist_attr as set_var_dist_attr
from paddle.utils import unique_name as unique_name

logger: Incomplete
FUSED_LINEAR_SOURCE_PATTERNS_LIST: Incomplete

class FusedLinearPromotionPass(PassBase):
    def __init__(self) -> None: ...
