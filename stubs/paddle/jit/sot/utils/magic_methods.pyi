from .utils import hashable as hashable
from _typeshed import Incomplete
from dataclasses import dataclass
from typing import Any, Callable

BinaryOp = Callable[[Any, Any], Any]
UnaryOp = Callable[[Any], Any]
INPLACE_BINARY_OPS_TO_MAGIC_NAMES: dict[BinaryOp, tuple[str, BinaryOp]]
NON_INPLACE_BINARY_OPS_TO_MAGIC_NAMES: dict[BinaryOp, tuple[str, str | None]]
UNARY_OPS_TO_MAGIC_NAMES: dict[UnaryOp, str]
INPLACE_BINARY_OPS: Incomplete
NON_INPLACE_BINARY_OPS: Incomplete
BINARY_OPS = INPLACE_BINARY_OPS | NON_INPLACE_BINARY_OPS
UNARY_OPS: Incomplete

@dataclass
class MagicMethod:
    name: str
    is_inplace: bool = ...
    is_reverse: bool = ...

def magic_method_builtin_dispatch(fn: BinaryOp | UnaryOp) -> list[MagicMethod]: ...
