from . import constants as constants
from _typeshed import Incomplete

class BaseConfig:
    def __init__(self, category, config_dict: Incomplete | None = None) -> None: ...
    def from_dict(self, config_dict) -> None: ...
    def to_dict(self): ...
    def __deepcopy__(self, memo): ...
    def get(self, k, d: Incomplete | None = None): ...

class RecomputeConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class FusedLinearPromotionConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class AMPConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class ShardingConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class GradientMergeConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class PipelineConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class QATConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class TuningConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class DatasetConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class FusedPassesConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class DPOptimizationConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class MPOptimizationConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class SPOptimizationConfig(BaseConfig):
    def __init__(self, config_dict: Incomplete | None = None) -> None: ...

class Strategy(BaseConfig):
    recompute: Incomplete
    amp: Incomplete
    sharding: Incomplete
    gradient_merge: Incomplete
    pipeline: Incomplete
    qat: Incomplete
    tuning: Incomplete
    dataset: Incomplete
    fused_passes: Incomplete
    fused_linear_promotion: Incomplete
    dp_optimization: Incomplete
    mp_optimization: Incomplete
    sp_optimization: Incomplete
    def __init__(self, config: Incomplete | None = None) -> None: ...
