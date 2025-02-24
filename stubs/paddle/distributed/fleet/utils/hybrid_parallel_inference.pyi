from _typeshed import Incomplete
from paddle.base import core as core
from paddle.distributed import fleet as fleet
from paddle.framework import Block as Block, Program as Program, in_dynamic_mode as in_dynamic_mode

class HybridParallelInferenceHelper:
    ring_id: int
    micro_batch_size: Incomplete
    beam_size: Incomplete
    init_comm: Incomplete
    role_maker: Incomplete
    mp_ring_id: int
    global_ring_id: int
    endpoints: Incomplete
    current_endpoint: Incomplete
    rank: Incomplete
    nranks: Incomplete
    num_pp: Incomplete
    num_mp: Incomplete
    global_endpoints: Incomplete
    global_rank: Incomplete
    global_nranks: Incomplete
    mp_group: Incomplete
    pp_group: Incomplete
    def __init__(self, startup_program, main_program, num_mp: int = 1, num_pp: int = 1, micro_batch_size: int = 1, beam_size: int = 1, init_comm: bool = True, role_maker: Incomplete | None = None) -> None: ...
    def gen_infer_program(self, sync_in_while_lastpp2firstpp_var_names: Incomplete | None = None, sync_in_while_var_names: Incomplete | None = None, debug: bool = False) -> None: ...
