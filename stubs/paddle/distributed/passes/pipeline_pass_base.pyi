from ..utils.log_utils import get_logger as get_logger
from .pass_base import PassBase as PassBase
from .pass_utils import set_skip_gc_vars as set_skip_gc_vars
from _typeshed import Incomplete
from paddle.base import core as core

logger: Incomplete

class PipelinePassBase(PassBase):
    def __init__(self) -> None: ...
