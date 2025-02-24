from _typeshed import Incomplete
from paddle.base import core as core, framework as framework, unique_name as unique_name
from paddle.base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from paddle.base.libpaddle import DataType as DataType
from paddle.common_ops_import import Variable as Variable, check_type as check_type, default_main_program as default_main_program
from paddle.framework import LayerHelper as LayerHelper, in_dynamic_mode as in_dynamic_mode, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode, in_pir_mode as in_pir_mode
from paddle.tensor.layer_function_generator import templatedoc as templatedoc

def clip_by_norm(x, max_norm, name: Incomplete | None = None): ...
def merge_selected_rows(x, name: Incomplete | None = None): ...
def get_tensor_from_selected_rows(x, name: Incomplete | None = None): ...

class BaseErrorClipAttr: ...

class ErrorClipByValue(BaseErrorClipAttr):
    max: Incomplete
    min: Incomplete
    def __init__(self, max, min: Incomplete | None = None) -> None: ...

def error_clip_callback(block, context) -> None: ...

class ClipGradBase:
    def __init__(self) -> None: ...
    def __call__(self, params_grads): ...

class ClipGradByValue(ClipGradBase):
    max: Incomplete
    min: Incomplete
    def __init__(self, max, min: Incomplete | None = None) -> None: ...

class ClipGradByNorm(ClipGradBase):
    clip_norm: Incomplete
    def __init__(self, clip_norm) -> None: ...

class ClipGradByGlobalNorm(ClipGradBase):
    clip_norm: Incomplete
    group_name: Incomplete
    auto_skip_clip: Incomplete
    def __init__(self, clip_norm, group_name: str = 'default_group', auto_skip_clip: bool = False) -> None: ...

def set_gradient_clip(clip, param_list: Incomplete | None = None, program: Incomplete | None = None) -> None: ...
def append_gradient_clip_ops(param_grads): ...
GradientClipBase = ClipGradBase
GradientClipByValue = ClipGradByValue
GradientClipByNorm = ClipGradByNorm
GradientClipByGlobalNorm = ClipGradByGlobalNorm
