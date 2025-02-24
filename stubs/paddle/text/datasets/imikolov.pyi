from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

URL: str
MD5: str

class Imikolov(Dataset):
    data_type: Incomplete
    mode: Incomplete
    window_size: Incomplete
    min_word_freq: Incomplete
    data_file: Incomplete
    word_idx: Incomplete
    def __init__(self, data_file: Incomplete | None = None, data_type: str = 'NGRAM', window_size: int = -1, mode: str = 'train', min_word_freq: int = 50, download: bool = True) -> None: ...
    def word_count(self, f, word_freq: Incomplete | None = None): ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
