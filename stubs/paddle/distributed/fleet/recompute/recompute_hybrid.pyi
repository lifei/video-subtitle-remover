from ..meta_parallel.parallel_layers.random import get_rng_state_tracker as get_rng_state_tracker
from ..meta_parallel.pp_utils import utils as utils
from .recompute import check_recompute_necessary as check_recompute_necessary, detach_variable as detach_variable, swith_rng_state_tracker as swith_rng_state_tracker
from paddle import framework as framework
from paddle.autograd import PyLayer as PyLayer
from paddle.framework import core as core

class _HPRecomputeFunction(PyLayer):
    @staticmethod
    def forward(ctx, run_function, all_outputs, mp_group, offload, partition, *args, **kwargs): ...
    @staticmethod
    def backward(ctx, *args): ...

def recompute_hybrid(ctx, function, *args, **kwargs): ...
