from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

URL_DEV_TEST: str
MD5_DEV_TEST: str
URL_TRAIN: str
MD5_TRAIN: str
START: str
END: str
UNK: str
UNK_IDX: int

class WMT14(Dataset):
    mode: Incomplete
    data_file: Incomplete
    dict_size: Incomplete
    def __init__(self, data_file: Incomplete | None = None, mode: str = 'train', dict_size: int = -1, download: bool = True) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
    def get_dict(self, reverse: bool = False): ...
