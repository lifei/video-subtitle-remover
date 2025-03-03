from _typeshed import Incomplete
from paddle.base import core as core
from paddle.base.core import CUDAPlace as CUDAPlace, is_compiled_with_cuda as is_compiled_with_cuda, is_compiled_with_rocm as is_compiled_with_rocm

def is_cuda_graph_supported(): ...

ALL_MODES: Incomplete
cuda_graph_id: int

class CUDAGraph:
    def __init__(self, place: Incomplete | None = None, mode: str = 'thread_local') -> None: ...
    def capture_begin(self) -> None: ...
    def capture_end(self) -> None: ...
    def replay(self) -> None: ...
    def reset(self) -> None: ...
    def print_to_dot_files(self, dirname, flags: Incomplete | None = None) -> None: ...

def wrap_cuda_graph(function, mode: str = 'thread_local', memory_pool: str = 'default'): ...
def copy_var_desc(dst, src) -> None: ...
def all_inputs_of_later_op(block, begin_idx): ...
def construct_program_and_find_ins_outs(section, origin_program, section_idx): ...
def get_cuda_graph_sections(program): ...
def replace_cuda_graph_section(ins_and_outs, section_program, section_idx, origin_program, cuda_graph_section, order, is_test) -> None: ...
def cuda_graph_transform(program): ...
