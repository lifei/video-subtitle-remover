import abc
from ..base.data_feeder import check_variable_and_dtype as check_variable_and_dtype
from ..base.framework import in_pir_mode as in_pir_mode
from ..base.layer_helper import LayerHelper as LayerHelper
from ..framework import in_dynamic_mode as in_dynamic_mode
from _typeshed import Incomplete

class Metric(metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    @abc.abstractmethod
    def reset(self): ...
    @abc.abstractmethod
    def update(self, *args): ...
    @abc.abstractmethod
    def accumulate(self): ...
    @abc.abstractmethod
    def name(self): ...
    def compute(self, *args): ...

class Accuracy(Metric):
    topk: Incomplete
    maxk: Incomplete
    def __init__(self, topk=(1,), name: Incomplete | None = None, *args, **kwargs) -> None: ...
    def compute(self, pred, label, *args): ...
    def update(self, correct, *args): ...
    total: Incomplete
    count: Incomplete
    def reset(self) -> None: ...
    def accumulate(self): ...
    def name(self): ...

class Precision(Metric):
    tp: int
    fp: int
    def __init__(self, name: str = 'precision', *args, **kwargs) -> None: ...
    def update(self, preds, labels) -> None: ...
    def reset(self) -> None: ...
    def accumulate(self): ...
    def name(self): ...

class Recall(Metric):
    tp: int
    fn: int
    def __init__(self, name: str = 'recall', *args, **kwargs) -> None: ...
    def update(self, preds, labels) -> None: ...
    def accumulate(self): ...
    def reset(self) -> None: ...
    def name(self): ...

class Auc(Metric):
    def __init__(self, curve: str = 'ROC', num_thresholds: int = 4095, name: str = 'auc', *args, **kwargs) -> None: ...
    def update(self, preds, labels) -> None: ...
    @staticmethod
    def trapezoid_area(x1, x2, y1, y2): ...
    def accumulate(self): ...
    def reset(self) -> None: ...
    def name(self): ...

def accuracy(input, label, k: int = 1, correct: Incomplete | None = None, total: Incomplete | None = None, name: Incomplete | None = None): ...
