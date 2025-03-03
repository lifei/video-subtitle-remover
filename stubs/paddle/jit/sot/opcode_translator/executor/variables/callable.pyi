import paddle
import types
from .... import psdb as psdb
from ....profiler import EventGuard as EventGuard
from ....utils import is_break_graph_api as is_break_graph_api, is_break_graph_tensor_methods as is_break_graph_tensor_methods, is_builtin_fn as is_builtin_fn, is_not_supported_paddle_layer as is_not_supported_paddle_layer, is_paddle_api as is_paddle_api, magic_method_builtin_dispatch as magic_method_builtin_dispatch
from ....utils.exceptions import BreakGraphError as BreakGraphError, FallbackError as FallbackError, SotErrorBase as SotErrorBase
from ..dispatcher import Dispatcher as Dispatcher
from ..function_graph import FunctionGraph as FunctionGraph
from ..guard import StringifyExpression as StringifyExpression, check_guard as check_guard, object_equal_stringify_guard as object_equal_stringify_guard, union_free_vars as union_free_vars
from ..tracker import ConstTracker as ConstTracker, CreateLayerTracker as CreateLayerTracker, DanglingTracker as DanglingTracker, DummyTracker as DummyTracker, GetAttrTracker as GetAttrTracker, GetItemTracker as GetItemTracker, GetIterTracker as GetIterTracker, Tracker as Tracker
from .base import VariableBase as VariableBase, VariableFactory as VariableFactory
from .basic import ConstantVariable as ConstantVariable, PrintStmtVariable as PrintStmtVariable, SliceVariable as SliceVariable
from _typeshed import Incomplete
from typing import Any, Callable

PD_ALL_CONTAINERS: Incomplete
PD_SEQ_CONTAINERS: Incomplete

class CallableVariable(VariableBase):
    def __init__(self, graph: FunctionGraph, tracker: Tracker) -> None: ...
    def __call__(self, /, *args, **kwargs) -> VariableBase: ...
    def call_function(self, /, *args, **kwargs) -> None: ...

class FunctionVariable(CallableVariable):
    value: Incomplete
    def __init__(self, fn: Callable[..., Any], graph: FunctionGraph, tracker: Tracker) -> None: ...
    def get_py_value(self, allow_tensor: bool = False): ...
    def get_code(self) -> types.CodeType: ...
    tracker: Incomplete
    def bind(self, instance: VariableBase, name: str): ...
    make_stringify_guard = object_equal_stringify_guard

class UserDefinedFunctionVariable(FunctionVariable):
    def __init__(self, fn: Callable[..., Any], graph: FunctionGraph, tracker: Tracker) -> None: ...
    def handle_psdb_function(self, /, *args, **kwargs): ...
    def call_function(self, /, *args, **kwargs) -> VariableBase: ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...
    @property
    def main_info(self) -> dict[str, Any]: ...

class PaddleApiVariable(FunctionVariable):
    def __init__(self, fn: Callable[..., Any], graph: FunctionGraph, tracker: Tracker) -> None: ...
    def call_function(self, /, *args, **kwargs): ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...
    @property
    def main_info(self) -> dict[str, Any]: ...
    make_stringify_guard = object_equal_stringify_guard

class TensorFunctionVariable(FunctionVariable):
    method_name: Incomplete
    def __init__(self, method_name: str, graph: FunctionGraph, tracker: Tracker) -> None: ...
    def call_function(self, /, *args, **kwargs): ...
    tracker: Incomplete
    def bind(self, instance: VariableBase, name: str): ...
    @property
    def main_info(self) -> dict[str, Any]: ...

class MethodVariable(CallableVariable):
    bound_instance: Incomplete
    fn: Incomplete
    method_name: Incomplete
    def __init__(self, bound_instance: VariableBase, fn: VariableBase, graph: FunctionGraph, tracker: Tracker, *, method_name: str | None = None) -> None: ...
    def get_py_value(self, allow_tensor: bool = False): ...
    def call_function(self, /, *args, **kwargs): ...
    @staticmethod
    def wrap_method(value: types.MethodType, *, graph: FunctionGraph, tracker: Tracker, instance: VariableBase | None = None, fn: VariableBase | None = None, method_name: str | None = None): ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...
    @property
    def main_info(self) -> dict[str, Any]: ...

class LayerVariable(CallableVariable):
    value: Incomplete
    def __init__(self, layer: paddle.nn.Layer, graph: FunctionGraph, tracker: Tracker) -> None: ...
    def get_py_value(self, allow_tensor: bool = False): ...
    def call_function(self, /, *args, **kwargs): ...
    def make_stringify_guard(self) -> list[StringifyExpression]: ...

class ContainerLayerVariable(LayerVariable):
    def __init__(self, layer: paddle.nn.Layer, graph: FunctionGraph, tracker: Tracker) -> None: ...
    def __len__(self) -> int: ...
    def len(self): ...
    def getitem(self, key): ...
    def get_iter(self): ...
    def make_stringify_guard(self) -> list[StringifyExpression]: ...
    @property
    def main_info(self) -> dict[str, Any]: ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...

class PaddleLayerVariable(LayerVariable):
    def __init__(self, layer: paddle.nn.Layer, graph: FunctionGraph, tracker: Tracker) -> None: ...
    def call_function(self, /, *args, **kwargs): ...
    def make_stringify_guard(self) -> list[StringifyExpression]: ...
    @property
    def main_info(self) -> dict[str, Any]: ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...

class UserDefinedLayerVariable(LayerVariable):
    def __init__(self, layer: paddle.nn.Layer, graph: FunctionGraph, tracker: Tracker) -> None: ...
    @property
    def main_info(self) -> dict[str, Any]: ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...

class BuiltinVariable(FunctionVariable):
    value: Incomplete
    def __init__(self, fn: Callable[..., Any], graph: FunctionGraph, tracker: Tracker) -> None: ...
    def call_function(self, /, *args, **kwargs): ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...
    @property
    def main_info(self) -> dict[str, Any]: ...

class UserDefinedGeneratorVariable(FunctionVariable):
    def __init__(self, fn: Callable[..., Any], graph: FunctionGraph, tracker: Tracker) -> None: ...
    def call_function(self, /, *args, **kwargs): ...
    @property
    def main_info(self) -> dict[str, Any]: ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...

class ClassVariable(CallableVariable):
    value: Incomplete
    def __init__(self, class_: type, graph: FunctionGraph, tracker: Tracker) -> None: ...
    def get_py_value(self, allow_tensor: bool = False): ...
    def call_function(self, /, *args, **kwargs): ...
    make_stringify_guard = object_equal_stringify_guard
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...

class PaddleLayerClassVariable(ClassVariable):
    def __init__(self, class_: type, graph: FunctionGraph, tracker: Tracker) -> None: ...
    def check_no_weight_and_buffers(self, paddle_layer): ...
    def call_function(self, /, *args, **kwargs): ...
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker): ...
