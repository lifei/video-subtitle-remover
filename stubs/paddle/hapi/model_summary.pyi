from _typeshed import Incomplete
from paddle import nn as nn
from paddle.autograd import no_grad as no_grad
from paddle.static import InputSpec as InputSpec

def summary(net, input_size: Incomplete | None = None, dtypes: Incomplete | None = None, input: Incomplete | None = None): ...
def summary_string(model, input_size: Incomplete | None = None, dtypes: Incomplete | None = None, input: Incomplete | None = None): ...
