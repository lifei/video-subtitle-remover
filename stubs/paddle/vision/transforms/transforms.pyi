from _typeshed import Incomplete

class Compose:
    transforms: Incomplete
    def __init__(self, transforms) -> None: ...
    def __call__(self, data): ...

class BaseTransform:
    keys: Incomplete
    params: Incomplete
    def __init__(self, keys: Incomplete | None = None) -> None: ...
    def __call__(self, inputs): ...

class ToTensor(BaseTransform):
    data_format: Incomplete
    def __init__(self, data_format: str = 'CHW', keys: Incomplete | None = None) -> None: ...

class Resize(BaseTransform):
    size: Incomplete
    interpolation: Incomplete
    def __init__(self, size, interpolation: str = 'bilinear', keys: Incomplete | None = None) -> None: ...

class RandomResizedCrop(BaseTransform):
    size: Incomplete
    scale: Incomplete
    ratio: Incomplete
    interpolation: Incomplete
    def __init__(self, size, scale=(0.08, 1.0), ratio=..., interpolation: str = 'bilinear', keys: Incomplete | None = None) -> None: ...

class CenterCrop(BaseTransform):
    size: Incomplete
    def __init__(self, size, keys: Incomplete | None = None) -> None: ...

class RandomHorizontalFlip(BaseTransform):
    prob: Incomplete
    def __init__(self, prob: float = 0.5, keys: Incomplete | None = None) -> None: ...

class RandomVerticalFlip(BaseTransform):
    prob: Incomplete
    def __init__(self, prob: float = 0.5, keys: Incomplete | None = None) -> None: ...

class Normalize(BaseTransform):
    mean: Incomplete
    std: Incomplete
    data_format: Incomplete
    to_rgb: Incomplete
    def __init__(self, mean: float = 0.0, std: float = 1.0, data_format: str = 'CHW', to_rgb: bool = False, keys: Incomplete | None = None) -> None: ...

class Transpose(BaseTransform):
    order: Incomplete
    def __init__(self, order=(2, 0, 1), keys: Incomplete | None = None) -> None: ...

class BrightnessTransform(BaseTransform):
    value: Incomplete
    def __init__(self, value, keys: Incomplete | None = None) -> None: ...

class ContrastTransform(BaseTransform):
    value: Incomplete
    def __init__(self, value, keys: Incomplete | None = None) -> None: ...

class SaturationTransform(BaseTransform):
    value: Incomplete
    def __init__(self, value, keys: Incomplete | None = None) -> None: ...

class HueTransform(BaseTransform):
    value: Incomplete
    def __init__(self, value, keys: Incomplete | None = None) -> None: ...

class ColorJitter(BaseTransform):
    brightness: Incomplete
    contrast: Incomplete
    saturation: Incomplete
    hue: Incomplete
    def __init__(self, brightness: int = 0, contrast: int = 0, saturation: int = 0, hue: int = 0, keys: Incomplete | None = None) -> None: ...

class RandomCrop(BaseTransform):
    size: Incomplete
    padding: Incomplete
    pad_if_needed: Incomplete
    fill: Incomplete
    padding_mode: Incomplete
    def __init__(self, size, padding: Incomplete | None = None, pad_if_needed: bool = False, fill: int = 0, padding_mode: str = 'constant', keys: Incomplete | None = None) -> None: ...

class Pad(BaseTransform):
    padding: Incomplete
    fill: Incomplete
    padding_mode: Incomplete
    def __init__(self, padding, fill: int = 0, padding_mode: str = 'constant', keys: Incomplete | None = None) -> None: ...

class RandomAffine(BaseTransform):
    degrees: Incomplete
    interpolation: Incomplete
    translate: Incomplete
    scale: Incomplete
    shear: Incomplete
    fill: Incomplete
    center: Incomplete
    def __init__(self, degrees, translate: Incomplete | None = None, scale: Incomplete | None = None, shear: Incomplete | None = None, interpolation: str = 'nearest', fill: int = 0, center: Incomplete | None = None, keys: Incomplete | None = None) -> None: ...

class RandomRotation(BaseTransform):
    degrees: Incomplete
    interpolation: Incomplete
    expand: Incomplete
    center: Incomplete
    fill: Incomplete
    def __init__(self, degrees, interpolation: str = 'nearest', expand: bool = False, center: Incomplete | None = None, fill: int = 0, keys: Incomplete | None = None) -> None: ...

class RandomPerspective(BaseTransform):
    prob: Incomplete
    distortion_scale: Incomplete
    interpolation: Incomplete
    fill: Incomplete
    def __init__(self, prob: float = 0.5, distortion_scale: float = 0.5, interpolation: str = 'nearest', fill: int = 0, keys: Incomplete | None = None) -> None: ...
    def get_params(self, width, height, distortion_scale): ...

class Grayscale(BaseTransform):
    num_output_channels: Incomplete
    def __init__(self, num_output_channels: int = 1, keys: Incomplete | None = None) -> None: ...

class RandomErasing(BaseTransform):
    prob: Incomplete
    scale: Incomplete
    ratio: Incomplete
    value: Incomplete
    inplace: Incomplete
    def __init__(self, prob: float = 0.5, scale=(0.02, 0.33), ratio=(0.3, 3.3), value: int = 0, inplace: bool = False, keys: Incomplete | None = None) -> None: ...
