import types
from .convert_operators import convert_enumerate as convert_enumerate, convert_len as convert_len, convert_print as convert_print, convert_range as convert_range, convert_zip as convert_zip
from .logging_utils import TranslatorLogger as TranslatorLogger
from .program_translator import CONVERSION_OPTIONS as CONVERSION_OPTIONS, StaticFunction as StaticFunction, convert_to_static as convert_to_static, unwrap_decorators as unwrap_decorators
from .utils import is_builtin as is_builtin, is_paddle_func as is_paddle_func
from _typeshed import Incomplete
from paddle.nn import Layer as Layer
from typing import Any, Callable

translator_logger: Incomplete

class ConversionOptions:
    not_convert: Incomplete
    def __init__(self, not_convert: bool = False) -> None: ...
    def attach(self, func) -> None: ...

def builtin_modules(): ...

BUILTIN_LIKELY_MODULES: Incomplete

def add_ignore_module(modules: list[types.ModuleType]): ...
def get_module_functions(module) -> list[Callable[..., Any]]: ...
def is_unsupported(func): ...
def convert_call(func): ...
