from . import quant_config as quant_config
from ...base.framework import IrGraph as IrGraph, core as core
from ..log_helper import get_logger as get_logger
from .post_training_quantization import PostTrainingQuantizationProgram as PostTrainingQuantizationProgram
from .quantization_pass import AddQuantDequantForInferencePass as AddQuantDequantForInferencePass, AddQuantDequantForResidual as AddQuantDequantForResidual, AddQuantDequantPass as AddQuantDequantPass, AddQuantDequantPassV2 as AddQuantDequantPassV2, ConvertToInt8Pass as ConvertToInt8Pass, OutScaleForInferencePass as OutScaleForInferencePass, OutScaleForTrainingPass as OutScaleForTrainingPass, QuantWeightPass as QuantWeightPass, QuantizationFreezePass as QuantizationFreezePass, QuantizationTransformPass as QuantizationTransformPass, QuantizationTransformPassV2 as QuantizationTransformPassV2
from _typeshed import Incomplete

WEIGHT_QUANTIZATION_TYPES: Incomplete
WEIGHT_QUANTIZATION_TYPES_TENSORRT: Incomplete
ACTIVATION_QUANTIZATION_TYPES: Incomplete
ACTIVATION_QUANTIZATION_TYPES_TENSORRT: Incomplete
VALID_DTYPES: Incomplete
TRANSFORM_PASS_OP_TYPES: Incomplete
QUANT_DEQUANT_PASS_OP_TYPES: Incomplete
TENSORRT_OP_TYPES: Incomplete
VARS_MAPPING_TABLE: str

def load_dict(): ...
def save_dict(table) -> None: ...
def quant_aware(program, place, config: Incomplete | None = None, scope: Incomplete | None = None, for_test: bool = False, weight_quantize_func: Incomplete | None = None, act_quantize_func: Incomplete | None = None, weight_preprocess_func: Incomplete | None = None, act_preprocess_func: Incomplete | None = None, optimizer_func: Incomplete | None = None, executor: Incomplete | None = None, return_program: bool = False, calib_config={}, draw_graph: bool = False, return_scale_dict: bool = False, scale_dict: Incomplete | None = None, model_type: Incomplete | None = None, pattern_ops: Incomplete | None = None): ...
def convert(program, place, config: Incomplete | None = None, scope: Incomplete | None = None, save_int8: bool = False): ...
