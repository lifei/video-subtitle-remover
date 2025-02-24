from ..log_helper import get_logger as get_logger
from .utils import bias_correction_w as bias_correction_w, calculate_quant_cos_error as calculate_quant_cos_error, dequant_tensor as dequant_tensor, load_variable_data as load_variable_data, quant_tensor as quant_tensor, set_variable_data as set_variable_data, stable_sigmoid as stable_sigmoid
from _typeshed import Incomplete
from paddle import static as static

GAMMA: float
ZETA: float

def compute_soft_rounding(alpha_v): ...
def compute_soft_rounding_np(alpha_v): ...

class AdaRoundLoss:
    default_reg_param: Incomplete
    default_beta_range: Incomplete
    def __init__(self, reg_param: float = 0.01, default_beta_range=(20, 2)) -> None: ...
    def compute_recon_loss(self, ada_quantized_output, orig_output): ...
    def compute_round_loss(self, alpha_v, warm_start, beta): ...
    def compute_beta(self, max_iter, cur_iter, warm_start): ...

class AdaRound:
    is_train: Incomplete
    num_iterations: Incomplete
    warm_start: float
    weight_bits: int
    offset: float
    adaround_loss: Incomplete
    ori_weight_tensor: Incomplete
    scale: Incomplete
    scope: Incomplete
    quant_axis: int
    weight_var_name: Incomplete
    alpha_name: Incomplete
    def __init__(self, scale, weight_tensor, scope: Incomplete | None = None, weight_var_name: Incomplete | None = None, weight_op_type: Incomplete | None = None, is_train: bool = True, num_iterations: int = 1000) -> None: ...
    alpha_v: Incomplete
    def initialize_alpha(self, tensor, scale, var_name) -> None: ...
    def update_final_weights(self): ...
    def get_loss(self, beta, warm_start, adaround_out_tensor, orig_out_tensor): ...
    def update_beta_warm(self, cur_iteration): ...

def run_adaround(data_loader, fp32_program, fetch_list, exe, scope, place, quantized_op_pairs, weight_op_pairs, scale_dict, num_iterations: int = 1000, lr: float = 0.001, bias_correction: bool = False, fast_mode: bool = True) -> None: ...
