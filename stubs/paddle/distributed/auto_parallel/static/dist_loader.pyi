import abc
from _typeshed import Incomplete
from paddle.io import BatchSampler as BatchSampler, IterableDataset as IterableDataset
from paddle.io.dataloader.batch_sampler import DistributedBatchSampler as DistributedBatchSampler
from paddle.io.dataloader.dataloader_iter import default_collate_fn as default_collate_fn, default_convert_fn as default_convert_fn

class DistributedDataLoaderBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __iter__(self): ...

class DistributedDataLoaderFromGenerator(DistributedDataLoaderBase):
    dataset: Incomplete
    feed_list: Incomplete
    capacity: Incomplete
    use_double_buffer: Incomplete
    iterable: Incomplete
    return_list: Incomplete
    use_multiprocess: Incomplete
    drop_last: Incomplete
    places: Incomplete
    batch_size: Incomplete
    epochs: Incomplete
    steps_per_epoch: Incomplete
    collate_fn: Incomplete
    split_data: Incomplete
    dp_world_sizes: Incomplete
    dp_ranks: Incomplete
    acc_steps: Incomplete
    dataset_kind: Incomplete
    batch_sampler: Incomplete
    auto_collate_batch: Incomplete
    sampler_iter: Incomplete
    dataset_fetcher: Incomplete
    def __init__(self, dataset, feed_list: Incomplete | None = None, capacity: Incomplete | None = None, use_double_buffer: bool = True, iterable: bool = True, return_list: bool = False, use_multiprocess: bool = False, drop_last: bool = True, places: Incomplete | None = None, batch_size: int = 1, epochs: int = 1, steps_per_epoch: Incomplete | None = None, collate_fn: Incomplete | None = None, split_data: bool = True, data_parallel_world_size=[], data_parallel_rank=[], acc_steps: int = 1) -> None: ...
    def __iter__(self): ...
    def __next__(self) -> None: ...
    @property
    def index_sampler(self): ...

class DistributedDataLoader(DistributedDataLoaderBase):
    dataset: Incomplete
    feed_list: Incomplete
    return_list: Incomplete
    places: Incomplete
    batch_size: Incomplete
    shuffle: Incomplete
    drop_last: Incomplete
    collate_fn: Incomplete
    num_workers: Incomplete
    use_buffer_reader: Incomplete
    use_shared_memory: Incomplete
    timeout: Incomplete
    worker_init_fn: Incomplete
    epochs: Incomplete
    steps_per_epoch: Incomplete
    dp_world_sizes: Incomplete
    dp_ranks: Incomplete
    split_data: Incomplete
    batch_sampler: Incomplete
    def __init__(self, dataset, feed_list: Incomplete | None = None, places: Incomplete | None = None, return_list: bool = True, batch_size: int = 1, shuffle: bool = False, drop_last: bool = False, collate_fn: Incomplete | None = None, num_workers: int = 0, use_buffer_reader: bool = True, use_shared_memory: bool = True, timeout: int = 0, worker_init_fn: Incomplete | None = None, epochs: int = 1, steps_per_epoch: Incomplete | None = None, split_data: bool = True, data_parallel_world_size=[], data_parallel_rank=[]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...
    def __call__(self): ...
