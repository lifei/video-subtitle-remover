import paddle
from paddle.base import core as core
from paddle.base.data_feeder import convert_dtype as convert_dtype
from paddle.base.executor import check_feed_shape_type as check_feed_shape_type
from paddle.base.framework import Operator as Operator, Program as Program
from paddle.distributed.auto_parallel.static.utils import get_logger as get_logger, is_comm_op as is_comm_op

def check_if_op_supports_runtime_profiling(op): ...
def measure_program_real_op_cost(program: paddle.static.Program, run_iters: int = 8, place=..., verbose_level: int = 0): ...
