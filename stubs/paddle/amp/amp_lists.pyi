from _typeshed import Incomplete

WHITE_LIST: Incomplete
ONLY_FP16_WHITE_LIST: Incomplete
FP16_WHITE_LIST = WHITE_LIST | ONLY_FP16_WHITE_LIST
FP16_BLACK_LIST: Incomplete
EXTRA_BLACK_LIST: Incomplete
BF16_WHITE_LIST = WHITE_LIST
BF16_BLACK_LIST = FP16_BLACK_LIST

def white_list(): ...
def black_list(): ...
