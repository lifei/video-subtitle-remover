from ..base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from ..base.proto import framework_pb2 as framework_pb2
from ..common_ops_import import Variable as Variable
from ..framework import LayerHelper as LayerHelper, OpProtoHolder as OpProtoHolder, convert_np_dtype_to_dtype_ as convert_np_dtype_to_dtype_, core as core, in_dynamic_mode as in_dynamic_mode, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode
from _typeshed import Incomplete

def escape_math(text): ...
def generate_layer_fn(op_type): ...
def generate_activation_fn(op_type): ...
def generate_inplace_fn(inplace_op_type): ...
def templatedoc(op_type: Incomplete | None = None): ...
def add_sample_code(func, sample_code) -> None: ...
