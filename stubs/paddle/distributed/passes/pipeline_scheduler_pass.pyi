from ..utils.log_utils import get_logger as get_logger
from .pass_base import PassContext as PassContext, new_pass as new_pass, register_pass as register_pass
from .pass_utils import AutoParallelStreamType as AutoParallelStreamType, split_program as split_program
from .pipeline_pass_base import PipelinePassBase as PipelinePassBase
from _typeshed import Incomplete
from paddle.base import core as core
from paddle.distributed.auto_parallel.static.cost import calc_time_by_cost_model as calc_time_by_cost_model

__not_shape_var_type__: Incomplete
FORWARD: str
BACKWARD: str
OPT: str
logger: Incomplete

class PipelineFThenBPass(PipelinePassBase):
    def __init__(self) -> None: ...

class Pipeline1F1BPass(PipelinePassBase):
    jobs_in_stable_phase: Incomplete
    def __init__(self) -> None: ...
    def is_comm_op_valid_to_overlap(self, op): ...

class PipelineEager1F1BPass(PipelinePassBase):
    def __init__(self) -> None: ...

def apply_pass(main_program, startup_program, pass_name, pass_attr={}): ...
