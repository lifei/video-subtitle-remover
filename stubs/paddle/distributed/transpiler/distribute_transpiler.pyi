from _typeshed import Incomplete
from paddle import framework as framework
from paddle.base.framework import grad_var_name as grad_var_name
from paddle.framework import Block as Block, Program as Program, core as core
from paddle.incubate.distributed.fleet.parameter_server.ir.ps_dispatcher import PSDispatcher as PSDispatcher, RoundRobin as RoundRobin
from paddle.nn.initializer import Constant as Constant
from paddle.static import Parameter as Parameter, default_main_program as default_main_program, default_startup_program as default_startup_program
from paddle.utils import unique_name as unique_name

LOOKUP_TABLE_TYPE: Incomplete
LOOKUP_TABLE_GRAD_TYPE: Incomplete
OP_NAME_SCOPE: str
CLIP_OP_NAME_SCOPE: str
OP_ROLE_VAR_ATTR_NAME: Incomplete
RPC_OP_ROLE_ATTR_NAME: Incomplete
op_role_attr_name: Incomplete
OPT_OP_ROLE_ATTR_VALUE: Incomplete
RPC_OP_ROLE_ATTR_VALUE: Incomplete
DIST_OP_ROLE_ATTR_VALUE: Incomplete
LR_SCHED_OP_ROLE_ATTR_VALUE: Incomplete
PRINT_LOG: bool

class DistributedMode:
    SYNC: int
    ASYNC: int
    HALF_ASYNC: int
    GEO: int

def log(*args) -> None: ...

class VarBlock:
    varname: Incomplete
    offset: Incomplete
    size: Incomplete
    def __init__(self, varname, offset, size) -> None: ...

def same_or_split_var(p_name, var_name): ...
def slice_variable(var_list, slice_count, min_block_size): ...

class DistributeTranspilerConfig:
    slice_var_up: bool
    split_method: Incomplete
    min_block_size: int
    enable_dc_asgd: bool
    mode: str
    print_log: bool
    wait_port: bool
    half_async: bool
    completely_not_async: bool
    geo_sgd_mode: bool
    geo_sgd_need_push_nums: int
    nccl_comm_num: int
    use_hierarchical_allreduce: bool
    hierarchical_allreduce_inter_nranks: int
    collective_mode: Incomplete
    def __init__(self) -> None: ...
    @property
    def runtime_split_send_recv(self): ...
    @runtime_split_send_recv.setter
    def runtime_split_send_recv(self, value) -> None: ...
    @property
    def sync_mode(self): ...
    @sync_mode.setter
    def sync_mode(self, value) -> None: ...

class ServerRuntimeConfig:
    def __init__(self) -> None: ...

class DistributeTranspiler:
    config: Incomplete
    distributed_mode: Incomplete
    counter_var: Incomplete
    def __init__(self, config: Incomplete | None = None) -> None: ...
    origin_program: Incomplete
    startup_program: Incomplete
    origin_startup_program: Incomplete
    trainer_num: Incomplete
    sync_mode: Incomplete
    trainer_id: Incomplete
    pserver_endpoints: Incomplete
    vars_overview: Incomplete
    table_name: Incomplete
    has_distributed_lookup_table: Incomplete
    param_name_to_grad_name: Incomplete
    grad_name_to_param_name: Incomplete
    sparse_update_ops: Incomplete
    sparse_param_to_height_sections: Incomplete
    need_delete_optimize_vars: Incomplete
    grad_name_to_send_dummy_out: Incomplete
    def transpile(self, trainer_id, program: Incomplete | None = None, pservers: str = '127.0.0.1:6174', trainers: int = 1, sync_mode: bool = True, startup_program: Incomplete | None = None, current_endpoint: str = '127.0.0.1:6174') -> None: ...
    def get_trainer_program(self, wait_port: bool = True): ...
    param_bak_list: Incomplete
    pserver_program: Incomplete
    def get_pserver_program(self, endpoint): ...
    def get_pserver_programs(self, endpoint): ...
    def get_startup_program(self, endpoint, pserver_program: Incomplete | None = None, startup_program: Incomplete | None = None): ...
