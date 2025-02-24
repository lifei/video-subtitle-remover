from _typeshed import Incomplete
from paddle.nn import Layer

__all__ = ['resnet_basic_block', 'ResNetBasicBlock']

def resnet_basic_block(x, filter1, scale1, bias1, mean1, var1, filter2, scale2, bias2, mean2, var2, filter3, scale3, bias3, mean3, var3, stride1, stride2, stride3, padding1, padding2, padding3, dilation1, dilation2, dilation3, groups, momentum, eps, data_format, has_shortcut, use_global_stats: Incomplete | None = None, training: bool = False, trainable_statistics: bool = False, find_conv_max: bool = True): ...

class ResNetBasicBlock(Layer):
    filter_1: Incomplete
    scale_1: Incomplete
    bias_1: Incomplete
    mean_1: Incomplete
    var_1: Incomplete
    filter_2: Incomplete
    scale_2: Incomplete
    bias_2: Incomplete
    mean_2: Incomplete
    var_2: Incomplete
    filter_3: Incomplete
    scale_3: Incomplete
    bias_3: Incomplete
    mean_3: Incomplete
    var_3: Incomplete
    def __init__(self, num_channels1, num_filter1, filter1_size, num_channels2, num_filter2, filter2_size, num_channels3, num_filter3, filter3_size, stride1: int = 1, stride2: int = 1, stride3: int = 1, act: str = 'relu', momentum: float = 0.9, eps: float = 1e-05, data_format: str = 'NCHW', has_shortcut: bool = False, use_global_stats: bool = False, is_test: bool = False, filter1_attr: Incomplete | None = None, scale1_attr: Incomplete | None = None, bias1_attr: Incomplete | None = None, moving_mean1_name: Incomplete | None = None, moving_var1_name: Incomplete | None = None, filter2_attr: Incomplete | None = None, scale2_attr: Incomplete | None = None, bias2_attr: Incomplete | None = None, moving_mean2_name: Incomplete | None = None, moving_var2_name: Incomplete | None = None, filter3_attr: Incomplete | None = None, scale3_attr: Incomplete | None = None, bias3_attr: Incomplete | None = None, moving_mean3_name: Incomplete | None = None, moving_var3_name: Incomplete | None = None, padding1: int = 0, padding2: int = 0, padding3: int = 0, dilation1: int = 1, dilation2: int = 1, dilation3: int = 1, trainable_statistics: bool = False, find_conv_max: bool = True) -> None: ...
    def forward(self, x): ...
