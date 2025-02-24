from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

URL: str
MD5: str

class Imdb(Dataset):
    mode: Incomplete
    data_file: Incomplete
    word_idx: Incomplete
    def __init__(self, data_file: Incomplete | None = None, mode: str = 'train', cutoff: int = 150, download: bool = True) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
