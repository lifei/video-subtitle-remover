from _typeshed import Incomplete
from paddle import framework as framework
from paddle.distributed.communication import stream as stream

def gather(tensor, gather_list: Incomplete | None = None, dst: int = 0, group: Incomplete | None = None, sync_op: bool = True): ...
