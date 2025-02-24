import paddle
from .graphs import CUDAGraph as CUDAGraph
from _typeshed import Incomplete

class CUDAGraphContext:
    step: int
    layer: Incomplete
    forward_graph: Incomplete
    backward_graph: Incomplete
    num_warmup_steps: Incomplete
    def __init__(self, layer, num_warmup_steps) -> None: ...

def detach(x): ...
def get_grad(x): ...

class _CUDAGraphedLayer(paddle.autograd.PyLayer):
    @staticmethod
    def forward(ctx, context, *args): ...
    @staticmethod
    def backward(ctx, dy): ...

class CUDAGraphedLayer(paddle.nn.Layer):
    context: Incomplete
    def __init__(self, layer: paddle.nn.Layer, num_warmup_steps: int = 3) -> None: ...
    def forward(self, *args): ...
