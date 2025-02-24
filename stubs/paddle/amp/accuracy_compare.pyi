from _typeshed import Incomplete

def is_infinite(value, dtype=...): ...
def is_allclose(actual, expected, atol: float = 0.01, rtol: float = 0.01): ...

class TensorInfo:
    device: Incomplete
    op_type: Incomplete
    tensor_name: Incomplete
    dtype: Incomplete
    numel: Incomplete
    max_value: Incomplete
    min_value: Incomplete
    mean_value: Incomplete
    has_inf: Incomplete
    has_nan: Incomplete
    num_zero: Incomplete
    def __init__(self) -> None: ...
    def key(self): ...
    def init_from_string(self, line): ...

class MixedPrecisionTensorInfo:
    is_normal: bool
    fp32_idx: Incomplete
    fp32_tensor_name: Incomplete
    fp32_dtype: Incomplete
    fp32_max_value: Incomplete
    fp32_min_value: Incomplete
    fp32_mean_value: Incomplete
    fp32_num_zero: Incomplete
    scaled_fp32_max_value: Incomplete
    scaled_fp32_min_value: Incomplete
    fp16_tensor_name: Incomplete
    fp16_dtype: Incomplete
    fp16_max_value: Incomplete
    fp16_min_value: Incomplete
    fp16_mean_value: Incomplete
    fp16_num_zero: Incomplete
    fp16_has_inf: Incomplete
    fp16_has_nan: Incomplete
    fp32_div_fp16_max_value: Incomplete
    fp32_div_fp16_min_value: Incomplete
    fp32_div_fp16_mean_value: Incomplete
    op_type: Incomplete
    numel: Incomplete
    def __init__(self, fp32_tensor_info, fp16_tensor_info, fp32_idx: int = 0, grad_scale: float = 1.0) -> None: ...
    def get_tensor_name(self): ...

class ExcelWriter:
    log_fp32_dir: Incomplete
    log_fp16_dir: Incomplete
    workbook: Incomplete
    title_format: Incomplete
    tensor_name_format: Incomplete
    red_bg_cell_format: Incomplete
    yellow_bg_cell_format: Incomplete
    orange_bg_cell_format: Incomplete
    def __init__(self, log_fp32_dir, log_fp16_dir, output_path) -> None: ...
    def close(self) -> None: ...
    def add_worksheet(self, mp_tensor_info_list, sheetname, loss_scale, skip_normal_tensors) -> None: ...

def parse_lines(lines, specified_op_list: Incomplete | None = None): ...
def parse_log(log_dir, filename, specified_op_list: Incomplete | None = None): ...
def merge_tensor_info_list(fp32_tensor_info_list, fp16_tensor_info_list, grad_scale): ...
def compare_accuracy(dump_path, another_dump_path, output_filename, loss_scale: int = 1, dump_all_tensors: bool = False) -> None: ...
