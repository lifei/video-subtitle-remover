from .base_transformer import BaseTransformer as BaseTransformer
from .utils import FunctionNameLivenessAnalysis as FunctionNameLivenessAnalysis
from .variable_trans_func import create_undefined_var as create_undefined_var
from _typeshed import Incomplete

class CreateVariableTransformer(BaseTransformer):
    root: Incomplete
    def __init__(self, root) -> None: ...
    def transform(self) -> None: ...
    def visit_FunctionDef(self, node): ...
