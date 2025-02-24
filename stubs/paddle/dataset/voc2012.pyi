from paddle.dataset.common import download as download
from paddle.utils import deprecated as deprecated

VOC_URL: str
VOC_MD5: str
SET_FILE: str
DATA_FILE: str
LABEL_FILE: str
CACHE_DIR: str

def reader_creator(filename, sub_name): ...
def train(): ...
def test(): ...
def val(): ...
