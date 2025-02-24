from .line_search import strong_wolfe as strong_wolfe
from .utils import check_initial_inverse_hessian_estimate as check_initial_inverse_hessian_estimate, check_input_type as check_input_type
from _typeshed import Incomplete

def minimize_lbfgs(objective_func, initial_position, history_size: int = 100, max_iters: int = 50, tolerance_grad: float = 1e-08, tolerance_change: float = 1e-08, initial_inverse_hessian_estimate: Incomplete | None = None, line_search_fn: str = 'strong_wolfe', max_line_search_iters: int = 50, initial_step_length: float = 1.0, dtype: str = 'float32', name: Incomplete | None = None): ...
