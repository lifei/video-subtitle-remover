from . import random as random
from ..base.core import CPUPlace as CPUPlace, CUDAPinnedPlace as CUDAPinnedPlace, CUDAPlace as CUDAPlace, CustomPlace as CustomPlace, IPUPlace as IPUPlace, XPUPlace as XPUPlace
from ..base.dygraph import base as base, to_variable as to_variable
from ..base.dygraph.base import grad as grad
from ..base.dygraph.math_op_patch import monkey_patch_math_tensor as monkey_patch_math_tensor
from ..base.framework import Block as Block, IrGraph as IrGraph, OpProtoHolder as OpProtoHolder, Parameter as Parameter, Program as Program, convert_np_dtype_to_dtype_ as convert_np_dtype_to_dtype_, deprecate_stat_dict as deprecate_stat_dict, disable_signal_handler as disable_signal_handler, dygraph_not_support as dygraph_not_support, dygraph_only as dygraph_only, generate_control_dev_var_name as generate_control_dev_var_name, get_flags as get_flags, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode, in_pir_mode as in_pir_mode, set_flags as set_flags, switch_main_program as switch_main_program, switch_startup_program as switch_startup_program, use_pir_api as use_pir_api
from ..base.layer_helper import LayerHelper as LayerHelper
from ..base.layers.math_op_patch import monkey_patch_variable as monkey_patch_variable
from ..base.param_attr import ParamAttr as ParamAttr
from .framework import get_default_dtype as get_default_dtype, set_default_dtype as set_default_dtype
from .io import async_save as async_save, clear_async_save_task_queue as clear_async_save_task_queue, load as load, save as save
from .io_utils import is_belong_to_optimizer as is_belong_to_optimizer, is_parameter as is_parameter, is_persistable as is_persistable
from .random import seed as seed
