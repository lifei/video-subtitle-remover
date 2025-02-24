from .node import DownpourServer as DownpourServer, DownpourWorker as DownpourWorker
from _typeshed import Incomplete
from paddle.framework import core as core

OpRole: Incomplete
FLEET_GLOBAL_DICT: Incomplete
logger: Incomplete
formatter: Incomplete
ch: Incomplete

class DistributedOptimizerImplBase:
    def __init__(self, optimizer) -> None: ...
    def minimize(self, losses, startup_program: Incomplete | None = None, parameter_list: Incomplete | None = None, no_grad_set: Incomplete | None = None) -> None: ...

class DistributedAdam(DistributedOptimizerImplBase):
    type: str
    data_norm_name: Incomplete
    supported_embedding_types: Incomplete
    supported_embedding_grad_types: Incomplete
    op_role_key: Incomplete
    def __init__(self, optimizer) -> None: ...
