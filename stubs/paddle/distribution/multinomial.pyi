from _typeshed import Incomplete
from paddle.distribution import categorical as categorical, distribution as distribution

class Multinomial(distribution.Distribution):
    probs: Incomplete
    total_count: Incomplete
    def __init__(self, total_count, probs) -> None: ...
    @property
    def mean(self): ...
    @property
    def variance(self): ...
    def prob(self, value): ...
    def log_prob(self, value): ...
    def sample(self, shape=()): ...
    def entropy(self): ...
