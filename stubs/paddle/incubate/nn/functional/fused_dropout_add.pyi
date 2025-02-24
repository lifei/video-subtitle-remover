from _typeshed import Incomplete
from paddle.base import core as core
from paddle.common_ops_import import default_main_program as default_main_program
from paddle.framework import LayerHelper as LayerHelper, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode

def fused_dropout_add(x, y, p: float = 0.5, training: bool = True, mode: str = 'upscale_in_train', name: Incomplete | None = None): ...
