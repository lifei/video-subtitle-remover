from .dataset import AudioClassificationDataset as AudioClassificationDataset
from _typeshed import Incomplete
from paddle.dataset.common import DATA_HOME as DATA_HOME
from paddle.utils import download as download
from typing import NamedTuple

class TESS(AudioClassificationDataset):
    archive: Incomplete
    label_list: Incomplete

    class meta_info(NamedTuple):
        speaker: Incomplete
        word: Incomplete
        emotion: Incomplete
    audio_path: str
    def __init__(self, mode: str = 'train', n_folds: int = 5, split: int = 1, feat_type: str = 'raw', archive: Incomplete | None = None, **kwargs) -> None: ...
