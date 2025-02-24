from _typeshed import Incomplete
from paddle.utils import deprecated as deprecated

URL_PREFIX: str
TEST_IMAGE_URL: Incomplete
TEST_IMAGE_MD5: str
TEST_LABEL_URL: Incomplete
TEST_LABEL_MD5: str
TRAIN_IMAGE_URL: Incomplete
TRAIN_IMAGE_MD5: str
TRAIN_LABEL_URL: Incomplete
TRAIN_LABEL_MD5: str

def reader_creator(image_filename, label_filename, buffer_size): ...
def train(): ...
def test(): ...
def fetch() -> None: ...
