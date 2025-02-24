from ...base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from ...base.layer_helper import LayerHelper as LayerHelper
from ...common_ops_import import Variable as Variable
from ...framework import in_dynamic_or_pir_mode as in_dynamic_or_pir_mode
from _typeshed import Incomplete

def one_hot(x, num_classes, name: Incomplete | None = None): ...
def embedding(x, weight, padding_idx: Incomplete | None = None, sparse: bool = False, name: Incomplete | None = None): ...
