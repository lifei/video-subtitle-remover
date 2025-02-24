from .base_transformer import BaseTransformer as BaseTransformer
from .utils import ast_to_source_code as ast_to_source_code
from _typeshed import Incomplete
from paddle.utils import gast as gast

class TensorShapeTransformer(BaseTransformer):
    root: Incomplete
    def __init__(self, root) -> None: ...
    def transform(self) -> None: ...
    def visit_Attribute(self, node): ...
