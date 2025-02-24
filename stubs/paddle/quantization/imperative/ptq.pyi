from . import fuse_utils as fuse_utils, ptq_config as ptq_config, ptq_hooks as ptq_hooks, ptq_quantizer as ptq_quantizer, utils as utils
from ...static.log_helper import get_logger as get_logger
from .ptq_registry import PTQRegistry as PTQRegistry
from _typeshed import Incomplete
from paddle.nn.quant import quant_layers as quant_layers

INFER_MODEL_SUFFIX: str
INFER_PARAMS_SUFFIX: str

class ImperativePTQ:
    def __init__(self, quant_config=...) -> None: ...
    def quantize(self, model, inplace: bool = False, fuse: bool = False, fuse_list: Incomplete | None = None): ...
    def save_quantized_model(self, model, path, input_spec: Incomplete | None = None, **config) -> None: ...
