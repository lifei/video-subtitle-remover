from _typeshed import Incomplete
from paddle.base.data_feeder import check_type as check_type, convert_dtype as convert_dtype
from paddle.base.framework import Variable as Variable
from paddle.distribution import distribution as distribution
from paddle.framework import in_dynamic_mode as in_dynamic_mode
from paddle.tensor import random as random

class Uniform(distribution.Distribution):
    all_arg_is_float: bool
    batch_size_unknown: bool
    name: Incomplete
    dtype: str
    low: Incomplete
    high: Incomplete
    def __init__(self, low, high, name: Incomplete | None = None) -> None: ...
    def sample(self, shape, seed: int = 0): ...
    def log_prob(self, value): ...
    def probs(self, value): ...
    def entropy(self): ...
