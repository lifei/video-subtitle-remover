from .base.topology import ParallelMode as ParallelMode
from paddle.base.dygraph import to_variable as to_variable
from paddle.distributed import fleet as fleet
from paddle.framework import core as core

def distributed_scaler(scaler): ...
