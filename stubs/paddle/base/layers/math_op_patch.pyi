from .. import core as core
from ..framework import Variable as Variable, static_only as static_only, unique_name as unique_name
from .layer_function_generator import OpProtoHolder as OpProtoHolder
from _typeshed import Incomplete
from paddle.base.dygraph.base import in_to_static_mode as in_to_static_mode

compare_ops: Incomplete
SUPPORT_PROMOTION_OPS: Incomplete
EXPRESSION_MAP: Incomplete

def monkey_patch_variable(): ...
