from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

URL: str
MD5: str
feature_names: Incomplete

class UCIHousing(Dataset):
    mode: Incomplete
    data_file: Incomplete
    dtype: Incomplete
    def __init__(self, data_file: Incomplete | None = None, mode: str = 'train', download: bool = True) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
