from .. import core as core, framework as framework, unique_name as unique_name
from ..framework import EagerParamBase as EagerParamBase, Parameter as Parameter, Variable as Variable, convert_np_dtype_to_dtype_ as convert_np_dtype_to_dtype_
from .base import switch_to_static_graph as switch_to_static_graph
from .math_op_patch import monkey_patch_math_tensor as monkey_patch_math_tensor
from paddle import profiler as profiler
from paddle.base.data_feeder import convert_uint16_to_float as convert_uint16_to_float
from paddle.profiler.utils import in_profiler_mode as in_profiler_mode
from paddle.utils import deprecated as deprecated

class TensorHookRemoveHelper:
    def __init__(self, tensor, hook_id) -> None: ...
    def remove(self): ...

def monkey_patch_tensor(): ...
