from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

URL_PREFIX: str
CIFAR10_URL: Incomplete
CIFAR10_MD5: str
CIFAR100_URL: Incomplete
CIFAR100_MD5: str
MODE_FLAG_MAP: Incomplete

class Cifar10(Dataset):
    mode: Incomplete
    backend: Incomplete
    data_file: Incomplete
    transform: Incomplete
    dtype: Incomplete
    def __init__(self, data_file: Incomplete | None = None, mode: str = 'train', transform: Incomplete | None = None, download: bool = True, backend: Incomplete | None = None) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...

class Cifar100(Cifar10):
    def __init__(self, data_file: Incomplete | None = None, mode: str = 'train', transform: Incomplete | None = None, download: bool = True, backend: Incomplete | None = None) -> None: ...
