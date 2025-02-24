from ..utils import limit_by_capacity as limit_by_capacity
from .naive_gate import NaiveGate as NaiveGate
from _typeshed import Incomplete

class SwitchGate(NaiveGate):
    switch_eps: Incomplete
    capacity: Incomplete
    group: Incomplete
    def __init__(self, d_model, num_expert, world_size, topk: int = 1, switch_eps: float = 0.1, capacity=(1.2, 2.4), group: Incomplete | None = None) -> None: ...
    def forward(self, inp): ...
