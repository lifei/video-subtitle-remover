from .common import download as download
from _typeshed import Incomplete
from paddle.dataset.image import load_image_bytes as load_image_bytes, simple_transform as simple_transform
from paddle.reader import map_readers as map_readers, xmap_readers as xmap_readers
from paddle.utils import deprecated as deprecated, try_import as try_import

DATA_URL: str
LABEL_URL: str
SETID_URL: str
DATA_MD5: str
LABEL_MD5: str
SETID_MD5: str
TRAIN_FLAG: str
TEST_FLAG: str
VALID_FLAG: str

def default_mapper(is_train, sample): ...

train_mapper: Incomplete
test_mapper: Incomplete

def reader_creator(data_file, label_file, setid_file, dataset_name, mapper, buffered_size: int = 1024, use_xmap: bool = True, cycle: bool = False): ...
def train(mapper=..., buffered_size: int = 1024, use_xmap: bool = True, cycle: bool = False): ...
def test(mapper=..., buffered_size: int = 1024, use_xmap: bool = True, cycle: bool = False): ...
def valid(mapper=..., buffered_size: int = 1024, use_xmap: bool = True): ...
def fetch() -> None: ...
