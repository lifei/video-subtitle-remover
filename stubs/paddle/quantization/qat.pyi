from .config import QuantConfig as QuantConfig
from .quantize import Quantization as Quantization
from paddle.nn import Layer as Layer

class QAT(Quantization):
    def __init__(self, config: QuantConfig) -> None: ...
    def quantize(self, model: Layer, inplace: bool = False): ...
