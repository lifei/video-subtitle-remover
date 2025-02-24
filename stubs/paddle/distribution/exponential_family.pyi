from paddle.distribution import distribution as distribution
from paddle.framework import in_dynamic_mode as in_dynamic_mode

class ExponentialFamily(distribution.Distribution):
    def entropy(self): ...
