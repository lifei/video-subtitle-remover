from _typeshed import Incomplete
from paddle.distributed.ps.utils.public import DistributedMode as DistributedMode
from paddle.framework import core as core

class Communicator:
    mode: Incomplete
    envs: Incomplete
    communicator_: Incomplete
    send_ctx_: Incomplete
    recv_ctx_: Incomplete
    def __init__(self, mode, kwargs: Incomplete | None = None, envs: Incomplete | None = None) -> None: ...
    def init_with_ctx(self, send_ctx, recv_ctx, proto_txt, unit64_hosts, scope: Incomplete | None = None) -> None: ...
    def create_client_to_client_connection(self, pserver_timeout_ms: int = 500000, pserver_connect_timeout_ms: int = 10000, max_retry: int = 3) -> None: ...
    def get_client_info(self): ...
    def set_clients(self, host_list) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def is_running(self) -> None: ...
    def recv(self) -> None: ...
    def init_params(self, context) -> None: ...
    def pull_dense(self, context) -> None: ...
    def push_sparse_param(self, var_name, table_id: int = -1, scope: Incomplete | None = None) -> None: ...

class FLCommunicator(Communicator):
    mode: str
    def __init__(self, ps_hosts, kwargs: Incomplete | None = None) -> None: ...
    def start_coordinator(self, self_endpoint, trainer_endpoints) -> None: ...
    def save_fl_strategy(self, mp) -> None: ...
    def query_fl_clients_info(self): ...

class LargeScaleKV:
    scale_kv: Incomplete
    def __init__(self) -> None: ...
    def save(self, varname, dirname) -> None: ...
    def load(self, varname, dirname) -> None: ...
    def size(self, varname): ...

class HeterClient:
    heter_client_: Incomplete
    def __init__(self, endpoint, previous_endpoint, trainer_id) -> None: ...
    def stop(self) -> None: ...
