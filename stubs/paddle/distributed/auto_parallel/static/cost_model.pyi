from _typeshed import Incomplete
from enum import Enum
from paddle.distributed.fleet.meta_optimizers.common import OpRole as OpRole
from paddle.framework import core as core

SUCC: int
PRED: int

class CostNodeType(Enum):
    DEFAULT = 0
    COMPUTATION = 1
    COMMUNICATION = 2
    VARIABLE = 3
    MERGED = 4
    NOP = 5

class Cost:
    runtime: Incomplete
    static_mem: Incomplete
    peak_mem: Incomplete
    def __init__(self) -> None: ...

class CostModelMode(Enum):
    DEFAULT = 0
    BENCHMARKING = 1
    ANALYSIS = 2
    MIXED = 3

class CostNode:
    id: Incomplete
    node: Incomplete
    type: Incomplete
    is_optim: bool
    is_bwd: bool
    def __init__(self, node, node_type, id: Incomplete | None = None) -> None: ...
    @property
    def cost(self): ...
    @cost.setter
    def cost(self, cost) -> None: ...

class MergedOpsCostNode(CostNode):
    node_list: Incomplete
    is_bwd: Incomplete
    def __init__(self, node_type, id: Incomplete | None = None, base_node_list: Incomplete | None = None, is_bwd: bool = False) -> None: ...

class CommOpCostNode(CostNode):
    node_list: Incomplete
    ranks: Incomplete
    comm_type: Incomplete
    is_bwd: Incomplete
    def __init__(self, node, node_type, id: Incomplete | None = None, comm_node_list: Incomplete | None = None, is_bwd: bool = False) -> None: ...
    def set_ranks(self, ranks) -> None: ...
    input_shape: Incomplete
    output_shape: Incomplete
    def set_shapes(self, input_shape, output_shape) -> None: ...
    def init_comm_cost(self, cluster: Incomplete | None = None) -> None: ...

class TensorCostNode(CostNode):
    shape: Incomplete
    dtype: Incomplete
    dtype_factor: int
    persistable: Incomplete
    shared_node_id: Incomplete
    batch_size: Incomplete
    def __init__(self, node, node_type, id: Incomplete | None = None, base_node_list: Incomplete | None = None, batch_size: Incomplete | None = None, shared_node_id: Incomplete | None = None) -> None: ...
    def get_size(self): ...

class CompOpCostNode(CostNode):
    is_bwd: Incomplete
    is_optim: Incomplete
    def __init__(self, node, node_type, id: Incomplete | None = None, is_bwd: bool = False, is_optim: bool = False) -> None: ...
    cost: Incomplete
    def init_comp_cost(self, cost_data) -> None: ...

class PipeEvent:
    stage_id: Incomplete
    name: Incomplete
    duration: Incomplete
    s_time: Incomplete
    e_time: int
    def __init__(self, stage_id, event_name, duration, start_time: int = -1) -> None: ...

class CostModel:
    mode: Incomplete
    opcall_overhead: Incomplete
    batch_size: Incomplete
    microbatch_num: Incomplete
    nodes: Incomplete
    origin_graph: Incomplete
    op_graph: Incomplete
    runtime_graph: Incomplete
    cluster: Incomplete
    cost_data: Incomplete
    pp2rank: Incomplete
    rank2pp: Incomplete
    ring2rank: Incomplete
    fwd_time: Incomplete
    bwd_time: Incomplete
    optim_time: Incomplete
    def __init__(self, mode=..., cluster: Incomplete | None = None, batch_size: int = 1, microbatch_num: int = 1, opcall_overhead: int = 0, standalone_cost_data: Incomplete | None = None, pipeline_config: Incomplete | None = None) -> None: ...
    distributed_program: Incomplete
    total_rank: Incomplete
    def parse_program(self, distributed_program): ...
    def build_op_graph(self) -> None: ...
    def build_runtime_graph(self) -> None: ...
    def eliminate_multi_edges(self, graph: Incomplete | None = None) -> None: ...
    def merge_comm(self) -> None: ...
    def merge_linear(self): ...
    def merge_branch(self): ...
    def get_runtime_cost(self): ...
    def get_mem(self): ...
    def get_pipeline_time(self): ...
    def get_cost(self): ...
    def init(self, distributed_program) -> None: ...

def estimate_cost(distributed_program, cluster, pipeline_config, standalone_cost_data, batch_size): ...
