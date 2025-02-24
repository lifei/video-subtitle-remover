from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

DATA_URL: str
DATA_MD5: str
TOTAL_EN_WORDS: int
TOTAL_DE_WORDS: int
START_MARK: str
END_MARK: str
UNK_MARK: str

class WMT16(Dataset):
    mode: Incomplete
    data_file: Incomplete
    lang: Incomplete
    src_dict_size: Incomplete
    trg_dict_size: Incomplete
    src_dict: Incomplete
    trg_dict: Incomplete
    data: Incomplete
    def __init__(self, data_file: Incomplete | None = None, mode: str = 'train', src_dict_size: int = -1, trg_dict_size: int = -1, lang: str = 'en', download: bool = True) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
    def get_dict(self, lang, reverse: bool = False): ...
