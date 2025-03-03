from _typeshed import Incomplete

class HistoryRecorder:
    history: Incomplete
    store_path: Incomplete
    def __init__(self) -> None: ...
    def add_cfg(self, **kwargs) -> None: ...
    def sort_metric(self, direction, metric_name) -> None: ...
    def get_best(self, metric, direction, mode: Incomplete | None = None) -> tuple[dict, bool]: ...
    def store_history(self, path: str = './history.csv') -> None: ...
    def load_history(self, path: str = './history.csv') -> tuple[list, bool]: ...
    def clean_history(self) -> None: ...
