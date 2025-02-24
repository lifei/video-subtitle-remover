from ..nn import Layer
from _typeshed import Incomplete

__all__ = ['viterbi_decode', 'ViterbiDecoder']

def viterbi_decode(potentials, transition_params, lengths, include_bos_eos_tag: bool = True, name: Incomplete | None = None): ...

class ViterbiDecoder(Layer):
    transitions: Incomplete
    include_bos_eos_tag: Incomplete
    name: Incomplete
    def __init__(self, transitions, include_bos_eos_tag: bool = True, name: Incomplete | None = None) -> None: ...
    def forward(self, potentials, lengths): ...
