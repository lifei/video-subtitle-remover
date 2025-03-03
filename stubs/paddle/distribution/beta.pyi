from paddle.distribution import dirichlet as dirichlet, exponential_family as exponential_family

class Beta(exponential_family.ExponentialFamily):
    def __init__(self, alpha, beta) -> None: ...
    @property
    def mean(self): ...
    @property
    def variance(self): ...
    def prob(self, value): ...
    def log_prob(self, value): ...
    def sample(self, shape=()): ...
    def entropy(self): ...
