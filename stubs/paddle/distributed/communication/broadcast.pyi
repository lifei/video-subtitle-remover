from .serialization_utils import convert_object_to_tensor as convert_object_to_tensor, convert_tensor_to_object as convert_tensor_to_object
from _typeshed import Incomplete
from paddle import framework as framework
from paddle.distributed.communication import stream as stream

def broadcast(tensor, src, group: Incomplete | None = None, sync_op: bool = True): ...
def broadcast_object_list(object_list, src, group: Incomplete | None = None) -> None: ...
