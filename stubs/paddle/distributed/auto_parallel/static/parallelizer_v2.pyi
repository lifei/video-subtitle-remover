from ...utils.log_utils import get_logger as get_logger
from ..random import init_auto_parallel_rng as init_auto_parallel_rng
from .partitioner import Partitioner as Partitioner
from .process_group import get_world_process_group as get_world_process_group
from .reshard import Resharder as Resharder
from .utils import get_pp_stage as get_pp_stage, is_sequential_run as is_sequential_run, use_new_executor as use_new_executor
from _typeshed import Incomplete
from paddle.distributed.passes import PassManager as PassManager, new_pass as new_pass
from paddle.framework import get_flags as get_flags
from paddle.static import append_backward as append_backward, program_guard as program_guard
from paddle.utils import unique_name as unique_name

NEW_IR_PASS: Incomplete

class Parallelizer:
    def __init__(self, mode, completer, dist_context) -> None: ...
    @property
    def is_train(self): ...
    @property
    def is_test(self): ...
    def parallel_all(self, parameter_list: Incomplete | None = None) -> None: ...
    def parallel(self, rank, parameter_list: Incomplete | None = None) -> None: ...
