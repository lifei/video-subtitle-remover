from .base_transformer import BaseTransformer as BaseTransformer
from _typeshed import Incomplete
from paddle.jit.dy2static.utils import ast_to_source_code as ast_to_source_code
from paddle.utils import gast as gast

class AssertTransformer(BaseTransformer):
    root: Incomplete
    def __init__(self, root) -> None: ...
    def transform(self) -> None: ...
    def visit_Assert(self, node): ...
