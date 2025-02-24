from ..framework import core as core
from _typeshed import Incomplete

MP_STATUS_CHECK_INTERVAL: float
multiprocess_queue_set: Incomplete

class CleanupFuncRegistrar:
    @classmethod
    def register(cls, function, signals=[]) -> None: ...
