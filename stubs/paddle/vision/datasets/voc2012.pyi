from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

VOC_URL: str
VOC_MD5: str
SET_FILE: str
DATA_FILE: str
LABEL_FILE: str
CACHE_DIR: str
MODE_FLAG_MAP: Incomplete

class VOC2012(Dataset):
    backend: Incomplete
    flag: Incomplete
    data_file: Incomplete
    transform: Incomplete
    dtype: Incomplete
    def __init__(self, data_file: Incomplete | None = None, mode: str = 'train', transform: Incomplete | None = None, download: bool = True, backend: Incomplete | None = None) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
    def __del__(self) -> None: ...
