from _typeshed import Incomplete

SUPPORT_WEIGHT_QUANTIZATION_OP_DICT: Incomplete
SUPPORT_ACT_QUANTIZATION_OP_DICT: Incomplete
SUPPORT_QUANTIZATION_OP_DICT: Incomplete

class BaseQuantizer:
    def __init__(self, quantizable_op_type=[], quant_bits: int = 8) -> None: ...
    @property
    def weight_quant_operation_types(self): ...
    @property
    def activation_quant_operation_types(self): ...
    @property
    def observer_operation_types(self): ...

class TensorRTQuantizer(BaseQuantizer):
    def __init__(self, quantizable_op_type=[], quant_bits: int = 8) -> None: ...
    @property
    def activation_quant_operation_types(self): ...

class MKLDNNQuantizer(BaseQuantizer):
    def __init__(self, quantizable_op_type=[], quant_bits: int = 8) -> None: ...
    @property
    def activation_quant_operation_types(self): ...

class ARMCPUQuantizer(BaseQuantizer):
    def __init__(self, quantizable_op_type=[], quant_bits: int = 8) -> None: ...
