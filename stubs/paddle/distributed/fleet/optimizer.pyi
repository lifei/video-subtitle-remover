from .meta_optimizers import HeterParallelOptimizer as HeterParallelOptimizer, HybridParallelOptimizer as HybridParallelOptimizer
from .utils.log_util import logger as logger
from paddle.distributed import fleet as fleet
from paddle.framework import in_dynamic_mode as in_dynamic_mode

def distributed_optimizer(*args, **kwargs): ...
