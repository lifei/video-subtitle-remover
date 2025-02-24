from ...backup_env import getenv_or_backup as getenv_or_backup
from _typeshed import Incomplete
from paddle.distributed.fleet import cloud_utils as cloud_utils, launch_utils as launch_utils
from paddle.distributed.utils.log_utils import get_logger as get_logger

logger: Incomplete
ELASTIC_EXIT_CODE: int
ELASTIC_AUTO_PARALLEL_EXIT_CODE: int
ELASTIC_TIMEOUT: Incomplete
ELASTIC_TTL: int

class ElasticLevel:
    FAULT_TOLERANCE: int
    ELASTIC: int

class ElasticStatus:
    COMPLETED: str
    ERROR: str
    HOLD: str
    RESTART: str
    EXIT: str

class LauncherInterface:
    args: Incomplete
    procs: Incomplete
    def __init__(self, args) -> None: ...
    def launch(self) -> None: ...
    def stop(self) -> None: ...
    def watch(self) -> None: ...

class ElasticManager:
    args: Incomplete
    host: Incomplete
    elastic_timeout: Incomplete
    start_port: Incomplete
    trainers: Incomplete
    np: Incomplete
    dist_endpoints: Incomplete
    trainer_endpoints_list: Incomplete
    curr_host: Incomplete
    elastic_level: Incomplete
    hosts: Incomplete
    stopped: bool
    sigint: int
    need_sync: bool
    elastic_startup_time: Incomplete
    enable: bool
    etcd: Incomplete
    prefix: Incomplete
    node_prefix: Incomplete
    np_path: Incomplete
    endpoints_path: Incomplete
    host_path: Incomplete
    watches: Incomplete
    launcher: Incomplete
    def __init__(self, args, etcd_client) -> None: ...
    def exit(self, completed: bool = False) -> None: ...
    def pre_hook(self) -> None: ...
    def wait(self) -> None: ...
    def run(self, launcher) -> None: ...
    def watch(self): ...
    def signal_handler(self, sigint, frame) -> None: ...
