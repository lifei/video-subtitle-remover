from .base_transformer import BaseTransformer as BaseTransformer
from .utils import is_builtin as is_builtin
from _typeshed import Incomplete
from paddle.jit.dy2static.utils import ast_to_source_code as ast_to_source_code, is_paddle_api as is_paddle_api
from paddle.utils import gast as gast

PDB_SET: str

class CallTransformer(BaseTransformer):
    root: Incomplete
    def __init__(self, root) -> None: ...
    def transform(self) -> None: ...
    def visit_Call(self, node): ...
