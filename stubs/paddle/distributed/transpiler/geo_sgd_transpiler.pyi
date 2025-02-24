from .distribute_transpiler import DistributeTranspiler as DistributeTranspiler, DistributeTranspilerConfig as DistributeTranspilerConfig, slice_variable as slice_variable
from _typeshed import Incomplete
from paddle import framework as framework
from paddle.distributed.distribute_lookup_table import find_distributed_lookup_table as find_distributed_lookup_table
from paddle.distributed.transpiler.details import VarsDistributed as VarsDistributed, wait_server_ready as wait_server_ready
from paddle.framework import Program as Program, core as core
from paddle.incubate.distributed.fleet.parameter_server.ir.ps_dispatcher import PSDispatcher as PSDispatcher, RoundRobin as RoundRobin
from paddle.incubate.distributed.fleet.parameter_server.mode import DistributedMode as DistributedMode
from paddle.static import Parameter as Parameter, default_main_program as default_main_program, default_startup_program as default_startup_program

RPC_OP_ROLE_ATTR_NAME: Incomplete
op_role_attr_name: Incomplete
RPC_OP_ROLE_ATTR_VALUE: Incomplete

class GeoSgdTranspiler(DistributeTranspiler):
    config: Incomplete
    def __init__(self, config: Incomplete | None = None) -> None: ...
    origin_program: Incomplete
    startup_program: Incomplete
    origin_startup_program: Incomplete
    trainer_num: Incomplete
    sync_mode: bool
    trainer_id: Incomplete
    pserver_endpoints: Incomplete
    vars_overview: Incomplete
    param_name_to_grad_name: Incomplete
    grad_name_to_param_name: Incomplete
    table_name: Incomplete
    has_distributed_lookup_table: Incomplete
    vars_info: Incomplete
    split_to_origin_mapping: Incomplete
    delta_vars_list: Incomplete
    sparse_var_list: Incomplete
    sparse_var_splited_list: Incomplete
    sparse_var: Incomplete
    sparse_tables: Incomplete
    trainer_startup_program: Incomplete
    def transpile(self, trainer_id, program: Incomplete | None = None, pservers: str = '127.0.0.1:6174', trainers: int = 1, sync_mode: bool = False, startup_program: Incomplete | None = None, current_endpoint: str = '127.0.0.1:6174') -> None: ...
    def get_trainer_program(self, wait_port: bool = True): ...
    param_grad_ep_mapping: Incomplete
    def get_pserver_programs(self, endpoint): ...
    pserver_program: Incomplete
    def get_pserver_program(self, endpoint): ...
