from _typeshed import Incomplete
from paddle.base import core as core
from paddle.base.framework import Parameter as Parameter, Variable as Variable, static_only as static_only
from paddle.base.log_helper import get_logger as get_logger
from paddle.base.wrapped_decorator import signature_safe_contextmanager as signature_safe_contextmanager

class _open_buffer:
    buffer: Incomplete
    def __init__(self, buffer) -> None: ...
    def __enter__(self): ...

class _buffer_reader(_open_buffer):
    initial_tell: Incomplete
    def __init__(self, buffer) -> None: ...
    def __exit__(self, *args) -> None: ...

class _buffer_writer(_open_buffer):
    def __exit__(self, *args) -> None: ...

def is_persistable(var): ...
def is_parameter(var): ...
def is_belong_to_optimizer(var): ...
