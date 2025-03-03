from .group_sharded_utils import Type as Type, cvt_to_device as cvt_to_device, device_guard as device_guard
from _typeshed import Incomplete
from paddle.framework import core as core

class BufferWarper(core.eager.Tensor):
    need_clip: bool
    is_distributed: bool
    trainable: bool
    def __init__(self) -> None: ...

class InternalStorage:
    buffer: Incomplete
    dev_id: Incomplete
    def __init__(self, size, dtype, device, convert_cpu: bool = False) -> None: ...
    def to(self, device, dtype: Incomplete | None = None, keep_alignment: bool = True) -> None: ...
    def warp_buffer(self) -> None: ...

class ParamStorage(InternalStorage):
    param2align: Incomplete
    def __init__(self, size, dtype, device) -> None: ...
    def to(self, device, dtype: Incomplete | None = None, keep_alignment: bool = True) -> None: ...
    buffer: Incomplete
    def add_rank_params(self, trainable_params, param2align, convert_gpu: bool = True) -> None: ...

class GradStorage(InternalStorage):
    params_checked_in: int
    destination: Incomplete
    sent: bool
    def __init__(self, size, dtype, device, destination, parm2align, convert_cpu: bool = False) -> None: ...
    def reset_checked_in(self) -> None: ...
    @property
    def all_checked_in(self): ...
    def can_add_grad_view(self, param, align): ...
    def to(self, device, dtype: Incomplete | None = None, keep_alignment: bool = True) -> None: ...
    def add_grad(self, param, align) -> None: ...
    buffer: Incomplete
    def manumal_relase(self) -> None: ...
    def rebuild(self) -> None: ...
