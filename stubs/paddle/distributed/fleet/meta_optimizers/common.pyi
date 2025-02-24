from ..base.private_helper_function import wait_server_ready as wait_server_ready
from _typeshed import Incomplete
from paddle.framework import core as core
from paddle.utils import unique_name as unique_name

OpRole: Incomplete
OP_ROLE_KEY: Incomplete
OP_ROLE_VAR_KEY: Incomplete

def is_update_op(op): ...
def is_loss_grad_op(op): ...
def is_backward_op(op): ...
def is_optimizer_op(op): ...

class CollectiveHelper:
    nrings: Incomplete
    wait_port: Incomplete
    role_maker: Incomplete
    def __init__(self, role_maker, nrings: int = 1, wait_port: bool = True) -> None: ...
    startup_program: Incomplete
    def update_startup_program(self, startup_program: Incomplete | None = None) -> None: ...
