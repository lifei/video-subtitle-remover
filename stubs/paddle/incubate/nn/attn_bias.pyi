import abc
import paddle
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Generator
from dataclasses import dataclass
from typing import Sequence

class AttentionBias(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def materialize(self, shape, dtype=...): ...

class LowerTriangularMask(AttentionBias):
    def materialize(self, shape, dtype=...): ...
    def add_bias(self, bias): ...

class LowerTriangularMaskWithTensorBias(LowerTriangularMask):
    def __init__(self, bias) -> None: ...
    def materialize(self, shape, dtype=...): ...

@dataclass
class SeqLenInfo:
    seqstart: paddle.Tensor
    max_seqlen: int
    seqstart_py: list[int]
    def intervals(self) -> Generator[Incomplete, Incomplete]: ...
    @classmethod
    def from_seqlens(cls, seqlens): ...
    def split(self, x, batch_sizes: Incomplete | None = None): ...

@dataclass
class PaddedSeqLenInfo(SeqLenInfo):
    seqlen: paddle.Tensor
    seqlen_py: Sequence[int]
    def intervals(self) -> Generator[Incomplete]: ...
    @classmethod
    def from_seqlens(cls, seqlens) -> None: ...
    @classmethod
    def from_seqlens_padded(cls, seqlens, padding): ...
    def split(self, x, batch_sizes: Incomplete | None = None) -> None: ...

@dataclass
class BlockDiagonalMask(AttentionBias):
    q_seqinfo: SeqLenInfo
    k_seqinfo: SeqLenInfo
    def materialize(self, shape, dtype=...): ...
    @classmethod
    def from_seqlens(cls, q_seqlen, kv_seqlen: Incomplete | None = None): ...
    @classmethod
    def from_tensor_list(cls, tensors): ...
    @classmethod
    def from_tensor_lists_qkv(cls, tensors_q, tensors_k, tensors_v: Incomplete | None = None): ...
    def split_queries(self, tensor): ...
    def split_kv(self, tensor): ...
    def split(self, tensor): ...
    def make_causal(self): ...

@dataclass
class BlockDiagonalCausalMask(BlockDiagonalMask): ...

@dataclass
class BlockDiagonalCausalWithOffsetPaddedKeysMask(AttentionBias):
    q_seqinfo: SeqLenInfo
    k_seqinfo: PaddedSeqLenInfo
    causal_diagonal: paddle.Tensor | None = ...
    def materialize(self, shape, dtype=...): ...
    @classmethod
    def from_seqlens(cls, q_seqlen, kv_padding, kv_seqlen, causal_diagonal: Incomplete | None = None): ...
