from ..common import OP_ROLE_KEY as OP_ROLE_KEY, OpRole as OpRole, is_optimizer_op as is_optimizer_op, is_update_op as is_update_op
from _typeshed import Incomplete
from paddle.framework import core as core
from paddle.utils import unique_name as unique_name

class PlaceType:
    CPU: int
    CUDA: int
    CUDA_PINNED: int
    XPU: int
    @staticmethod
    def default_device(): ...
    @staticmethod
    def default_pinned(): ...

class OffloadHelper:
    cpu_place_type: int
    cuda_place_type: Incomplete
    cuda_pinned_place_type: Incomplete
    mp_ring_id: Incomplete
    dp_ring_id: Incomplete
    def __init__(self, mp_ring_id: Incomplete | None = None, dp_ring_id: Incomplete | None = None) -> None: ...
    def offload_fp32param(self, block, startup_block, offload: bool = True) -> None: ...
    def cast_fp32param_in_optimize(self, block, startup_block) -> None: ...
    def offload(self, block, startup_block) -> None: ...
    def opt_sharding_cast_fp32param(self, block, startup_block, params, offload: bool = False) -> None: ...
