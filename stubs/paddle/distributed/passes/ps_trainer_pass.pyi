from ..ps.utils.public import *
from _typeshed import Incomplete
from paddle.base import framework as framework
from paddle.distributed.passes.pass_base import PassBase as PassBase, register_pass as register_pass
from paddle.framework import core as core
from paddle.static import Parameter as Parameter, Program as Program

class AppendSendOpsPass(PassBase):
    def __init__(self) -> None: ...

class DistributedOpsPass(PassBase):
    w_2_table_id: Incomplete
    emb_size: Incomplete
    def __init__(self) -> None: ...

class DeleteOptimizesPass(PassBase):
    def __init__(self) -> None: ...

class DeleteExtraOptimizerPass(PassBase):
    def __init__(self) -> None: ...

class FakeInitOpsPass(PassBase):
    def __init__(self) -> None: ...

class PsGpuPass(PassBase):
    def __init__(self) -> None: ...

class PsTranspilePass(PassBase):
    def __init__(self) -> None: ...

class SplitHeterWorkerOpsPass(PassBase):
    def __init__(self) -> None: ...

class SplitTrainerOpsPass(PassBase):
    def __init__(self) -> None: ...

class SetHeterPipelineOptPass(PassBase):
    def __init__(self) -> None: ...

class SplitFlOpsPass(PassBase):
    PART_A_DEVICE_FlAG: str
    PART_A_JOINT_OP_DEVICE_FlAG: str
    PART_B_DEVICE_FlAG: str
    PART_B_JOINT_OP_DEVICE_FlAG: str
    def __init__(self) -> None: ...
