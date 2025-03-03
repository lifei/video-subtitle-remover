from ....profiler import event_register as event_register
from ....utils import NameGenerator as NameGenerator, get_unbound_method as get_unbound_method, log as log
from ....utils.exceptions import FallbackError as FallbackError, HasNoAttributeError as HasNoAttributeError
from ..dispatcher import Dispatcher as Dispatcher
from ..function_graph import FunctionGraph as FunctionGraph
from ..guard import StringifyExpression as StringifyExpression, check_guard as check_guard, union_free_vars as union_free_vars
from ..mutable_data import MutableDictLikeData as MutableDictLikeData
from ..pycode_generator import PyCodeGen as PyCodeGen
from ..tracker import DummyTracker as DummyTracker, GetAttrTracker as GetAttrTracker, GetItemTracker as GetItemTracker, GetIterTracker as GetIterTracker, Tracker as Tracker
from _typeshed import Incomplete
from functools import cached_property as cached_property
from typing import Any

FromValueFunc: Incomplete
ConstTypes: Incomplete

def find_traceable_vars(root_vars: list[VariableBase]) -> list[VariableBase]: ...
def map_variables(map_func, variables: list[VariableBase]): ...

class VariableFactory:
    registered_funcs: dict[str, list[str]]
    mapping_str_func: dict[str, FromValueFunc]
    @staticmethod
    def default_from_value(value, graph, tracker): ...
    @staticmethod
    def register_from_value(*, successor: str | None = None): ...
    @staticmethod
    def from_value(value: Any, graph: FunctionGraph, tracker: Tracker, *, debug_name: str | None = None) -> VariableBase: ...

class VariableBase:
    tracker: Tracker
    value: Any
    name_generator: Incomplete
    mutable_attrs: Incomplete
    graph: Incomplete
    id: Incomplete
    def __init__(self, graph: FunctionGraph, tracker: Tracker) -> None: ...
    @property
    def main_info(self) -> dict[str, Any]: ...
    @property
    def debug_info(self) -> dict[str, Any]: ...
    @property
    def debug_name(self) -> str: ...
    @debug_name.setter
    def debug_name(self, name) -> None: ...
    def __hash__(self): ...
    def make_stringify_guard(self) -> list[StringifyExpression]: ...
    def get_py_value(self, allow_tensor: bool = False) -> Any: ...
    def get_py_type(self): ...
    def is_none(self) -> bool: ...
    def reconstruct(self, codegen: PyCodeGen, *, use_tracker: bool = True, add_to_global_guarded_vars: bool = True): ...
    def flatten_items(self) -> list[VariableBase]: ...
    def get_inputs(self) -> list[VariableBase]: ...
    def get_traceable_inputs(self) -> list[VariableBase]: ...
    def call_function(self, /, *args, **kwargs) -> None: ...
    @cached_property
    def attr_proxy(self): ...
    def attr_proxy_getter(self, proxy: MutableDictLikeData, name: str): ...
    def hasattr(self, name: str): ...
    def getattr(self, name: str, default: Incomplete | None = None): ...
    def setattr(self, key: str, value): ...
    def delattr(self, key: str): ...
    def __setitem__(self, key, value) -> None: ...
    def setitem(self, key, value) -> None: ...
    def __getitem__(self, idx): ...
    def getitem(self, item): ...
    def __call__(self, /, *args, **kwargs): ...
    def get_iter(self): ...
    def from_value(value: Any, graph: FunctionGraph | None, tracker: Tracker) -> VariableBase | None: ...
