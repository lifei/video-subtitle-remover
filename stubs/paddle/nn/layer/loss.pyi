from .layers import Layer as Layer
from _typeshed import Incomplete
from paddle import base as base, in_dynamic_mode as in_dynamic_mode
from paddle.base.framework import in_dynamic_or_pir_mode as in_dynamic_or_pir_mode

class BCEWithLogitsLoss(Layer):
    weight: Incomplete
    reduction: Incomplete
    pos_weight: Incomplete
    name: Incomplete
    def __init__(self, weight: Incomplete | None = None, reduction: str = 'mean', pos_weight: Incomplete | None = None, name: Incomplete | None = None) -> None: ...
    def forward(self, logit, label): ...

class CrossEntropyLoss(Layer):
    weight: Incomplete
    reduction: Incomplete
    ignore_index: Incomplete
    soft_label: Incomplete
    axis: Incomplete
    use_softmax: Incomplete
    label_smoothing: Incomplete
    name: Incomplete
    def __init__(self, weight: Incomplete | None = None, ignore_index: int = -100, reduction: str = 'mean', soft_label: bool = False, axis: int = -1, use_softmax: bool = True, label_smoothing: float = 0.0, name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class HSigmoidLoss(Layer):
    weight: Incomplete
    bias: Incomplete
    def __init__(self, feature_size, num_classes, weight_attr: Incomplete | None = None, bias_attr: Incomplete | None = None, is_custom: bool = False, is_sparse: bool = False, name: Incomplete | None = None) -> None: ...
    def forward(self, input, label, path_table: Incomplete | None = None, path_code: Incomplete | None = None): ...

class MSELoss(Layer):
    reduction: Incomplete
    def __init__(self, reduction: str = 'mean') -> None: ...
    def forward(self, input, label): ...

class L1Loss(Layer):
    reduction: Incomplete
    name: Incomplete
    def __init__(self, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class BCELoss(Layer):
    weight: Incomplete
    reduction: Incomplete
    name: Incomplete
    def __init__(self, weight: Incomplete | None = None, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class NLLLoss(Layer):
    def __init__(self, weight: Incomplete | None = None, ignore_index: int = -100, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class PoissonNLLLoss(Layer):
    def __init__(self, log_input: bool = True, full: bool = False, epsilon: float = 1e-08, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class KLDivLoss(Layer):
    reduction: Incomplete
    def __init__(self, reduction: str = 'mean') -> None: ...
    def forward(self, input, label): ...

class MarginRankingLoss(Layer):
    margin: Incomplete
    reduction: Incomplete
    name: Incomplete
    def __init__(self, margin: float = 0.0, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, other, label): ...

class CTCLoss(Layer):
    blank: Incomplete
    reduction: Incomplete
    def __init__(self, blank: int = 0, reduction: str = 'mean') -> None: ...
    def forward(self, log_probs, labels, input_lengths, label_lengths, norm_by_times: bool = False): ...

class RNNTLoss(Layer):
    blank: Incomplete
    reduction: Incomplete
    fastemit_lambda: Incomplete
    name: Incomplete
    def __init__(self, blank: int = 0, fastemit_lambda: float = 0.001, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label, input_lengths, label_lengths): ...

class SmoothL1Loss(Layer):
    reduction: Incomplete
    delta: Incomplete
    name: Incomplete
    def __init__(self, reduction: str = 'mean', delta: float = 1.0, name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class MultiLabelSoftMarginLoss(Layer):
    weight: Incomplete
    reduction: Incomplete
    name: Incomplete
    def __init__(self, weight: Incomplete | None = None, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class HingeEmbeddingLoss(Layer):
    margin: Incomplete
    reduction: Incomplete
    name: Incomplete
    def __init__(self, margin: float = 1.0, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class CosineEmbeddingLoss(Layer):
    margin: Incomplete
    reduction: Incomplete
    name: Incomplete
    def __init__(self, margin: int = 0, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input1, input2, label): ...

class TripletMarginWithDistanceLoss(Layer):
    margin: Incomplete
    swap: Incomplete
    reduction: Incomplete
    distance_function: Incomplete
    name: Incomplete
    def __init__(self, distance_function: Incomplete | None = None, margin: float = 1.0, swap: bool = False, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, positive, negative): ...

class TripletMarginLoss(Layer):
    margin: Incomplete
    p: Incomplete
    epsilon: Incomplete
    swap: Incomplete
    reduction: Incomplete
    name: Incomplete
    def __init__(self, margin: float = 1.0, p: float = 2.0, epsilon: float = 1e-06, swap: bool = False, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, positive, negative): ...

class MultiMarginLoss(Layer):
    p: Incomplete
    margin: Incomplete
    weight: Incomplete
    reduction: Incomplete
    name: Incomplete
    def __init__(self, p: int = 1, margin: float = 1.0, weight: Incomplete | None = None, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class SoftMarginLoss(Layer):
    reduction: Incomplete
    name: Incomplete
    def __init__(self, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label): ...

class GaussianNLLLoss(Layer):
    full: Incomplete
    epsilon: Incomplete
    reduction: Incomplete
    name: Incomplete
    def __init__(self, full: bool = False, epsilon: float = 1e-06, reduction: str = 'mean', name: Incomplete | None = None) -> None: ...
    def forward(self, input, label, variance): ...
