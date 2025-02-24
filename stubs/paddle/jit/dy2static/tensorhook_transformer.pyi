from .base_transformer import BaseTransformer as BaseTransformer
from _typeshed import Incomplete
from paddle.utils import gast as gast

class RegisterHookTransformer(BaseTransformer):
    register_hook_pos_map: Incomplete
    assignment_pos_map: Incomplete
    root: Incomplete
    def __init__(self, root) -> None: ...
    def transform(self) -> None: ...
    def visit_FunctionDef(self, func_def): ...
