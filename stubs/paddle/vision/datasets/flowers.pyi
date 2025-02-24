from _typeshed import Incomplete
from paddle.io import Dataset as Dataset
from paddle.utils import try_import as try_import

DATA_URL: str
LABEL_URL: str
SETID_URL: str
DATA_MD5: str
LABEL_MD5: str
SETID_MD5: str
MODE_FLAG_MAP: Incomplete

class Flowers(Dataset):
    backend: Incomplete
    transform: Incomplete
    data_path: Incomplete
    labels: Incomplete
    indexes: Incomplete
    def __init__(self, data_file: Incomplete | None = None, label_file: Incomplete | None = None, setid_file: Incomplete | None = None, mode: str = 'train', transform: Incomplete | None = None, download: bool = True, backend: Incomplete | None = None) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
