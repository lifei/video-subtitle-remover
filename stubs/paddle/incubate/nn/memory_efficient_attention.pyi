from .attn_bias import BlockDiagonalCausalMask as BlockDiagonalCausalMask, BlockDiagonalCausalWithOffsetPaddedKeysMask as BlockDiagonalCausalWithOffsetPaddedKeysMask, BlockDiagonalMask as BlockDiagonalMask, LowerTriangularMask as LowerTriangularMask, LowerTriangularMaskWithTensorBias as LowerTriangularMaskWithTensorBias
from _typeshed import Incomplete
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.framework import in_dynamic_mode as in_dynamic_mode

SUPPORTED_ATTN_BIAS_TYPES: Incomplete

def memory_efficient_attention(query, key, value, attn_bias: Incomplete | None = None, p: float = 0.0, scale: Incomplete | None = None, training: bool = True): ...
