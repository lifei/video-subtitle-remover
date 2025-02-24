from ...backup_env import getenv_or_backup as getenv_or_backup
from _typeshed import Incomplete
from paddle.base import core as core
from paddle.distributed.fleet.base.private_helper_function import wait_server_ready as wait_server_ready

class Role:
    WORKER: int
    SERVER: int
    HETER_WORKER: int
    ALL: int
    COORDINATOR: int

class Gloo:
    class RENDEZVOUS:
        HDFS: int
        FILE: int
        HTTP: int
    def __init__(self) -> None: ...
    def init(self, rendezvous, role, role_id, worker_num, server_num, need_init_all: bool = False, kwargs: Incomplete | None = None) -> None: ...
    def barrier(self, comm_world) -> None: ...
    def all_reduce(self, input, mode: str = 'sum', comm_world: str = 'worker'): ...
    def all_gather(self, input, comm_world: str = 'worker'): ...

class RoleMakerBase:
    def __init__(self) -> None: ...
    def to_string(self): ...

class PaddleCloudRoleMaker(RoleMakerBase):
    def __init__(self, is_collective: bool = False, **kwargs) -> None: ...

class UserDefinedRoleMaker(PaddleCloudRoleMaker):
    def __init__(self, is_collective: bool = False, init_gloo: bool = False, **kwargs) -> None: ...
