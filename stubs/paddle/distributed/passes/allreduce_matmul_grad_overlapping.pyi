from .pass_base import PassBase as PassBase, register_pass as register_pass
from .pass_utils import AutoParallelStreamType as AutoParallelStreamType

class AllreduceMatmulGradOverlappingPass(PassBase):
    def __init__(self) -> None: ...
