from .dataset import AudioClassificationDataset as AudioClassificationDataset
from _typeshed import Incomplete
from paddle.dataset.common import DATA_HOME as DATA_HOME
from paddle.utils import download as download
from typing import NamedTuple

class ESC50(AudioClassificationDataset):
    archive: Incomplete
    label_list: Incomplete
    meta: Incomplete

    class meta_info(NamedTuple):
        filename: Incomplete
        fold: Incomplete
        target: Incomplete
        category: Incomplete
        esc10: Incomplete
        src_file: Incomplete
        take: Incomplete
    audio_path: Incomplete
    def __init__(self, mode: str = 'train', split: int = 1, feat_type: str = 'raw', archive: Incomplete | None = None, **kwargs) -> None: ...
