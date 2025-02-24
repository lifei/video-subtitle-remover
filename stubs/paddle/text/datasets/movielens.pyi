from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

age_table: Incomplete
URL: str
MD5: str

class MovieInfo:
    index: Incomplete
    categories: Incomplete
    title: Incomplete
    def __init__(self, index, categories, title) -> None: ...
    def value(self, categories_dict, movie_title_dict): ...

class UserInfo:
    index: Incomplete
    is_male: Incomplete
    age: Incomplete
    job_id: Incomplete
    def __init__(self, index, gender, age, job_id) -> None: ...
    def value(self): ...

class Movielens(Dataset):
    mode: Incomplete
    data_file: Incomplete
    test_ratio: Incomplete
    rand_seed: Incomplete
    def __init__(self, data_file: Incomplete | None = None, mode: str = 'train', test_ratio: float = 0.1, rand_seed: int = 0, download: bool = True) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
