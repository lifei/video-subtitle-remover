from _typeshed import Incomplete
from paddle import framework as framework
from paddle.base import data_feeder as data_feeder

def recv(tensor, src: int = 0, group: Incomplete | None = None, sync_op: bool = True, use_calc_stream: bool = False): ...
