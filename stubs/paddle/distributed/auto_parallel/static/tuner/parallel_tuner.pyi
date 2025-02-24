from ...process_mesh import ProcessMesh as ProcessMesh
from ..completion import Completer as Completer
from ..cost import CostEstimator as CostEstimator
from ..dist_op import DistributedOperator as DistributedOperator
from ..operators.common import find_compatible_distributed_operator_impls as find_compatible_distributed_operator_impls
from ..parallelizer_v2 import Parallelizer as Parallelizer
from .trial import Trial as Trial, TrialStatus as TrialStatus
from .tunable_space import TunableSpace as TunableSpace
from .tunable_variable import Boolean as Boolean, IntRange as IntRange
from _typeshed import Incomplete

class ParallelTuner:
    def __init__(self, dist_context, mode: str = 'train', max_trials: int = 25, tuner_id: Incomplete | None = None, seed: Incomplete | None = None, logger: Incomplete | None = None, loop_count: int = 10) -> None: ...
    def construct_space(self) -> None: ...
    def tune(self) -> None: ...
