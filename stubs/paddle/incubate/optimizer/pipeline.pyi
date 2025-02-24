from _typeshed import Incomplete
from paddle.base import core as core, unique_name as unique_name
from paddle.base.framework import Parameter as Parameter, Program as Program, default_startup_program as default_startup_program, in_dygraph_mode as in_dygraph_mode

class PipelineOptimizer:
    output_var_to_op: Incomplete
    input_var_to_op: Incomplete
    def __init__(self, optimizer, num_microbatches: int = 1, start_cpu_core_id: int = 0) -> None: ...
    origin_main_block: Incomplete
    local_rank: Incomplete
    schedule_mode: Incomplete
    micro_batch_size: Incomplete
    use_sharding: Incomplete
    ring_id: Incomplete
    global_ring_id: Incomplete
    mp_degree: Incomplete
    mp_rank: Incomplete
    scale_gradient: Incomplete
    def minimize(self, loss, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None): ...
