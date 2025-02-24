from .ast_utils import ast_to_source_code as ast_to_source_code
from .logging_utils import warn as warn
from _typeshed import Incomplete
from paddle import base as base
from paddle.base import dygraph as dygraph, layers as layers
from paddle.base.dygraph import to_variable as to_variable
from paddle.utils import gast as gast

def index_in_list(array_list, item): ...

PADDLE_MODULE_PREFIX: str
DYGRAPH_TO_STATIC_MODULE_PREFIX: str
DYGRAPH_MODULE_PREFIX: str

def is_dygraph_api(node): ...
def is_api_in_module(node, module_prefix): ...
def is_numpy_api(node): ...
def is_paddle_api(node): ...

class NodeVarType:
    ERROR: int
    UNKNOWN: int
    STATEMENT: int
    CALLABLE: int
    NONE: int
    BOOLEAN: int
    INT: int
    FLOAT: int
    STRING: int
    TENSOR: int
    NUMPY_NDARRAY: int
    LIST: int
    SET: int
    DICT: int
    PADDLE_DYGRAPH_API: int
    PADDLE_CONTROL_IF: int
    PADDLE_CONTROL_WHILE: int
    PADDLE_CONTROL_FOR: int
    PADDLE_RETURN_TYPES: int
    TENSOR_TYPES: Incomplete
    Annotation_map: Incomplete
    @staticmethod
    def binary_op_output_type(in_type1, in_type2): ...
    @staticmethod
    def type_from_annotation(annotation): ...

def set_dynamic_shape(variable, shape_list) -> None: ...
