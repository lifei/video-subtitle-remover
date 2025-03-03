from _typeshed import Incomplete
from collections.abc import Generator
from enum import Enum

__all__ = ['DebugMode', 'TensorCheckerConfig', 'check_numerics', 'enable_operator_stats_collection', 'disable_operator_stats_collection', 'collect_operator_stats', 'enable_tensor_checker', 'disable_tensor_checker', 'compare_accuracy', 'check_layer_numerics']

class DebugMode(Enum):
    CHECK_NAN_INF_AND_ABORT = 0
    CHECK_NAN_INF = 1
    CHECK_ALL_FOR_OVERFLOW = 2
    CHECK_ALL = 3

def check_layer_numerics(func): ...

class TensorCheckerConfig:
    current_step_id: int
    enable: Incomplete
    debug_mode: Incomplete
    output_dir: Incomplete
    checked_op_list: Incomplete
    skipped_op_list: Incomplete
    debug_step: Incomplete
    stack_height_limit: Incomplete
    start_step: Incomplete
    end_step: Incomplete
    seed: int
    initial_seed: int
    def __init__(self, enable, debug_mode=..., output_dir: Incomplete | None = None, checked_op_list: Incomplete | None = None, skipped_op_list: Incomplete | None = None, debug_step: Incomplete | None = None, stack_height_limit: int = 1) -> None: ...
    def update_and_check_step_id(self): ...
    def start_check_nan_inf(self) -> None: ...
    def stop_check_nan_inf(self) -> None: ...

def check_numerics(tensor, op_type, var_name, debug_mode=...): ...
def enable_operator_stats_collection() -> None: ...
def disable_operator_stats_collection() -> None: ...
def collect_operator_stats() -> Generator[None]: ...
def compare_accuracy(dump_path, another_dump_path, output_filename, loss_scale: int = 1, dump_all_tensors: bool = False) -> None: ...
def enable_tensor_checker(checker_config) -> None: ...
def disable_tensor_checker() -> None: ...
