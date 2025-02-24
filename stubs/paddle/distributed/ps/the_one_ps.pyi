from paddle.distributed.ps.utils.public import *
from _typeshed import Incomplete
from paddle.distributed.fleet.runtime.runtime_base import RuntimeBase

__all__ = ['Table', 'SparseTable', 'GeoSparseTable', 'BarrierTable', 'TensorTable', 'DenseTable']

class Service:
    def __init__(self) -> None: ...

class GpuService(Service):
    def __init__(self) -> None: ...

class Accessor:
    accessor_class: str
    optimizer: Incomplete
    feature_dim: int
    embedding_dim: int
    def __init__(self) -> None: ...

class CommonAccessor(Accessor):
    table_name: str
    entry: str
    attrs: Incomplete
    params: Incomplete
    dims: Incomplete
    trainer_num: int
    sync: bool
    initializers: Incomplete
    opt_input_map: Incomplete
    opt_attr_map: Incomplete
    opt_init_map: Incomplete
    def __init__(self) -> None: ...
    def define_optimize_map(self) -> None: ...
    def parse_entry(self, varname, program_id, context) -> None: ...
    def get_shard(self, total_dim, shard_num, pserver_id): ...
    def get_initializer_attr(self, value_name, o_startup_program): ...
    table_num: Incomplete
    table_dim: Incomplete
    accessor_class: str
    def parse_by_optimizer(self, ctx, context) -> None: ...

class Tensor:
    tensor_dict: Incomplete
    def __init__(self, tesnor_dcit) -> None: ...

class Table:
    table_class: Incomplete
    shard_num: int
    type: Incomplete
    accessor: Incomplete
    common: Incomplete
    tensor: Incomplete
    def __init__(self) -> None: ...

class BarrierTable(Table):
    type: Incomplete
    shard_num: int
    is_heter_ps_mode: Incomplete
    role_maker: Incomplete
    idx: Incomplete
    is_sync: Incomplete
    def __init__(self, context, idx) -> None: ...

class TensorTable(Table):
    idx: Incomplete
    tensor_dict: Incomplete
    role_maker: Incomplete
    def __init__(self, idx, tensor_dict, role_maker) -> None: ...

class SparseTable(Table):
    context: Incomplete
    ctx: Incomplete
    type: Incomplete
    table_class: str
    accessor: Incomplete
    def __init__(self, context, send_ctx) -> None: ...

class GeoSparseTable(SparseTable):
    table_class: str
    def __init__(self, context, send_ctx) -> None: ...

class DenseTable(Table):
    context: Incomplete
    ctx: Incomplete
    accessor: Incomplete
    def __init__(self, context, send_ctx) -> None: ...

class Server:
    def __init__(self) -> None: ...

class DownpourServer(Server):
    def __init__(self) -> None: ...

class Worker:
    def __init__(self) -> None: ...

class DownpourWorker(Worker):
    def __init__(self) -> None: ...

class fsClient:
    fs_client_param: Incomplete
    def __init__(self, fs_client_param) -> None: ...

class PsDescBuilder:
    context: Incomplete
    is_sync: Incomplete
    ps_mode: Incomplete
    is_heter_ps_mode: Incomplete
    use_ps_gpu: Incomplete
    barrier_table_id: Incomplete
    send_ctx: Incomplete
    tensor_table_dict: Incomplete
    tables: Incomplete
    service: Incomplete
    fs_client: Incomplete
    ps_desc: Incomplete
    fl_desc: Incomplete
    def __init__(self, context) -> None: ...
    def build_fl_client_desc(self, client_info) -> None: ...
    def build_worker_desc(self): ...
    sparse_table_maps: Incomplete
    def build_server_desc(self): ...

class TheOnePSRuntime(RuntimeBase):
    def __init__(self) -> None: ...
