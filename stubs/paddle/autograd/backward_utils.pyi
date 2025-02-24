from _typeshed import Incomplete
from collections.abc import Generator
from paddle.base import core as core
from paddle.base.wrapped_decorator import signature_safe_contextmanager as signature_safe_contextmanager

class State:
    block: Incomplete
    value_to_valuegrad: Incomplete
    value_to_sumvaluegrad: Incomplete
    op_to_opgrad: Incomplete
    valuegrad_to_value: Incomplete
    sumvaluegrad_to_value: Incomplete
    opgrad_to_op: Incomplete
    def __init__(self, block) -> None: ...
    def turn_map(self) -> None: ...
    def copy(self, new_block): ...

def dynamic_shape_prim_vjp_guard(op, inputs) -> Generator[None]: ...
