from _typeshed import Incomplete
from paddle.base.data_feeder import check_type as check_type
from paddle.regularizer import WeightDecayRegularizer as WeightDecayRegularizer

class ParamAttr:
    name: Incomplete
    initializer: Incomplete
    learning_rate: Incomplete
    regularizer: Incomplete
    trainable: Incomplete
    do_model_average: Incomplete
    need_clip: Incomplete
    def __init__(self, name: Incomplete | None = None, initializer: Incomplete | None = None, learning_rate: float = 1.0, regularizer: Incomplete | None = None, trainable: bool = True, do_model_average: bool = True, need_clip: bool = True) -> None: ...

class WeightNormParamAttr(ParamAttr):
    params_with_weight_norm: Incomplete
    dim: Incomplete
    def __init__(self, dim: Incomplete | None = None, name: Incomplete | None = None, initializer: Incomplete | None = None, learning_rate: float = 1.0, regularizer: Incomplete | None = None, trainable: bool = True, do_model_average: bool = False, need_clip: bool = True) -> None: ...
