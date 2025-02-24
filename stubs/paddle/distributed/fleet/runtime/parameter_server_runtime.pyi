from ..base.private_helper_function import wait_server_ready as wait_server_ready
from .runtime_base import RuntimeBase as RuntimeBase
from paddle.framework import core as core
from paddle.static import CompiledProgram as CompiledProgram, Executor as Executor, Program as Program, Variable as Variable, default_main_program as default_main_program, default_startup_program as default_startup_program

class ParameterServerRuntime(RuntimeBase):
    def __init__(self) -> None: ...
    def build_compiled_startegy(self): ...
