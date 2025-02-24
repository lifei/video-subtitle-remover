from . import utils as utils
from ... import io as io, static as static
from ...framework import core as core
from ...utils import unique_name as unique_name
from ..log_helper import get_logger as get_logger
from .adaround import run_adaround as run_adaround
from .cal_kl_threshold import cal_kl_threshold as cal_kl_threshold
from .quant_config import ARMCPUQuantizer as ARMCPUQuantizer, BaseQuantizer as BaseQuantizer, MKLDNNQuantizer as MKLDNNQuantizer, SUPPORT_QUANTIZATION_OP_DICT as SUPPORT_QUANTIZATION_OP_DICT, TensorRTQuantizer as TensorRTQuantizer
from .quantization_pass import AddQuantDequantForInferencePass as AddQuantDequantForInferencePass, AddQuantDequantPass as AddQuantDequantPass, AddQuantDequantPassV2 as AddQuantDequantPassV2, QuantWeightPass as QuantWeightPass, QuantizationFreezePass as QuantizationFreezePass, QuantizationTransformPass as QuantizationTransformPass, QuantizationTransformPassV2 as QuantizationTransformPassV2
from .utils import tqdm as tqdm
from _typeshed import Incomplete
from paddle.base.framework import IrGraph as IrGraph

class PostTrainingQuantization:
    FLAG: bool
    quant_config: Incomplete
    def __init__(self, executor, model_dir, scope: Incomplete | None = None, model_filename: Incomplete | None = None, params_filename: Incomplete | None = None, batch_generator: Incomplete | None = None, sample_generator: Incomplete | None = None, data_loader: Incomplete | None = None, batch_size: int = 10, batch_nums: Incomplete | None = None, algo: str = 'KL', hist_percent: float = 0.99999, quantizable_op_type=[], round_type: str = 'round', learning_rate: float = 0.001, is_full_quantize: bool = False, bias_correction: bool = False, activation_bits: int = 8, weight_bits: int = 8, activation_quantize_type: str = 'range_abs_max', weight_quantize_type: str = 'channel_wise_abs_max', onnx_format: bool = False, freeze_model: bool = True, optimize_model: bool = False, is_use_cache_file: bool = False, skip_tensor_list: Incomplete | None = None, same_scale_tensor_list: Incomplete | None = None, cache_dir: Incomplete | None = None, scale_dict: Incomplete | None = None, return_graph: bool = False, deploy_backend: Incomplete | None = None) -> None: ...
    def quantize(self): ...
    def save_quantized_model(self, save_model_path, model_filename: Incomplete | None = None, params_filename: Incomplete | None = None) -> None: ...

class PostTrainingQuantizationProgram(PostTrainingQuantization):
    FLAG: bool
    def __init__(self, executor, program, feed_list: Incomplete | None = None, fetch_list: Incomplete | None = None, scope: Incomplete | None = None, batch_generator: Incomplete | None = None, sample_generator: Incomplete | None = None, data_loader: Incomplete | None = None, batch_size: int = 10, batch_nums: Incomplete | None = None, algo: str = 'KL', hist_percent: float = 0.99999, quantizable_op_type=['conv2d', 'depthwise_conv2d', 'mul'], round_type: str = 'round', learning_rate: float = 0.001, is_full_quantize: bool = False, bias_correction: bool = False, activation_bits: int = 8, weight_bits: int = 8, activation_quantize_type: str = 'range_abs_max', weight_quantize_type: str = 'channel_wise_abs_max', onnx_format: bool = False, freeze_model: bool = True, optimize_model: bool = False, is_use_cache_file: bool = False, skip_tensor_list: Incomplete | None = None, same_scale_tensor_list: Incomplete | None = None, cache_dir: Incomplete | None = None, scale_dict: Incomplete | None = None, return_graph: bool = True) -> None: ...

class WeightQuantization:
    def __init__(self, model_dir, model_filename: Incomplete | None = None, params_filename: Incomplete | None = None) -> None: ...
    def quantize_weight_to_int(self, save_model_dir, save_model_filename: Incomplete | None = None, save_params_filename: Incomplete | None = None, quantizable_op_type=['conv2d', 'mul'], weight_bits: int = 8, weight_quantize_type: str = 'channel_wise_abs_max', generate_test_model: bool = False, threshold_rate: float = 0.0) -> None: ...
    def convert_weight_to_fp16(self, save_model_dir) -> None: ...
