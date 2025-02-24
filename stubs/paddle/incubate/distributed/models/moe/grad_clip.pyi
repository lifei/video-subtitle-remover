from _typeshed import Incomplete
from paddle.autograd import no_grad as no_grad
from paddle.framework import core as core
from paddle.nn import clip as clip
from paddle.nn.clip import ClipGradBase as ClipGradBase

class ClipGradForMOEByGlobalNorm(ClipGradBase):
    clip_norm: Incomplete
    group_name: Incomplete
    moe_group: Incomplete
    is_expert_param_func: Incomplete
    def __init__(self, clip_norm, is_expert_param_func: Incomplete | None = None, moe_group: Incomplete | None = None, group_name: str = 'default_moe_group') -> None: ...
    @staticmethod
    def get_l2_norm_pow(params_grads, sum_dtype: Incomplete | None = None): ...
ClipGradByGlobalNorm = ClipGradForMOEByGlobalNorm
