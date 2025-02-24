from .device_worker import DownpourLite as DownpourLite, DownpourSGD as DownpourSGD, DownpourSGDOPT as DownpourSGDOPT, HeterSection as HeterSection, Hogwild as Hogwild, Section as Section
from .framework import Variable as Variable
from .trainer_desc import DistMultiTrainer as DistMultiTrainer, HeterPipelineTrainer as HeterPipelineTrainer, HeterXpuTrainer as HeterXpuTrainer, MultiTrainer as MultiTrainer, PSGPUTrainer as PSGPUTrainer, PipelineTrainer as PipelineTrainer
from _typeshed import Incomplete
from paddle.base.log_helper import get_logger as get_logger

local_logger: Incomplete

class TrainerFactory:
    def __init__(self) -> None: ...

class FetchHandlerMonitor:
    fetch_instance: Incomplete
    fetch_thread: Incomplete
    running_lock: Incomplete
    running: bool
    def __init__(self, scope, handler) -> None: ...
    def handler_launch_func(self, scope, handler) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
