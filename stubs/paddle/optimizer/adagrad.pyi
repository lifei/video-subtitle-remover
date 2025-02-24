from ..base import framework as framework
from .optimizer import Optimizer as Optimizer
from _typeshed import Incomplete

class Adagrad(Optimizer):
    type: str
    initial_accumulator_value: Incomplete
    def __init__(self, learning_rate, epsilon: float = 1e-06, parameters: Incomplete | None = None, weight_decay: Incomplete | None = None, grad_clip: Incomplete | None = None, name: Incomplete | None = None, initial_accumulator_value: float = 0.0) -> None: ...
