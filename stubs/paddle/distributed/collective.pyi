from .communication.group import Group as Group, is_initialized as is_initialized
from .fleet.layers.mpu.mp_ops import split as split
from _typeshed import Incomplete
from paddle.base import core as core
from paddle.framework import in_dynamic_mode as in_dynamic_mode

def new_group(ranks: Incomplete | None = None, backend: Incomplete | None = None, timeout=...): ...
def is_available(): ...
