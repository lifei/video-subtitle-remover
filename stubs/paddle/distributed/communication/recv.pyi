from _typeshed import Incomplete
from paddle.distributed.communication import stream as stream

def recv(tensor, src: int = 0, group: Incomplete | None = None, sync_op: bool = True): ...
def irecv(tensor, src: Incomplete | None = None, group: Incomplete | None = None): ...
