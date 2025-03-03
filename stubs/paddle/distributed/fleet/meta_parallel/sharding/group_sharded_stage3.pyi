from .group_sharded_storage import GradStorage as GradStorage
from .group_sharded_utils import GroupShardedClipGrad as GroupShardedClipGrad, Type as Type, device_guard as device_guard
from _typeshed import Incomplete
from paddle import framework as framework, nn as nn
from paddle.autograd import PyLayer as PyLayer
from paddle.base.framework import EagerParamBase as EagerParamBase
from paddle.distributed import collective as collective
from paddle.framework import core as core
from paddle.nn import ClipGradByGlobalNorm as ClipGradByGlobalNorm

class OrderedSet:
    def __init__(self, iterable: Incomplete | None = None) -> None: ...
    def __contains__(self, item) -> bool: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def add(self, item) -> None: ...
    def discard(self, item) -> None: ...
    def update(self, iterable) -> None: ...

alignment: Incomplete
align: Incomplete
CHECK_LAYER: Incomplete

class GroupShardedStage3(nn.Layer):
    def __init__(self, layer, optimizer, group: Incomplete | None = None, sync_buffers: bool = False, device: str = 'gpu', segment_size=..., pertrain_sync_models: bool = True, offload: bool = False, sync_comm: bool = False, dp_group: Incomplete | None = None, exclude_layer: Incomplete | None = None) -> None: ...
    def forward(self, *inputs, **kwargs): ...
    def set_state_dict(self, state_dict, use_structured_name: bool = True) -> None: ...
    def state_dict(self, destination: Incomplete | None = None, include_sublayers: bool = True, structured_name_prefix: str = ''): ...
    def __getattr__(self, name): ...
    def get_all_parameters(self, convert2cpu: bool = False): ...

def ForwardPreHooks(layer, order_tracer, trainable_params, param2buffer_size, group, sync_comm, offload, task_flow) -> None: ...

class ForwardPostHooks(PyLayer):
    @staticmethod
    def forward(ctx, inputs, layer, order_tracer, trainable_params, param2buffer, param2buffer_size, rank, group, sync_comm, offload, task_flow): ...
    @staticmethod
    def backward(ctx, *args): ...

class TaskFlow:
    full_param: Incomplete
    full_grad: Incomplete
    use_calc: Incomplete
    callback: Incomplete
    def __init__(self, full_param={}, full_grad={}, use_calc={}, callback: Incomplete | None = None) -> None: ...
