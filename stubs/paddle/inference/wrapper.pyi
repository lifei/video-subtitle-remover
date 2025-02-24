from _typeshed import Incomplete
from paddle.base import core as core
from paddle.base.core import AnalysisConfig as AnalysisConfig, PaddleDType as PaddleDType, PaddleInferPredictor as PaddleInferPredictor, PaddleInferTensor as PaddleInferTensor, PaddlePlace as PaddlePlace, convert_to_mixed_precision_bind as convert_to_mixed_precision_bind
from paddle.base.log_helper import get_logger as get_logger

DataType = PaddleDType
PlaceType = PaddlePlace
PrecisionType: Incomplete
Config = AnalysisConfig
Tensor = PaddleInferTensor
Predictor = PaddleInferPredictor

def tensor_copy_from_cpu(self, data) -> None: ...
def tensor_share_external_data(self, data) -> None: ...
def convert_to_mixed_precision(model_file: str, params_file: str, mixed_model_file: str, mixed_params_file: str, mixed_precision: PrecisionType, backend: PlaceType, keep_io_types: bool = True, black_list: set[str] = ..., **kwargs): ...
