import dataclasses
from ...utils import InnerError as InnerError, OrderedSet as OrderedSet
from .instruction_utils import Instruction as Instruction
from .opcode_info import ALL_JUMP as ALL_JUMP, HAS_FREE as HAS_FREE, HAS_LOCAL as HAS_LOCAL, UNCONDITIONAL_JUMP as UNCONDITIONAL_JUMP
from enum import Enum

@dataclasses.dataclass
class State:
    reads: OrderedSet[str]
    writes: OrderedSet[str]
    visited: OrderedSet[int]

def is_read_opcode(opname): ...
def is_write_opcode(opname): ...
def analysis_inputs(instructions: list[Instruction], current_instr_idx: int, stop_instr_idx: int | None = None) -> OrderedSet[str]: ...

@dataclasses.dataclass
class SpaceState:
    reads: dict[str, Space]
    writes: dict[str, Space]
    visited: OrderedSet[int]
    def __or__(self, other): ...

class Space(Enum):
    locals = 1
    globals = 2
    cells = 3
    all = 4

def get_space(opname: str): ...
def analysis_used_names_with_space(instructions: list[Instruction], start_instr_idx: int, stop_instr_idx: int | None = None): ...
