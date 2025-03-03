from ..data_feeder import convert_dtype as convert_dtype
from ..wrapped_decorator import signature_safe_contextmanager as signature_safe_contextmanager, wrap_decorator as wrap_decorator
from .tracer import Tracer as Tracer
from _typeshed import Incomplete
from collections.abc import Generator
from paddle.base import core as core, framework as framework
from paddle.base.framework import global_var as global_var
from paddle.base.multiprocess_utils import CleanupFuncRegistrar as CleanupFuncRegistrar

NON_PERSISTABLE_VAR_NAME_SUFFIX: str

def in_to_static_mode(): ...
in_declarative_mode = in_to_static_mode

def to_static_unsupport_argument_warning(func_name, input_names, inputs, support_values) -> None: ...

switch_to_static_graph: Incomplete

def program_desc_tracing_guard(enable) -> Generator[None]: ...
def param_guard(parameters) -> Generator[None]: ...
def enabled(): ...
def enable_dygraph(place: Incomplete | None = None) -> None: ...
def disable_dygraph() -> None: ...
def no_grad(func: Incomplete | None = None): ...

class _DecoratorContextManager:
    def __call__(self, func): ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: types.TracebackType | None) -> None: ...
    def clone(self): ...

def is_grad_enabled(): ...

class set_grad_enabled(_DecoratorContextManager):
    prev: Incomplete
    mode: Incomplete
    def __init__(self, mode) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...
    def clone(self): ...

class no_grad_(_DecoratorContextManager):
    prev: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

class enable_grad(_DecoratorContextManager):
    prev: Incomplete
    def __enter__(self) -> None: ...
    def __exit__(self, *args) -> None: ...

def guard(place: Incomplete | None = None) -> Generator[None]: ...
def grad(outputs, inputs, grad_outputs: Incomplete | None = None, retain_graph: Incomplete | None = None, create_graph: bool = False, only_inputs: bool = True, allow_unused: bool = False, no_grad_vars: Incomplete | None = None): ...
def to_variable(value, name: Incomplete | None = None, zero_copy: Incomplete | None = None, dtype: Incomplete | None = None): ...
