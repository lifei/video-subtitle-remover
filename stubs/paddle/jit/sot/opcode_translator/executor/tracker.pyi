from ...utils import InnerError as InnerError, NameGenerator as NameGenerator
from .guard import StringifyExpression as StringifyExpression, union_free_vars as union_free_vars
from .pycode_generator import PyCodeGen as PyCodeGen
from .variables import VariableBase as VariableBase
from _typeshed import Incomplete
from typing import Sequence

class Tracker:
    inputs: Sequence[VariableBase]
    name_generator: Incomplete
    changed: Incomplete
    id: Incomplete
    def __init__(self, inputs: Sequence[VariableBase], changed: bool = False) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen) -> None: ...
    def trace_value_from_frame(self) -> StringifyExpression: ...
    def is_traceable(self) -> bool: ...
    def need_guard(self) -> bool: ...

class DummyTracker(Tracker):
    def __init__(self, inputs: Sequence[VariableBase]) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen): ...
    def trace_value_from_frame(self) -> None: ...
    def is_traceable(self): ...
    def need_guard(self) -> bool: ...

class DanglingTracker(Tracker):
    def __init__(self) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen): ...
    def trace_value_from_frame(self) -> None: ...
    def is_traceable(self): ...

class LocalTracker(Tracker):
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen) -> None: ...
    def trace_value_from_frame(self) -> StringifyExpression: ...

class CellTracker(LocalTracker):
    def gen_instructions(self, codegen: PyCodeGen): ...
    def trace_value_from_frame(self): ...

class GlobalTracker(Tracker):
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen) -> None: ...
    def trace_value_from_frame(self) -> StringifyExpression: ...

class BuiltinTracker(Tracker):
    name: Incomplete
    def __init__(self, name: str) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen) -> None: ...
    def trace_value_from_frame(self) -> StringifyExpression: ...

class ConstTracker(Tracker):
    value: Incomplete
    def __init__(self, value) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen): ...
    def trace_value_from_frame(self): ...
    def need_guard(self) -> bool: ...

class BinaryOperatorTracker(Tracker):
    operands: Incomplete
    operator: Incomplete
    addition: Incomplete
    def __init__(self, operator: str, operands: list[VariableBase], addition: Incomplete | None = None) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen): ...
    def gen_operator_instr(self, codegen: PyCodeGen): ...
    def get_operator_symbol(self): ...
    def trace_value_from_frame(self): ...

class GetAttrTracker(Tracker):
    obj: Incomplete
    attr: Incomplete
    def __init__(self, obj: VariableBase, attr: str, changed: bool = False) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen): ...
    def trace_value_from_frame(self): ...
    def need_guard(self) -> bool: ...

class GetItemTracker(Tracker):
    container: Incomplete
    key: Incomplete
    def __init__(self, container_var: VariableBase, key: object, changed: bool = False) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen): ...
    def trace_value_from_frame(self): ...
    def need_guard(self) -> bool: ...

class GetIterTracker(Tracker):
    iter_source: Incomplete
    def __init__(self, iter_source: VariableBase) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen): ...
    def trace_value_from_frame(self): ...

class CreateLayerTracker(Tracker):
    layer_class: Incomplete
    args: Incomplete
    kwargs: Incomplete
    def __init__(self, layer_class, args, kwargs) -> None: ...
    def gen_instructions(self, codegen: PyCodeGen): ...
