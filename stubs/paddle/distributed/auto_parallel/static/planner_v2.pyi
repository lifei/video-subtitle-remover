from ...utils.log_utils import get_logger as get_logger
from .completion import Completer as Completer
from .dist_context import get_default_distributed_context as get_default_distributed_context
from .tuner.parallel_tuner import ParallelTuner as ParallelTuner
from .tuner.rule_based_tuner import RuleBasedTuner as RuleBasedTuner
from .utils import is_naive_data_parallel as is_naive_data_parallel
from paddle.distributed.auto_parallel.process_mesh import ProcessMesh as ProcessMesh
from paddle.distributed.auto_parallel.static.dist_attribute import OperatorDistAttr as OperatorDistAttr, TensorDistAttr as TensorDistAttr
from paddle.distributed.auto_parallel.static.dist_op import DistributedOperator as DistributedOperator
from paddle.distributed.auto_parallel.static.dist_tensor import DistributedTensor as DistributedTensor

class Planner:
    def __init__(self, mode, dist_context) -> None: ...
    @property
    def completer(self): ...
    def plan(self) -> None: ...
