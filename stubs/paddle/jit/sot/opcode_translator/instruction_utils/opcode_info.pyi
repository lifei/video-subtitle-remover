from _typeshed import Incomplete
from enum import Enum

REL_JUMP: Incomplete
REL_BWD_JUMP: Incomplete
REL_FWD_JUMP: Incomplete
ABS_JUMP: Incomplete
HAS_LOCAL: Incomplete
HAS_FREE: Incomplete
ALL_JUMP = REL_JUMP | ABS_JUMP
UNCONDITIONAL_JUMP: Incomplete

class JumpDirection(Enum):
    FORWARD = 'FORWARD'
    BACKWARD = 'BACKWARD'

class PopJumpCond(Enum):
    FALSE = 'FALSE'
    TRUE = 'TRUE'
    NONE = 'NONE'
    NOT_NONE = 'NOT_NONE'

PYOPCODE_CACHE_SIZE: Incomplete
