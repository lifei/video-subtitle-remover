import abc
from .base_quanter import BaseQuanter as BaseQuanter
from _typeshed import Incomplete
from paddle.nn import Layer as Layer

class ClassWithArguments(metaclass=abc.ABCMeta):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def args(self): ...
    @property
    def kwargs(self): ...

class QuanterFactory(ClassWithArguments, metaclass=abc.ABCMeta):
    partial_class: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
ObserverFactory = QuanterFactory

def quanter(class_name): ...
