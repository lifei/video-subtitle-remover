from . import logging_utils as logging_utils
from .assert_transformer import AssertTransformer as AssertTransformer
from .base_transformer import BaseTransformer as BaseTransformer
from .basic_api_transformer import BasicApiTransformer as BasicApiTransformer, NameloadJstTransformer as NameloadJstTransformer
from .break_continue_transformer import BreakContinueTransformer as BreakContinueTransformer, BreakTransformOptimizer as BreakTransformOptimizer
from .call_transformer import CallTransformer as CallTransformer
from .cast_transformer import CastTransformer as CastTransformer
from .create_variable_transformer import CreateVariableTransformer as CreateVariableTransformer
from .decorator_transformer import DecoratorTransformer as DecoratorTransformer
from .early_return_transformer import EarlyReturnTransformer as EarlyReturnTransformer
from .ifelse_transformer import IfElseTransformer as IfElseTransformer
from .logical_transformer import LogicalTransformer as LogicalTransformer
from .loop_transformer import LoopTransformer as LoopTransformer
from .return_transformer import ReturnTransformer as ReturnTransformer
from .tensor_shape_transformer import TensorShapeTransformer as TensorShapeTransformer
from .tensorhook_transformer import RegisterHookTransformer as RegisterHookTransformer
from .typehint_transformer import TypeHintTransformer as TypeHintTransformer
from .utils import ast_to_source_code as ast_to_source_code
from _typeshed import Incomplete

def apply_optimization(transformers) -> None: ...

class DygraphToStaticAst(BaseTransformer):
    translator_logger: Incomplete
    def __init__(self) -> None: ...
    root: Incomplete
    decorate_func_name: Incomplete
    def get_static_ast(self, root): ...
    def transfer_from_node_type(self, node) -> None: ...
    def visit_FunctionDef(self, node): ...
    def get_module_name(self): ...
