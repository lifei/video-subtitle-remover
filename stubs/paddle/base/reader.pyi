from . import core as core
from .data_feeder import BatchedTensorProvider as BatchedTensorProvider, DataFeeder as DataFeeder
from .executor import global_scope as global_scope
from .framework import Program as Program, default_main_program as default_main_program, default_startup_program as default_startup_program, in_dygraph_mode as in_dygraph_mode, program_guard as program_guard
from .layers.io import __create_unshared_decorated_reader__ as __create_unshared_decorated_reader__, monkey_patch_reader_methods as monkey_patch_reader_methods
from .multiprocess_utils import CleanupFuncRegistrar as CleanupFuncRegistrar, multiprocess_queue_set as multiprocess_queue_set
from .unique_name import UniqueNameGenerator as UniqueNameGenerator
from _typeshed import Incomplete

QUEUE_GET_TIMEOUT: int
data_loader_unique_name_generator: Incomplete
KEEP_DATA_LOADER_ORDER: bool
USE_PINNED_MEMORY: Incomplete

def keep_data_loader_order(*args): ...
def use_pinned_memory(*args): ...

class DataLoaderBase:
    def __init__(self) -> None: ...
    def __call__(self): ...
    def __iter__(self): ...
    def __next__(self) -> None: ...

class DataLoader:
    @staticmethod
    def from_generator(feed_list: Incomplete | None = None, capacity: Incomplete | None = None, use_double_buffer: bool = True, iterable: bool = True, return_list: bool = False, use_multiprocess: bool = False, drop_last: bool = True): ...
    @staticmethod
    def from_dataset(dataset, places, drop_last: bool = True): ...

class DygraphGeneratorLoader(DataLoaderBase):
    def __init__(self, feed_list: Incomplete | None = None, capacity: Incomplete | None = None, use_double_buffer: bool = True, iterable: bool = True, return_list: bool = True, use_multiprocess: bool = False) -> None: ...
    @property
    def queue(self): ...
    @property
    def iterable(self): ...
    def __iter__(self): ...
    def __next__(self): ...
    def set_sample_generator(self, reader, batch_size, drop_last: bool = True, places: Incomplete | None = None): ...
    def set_sample_list_generator(self, reader, places: Incomplete | None = None): ...
    def set_batch_generator(self, reader, places: Incomplete | None = None): ...

class GeneratorLoader(DataLoaderBase):
    def __init__(self, feed_list: Incomplete | None = None, capacity: Incomplete | None = None, use_double_buffer: bool = True, iterable: bool = True, return_list: bool = False, drop_last: bool = True) -> None: ...
    @property
    def queue(self): ...
    @property
    def iterable(self): ...
    def __iter__(self): ...
    def __next__(self): ...
    def start(self) -> None: ...
    def reset(self) -> None: ...
    def set_sample_generator(self, reader, batch_size, drop_last: bool = True, places: Incomplete | None = None): ...
    def set_sample_list_generator(self, reader, places: Incomplete | None = None): ...
    def set_batch_generator(self, reader, places: Incomplete | None = None): ...

class PyReader(DataLoaderBase):
    def __init__(self, feed_list: Incomplete | None = None, capacity: Incomplete | None = None, use_double_buffer: bool = True, iterable: bool = True, return_list: bool = False) -> None: ...
    @property
    def queue(self): ...
    @property
    def iterable(self): ...
    def __iter__(self): ...
    def __next__(self): ...
    def start(self) -> None: ...
    def reset(self) -> None: ...
    def decorate_sample_generator(self, sample_generator, batch_size, drop_last: bool = True, places: Incomplete | None = None) -> None: ...
    def decorate_sample_list_generator(self, reader, places: Incomplete | None = None) -> None: ...
    def decorate_batch_generator(self, reader, places: Incomplete | None = None) -> None: ...

class DatasetLoader(DataLoaderBase):
    def __init__(self, dataset, places, drop_last) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...
