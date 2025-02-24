import abc
from .base_quanter import BaseQuanter as BaseQuanter

class BaseObserver(BaseQuanter, metaclass=abc.ABCMeta):
    def __init__(self) -> None: ...
    @abc.abstractmethod
    def cal_thresholds(self): ...
