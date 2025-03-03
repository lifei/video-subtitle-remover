from .primreg import REGISTER_FN as REGISTER_FN
from _typeshed import Incomplete
from paddle.base.layer_helper import LayerHelper as LayerHelper

def fill_const(value, shape, dtype, out: Incomplete | None = None): ...
def bernoulli(shape, dtype, p, out: Incomplete | None = None): ...
def neg(x, out: Incomplete | None = None): ...
def set_value(x, y, axis, starts, ends, strides, out): ...
def mean(x, axis: Incomplete | None = None, keepdim: bool = False): ...
def ones(shape, dtype): ...
def zeros(shape, dtype): ...
def batch_norm(x, axis, gamma, beta, run_mean, run_var, eps: float = 1e-05, momentum: float = 0.9, use_run_stat: bool = False, reserve_space: Incomplete | None = None): ...
def square(x): ...
def add(x, y, out: Incomplete | None = None): ...
def sub(x, y, out: Incomplete | None = None): ...
def mul(x, y, out: Incomplete | None = None): ...
def div(x, y, out: Incomplete | None = None): ...
def sqrt(x, out: Incomplete | None = None): ...
def tanh(x, out: Incomplete | None = None): ...
def sin(x, out: Incomplete | None = None): ...
def cos(x, out: Incomplete | None = None): ...
def exp(x, out: Incomplete | None = None): ...
def abs(x, out: Incomplete | None = None): ...
def reshape(x, shape, out: Incomplete | None = None): ...
def broadcast(x, shape, out: Incomplete | None = None): ...
def transpose(x, axis: Incomplete | None = None, out: Incomplete | None = None): ...
def split(x, num_or_sections, axis: int = 0, outs: Incomplete | None = None): ...
def concat(xs, axis: int = 0, out: Incomplete | None = None): ...
def reduce_sum(x, axis: Incomplete | None = None, keepdim: bool = False, out: Incomplete | None = None): ...
def matmul(x, y, out: Incomplete | None = None): ...
def slice_select(x, axis, starts, ends, strides, out: Incomplete | None = None): ...
def slice_assign(x, y, axis, starts, ends, strides, out: Incomplete | None = None): ...
def gather(x, indextensor, axis, out: Incomplete | None = None): ...
def scatter_add(x, y, indextensor, axis, out: Incomplete | None = None): ...
def log(x, out: Incomplete | None = None): ...
def select(cond, x, y, out: Incomplete | None = None): ...
def eq(x, y, out: Incomplete | None = None): ...
def gt(x, y, out: Incomplete | None = None): ...
def ge(x, y, out: Incomplete | None = None): ...
def ne(x, y, out: Incomplete | None = None): ...
def pow(x, y, out: Incomplete | None = None): ...
def max(x, y, out: Incomplete | None = None): ...
def erf(x, out: Incomplete | None = None): ...
def cast(x, dtype, out: Incomplete | None = None): ...
def rsqrt(x, out: Incomplete | None = None): ...
def uniform_random(dtype, min_value, max_value, seed, shape: Incomplete | None = None, out: Incomplete | None = None): ...
