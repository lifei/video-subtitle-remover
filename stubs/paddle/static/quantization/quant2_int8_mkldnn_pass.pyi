from ...base.framework import IrGraph as IrGraph
from ...framework import core as core
from _typeshed import Incomplete

OpRole: Incomplete

class Quant2Int8MkldnnPass:
    def __init__(self, _ops_to_quantize, _op_ids_to_skip: Incomplete | None = None, _scope: Incomplete | None = None, _place: Incomplete | None = None, _core: Incomplete | None = None, _debug: bool = False) -> None: ...
    def apply(self, graph): ...
    def prepare_and_optimize_fp32(self, graph): ...
