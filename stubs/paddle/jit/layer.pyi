from _typeshed import Incomplete
from paddle.base import core as core
from paddle.base.core import Load as Load

class Layer:
    cpp_layer: Incomplete
    functions: Incomplete
    def __init__(self) -> None: ...
    def load(self, load_path, place) -> None: ...

class Function:
    function: Incomplete
    info: Incomplete
    def __init__(self, function, info) -> None: ...
    def __call__(self, *args): ...

class FunctionInfo:
    info: Incomplete
    def __init__(self, info) -> None: ...
    def name(self): ...
