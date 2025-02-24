from _typeshed import Incomplete
from paddle.base import core as core, framework as framework
from paddle.base.backward import gradients_with_optimizer as gradients_with_optimizer

def backward(tensors, grad_tensors: Incomplete | None = None, retain_graph: bool = False): ...
