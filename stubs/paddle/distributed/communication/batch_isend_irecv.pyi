from _typeshed import Incomplete
from paddle import framework as framework

class P2POp:
    op: Incomplete
    tensor: Incomplete
    peer: Incomplete
    group: Incomplete
    def __init__(self, op, tensor, peer, group: Incomplete | None = None) -> None: ...

def batch_isend_irecv(p2p_op_list): ...
