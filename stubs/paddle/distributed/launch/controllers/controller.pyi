from .master import Master as Master
from .watcher import Watcher as Watcher
from _typeshed import Incomplete
from paddle.distributed.launch.job.container import Container as Container
from paddle.distributed.launch.job.job import Job as Job
from paddle.distributed.launch.job.pod import Pod as Pod

class ControleMode:
    COLLECTIVE: str
    PS: str
    IPU: str
    RPC: str

class ControllerBase:
    ctx: Incomplete
    master: Incomplete
    watcher: Incomplete
    job: Incomplete
    pod: Incomplete
    join_server: Incomplete
    def __init__(self, ctx) -> None: ...
    def deploy_pod(self) -> None: ...
    def run(self) -> None: ...
    def watch(self) -> bool: ...
    def stop(self, sigint: Incomplete | None = None) -> None: ...
    def finalize(self, exit: bool = True) -> None: ...
    sigint: Incomplete
    def signal_handler(self, sigint, frame) -> None: ...
    def not_exit_signal_handler(self, sigint, frame) -> None: ...

class Controller(ControllerBase):
    def build_job(self) -> None: ...
    def build_pod(self) -> bool: ...
    def new_container(self, entrypoint: Incomplete | None = None, envs={}, use_ctx_env: bool = True, out: Incomplete | None = None, err: Incomplete | None = None): ...
    def add_container(self, container: Incomplete | None = None, entrypoint: Incomplete | None = None, envs={}, log_file: Incomplete | None = None, is_init: bool = False) -> None: ...
    def pod_replicas(self): ...
    def save_pod_log(self, info) -> None: ...
    def save_pod_env(self) -> None: ...
