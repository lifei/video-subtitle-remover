from . import core as core, unique_name as unique_name
from .framework import Variable as Variable, default_main_program as default_main_program, default_startup_program as default_startup_program, in_dygraph_mode as in_dygraph_mode, in_pir_mode as in_pir_mode
from .param_attr import ParamAttr as ParamAttr, WeightNormParamAttr as WeightNormParamAttr
from _typeshed import Incomplete

class LayerHelperBase:
    def __init__(self, name, layer_type) -> None: ...
    @property
    def name(self): ...
    @property
    def layer_type(self): ...
    @property
    def main_program(self): ...
    @property
    def startup_program(self): ...
    @classmethod
    def set_default_dtype(cls, dtype) -> None: ...
    @classmethod
    def get_default_dtype(cls): ...
    def to_variable(self, value, name: Incomplete | None = None): ...
    def create_parameter(self, attr, shape, dtype: Incomplete | None = None, is_bias: bool = False, default_initializer: Incomplete | None = None, stop_gradient: bool = False, type=...): ...
    def create_variable_for_type_inference(self, dtype, stop_gradient: bool = False, shape: Incomplete | None = None): ...
    def create_sparse_variable_for_type_inference(self, dtype, stop_gradient: bool = False, shape: Incomplete | None = None): ...
    def create_variable(self, *args, **kwargs): ...
    def create_global_variable(self, persistable: bool = False, *args, **kwargs): ...
    def create_or_get_global_variable(self, name, *args, **kwargs): ...
    def set_variable_initializer(self, var, initializer) -> None: ...
