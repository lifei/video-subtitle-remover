from .wrapped_decorator import signature_safe_contextmanager as signature_safe_contextmanager
from _typeshed import Incomplete
from collections.abc import Generator

class UniqueNameGenerator:
    ids: Incomplete
    prefix: Incomplete
    def __init__(self, prefix: Incomplete | None = None) -> None: ...
    def __call__(self, key): ...

class DygraphParameterNameChecker:
    def __init__(self) -> None: ...
    def __call__(self, name): ...

dygraph_parameter_name_checker: Incomplete
generator: Incomplete

def generate(key): ...
def generate_with_ignorable_key(key): ...
def switch(new_generator: Incomplete | None = None, new_para_name_checker: Incomplete | None = None): ...
def guard(new_generator: Incomplete | None = None) -> Generator[None]: ...
