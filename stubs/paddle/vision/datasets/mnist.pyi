from _typeshed import Incomplete
from paddle.io import Dataset as Dataset

class MNIST(Dataset):
    NAME: str
    URL_PREFIX: str
    TEST_IMAGE_URL: Incomplete
    TEST_IMAGE_MD5: str
    TEST_LABEL_URL: Incomplete
    TEST_LABEL_MD5: str
    TRAIN_IMAGE_URL: Incomplete
    TRAIN_IMAGE_MD5: str
    TRAIN_LABEL_URL: Incomplete
    TRAIN_LABEL_MD5: str
    backend: Incomplete
    mode: Incomplete
    image_path: Incomplete
    label_path: Incomplete
    transform: Incomplete
    dtype: Incomplete
    def __init__(self, image_path: Incomplete | None = None, label_path: Incomplete | None = None, mode: str = 'train', transform: Incomplete | None = None, download: bool = True, backend: Incomplete | None = None) -> None: ...
    def __getitem__(self, idx): ...
    def __len__(self) -> int: ...

class FashionMNIST(MNIST):
    NAME: str
    URL_PREFIX: str
    TEST_IMAGE_URL: Incomplete
    TEST_IMAGE_MD5: str
    TEST_LABEL_URL: Incomplete
    TEST_LABEL_MD5: str
    TRAIN_IMAGE_URL: Incomplete
    TRAIN_IMAGE_MD5: str
    TRAIN_LABEL_URL: Incomplete
    TRAIN_LABEL_MD5: str
