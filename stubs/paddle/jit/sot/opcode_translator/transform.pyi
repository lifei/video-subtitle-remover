from ..profiler import EventGuard as EventGuard
from ..utils import log_do as log_do, log_format as log_format
from .custom_code import CustomCode as CustomCode
from .executor.executor_cache import OpcodeExecutorCache as OpcodeExecutorCache

def print_locals(frame): ...
def eval_frame_callback(frame, **kwargs) -> CustomCode: ...
