from . import backward as backward, compiler as compiler, core as core, data_feed_desc as data_feed_desc, dataset as dataset, dygraph as dygraph, executor as executor, framework as framework, incubate as incubate, initializer as initializer, io as io, layers as layers, trainer_desc as trainer_desc, unique_name as unique_name
from .backward import append_backward as append_backward, gradients as gradients
from .compiler import BuildStrategy as BuildStrategy, CompiledProgram as CompiledProgram, ExecutionStrategy as ExecutionStrategy, IpuCompiledProgram as IpuCompiledProgram, IpuStrategy as IpuStrategy
from .core import CPUPlace as CPUPlace, CUDAPinnedPlace as CUDAPinnedPlace, CUDAPlace as CUDAPlace, CustomPlace as CustomPlace, IPUPlace as IPUPlace, LoDTensor as LoDTensor, LoDTensorArray as LoDTensorArray, Scope as Scope, XPUPlace as XPUPlace
from .data_feed_desc import DataFeedDesc as DataFeedDesc
from .data_feeder import DataFeeder as DataFeeder
from .dataset import DatasetFactory as DatasetFactory, InMemoryDataset as InMemoryDataset
from .dygraph.base import disable_dygraph as disable_dygraph, enable_dygraph as enable_dygraph
from .dygraph.tensor_patch_methods import monkey_patch_tensor as monkey_patch_tensor
from .executor import Executor as Executor, global_scope as global_scope, scope_guard as scope_guard
from .framework import Program as Program, Variable as Variable, cpu_places as cpu_places, cuda_pinned_places as cuda_pinned_places, cuda_places as cuda_places, default_main_program as default_main_program, default_startup_program as default_startup_program, device_guard as device_guard, get_flags as get_flags, in_dygraph_mode as in_dygraph_mode, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode, in_pir_mode as in_pir_mode, ipu_shard_guard as ipu_shard_guard, is_compiled_with_cinn as is_compiled_with_cinn, is_compiled_with_cuda as is_compiled_with_cuda, is_compiled_with_rocm as is_compiled_with_rocm, is_compiled_with_xpu as is_compiled_with_xpu, name_scope as name_scope, program_guard as program_guard, require_version as require_version, set_flags as set_flags, set_ipu_shard as set_ipu_shard, xpu_places as xpu_places
from .initializer import set_global_initializer as set_global_initializer
from .lod_tensor import create_lod_tensor as create_lod_tensor, create_random_int_lodtensor as create_random_int_lodtensor
from .param_attr import ParamAttr as ParamAttr, WeightNormParamAttr as WeightNormParamAttr
from .trainer_desc import DistMultiTrainer as DistMultiTrainer, HeterPipelineTrainer as HeterPipelineTrainer, HeterXpuTrainer as HeterXpuTrainer, MultiTrainer as MultiTrainer, PipelineTrainer as PipelineTrainer, TrainerDesc as TrainerDesc
from _typeshed import Incomplete
from paddle.base.layers.math_op_patch import monkey_patch_variable as monkey_patch_variable

core_suffix: str
legacy_core: Incomplete
Tensor = LoDTensor
enable_imperative = enable_dygraph
disable_imperative = disable_dygraph

def __bootstrap__() -> None: ...
