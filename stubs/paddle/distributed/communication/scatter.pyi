from .serialization_utils import convert_object_to_tensor as convert_object_to_tensor, convert_tensor_to_object as convert_tensor_to_object
from _typeshed import Incomplete
from paddle import framework as framework
from paddle.distributed.communication import stream as stream

def scatter(tensor, tensor_list: Incomplete | None = None, src: int = 0, group: Incomplete | None = None, sync_op: bool = True): ...
def scatter_object_list(out_object_list, in_object_list: Incomplete | None = None, src: int = 0, group: Incomplete | None = None) -> None: ...
