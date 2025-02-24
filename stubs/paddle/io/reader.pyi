from ..framework import core as core, in_dynamic_mode as in_dynamic_mode
from .dataloader import BatchSampler as BatchSampler, IterableDataset as IterableDataset, Subset as Subset
from _typeshed import Incomplete

QUEUE_GET_TIMEOUT: int
USE_PINNED_MEMORY: Incomplete
USE_AUTOTUNE: bool
TUNING_STEPS: int

def set_autotune_config(use_autotune, tuning_steps: int = 500) -> None: ...
def use_pinned_memory(*args): ...

class AuToTune:
    loader: Incomplete
    max_num_worker: Incomplete
    def __init__(self, loader) -> None: ...
    def __call__(self): ...
    def need_autotune(self): ...
    def get_sub_dataset(self, dataset, batch_size): ...
    def get_autotune_loader(self): ...
    def evaluate_reader_cost(self, reader): ...
    def is_best(self, reader, best_workers, best_time, num_work_boundary): ...

class DataLoader:
    return_list: Incomplete
    collate_fn: Incomplete
    use_buffer_reader: Incomplete
    prefetch_factor: Incomplete
    worker_init_fn: Incomplete
    dataset: Incomplete
    feed_list: Incomplete
    places: Incomplete
    num_workers: Incomplete
    use_shared_memory: Incomplete
    timeout: Incomplete
    dataset_kind: Incomplete
    batch_sampler: Incomplete
    batch_size: Incomplete
    drop_last: Incomplete
    auto_collate_batch: Incomplete
    pin_memory: bool
    def __init__(self, dataset, feed_list: Incomplete | None = None, places: Incomplete | None = None, return_list: bool = True, batch_sampler: Incomplete | None = None, batch_size: int = 1, shuffle: bool = False, drop_last: bool = False, collate_fn: Incomplete | None = None, num_workers: int = 0, use_buffer_reader: bool = True, prefetch_factor: int = 2, use_shared_memory: bool = True, timeout: int = 0, worker_init_fn: Incomplete | None = None, persistent_workers: bool = False) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __call__(self): ...
