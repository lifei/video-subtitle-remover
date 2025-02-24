from ...base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from _typeshed import Incomplete
from paddle.base.framework import static_only as static_only
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.base.layers.layer_function_generator import templatedoc as templatedoc
from paddle.base.param_attr import ParamAttr as ParamAttr
from paddle.nn.initializer import Assign as Assign

def nce(input, label, num_total_classes, sample_weight: Incomplete | None = None, param_attr: Incomplete | None = None, bias_attr: Incomplete | None = None, num_neg_samples: Incomplete | None = None, name: Incomplete | None = None, sampler: str = 'uniform', custom_dist: Incomplete | None = None, seed: int = 0, is_sparse: bool = False): ...
