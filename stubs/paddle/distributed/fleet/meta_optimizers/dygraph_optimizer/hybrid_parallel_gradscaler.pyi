from ...base.topology import ParallelMode as ParallelMode

class HybridParallelGradScaler:
    def __init__(self, scaler, hcg) -> None: ...
    def scale(self, var): ...
    def minimize(self, optimizer, *args, **kwargs): ...
    def __getattr__(self, item): ...
