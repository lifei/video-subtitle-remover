from ..base.data_feeder import check_dtype as check_dtype, check_variable_and_dtype as check_variable_and_dtype
from ..framework import LayerHelper as LayerHelper, convert_np_dtype_to_dtype_ as convert_np_dtype_to_dtype_, core as core, in_dynamic_mode as in_dynamic_mode, in_dynamic_or_pir_mode as in_dynamic_or_pir_mode
from _typeshed import Incomplete
from paddle.common_ops_import import VarDesc as VarDesc, Variable as Variable
from paddle.utils.inplace_utils import inplace_apis_in_dygraph_only as inplace_apis_in_dygraph_only

def argsort(x, axis: int = -1, descending: bool = False, name: Incomplete | None = None): ...
def argmax(x, axis: Incomplete | None = None, keepdim: bool = False, dtype: str = 'int64', name: Incomplete | None = None): ...
def argmin(x, axis: Incomplete | None = None, keepdim: bool = False, dtype: str = 'int64', name: Incomplete | None = None): ...
def index_select(x, index, axis: int = 0, name: Incomplete | None = None): ...
def nonzero(x, as_tuple: bool = False): ...
def sort(x, axis: int = -1, descending: bool = False, name: Incomplete | None = None): ...
def mode(x, axis: int = -1, keepdim: bool = False, name: Incomplete | None = None): ...
def where(condition, x: Incomplete | None = None, y: Incomplete | None = None, name: Incomplete | None = None): ...
def where_(condition, x: Incomplete | None = None, y: Incomplete | None = None, name: Incomplete | None = None): ...
def index_sample(x, index): ...
def masked_select(x, mask, name: Incomplete | None = None): ...
def topk(x, k, axis: Incomplete | None = None, largest: bool = True, sorted: bool = True, name: Incomplete | None = None): ...
def bucketize(x, sorted_sequence, out_int32: bool = False, right: bool = False, name: Incomplete | None = None): ...
def searchsorted(sorted_sequence, values, out_int32: bool = False, right: bool = False, name: Incomplete | None = None): ...
def kthvalue(x, k, axis: Incomplete | None = None, keepdim: bool = False, name: Incomplete | None = None): ...
def top_p_sampling(x, ps, threshold: Incomplete | None = None, seed: Incomplete | None = None, name: Incomplete | None = None): ...
