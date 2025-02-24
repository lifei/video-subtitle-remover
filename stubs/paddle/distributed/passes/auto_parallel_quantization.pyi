from ..auto_parallel.static.converter import Converter as Converter
from ..auto_parallel.static.dist_attribute import OperatorDistAttr as OperatorDistAttr, TensorDistAttr as TensorDistAttr
from .pass_base import PassBase as PassBase, register_pass as register_pass
from _typeshed import Incomplete
from paddle.framework import IrGraph as IrGraph, core as core
from paddle.static.quantization import AddQuantDequantForInferencePass as AddQuantDequantForInferencePass, AddQuantDequantPassV2 as AddQuantDequantPassV2, OutScaleForTrainingPass as OutScaleForTrainingPass, QuantizationTransformPassV2 as QuantizationTransformPassV2, quant_config as quant_config

TRANSFORM_PASS_OP_TYPES: Incomplete
QUANT_DEQUANT_PASS_OP_TYPES: Incomplete

class QuantizationPass(PassBase):
    def __init__(self) -> None: ...
    def move_presist_var_to_global_block(self, program): ...
    def reset_scope_var(self, quant_program, dist_context, scope, place) -> None: ...
    def set_dist_attr_for_qat_program(self, quant_program, main_program, dist_context) -> None: ...
