from _typeshed import Incomplete
from paddle.distributed.communication import stream as stream
from paddle.distributed.communication.reduce import ReduceOp as ReduceOp

def all_reduce(tensor, op=..., group: Incomplete | None = None, sync_op: bool = True): ...
