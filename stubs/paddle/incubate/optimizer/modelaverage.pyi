from _typeshed import Incomplete
from collections.abc import Generator
from paddle.base import framework as framework
from paddle.base.framework import Program as Program
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.base.wrapped_decorator import signature_safe_contextmanager as signature_safe_contextmanager
from paddle.framework import in_dynamic_mode as in_dynamic_mode
from paddle.optimizer import Optimizer as Optimizer

class ModelAverage(Optimizer):
    helper: Incomplete
    average_window: Incomplete
    min_average_window: Incomplete
    max_average_window: Incomplete
    type: str
    apply_program: Incomplete
    restore_program: Incomplete
    def __init__(self, average_window_rate, parameters: Incomplete | None = None, min_average_window: int = 10000, max_average_window: int = 10000, name: Incomplete | None = None) -> None: ...
    def minimize(self, loss, startup_program: Incomplete | None = None, parameters: Incomplete | None = None, no_grad_set: Incomplete | None = None) -> None: ...
    def step(self) -> None: ...
    def apply(self, executor: Incomplete | None = None, need_restore: bool = True) -> Generator[None]: ...
    def restore(self, executor: Incomplete | None = None) -> None: ...
