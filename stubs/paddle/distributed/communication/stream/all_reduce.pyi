from _typeshed import Incomplete
from paddle import framework as framework
from paddle.base import data_feeder as data_feeder
from paddle.distributed.communication.reduce import ReduceOp as ReduceOp

def all_reduce(tensor, op=..., group: Incomplete | None = None, sync_op: bool = True, use_calc_stream: bool = False): ...
