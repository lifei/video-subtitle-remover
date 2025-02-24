from . import Value as Value
from _typeshed import Incomplete
from paddle.base.libpaddle import DataType as DataType
from paddle.base.wrapped_decorator import wrap_decorator as wrap_decorator

fake_interface_only: Incomplete

def create_tensor_with_batchsize(ref_var, value, dtype): ...
def monkey_patch_value(): ...
