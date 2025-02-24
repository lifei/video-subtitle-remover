from paddle import base as base
from paddle.base import core as core, dygraph_utils as dygraph_utils
from paddle.base.core import VarDesc as VarDesc
from paddle.base.data_feeder import check_dtype as check_dtype, check_type as check_type, check_variable_and_dtype as check_variable_and_dtype, convert_dtype as convert_dtype
from paddle.base.framework import OpProtoHolder as OpProtoHolder, Variable as Variable, convert_np_dtype_to_dtype_ as convert_np_dtype_to_dtype_, default_main_program as default_main_program, device_guard as device_guard, dygraph_only as dygraph_only, in_dygraph_mode as in_dygraph_mode
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.base.layers.layer_function_generator import templatedoc as templatedoc
from paddle.base.param_attr import ParamAttr as ParamAttr
