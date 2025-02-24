from ..utils.nvsmi import get_gpu_info as get_gpu_info, get_gpu_process as get_gpu_process, get_gpu_util as get_gpu_util
from _typeshed import Incomplete

class Watcher:
    ctx: Incomplete
    interval: int
    gpu_util: Incomplete
    gpus: Incomplete
    gpu_fd: Incomplete
    proc: Incomplete
    def __init__(self, ctx) -> None: ...
    def watch(self) -> None: ...
    def stop(self) -> None: ...
