from ..layer.layers import Layer as Layer
from _typeshed import Incomplete
from paddle.autograd import PyLayer as PyLayer
from paddle.framework import ParamAttr as ParamAttr
from paddle.nn.initializer import Constant as Constant
from paddle.utils import unique_name as unique_name

def round(x): ...

class LsqFunc(PyLayer):
    @staticmethod
    def forward(ctx, weight, alpha, g, Qn, Qp, per_channel: bool = False, quant_axis: int = 0): ...
    @staticmethod
    def backward(ctx, grad_weight): ...

class LsqPlusActFunc(PyLayer):
    @staticmethod
    def forward(ctx, x, alpha, beta, g, Qn, Qp): ...
    @staticmethod
    def backward(ctx, grad_x): ...

class FakeQuantActLSQPlus(Layer):
    bits: Incomplete
    all_positive: Incomplete
    symmetric: Incomplete
    batch_init: Incomplete
    name: Incomplete
    reduce_type: Incomplete
    Qn: int
    Qp: Incomplete
    s: Incomplete
    beta: Incomplete
    init_state: int
    def __init__(self, quant_bits, all_postive: bool = False, symmetric: bool = False, batch_init: int = 20, dtype: str = 'float32', name: Incomplete | None = None, reduce_type: Incomplete | None = None) -> None: ...
    g: Incomplete
    def forward(self, activation): ...

class FakeQuantWeightLSQPlus(Layer):
    bits: Incomplete
    all_positive: Incomplete
    per_channel: Incomplete
    quant_linear: Incomplete
    batch_init: Incomplete
    name: Incomplete
    quant_axis: Incomplete
    collect_axis: Incomplete
    reduce_type: Incomplete
    Qn: int
    Qp: Incomplete
    init_state: int
    s: Incomplete
    def __init__(self, quant_bits, all_postive: bool = False, per_channel: bool = False, batch_init: int = 20, channel_num: Incomplete | None = None, quant_linear: bool = False, dtype: str = 'float32', name: Incomplete | None = None, reduce_type: Incomplete | None = None) -> None: ...
    g: Incomplete
    div: Incomplete
    def forward(self, weight): ...
