import abc
from .base_quanter import BaseQuanter as BaseQuanter
from .config import QuantConfig as QuantConfig
from paddle.nn import Layer as Layer
from paddle.nn.quant.format import ConvertibleQuantedLayer as ConvertibleQuantedLayer, LinearQuanterDequanter as LinearQuanterDequanter

class Quantization(metaclass=abc.ABCMeta):
    def __init__(self, config: QuantConfig) -> None: ...
    @abc.abstractmethod
    def quantize(self, model: Layer, inplace: bool = False): ...
    def convert(self, model: Layer, inplace: bool = False, remain_weight: bool = False): ...
