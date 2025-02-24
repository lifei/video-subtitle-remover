from _typeshed import Incomplete
from paddle import base as base
from paddle.base.layer_helper import LayerHelper as LayerHelper
from paddle.base.param_attr import ParamAttr as ParamAttr
from paddle.nn import Layer as Layer

def resnet_unit(x, filter_x, scale_x, bias_x, mean_x, var_x, z, filter_z, scale_z, bias_z, mean_z, var_z, stride, stride_z, padding, dilation, groups, momentum, eps, data_format, fuse_add, has_shortcut, use_global_stats, is_test, act): ...

class ResNetUnit(Layer):
    filter_x: Incomplete
    scale_x: Incomplete
    bias_x: Incomplete
    mean_x: Incomplete
    var_x: Incomplete
    filter_z: Incomplete
    scale_z: Incomplete
    bias_z: Incomplete
    mean_z: Incomplete
    var_z: Incomplete
    def __init__(self, num_channels_x, num_filters, filter_size, stride: int = 1, momentum: float = 0.9, eps: float = 1e-05, data_format: str = 'NHWC', act: str = 'relu', fuse_add: bool = False, has_shortcut: bool = False, use_global_stats: bool = False, is_test: bool = False, filter_x_attr: Incomplete | None = None, scale_x_attr: Incomplete | None = None, bias_x_attr: Incomplete | None = None, moving_mean_x_name: Incomplete | None = None, moving_var_x_name: Incomplete | None = None, num_channels_z: int = 1, stride_z: int = 1, filter_z_attr: Incomplete | None = None, scale_z_attr: Incomplete | None = None, bias_z_attr: Incomplete | None = None, moving_mean_z_name: Incomplete | None = None, moving_var_z_name: Incomplete | None = None) -> None: ...
    def forward(self, x, z: Incomplete | None = None): ...
