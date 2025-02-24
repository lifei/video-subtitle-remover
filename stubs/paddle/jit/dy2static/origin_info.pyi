from .utils import ORIGI_INFO as ORIGI_INFO, unwrap as unwrap
from _typeshed import Incomplete
from collections.abc import Generator
from paddle.base import core as core
from paddle.base.framework import Program as Program
from paddle.utils import gast as gast

class Location:
    filepath: Incomplete
    lineno: Incomplete
    col_offset: Incomplete
    def __init__(self, filepath, lineno, col_offset: Incomplete | None = None) -> None: ...
    @property
    def line_location(self): ...

class OriginInfo:
    location: Incomplete
    function_name: Incomplete
    source_code: Incomplete
    def __init__(self, location, function_name, source_code) -> None: ...
    def formated_message(self): ...
    def as_frame(self): ...

class OriginInfoAttacher(gast.NodeTransformer):
    root: Incomplete
    func: Incomplete
    filepath: Incomplete
    source_code: Incomplete
    current_func: Incomplete
    def __init__(self, root, func) -> None: ...
    col_offset: Incomplete
    source_lines: Incomplete
    lineno_offset: Incomplete
    def transform(self) -> None: ...
    def visit(self, node): ...

global_origin_info_map: Incomplete

def create_and_update_origin_info_map(transformed_node, static_func, is_global: bool = True): ...
def attach_origin_info(ast_node, func): ...
def ast_walk(transformed_node, static_node) -> Generator[Incomplete, None, Incomplete]: ...
def update_op_callstack_with_origin_info(program): ...
