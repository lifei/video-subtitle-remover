from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

DATA_URL: str
DATA_MD5: str
WORDDICT_URL: str
WORDDICT_MD5: str
VERBDICT_URL: str
VERBDICT_MD5: str
TRGDICT_URL: str
TRGDICT_MD5: str
EMB_URL: str
EMB_MD5: str
UNK_IDX: int

class Conll05st(Dataset):
    data_file: Incomplete
    word_dict_file: Incomplete
    verb_dict_file: Incomplete
    target_dict_file: Incomplete
    emb_file: Incomplete
    word_dict: Incomplete
    predicate_dict: Incomplete
    label_dict: Incomplete
    def __init__(self, data_file: Incomplete | None = None, word_dict_file: Incomplete | None = None, verb_dict_file: Incomplete | None = None, target_dict_file: Incomplete | None = None, emb_file: Incomplete | None = None, download: bool = True) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...
    def get_dict(self): ...
    def get_embedding(self): ...
