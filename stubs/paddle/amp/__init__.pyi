from .auto_cast import auto_cast as auto_cast, decorate as decorate
from .grad_scaler import GradScaler as GradScaler
from _typeshed import Incomplete

__all__ = ['auto_cast', 'GradScaler', 'decorate', 'is_float16_supported', 'is_bfloat16_supported']

def is_float16_supported(device: Incomplete | None = None): ...
def is_bfloat16_supported(device: Incomplete | None = None): ...
