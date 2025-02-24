from .profiler_statistic import SortedKeys as SortedKeys, StatisticData as StatisticData, gen_layer_flops as gen_layer_flops
from .timer import benchmark as benchmark
from .utils import RecordEvent as RecordEvent, wrap_optimizers as wrap_optimizers
from _typeshed import Incomplete
from enum import Enum
from paddle.base.core import ProfilerOptions as ProfilerOptions, TracerEventType as TracerEventType, disable_memory_recorder as disable_memory_recorder, disable_op_info_recorder as disable_op_info_recorder, enable_memory_recorder as enable_memory_recorder, enable_op_info_recorder as enable_op_info_recorder
from paddle.profiler import utils as utils
from typing import Any, Callable, Iterable

class SummaryView(Enum):
    DeviceView = 0
    OverView = 1
    ModelView = 2
    DistributedView = 3
    KernelView = 4
    OperatorView = 5
    MemoryView = 6
    MemoryManipulationView = 7
    UDFView = 8

class ProfilerState(Enum):
    CLOSED = 0
    READY = 1
    RECORD = 2
    RECORD_AND_RETURN = 3

class ProfilerTarget(Enum):
    CPU = 0
    GPU = 1
    XPU = 2
    CUSTOM_DEVICE = 3

def make_scheduler(*, closed: int, ready: int, record: int, repeat: int = 0, skip_first: int = 0) -> Callable: ...
def export_chrome_tracing(dir_name: str, worker_name: str | None = None) -> Callable: ...
def export_protobuf(dir_name: str, worker_name: str | None = None) -> Callable: ...

class Profiler:
    targets: Incomplete
    profiler: Incomplete
    scheduler: Incomplete
    on_trace_ready: Incomplete
    step_num: int
    previous_state: Incomplete
    current_state: Incomplete
    record_event: Incomplete
    profiler_result: Incomplete
    timer_only: Incomplete
    record_shapes: Incomplete
    profile_memory: Incomplete
    with_flops: Incomplete
    emit_nvtx: Incomplete
    def __init__(self, *, targets: Iterable[ProfilerTarget] | None = None, scheduler: Callable[[int], ProfilerState] | tuple | None = None, on_trace_ready: Callable[..., Any] | None = None, record_shapes: bool | None = False, profile_memory: bool | None = False, timer_only: bool | None = False, emit_nvtx: bool | None = False, custom_device_types: list | None = [], with_flops: bool | None = False) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def step(self, num_samples: int | None = None): ...
    def step_info(self, unit: Incomplete | None = None): ...
    def export(self, path: str = '', format: str = 'json') -> None: ...
    def summary(self, sorted_by=..., op_detail: bool = True, thread_sep: bool = False, time_unit: str = 'ms', views: Incomplete | None = None) -> None: ...

def get_profiler(config_path): ...
