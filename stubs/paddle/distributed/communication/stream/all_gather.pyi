from _typeshed import Incomplete
from paddle import framework as framework
from paddle.base import data_feeder as data_feeder

def all_gather(tensor_or_tensor_list, tensor, group: Incomplete | None = None, sync_op: bool = True, use_calc_stream: bool = False): ...
