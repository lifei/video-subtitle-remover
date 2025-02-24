from ... import tensor as tensor
from ...framework import ParamAttr as ParamAttr
from .common import Dropout as Dropout, Linear as Linear
from .container import LayerList as LayerList
from .layers import Layer as Layer
from .norm import LayerNorm as LayerNorm
from _typeshed import Incomplete
from paddle.base.data_feeder import convert_dtype as convert_dtype
from typing import NamedTuple

class MultiHeadAttention(Layer):
    class Cache(NamedTuple):
        k: Incomplete
        v: Incomplete

    class StaticCache(NamedTuple):
        k: Incomplete
        v: Incomplete
    embed_dim: Incomplete
    kdim: Incomplete
    vdim: Incomplete
    num_heads: Incomplete
    dropout: Incomplete
    need_weights: Incomplete
    head_dim: Incomplete
    q_proj: Incomplete
    k_proj: Incomplete
    v_proj: Incomplete
    out_proj: Incomplete
    def __init__(self, embed_dim, num_heads, dropout: float = 0.0, kdim: Incomplete | None = None, vdim: Incomplete | None = None, need_weights: bool = False, weight_attr: Incomplete | None = None, bias_attr: Incomplete | None = None) -> None: ...
    def compute_kv(self, key, value): ...
    def gen_cache(self, key, value: Incomplete | None = None, type=...): ...
    def forward(self, query, key: Incomplete | None = None, value: Incomplete | None = None, attn_mask: Incomplete | None = None, cache: Incomplete | None = None): ...

class TransformerEncoderLayer(Layer):
    normalize_before: Incomplete
    self_attn: Incomplete
    linear1: Incomplete
    dropout: Incomplete
    linear2: Incomplete
    norm1: Incomplete
    norm2: Incomplete
    dropout1: Incomplete
    dropout2: Incomplete
    activation: Incomplete
    def __init__(self, d_model, nhead, dim_feedforward, dropout: float = 0.1, activation: str = 'relu', attn_dropout: Incomplete | None = None, act_dropout: Incomplete | None = None, normalize_before: bool = False, weight_attr: Incomplete | None = None, bias_attr: Incomplete | None = None) -> None: ...
    def forward(self, src, src_mask: Incomplete | None = None, cache: Incomplete | None = None): ...
    def gen_cache(self, src): ...

class TransformerEncoder(Layer):
    layers: Incomplete
    num_layers: Incomplete
    norm: Incomplete
    def __init__(self, encoder_layer, num_layers, norm: Incomplete | None = None) -> None: ...
    def forward(self, src, src_mask: Incomplete | None = None, cache: Incomplete | None = None): ...
    def gen_cache(self, src): ...

class TransformerDecoderLayer(Layer):
    normalize_before: Incomplete
    self_attn: Incomplete
    cross_attn: Incomplete
    linear1: Incomplete
    dropout: Incomplete
    linear2: Incomplete
    norm1: Incomplete
    norm2: Incomplete
    norm3: Incomplete
    dropout1: Incomplete
    dropout2: Incomplete
    dropout3: Incomplete
    activation: Incomplete
    def __init__(self, d_model, nhead, dim_feedforward, dropout: float = 0.1, activation: str = 'relu', attn_dropout: Incomplete | None = None, act_dropout: Incomplete | None = None, normalize_before: bool = False, weight_attr: Incomplete | None = None, bias_attr: Incomplete | None = None) -> None: ...
    def forward(self, tgt, memory, tgt_mask: Incomplete | None = None, memory_mask: Incomplete | None = None, cache: Incomplete | None = None): ...
    def gen_cache(self, memory): ...

class TransformerDecoder(Layer):
    layers: Incomplete
    num_layers: Incomplete
    norm: Incomplete
    def __init__(self, decoder_layer, num_layers, norm: Incomplete | None = None) -> None: ...
    def forward(self, tgt, memory, tgt_mask: Incomplete | None = None, memory_mask: Incomplete | None = None, cache: Incomplete | None = None): ...
    def gen_cache(self, memory, do_zip: bool = False): ...

class Transformer(Layer):
    encoder: Incomplete
    decoder: Incomplete
    d_model: Incomplete
    nhead: Incomplete
    def __init__(self, d_model: int = 512, nhead: int = 8, num_encoder_layers: int = 6, num_decoder_layers: int = 6, dim_feedforward: int = 2048, dropout: float = 0.1, activation: str = 'relu', attn_dropout: Incomplete | None = None, act_dropout: Incomplete | None = None, normalize_before: bool = False, weight_attr: Incomplete | None = None, bias_attr: Incomplete | None = None, custom_encoder: Incomplete | None = None, custom_decoder: Incomplete | None = None) -> None: ...
    def forward(self, src, tgt, src_mask: Incomplete | None = None, tgt_mask: Incomplete | None = None, memory_mask: Incomplete | None = None): ...
    def generate_square_subsequent_mask(self, length): ...
