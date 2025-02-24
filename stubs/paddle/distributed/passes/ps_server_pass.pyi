from ..ps.utils.public import get_optimize_ops as get_optimize_ops, get_ps_endpoint as get_ps_endpoint, get_role_id as get_role_id, get_trainers as get_trainers
from .pass_base import PassBase as PassBase, register_pass as register_pass
from paddle.optimizer.lr import ExponentialDecay as ExponentialDecay, InverseTimeDecay as InverseTimeDecay, LRScheduler as LRScheduler, NaturalExpDecay as NaturalExpDecay, NoamDecay as NoamDecay, exponential_decay as exponential_decay, inverse_time_decay as inverse_time_decay, noam_decay as noam_decay

class AddLrDecayTablePass(PassBase):
    def __init__(self) -> None: ...

class AddListenAndServPass(PassBase):
    def __init__(self) -> None: ...

class AddRpcGlobalFlagsPass(PassBase):
    def __init__(self) -> None: ...

class AddOptimizerPass(PassBase):
    def __init__(self) -> None: ...

class AddGeoOptimizerPass(PassBase):
    def __init__(self) -> None: ...

class BuildPserverStartupProgramPass(PassBase):
    def __init__(self) -> None: ...

class DeleteUnusedInStartupPass(PassBase):
    def __init__(self) -> None: ...
