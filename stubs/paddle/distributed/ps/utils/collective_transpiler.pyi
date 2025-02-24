from _typeshed import Incomplete
from paddle.base import unique_name as unique_name
from paddle.distributed.fleet.base.private_helper_function import wait_server_ready as wait_server_ready
from paddle.framework import core as core
from paddle.static import default_main_program as default_main_program, default_startup_program as default_startup_program

OpRole: Incomplete

class Collective:
    nrings: Incomplete
    endpoints: Incomplete
    current_endpoint: Incomplete
    other_endpoints: Incomplete
    nranks: Incomplete
    rank: Incomplete
    startup_program: Incomplete
    main_program: Incomplete
    op_role_key: Incomplete
    op_role_var_key: Incomplete
    def __init__(self, nrings) -> None: ...
    wait_port: Incomplete
    def transpile(self, startup_program, main_program, rank, endpoints, current_endpoint, wait_port) -> None: ...

class GradAllReduce(Collective):
    mode: str
    def __init__(self, nrings: int = 2) -> None: ...

class LocalSGD(Collective):
    snapshot_key: str
    mode: str
    def __init__(self, nrings: int = 2) -> None: ...
    def snapshot_name(self, param_name): ...

class SingleProcessMultiThread(GradAllReduce):
    mode: str
    def __init__(self) -> None: ...

class MultiThread(GradAllReduce):
    mode: str
    trans_mode: Incomplete
    fuse_grad_size_in_num: int
    gpu_num: Incomplete
    def __init__(self, nrings: int = 1, trans_mode: str = 'all_reduce') -> None: ...
