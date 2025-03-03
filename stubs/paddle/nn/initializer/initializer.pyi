from ...base.framework import default_main_program as default_main_program, in_dygraph_mode as in_dygraph_mode
from .lazy_init import lazy_init_helper as lazy_init_helper
from _typeshed import Incomplete

class Initializer:
    def __init__(self) -> None: ...
    def __call__(self, param, block: Incomplete | None = None): ...
    def forward(self, param, block: Incomplete | None = None) -> None: ...

def calculate_gain(nonlinearity, param: Incomplete | None = None): ...
