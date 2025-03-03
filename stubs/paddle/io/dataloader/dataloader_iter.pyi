from ...framework import core as core, in_dynamic_mode as in_dynamic_mode
from ..multiprocess_utils import CleanupFuncRegistrar as CleanupFuncRegistrar, MP_STATUS_CHECK_INTERVAL as MP_STATUS_CHECK_INTERVAL
from .collate import default_collate_fn as default_collate_fn, default_convert_fn as default_convert_fn
from paddle import profiler as profiler
from paddle.profiler.timer import benchmark as benchmark
from paddle.profiler.utils import in_profiler_mode as in_profiler_mode

class _DataLoaderIterBase:
    def __init__(self, loader) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class _DataLoaderIterSingleProcess(_DataLoaderIterBase):
    def __init__(self, loader) -> None: ...
    def __next__(self): ...
    def __del__(self) -> None: ...

class _DataLoaderIterMultiProcess(_DataLoaderIterBase):
    def __init__(self, loader) -> None: ...
    def __del__(self) -> None: ...
    def __next__(self): ...
