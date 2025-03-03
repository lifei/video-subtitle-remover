from .base_transformer import BaseTransformer as BaseTransformer, ForLoopTuplePreTransformer as ForLoopTuplePreTransformer, ForNodeVisitor as ForNodeVisitor
from .ifelse_transformer import ARGS_NAME as ARGS_NAME
from .static_analysis import NodeVarType as NodeVarType, StaticAnalysisVisitor as StaticAnalysisVisitor
from .utils import FOR_BODY_PREFIX as FOR_BODY_PREFIX, FOR_CONDITION_PREFIX as FOR_CONDITION_PREFIX, FunctionNameLivenessAnalysis as FunctionNameLivenessAnalysis, GetterSetterHelper as GetterSetterHelper, WHILE_BODY_PREFIX as WHILE_BODY_PREFIX, WHILE_CONDITION_PREFIX as WHILE_CONDITION_PREFIX, ast_to_source_code as ast_to_source_code, create_get_args_node as create_get_args_node, create_name_str as create_name_str, create_nonlocal_stmt_nodes as create_nonlocal_stmt_nodes, create_set_args_node as create_set_args_node, get_attribute_full_name as get_attribute_full_name
from _typeshed import Incomplete
from paddle.base import unique_name as unique_name
from paddle.utils import gast as gast

def create_while_nodes(condition_name, body_name, loop_var_names, push_pop_names, getter_name, setter_name): ...

class NameVisitor(gast.NodeVisitor):
    current_seen_vars: Incomplete
    current_loop: Incomplete
    nodes_with_scope: Incomplete
    blacklist_names: Incomplete
    before_loop_body_vars: Incomplete
    in_loop_vars: Incomplete
    write_in_loop: Incomplete
    condition_vars: Incomplete
    in_condition: bool
    type_vars: Incomplete
    static_analysis_visitor: Incomplete
    node_to_wrapper_map: Incomplete
    def __init__(self, root_node) -> None: ...
    def get_loop_var_names(self, node): ...
    def visit_Name(self, node) -> None: ...
    def visit_FunctionDef(self, node) -> None: ...
    def visit(self, node): ...
    def visit_Attribute(self, node) -> None: ...
    def visit_For(self, node) -> None: ...
    def visit_While(self, node) -> None: ...
    def visit_Call(self, node) -> None: ...

class LoopTransformer(BaseTransformer):
    root: Incomplete
    def __init__(self, root) -> None: ...
    def transform(self) -> None: ...
    def visit_While(self, node): ...
    def visit_For(self, node): ...
    def replace_stmt_list(self, body_list) -> None: ...
    def get_for_stmt_nodes(self, node): ...
    def get_while_stmt_nodes(self, node): ...
