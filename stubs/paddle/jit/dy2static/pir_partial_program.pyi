from .utils import RETURN_NO_VALUE_MAGIC_NUM as RETURN_NO_VALUE_MAGIC_NUM, backend_guard as backend_guard
from _typeshed import Incomplete
from paddle.autograd.ir_backward import grad as grad
from paddle.base import core as core, framework as framework
from paddle.base.compiler import BuildStrategy as BuildStrategy
from paddle.base.data_feeder import check_type as check_type, convert_dtype as convert_dtype
from paddle.base.dygraph.base import switch_to_static_graph as switch_to_static_graph
from paddle.optimizer.lr import LRScheduler as LRScheduler
from paddle.pir import OpResult as OpResult, fake_op_result as fake_op_result, is_fake_op_result as is_fake_op_result

class cached_property:
    function: Incomplete
    def __init__(self, function) -> None: ...
    def __get__(self, instance, cls): ...

class NestSequence:
    def __init__(self, raw_input) -> None: ...
    @property
    def var_list(self): ...
    def restore(self, value_list): ...
    def __getitem__(self, item): ...

class RunableProgram:
    def get_value_name_map(self): ...
    def get_name_value_map(self): ...
    def convert_name(self, values): ...
    def x_values(self): ...
    def param_values(self): ...
    def out_values(self): ...
    def x_grad_values(self): ...
    def param_grad_values(self): ...
    def out_grad_values(self): ...
    program: Incomplete
    x_names: Incomplete
    param_names: Incomplete
    out_names: Incomplete
    forward_range: Incomplete
    backward_range: Incomplete
    has_splited: bool
    finish_pass: bool
    x_grad_names: Incomplete
    p_grad_names: Incomplete
    o_grad_names: Incomplete
    def __init__(self, program, in_out_values, grad_in_out_values: Incomplete | None = None, forward_range: Incomplete | None = None, backward_range: Incomplete | None = None) -> None: ...
    def clone(self): ...
    def split_forward_backward(self): ...
    def apply_pir_program_pass(self, pass_fn) -> None: ...
    def program_attr(self): ...
    def program_name_attr(self): ...
    def forward_program(self): ...
    def backward_program(self): ...

class PirPassContext:
    INPUT_OP_NAME: str
    PARM_OP_NAME: str
    OUTPUT_OP_NAME: str
    @classmethod
    def apply(cls, runable_program, build_strategy): ...

class PartialProgramLayerHook:
    def before_append_backward(self, forward_program, src_vars) -> None: ...
    def after_append_backward(self, whole_program, src_vars, backward_start_idx) -> None: ...
    def after_infer(self, infer_program) -> None: ...

class PartialProgramLayer:
    training: bool
    def __init__(self, main_program, inputs, outputs, parameters: Incomplete | None = None, **kwargs) -> None: ...
    def __call__(self, inputs): ...
    def sot_call(self, inputs): ...
    def origin_runable_program(self): ...
    def set_hooker(self, hooker) -> None: ...
    @property
    def program(self): ...
    @property
    def program_id(self): ...
    def train_program(self): ...
    def infer_program(self): ...
    def prepare_gradient_aggregation(self, start_idx, main_program, target_program): ...

def partial_program_from(concrete_program, from_method: bool = False): ...
