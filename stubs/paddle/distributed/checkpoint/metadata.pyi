from dataclasses import dataclass

@dataclass
class LocalTensorMetadata:
    global_offset: tuple[int]
    local_shape: tuple[int]

@dataclass(frozen=True)
class LocalTensorIndex:
    tensor_key: str
    global_offset: tuple[int]

@dataclass
class Metadata:
    state_dict_metadata: dict[str, list[LocalTensorMetadata]] = ...
    storage_metadata: dict[LocalTensorIndex, str] = ...
