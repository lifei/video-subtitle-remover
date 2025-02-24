from _typeshed import Incomplete
from paddle.framework import core as core
from paddle.framework.io import Variable as Variable

dtype_to_size: Incomplete

class VarBlock:
    varname: Incomplete
    offset: Incomplete
    size: Incomplete
    def __init__(self, varname, offset, size) -> None: ...

def create_var_struct(var): ...

class VarStruct:
    name: Incomplete
    shape: Incomplete
    dtype: Incomplete
    type: Incomplete
    lod_level: Incomplete
    persistable: Incomplete
    m_size: int
    def __init__(self, name, shape, dtype, type, lod_level, persistable) -> None: ...

class VarDistributed:
    origin: Incomplete
    slice: Incomplete
    is_slice: bool
    block_id: int
    offset: int
    vtype: Incomplete
    endpoint: Incomplete
    def __init__(self, origin_var, slice_var, is_slice: Incomplete | None = None, block_id: Incomplete | None = None, offset: Incomplete | None = None, vtype: Incomplete | None = None, endpoint: Incomplete | None = None) -> None: ...
    @staticmethod
    def equal(var1, var2): ...

class VarsDistributed:
    distributed_vars: Incomplete
    def __init__(self) -> None: ...
    def add_distributed_var(self, origin_var, slice_var, is_slice: Incomplete | None = None, block_id: Incomplete | None = None, offset: Incomplete | None = None, vtype: Incomplete | None = None, endpoint: Incomplete | None = None) -> None: ...
