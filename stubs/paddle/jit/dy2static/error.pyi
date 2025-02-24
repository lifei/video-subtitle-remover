from .origin_info import Location as Location, OriginInfo as OriginInfo, global_origin_info_map as global_origin_info_map
from .utils import RE_PYMODULE as RE_PYMODULE
from _typeshed import Incomplete

ERROR_DATA: str
SIMPLIFY_ERROR_ENV_NAME: str
DEFAULT_SIMPLIFY_NEW_ERROR: int
DISABLE_ERROR_ENV_NAME: str
DEFAULT_DISABLE_NEW_ERROR: int
SOURCE_CODE_RANGE: int
BLANK_COUNT_BEFORE_FILE_STR: int

def attach_error_data(error, in_runtime: bool = False): ...

class TraceBackFrame(OriginInfo):
    location: Incomplete
    function_name: Incomplete
    source_code: Incomplete
    error_line: str
    def __init__(self, location, function_name, source_code) -> None: ...
    def formated_message(self): ...

class TraceBackFrameRange(OriginInfo):
    location: Incomplete
    function_name: Incomplete
    source_code: Incomplete
    error_line: str
    def __init__(self, location, function_name) -> None: ...
    def formated_message(self): ...

class SuggestionDict:
    suggestion_dict: Incomplete
    def __init__(self) -> None: ...
    def keys(self): ...
    def __getitem__(self, key): ...

class Dy2StKeyError(Exception): ...

class ErrorData:
    error_type: Incomplete
    error_value: Incomplete
    origin_traceback: Incomplete
    origin_info_map: Incomplete
    in_runtime: bool
    suggestion_dict: Incomplete
    def __init__(self, error_type, error_value, origin_traceback, origin_info_map) -> None: ...
    def create_exception(self): ...
    def numpy_api_check(self, format_exception, error_line): ...
    def create_message(self): ...
    def raise_new_exception(self) -> None: ...
