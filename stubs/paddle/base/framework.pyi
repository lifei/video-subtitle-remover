import threading
from . import core as core, unique_name as unique_name
from .. import pir as pir
from .libpaddle import DataType as DataType
from .proto import data_feed_pb2 as data_feed_pb2, framework_pb2 as framework_pb2
from .wrapped_decorator import signature_safe_contextmanager as signature_safe_contextmanager, wrap_decorator as wrap_decorator
from _typeshed import Incomplete
from collections.abc import Generator
from paddle.static.amp.fp16_utils import AmpOptions as AmpOptions

EMPTY_VAR_NAME: Incomplete
TEMP_VAR_NAME: Incomplete
GRAD_VAR_SUFFIX: Incomplete
ZERO_VAR_SUFFIX: Incomplete
CONTROL_DEP_VAR_PREFIX: Incomplete

def set_flags(flags) -> None: ...
def get_flags(flags): ...

class GlobalThreadLocal(threading.local):
    def __init__(self) -> None: ...
    def __setattr__(self, name, val) -> None: ...

global_var: Incomplete
global_prog_seed: int
special_op_attrs: Incomplete
extra_op_attrs: Incomplete
paddle_type_to_proto_type: Incomplete

def in_dygraph_mode(): ...
def in_pir_mode(): ...
def use_pir_api(): ...
def in_dynamic_or_pir_mode(): ...

global_ipu_index: int
global_ipu_stage: int
ipu_index_attr_name: str
ipu_stage_attr_name: str

def ipu_shard_guard(index: int = -1, stage: int = -1) -> Generator[None]: ...
def set_ipu_shard(call_func, index: int = -1, stage: int = -1): ...
def require_version(min_version, max_version: Incomplete | None = None): ...
def deprecate_stat_dict(func): ...

dygraph_not_support: Incomplete
dygraph_only: Incomplete
static_only: Incomplete
fake_interface_only: Incomplete
non_static_only: Incomplete

def is_compiled_with_xpu(): ...
def disable_signal_handler() -> None: ...
def is_compiled_with_cinn(): ...
def is_compiled_with_cuda(): ...
def is_compiled_with_distribute(): ...
def is_compiled_with_rocm(): ...
def cuda_places(device_ids: Incomplete | None = None): ...
def xpu_places(device_ids: Incomplete | None = None): ...
def cpu_places(device_count: Incomplete | None = None): ...
def cuda_pinned_places(device_count: Incomplete | None = None): ...

class NameScope:
    def __init__(self, name: str = '', parent: Incomplete | None = None) -> None: ...
    def child(self, prefix): ...
    def parent(self): ...
    def name(self): ...

def name_scope(prefix: Incomplete | None = None) -> Generator[None]: ...
def generate_control_dev_var_name(): ...
def grad_var_name(var_name): ...
def convert_np_dtype_to_dtype_(np_dtype): ...
def dtype_is_floating(dtype): ...
def wrap_as_scalar(number): ...
def wrap_as_scalars(array): ...
def extract_plain_list(array): ...
def canonicalize_attrs(attrs, op_proto): ...

class VariableMetaClass(type):
    @classmethod
    def __instancecheck__(cls, instance): ...

class ParameterMetaClass(VariableMetaClass):
    @classmethod
    def __instancecheck__(cls, instance): ...

class Variable(metaclass=VariableMetaClass):
    block: Incomplete
    belong_to_optimizer: Incomplete
    error_clip: Incomplete
    desc: Incomplete
    op: Incomplete
    is_data: Incomplete
    is_view_var: bool
    def __init__(self, block, type=..., name: Incomplete | None = None, shape: Incomplete | None = None, dtype: Incomplete | None = None, lod_level: Incomplete | None = None, capacity: Incomplete | None = None, persistable: Incomplete | None = None, error_clip: Incomplete | None = None, stop_gradient: bool = False, is_data: bool = False, need_check_feed: bool = False, belong_to_optimizer: bool = False, **kwargs) -> None: ...
    def detach(self): ...
    def numpy(self) -> None: ...
    def backward(self, retain_graph: bool = False) -> None: ...
    def gradient(self) -> None: ...
    def clear_gradient(self) -> None: ...
    def register_hook(self, hook): ...
    def to_string(self, throw_on_error, with_details: bool = False): ...
    def element_size(self): ...
    @property
    def stop_gradient(self): ...
    @stop_gradient.setter
    def stop_gradient(self, s) -> None: ...
    @property
    def persistable(self): ...
    @persistable.setter
    def persistable(self, p) -> None: ...
    @property
    def is_parameter(self): ...
    @is_parameter.setter
    def is_parameter(self, p) -> None: ...
    @property
    def name(self): ...
    @property
    def grad_name(self): ...
    @name.setter
    def name(self, new_name) -> None: ...
    @property
    def shape(self): ...
    @property
    def dtype(self): ...
    @property
    def lod_level(self): ...
    @property
    def type(self): ...
    @property
    def T(self): ...
    def clone(self): ...
    def __getitem__(self, item): ...
    def __setitem__(self, item, value) -> None: ...
    def get_value(self, scope: Incomplete | None = None): ...
    def set_value(self, value, scope: Incomplete | None = None) -> None: ...
    def size(self): ...
    @property
    def attr_names(self): ...
    def attr(self, name): ...
    @property
    def dist_attr(self): ...
    @dist_attr.setter
    def dist_attr(self, dist_attr) -> None: ...

def get_all_op_protos(): ...

class OpProtoHolder:
    @classmethod
    def instance(cls): ...
    op_proto_map: Incomplete
    def __init__(self) -> None: ...
    def get_op_proto(self, type): ...
    def update_op_proto(self): ...
    def has_op_proto(self, type): ...
    @staticmethod
    def generated_op_attr_names(): ...

class Operator:
    OP_WITHOUT_KERNEL_SET: Incomplete
    attrs: Incomplete
    block: Incomplete
    desc: Incomplete
    def __init__(self, block, desc, type: Incomplete | None = None, inputs: Incomplete | None = None, outputs: Incomplete | None = None, attrs: Incomplete | None = None) -> None: ...
    def to_string(self, throw_on_error): ...
    @property
    def type(self): ...
    def input(self, name): ...
    @property
    def input_names(self): ...
    @property
    def input_arg_names(self): ...
    @property
    def output_arg_names(self): ...
    def output(self, name): ...
    @property
    def output_names(self): ...
    @property
    def idx(self): ...
    def has_attr(self, name): ...
    def attr_type(self, name): ...
    @property
    def attr_names(self): ...
    def attr(self, name): ...
    def all_attrs(self): ...
    @property
    def dist_attr(self): ...
    @dist_attr.setter
    def dist_attr(self, dist_attr) -> None: ...
    def set_amp_options(self, amp_options) -> None: ...
    @property
    def amp_options(self): ...

def check_if_to_static_diff_with_dygraph(op_type, inplace_map, outputs) -> None: ...
def record_is_view_var(op_type, inputs, outputs) -> None: ...

class Block:
    desc: Incomplete
    vars: Incomplete
    ops: Incomplete
    program: Incomplete
    def __init__(self, program, idx) -> None: ...
    def to_string(self, throw_on_error, with_details: bool = False): ...
    @property
    def parent_idx(self): ...
    @property
    def forward_block_idx(self): ...
    @property
    def backward_block_idx(self): ...
    @property
    def idx(self): ...
    def var(self, name): ...
    def all_parameters(self): ...
    def iter_parameters(self): ...
    def create_var(self, *args, **kwargs): ...
    def has_var(self, name): ...
    def create_parameter(self, *args, **kwargs): ...
    def append_op(self, *args, **kwargs): ...

class IrNode:
    node: Incomplete
    def __init__(self, node) -> None: ...
    def name(self): ...
    def node_type(self): ...
    def var(self): ...
    def op(self): ...
    def id(self): ...
    def is_op(self): ...
    def is_var(self): ...
    def is_ctrl_var(self): ...
    def clear_inputs(self) -> None: ...
    def remove_input_by_id(self, node_id) -> None: ...
    def remove_input(self, node) -> None: ...
    def append_input(self, node) -> None: ...
    def clear_outputs(self) -> None: ...
    def remove_output_by_id(self, node_id) -> None: ...
    def remove_output(self, node) -> None: ...
    def append_output(self, node) -> None: ...
    @property
    def inputs(self): ...
    @property
    def outputs(self): ...

class IrVarNode(IrNode):
    node: Incomplete
    def __init__(self, node) -> None: ...
    def set_shape(self, shape) -> None: ...
    def persistable(self): ...
    def type(self): ...
    def dtype(self): ...
    def shape(self): ...
    @property
    def inputs(self): ...
    @property
    def outputs(self): ...

class IrOpNode(IrNode):
    node: Incomplete
    def __init__(self, node) -> None: ...
    def rename_input(self, old_input_name, new_input_name) -> None: ...
    def rename_output(self, old_output_name, new_output_name) -> None: ...
    def input(self, name): ...
    def output(self, name): ...
    def set_type(self, new_type): ...
    def set_attr(self, name, val) -> None: ...
    def input_arg_names(self): ...
    def output_arg_names(self): ...
    @property
    def inputs(self): ...
    @property
    def outputs(self): ...

class IrGraph:
    graph: Incomplete
    def __init__(self, graph, for_test: bool = False) -> None: ...
    def clone(self): ...
    def is_test(self): ...
    def all_nodes(self): ...
    def all_var_nodes(self): ...
    def all_persistable_nodes(self): ...
    def all_op_nodes(self): ...
    def all_sub_graphs(self, for_test: bool = False): ...
    def get_sub_graph(self, i, for_test: bool = False): ...
    def create_persistable_node(self, name, var_type, shape, var_dtype): ...
    def create_var_node(self, name, var_type, shape, var_dtype): ...
    def create_control_dep_var(self): ...
    def create_var_node_from_desc(self, var_desc): ...
    def create_op_node(self, op_type, attrs, inputs, outputs): ...
    def create_op_node_from_desc(self, op_desc): ...
    def update_input_link(self, old_input_node, new_input_node, op_node) -> None: ...
    def update_output_link(self, old_output_node, new_output_node, op_node) -> None: ...
    def link_to(self, node_in, node_out) -> None: ...
    def safe_remove_nodes(self, remove_nodes) -> None: ...
    def resolve_hazard(self) -> None: ...
    def has_circle(self): ...
    def graph_num(self): ...
    def topology_sort(self): ...
    def build_adjacency_list(self): ...
    def draw(self, save_path, name, marked_nodes: Incomplete | None = None, remove_ctr_var: bool = True) -> None: ...
    def to_program(self): ...

class Program:
    desc: Incomplete
    blocks: Incomplete
    current_block_idx: int
    def __init__(self) -> None: ...
    def global_seed(self, seed: int = 0) -> None: ...
    def to_string(self, throw_on_error, with_details: bool = False): ...
    def clone(self, for_test: bool = False): ...
    @staticmethod
    def parse_from_string(binary_str): ...
    @property
    def random_seed(self): ...
    @property
    def num_blocks(self): ...
    @random_seed.setter
    def random_seed(self, seed) -> None: ...
    def global_block(self): ...
    def block(self, index): ...
    def current_block(self): ...
    def list_vars(self) -> Generator[Incomplete, Incomplete]: ...
    def all_parameters(self): ...
    def state_dict(self, mode: str = 'all', scope: Incomplete | None = None): ...
    def set_state_dict(self, state_dict, scope: Incomplete | None = None) -> None: ...

class Parameter(Variable, metaclass=ParameterMetaClass):
    trainable: Incomplete
    stop_gradient: Incomplete
    optimize_attr: Incomplete
    regularizer: Incomplete
    do_model_average: Incomplete
    need_clip: Incomplete
    is_distributed: bool
    is_parameter: bool
    def __init__(self, block, shape, dtype, type=..., **kwargs) -> None: ...
    def to_string(self, throw_on_error, with_details: bool = False): ...

class EagerParamBase(core.eager.Tensor):
    stop_gradient: Incomplete
    optimize_attr: Incomplete
    regularizer: Incomplete
    do_model_average: Incomplete
    need_clip: Incomplete
    is_distributed: Incomplete
    def __init__(self, shape, dtype, **kwargs) -> None: ...
    @classmethod
    def from_tensor(cls, tensor, **kwargs): ...
    def set_init_func(self, obj) -> None: ...
    def initialize(self) -> None: ...
    @property
    def trainable(self): ...
    @trainable.setter
    def trainable(self, trainable) -> None: ...
    def __deepcopy__(self, memo): ...

def default_startup_program(): ...
def default_main_program(): ...
def switch_main_program(program): ...
def switch_startup_program(program): ...
def program_guard(main_program, startup_program: Incomplete | None = None) -> Generator[None]: ...
def dygraph_guard_if_declarative() -> Generator[None]: ...
def switch_device(device): ...
def device_guard(device: Incomplete | None = None) -> Generator[None]: ...
