from _typeshed import Incomplete
from paddle import framework as framework
from paddle.distributed.communication import stream as stream

class ReduceOp:
    SUM: int
    MAX: int
    MIN: int
    PROD: int
    AVG: int

def reduce(tensor, dst, op=..., group: Incomplete | None = None, sync_op: bool = True): ...
