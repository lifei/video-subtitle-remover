from .dataset import IterableDataset as IterableDataset
from .sampler import RandomSampler as RandomSampler, Sampler as Sampler, SequenceSampler as SequenceSampler
from _typeshed import Incomplete

class BatchSampler(Sampler):
    sampler: Incomplete
    batch_size: Incomplete
    drop_last: Incomplete
    def __init__(self, dataset: Incomplete | None = None, sampler: Incomplete | None = None, shuffle: bool = False, batch_size: int = 1, drop_last: bool = False) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...

class _InfiniteIterableSampler:
    dataset: Incomplete
    batch_size: Incomplete
    def __init__(self, dataset, batch_size: int = 1) -> None: ...
    def __iter__(self): ...

class DistributedBatchSampler(BatchSampler):
    dataset: Incomplete
    batch_size: Incomplete
    shuffle: Incomplete
    nranks: Incomplete
    local_rank: Incomplete
    drop_last: Incomplete
    epoch: int
    num_samples: Incomplete
    total_size: Incomplete
    def __init__(self, dataset, batch_size, num_replicas: Incomplete | None = None, rank: Incomplete | None = None, shuffle: bool = False, drop_last: bool = False) -> None: ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def set_epoch(self, epoch) -> None: ...
