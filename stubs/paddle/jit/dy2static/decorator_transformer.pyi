from .base_transformer import BaseTransformer as BaseTransformer
from .utils import RE_PYMODULE as RE_PYMODULE, RE_PYNAME as RE_PYNAME, ast_to_source_code as ast_to_source_code
from _typeshed import Incomplete
from paddle.utils import gast as gast

IGNORE_NAMES: Incomplete

class DecoratorTransformer(BaseTransformer):
    root: Incomplete
    ancestor_nodes: Incomplete
    def __init__(self, root) -> None: ...
    def transform(self) -> None: ...
    def visit_FunctionDef(self, node): ...
