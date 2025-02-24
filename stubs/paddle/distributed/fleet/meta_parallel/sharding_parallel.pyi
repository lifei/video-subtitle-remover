from ..utils.hybrid_parallel_util import broadcast_dp_parameters as broadcast_dp_parameters, broadcast_sharding_parameters as broadcast_sharding_parameters
from ..utils.log_util import logger as logger
from .meta_parallel_base import MetaParallelBase as MetaParallelBase

class ShardingParallel(MetaParallelBase):
    def __init__(self, layers, hcg, **kwargs) -> None: ...
