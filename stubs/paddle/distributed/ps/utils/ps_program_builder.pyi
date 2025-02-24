from .public import *
from _typeshed import Incomplete
from paddle import base as base
from paddle.distributed.fleet.base.private_helper_function import wait_server_ready as wait_server_ready
from paddle.distributed.passes import new_pass as new_pass

class PsProgramBuilder:
    pass_ctx: Incomplete
    attrs: Incomplete
    loss: Incomplete
    origin_startup_program: Incomplete
    main_program: Incomplete
    cloned_main: Incomplete
    cloned_startup: Incomplete
    use_ps_gpu: Incomplete
    use_heter_ps: Incomplete
    is_worker: Incomplete
    is_heter_worker: Incomplete
    is_server: Incomplete
    ps_mode: Incomplete
    launch_barrier: Incomplete
    launch_barrier_flag: Incomplete
    server_endpoints: Incomplete
    def __init__(self, pass_ctx) -> None: ...

class GeoPsProgramBuilder(PsProgramBuilder):
    def __init__(self, pass_ctx) -> None: ...

class NuPsProgramBuilder(PsProgramBuilder):
    def __init__(self, pass_ctx) -> None: ...

class CpuSyncPsProgramBuilder(PsProgramBuilder):
    def __init__(self, pass_ctx) -> None: ...

class CpuAsyncPsProgramBuilder(CpuSyncPsProgramBuilder):
    def __init__(self, pass_ctx) -> None: ...

class GpuPsProgramBuilder(PsProgramBuilder):
    def __init__(self, pass_ctx) -> None: ...

class HeterAsyncPsProgramBuilder(PsProgramBuilder):
    def __init__(self, pass_ctx) -> None: ...

class FlPsProgramBuilder(HeterAsyncPsProgramBuilder):
    def __init__(self, pass_ctx) -> None: ...
