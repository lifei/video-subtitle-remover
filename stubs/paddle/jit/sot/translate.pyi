from .opcode_translator import eval_frame_callback as eval_frame_callback
from .utils import GraphLogger as GraphLogger, StepInfoManager as StepInfoManager, StepState as StepState, log_do as log_do
from typing import Callable, TypeVar
from typing_extensions import ParamSpec

P = ParamSpec('P')
R = TypeVar('R')

def symbolic_translate(fn: Callable[P, R], **kwargs) -> Callable[P, R]: ...
