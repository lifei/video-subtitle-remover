from .base_gate import BaseGate as BaseGate
from _typeshed import Incomplete
from paddle import nn as nn

class NaiveGate(BaseGate):
    gate: Incomplete
    top_k: Incomplete
    def __init__(self, d_model, num_expert, world_size, topk: int = 2) -> None: ...
    def forward(self, inp, return_all_scores: bool = False): ...
