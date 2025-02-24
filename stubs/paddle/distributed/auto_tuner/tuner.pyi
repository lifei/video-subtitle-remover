from .utils import default_candidates as default_candidates, gbs_default_candidates as gbs_default_candidates
from _typeshed import Incomplete

class AutoTuner:
    cur_task_id: int
    task_limit: Incomplete
    algo: Incomplete
    history_cfgs: Incomplete
    def __init__(self, tuner_cfg) -> None: ...
    def search_once(self): ...
    def add_cfg(self, cfg) -> None: ...
