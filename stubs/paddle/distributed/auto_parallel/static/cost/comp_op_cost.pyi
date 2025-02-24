from .base_cost import CompOpCost as CompOpCost, register_op_cost as register_op_cost
from _typeshed import Incomplete

class AdamOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ArgsortOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class AssignOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class AssignValueOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class BeamSearchOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class BeamSearchDecodeOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class CastOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ConcatOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class DropoutOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class DropoutGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ElementwiseAddOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ElementwiseAddGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ElementwiseDivOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ElementwiseDivGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ElementwiseMulOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ElementwiseMulGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ElementwiseSubOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ElementwiseSubGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class EqualOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class EmbeddingOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class EmbeddingGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class FillConstantOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class FillConstantBatchSizeLikeOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class FusedSoftmaxMaskUpperTriangleOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class FusedSoftmaxMaskUpperTriangleGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class GatherOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class GeluOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class GeluGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class GreaterEqualOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class IncrementOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class IsEmptyOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LayerNormOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LayerNormGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LessThanOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LogicalNotOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LogicalAndOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LodResetOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LogOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LookupTableV2OpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class LookupTableV2GradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class MatmulOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class MatmulGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class MatmulV2OpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class MatmulV2GradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class MemcpyOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class MulOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class MulGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class OneHotOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ReadFromArrayOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ReduceSumOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ReduceSumGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class Reshape2OpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class Reshape2GradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ReduceMeanOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ReduceMeanGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SamplingIdOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ScaleOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class ShapeOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SliceOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SoftmaxOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SoftmaxGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SoftmaxWithCrossEntropyOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SoftmaxWithCrossEntropyGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SplitOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class Squeeze2OpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SquareOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SquareGradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class SumOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class TopKOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class Transpose2OpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class Transpose2GradOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class Unsqueeze2OpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...

class WriteToArrayOpCost(CompOpCost):
    OP_TYPE: str
    def __init__(self, op: Incomplete | None = None, op_desc: Incomplete | None = None, cluster: Incomplete | None = None) -> None: ...
