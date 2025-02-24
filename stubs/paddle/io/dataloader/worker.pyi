from ...framework import core as core
from ..multiprocess_utils import CleanupFuncRegistrar as CleanupFuncRegistrar, MP_STATUS_CHECK_INTERVAL as MP_STATUS_CHECK_INTERVAL
from _typeshed import Incomplete

class _IterableDatasetStopIteration:
    worker_id: Incomplete
    def __init__(self, worker_id) -> None: ...

class _ResumeIteration: ...

class _DatasetKind:
    MAP: int
    ITER: int
    @staticmethod
    def create_fetcher(kind, dataset, auto_collate_batch, collate_fn, drop_last): ...

class ParentWatchDog:
    def __init__(self) -> None: ...
    def is_alive(self): ...

def get_worker_info(): ...

class WorkerInfo:
    def __init__(self, **kwargs) -> None: ...
    def __setattr__(self, key, val): ...

class _WorkerException:
    worker_id: Incomplete
    exc_type: Incomplete
    exc_msg: Incomplete
    def __init__(self, worker_id, exc_info: Incomplete | None = None) -> None: ...
    def reraise(self) -> None: ...

INIT_A: int
MULT_A: int
INIT_B: int
MULT_B: int
MIX_MULT_L: int
MIX_MULT_R: int
XSHIFT: Incomplete
MASK32: int
