from .streams import Event as Event, Stream as Stream
from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ['Stream', 'Event', 'current_stream', 'synchronize', 'device_count', 'empty_cache', 'max_memory_allocated', 'max_memory_reserved', 'memory_allocated', 'memory_reserved', 'stream_guard', 'get_device_properties', 'get_device_name', 'get_device_capability']

def current_stream(device: Incomplete | None = None): ...
def synchronize(device: Incomplete | None = None): ...
def device_count(): ...
def empty_cache() -> None: ...
def max_memory_allocated(device: Incomplete | None = None): ...
def max_memory_reserved(device: Incomplete | None = None): ...
def memory_allocated(device: Incomplete | None = None): ...
def memory_reserved(device: Incomplete | None = None): ...
def stream_guard(stream) -> Generator[None]: ...
def get_device_properties(device: Incomplete | None = None): ...
def get_device_name(device: Incomplete | None = None): ...
def get_device_capability(device: Incomplete | None = None): ...
