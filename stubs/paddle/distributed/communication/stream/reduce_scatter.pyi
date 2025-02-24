from _typeshed import Incomplete
from paddle import framework as framework
from paddle.base import data_feeder as data_feeder
from paddle.distributed.communication.reduce import ReduceOp as ReduceOp

def reduce_scatter(tensor, tensor_or_tensor_list, op=..., group: Incomplete | None = None, sync_op: bool = True, use_calc_stream: bool = False): ...
