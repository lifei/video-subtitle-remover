from ..layer.common import Linear as Linear
from ..layer.conv import Conv1DTranspose as Conv1DTranspose, Conv2DTranspose as Conv2DTranspose, Conv3DTranspose as Conv3DTranspose
from _typeshed import Incomplete

def normal_(x, mean: float = 0.0, std: float = 1.0): ...

class SpectralNorm:
    name: Incomplete
    dim: Incomplete
    n_power_iterations: Incomplete
    eps: Incomplete
    def __init__(self, name: str = 'weight', n_power_iterations: int = 1, dim: int = 0, eps: float = 1e-12) -> None: ...
    def reshape_weight_to_matrix(self, weight): ...
    def compute_weight(self, layer, do_power_iteration): ...
    def __call__(self, layer, inputs) -> None: ...
    @staticmethod
    def apply(layer, name, n_power_iterations, dim, eps): ...

def spectral_norm(layer, name: str = 'weight', n_power_iterations: int = 1, eps: float = 1e-12, dim: Incomplete | None = None): ...
