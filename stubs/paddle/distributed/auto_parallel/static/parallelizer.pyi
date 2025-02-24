from .cluster import Cluster as Cluster
from .completion import Completer as Completer
from .dist_context import DistributedContext as DistributedContext, set_default_distributed_context as set_default_distributed_context
from .dist_op import DistributedOperator as DistributedOperator
from .dist_tensor import DistributedTensor as DistributedTensor
from .mapper import mapping as mapping
from .partitioner import Partitioner as Partitioner
from .planner import Planner as Planner
from .process_group import ProcessGroup as ProcessGroup, get_all_process_groups as get_all_process_groups, get_process_group as get_process_group, get_world_process_group as get_world_process_group
from .reshard import Resharder as Resharder
from .utils import SerialProgramInfo as SerialProgramInfo, make_data_unshard as make_data_unshard
from _typeshed import Incomplete
from paddle.distributed.passes import PassContext as PassContext, new_pass as new_pass
from paddle.distributed.utils.log_utils import get_logger as get_logger
from paddle.framework import core as core
from paddle.static import append_backward as append_backward, program_guard as program_guard

class AutoParallelizer:
    def __init__(self, fleet) -> None: ...
    def parallelize(self, loss, startup_program, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None, callbacks: Incomplete | None = None): ...
    def __deepcopy__(self, memo): ...
