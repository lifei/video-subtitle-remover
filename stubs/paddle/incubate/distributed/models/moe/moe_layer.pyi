from .gate import BaseGate as BaseGate, GShardGate as GShardGate, NaiveGate as NaiveGate, SwitchGate as SwitchGate
from .utils import count_by_gate as count_by_gate
from _typeshed import Incomplete
from paddle import nn as nn
from paddle.autograd import PyLayer as PyLayer
from paddle.distributed.utils.moe_utils import global_gather as global_gather, global_scatter as global_scatter
from paddle.distributed.utils.nccl_utils import check_nccl_version_for_p2p as check_nccl_version_for_p2p
from paddle.framework import in_dynamic_mode as in_dynamic_mode
from paddle.incubate.distributed.fleet import recompute_hybrid as recompute_hybrid

class MoEScatter(PyLayer):
    @staticmethod
    def forward(ctx, inp, pos, local_expert_count, global_expert_count, fwd_batch_size, world_size, group: Incomplete | None = None): ...
    @staticmethod
    def backward(ctx, grad): ...

class MoEGather(PyLayer):
    @staticmethod
    def forward(ctx, global_output_buf, pos, local_expert_count, global_expert_count, local_batch_size, world_size, group: Incomplete | None = None): ...
    @staticmethod
    def backward(ctx, grad_out): ...

class AllGather(PyLayer):
    @staticmethod
    def forward(ctx, inp, rank, world_size, group): ...
    @staticmethod
    def backward(ctx, grad_out): ...

class Slice(PyLayer):
    @staticmethod
    def forward(ctx, inp, rank, world_size, group): ...
    @staticmethod
    def backward(ctx, grad_out): ...

def prepare_forward(gate, num_expert, world_size, moe_group): ...

class MoELayer(nn.Layer):
    recompute_ctx: Incomplete
    group: Incomplete
    world_size: int
    num_expert: Incomplete
    recompute_interval: Incomplete
    experts: Incomplete
    mp_group: Incomplete
    d_model: Incomplete
    top_k: Incomplete
    gate: Incomplete
    def __init__(self, d_model, experts, gate: Incomplete | None = None, moe_group: Incomplete | None = None, mp_group: Incomplete | None = None, recompute_interval: int = 0, recompute_ctx: Incomplete | None = None) -> None: ...
    def forward(self, inp): ...
