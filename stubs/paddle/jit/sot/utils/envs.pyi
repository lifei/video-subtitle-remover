from _typeshed import Incomplete
from paddle.utils.environments import BooleanEnvironmentVariable as BooleanEnvironmentVariable, EnvironmentVariableGuard as EnvironmentVariableGuard, IntegerEnvironmentVariable as IntegerEnvironmentVariable, StringEnvironmentVariable as StringEnvironmentVariable

ENV_COST_MODEL: Incomplete
ENV_MIN_GRAPH_SIZE: Incomplete
ENV_SOT_LOG_LEVEL: Incomplete
ENV_STRICT_MODE: Incomplete
ENV_SHOW_TRACKERS: Incomplete
ENV_CLEAN_CODE: Incomplete

def cost_model_guard(value: bool): ...
def strict_mode_guard(value: bool): ...
def min_graph_size_guard(value: int): ...
