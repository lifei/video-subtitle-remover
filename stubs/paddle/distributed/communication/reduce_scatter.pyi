from _typeshed import Incomplete
from paddle.distributed.communication import stream as stream
from paddle.distributed.communication.reduce import ReduceOp as ReduceOp

def reduce_scatter(tensor, tensor_list, op=..., group: Incomplete | None = None, sync_op: bool = True): ...
