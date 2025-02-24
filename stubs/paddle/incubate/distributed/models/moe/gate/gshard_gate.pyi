from ..utils import limit_by_capacity as limit_by_capacity
from .naive_gate import NaiveGate as NaiveGate
from _typeshed import Incomplete

class GShardGate(NaiveGate):
    capacity: Incomplete
    random_routing: Incomplete
    group: Incomplete
    def __init__(self, d_model, num_expert, world_size, topk: int = 2, capacity=(1.2, 2.4), random_routing: bool = True, group: Incomplete | None = None) -> None: ...
    def forward(self, x): ...
