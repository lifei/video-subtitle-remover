from ...base.data_feeder import check_type as check_type, check_variable_and_dtype as check_variable_and_dtype
from ...base.layer_helper import LayerHelper as LayerHelper
from ...common_ops_import import Variable as Variable
from ...framework import convert_np_dtype_to_dtype_ as convert_np_dtype_to_dtype_, core as core, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode
from _typeshed import Incomplete
from paddle import in_dynamic_mode as in_dynamic_mode, tensor as tensor
from paddle.utils import deprecated as deprecated

def diag_embed(input, offset: int = 0, dim1: int = -2, dim2: int = -1): ...
def sequence_mask(x, maxlen: Incomplete | None = None, dtype: str = 'int64', name: Incomplete | None = None): ...
def gather_tree(ids, parents): ...
def temporal_shift(x, seg_num, shift_ratio: float = 0.25, name: Incomplete | None = None, data_format: str = 'NCHW'): ...
