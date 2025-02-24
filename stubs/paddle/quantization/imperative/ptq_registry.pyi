from _typeshed import Incomplete

class LayerInfo:
    layer: Incomplete
    input_names: Incomplete
    weight_names: Incomplete
    output_names: Incomplete
    def __init__(self, layer, input_names, weight_names, output_names) -> None: ...

PTQ_LAYERS_INFO: Incomplete
QUANT_LAYERS_INFO: Incomplete
SIMULATED_LAYERS: Incomplete

class PTQRegistry:
    supported_layers_map: Incomplete
    registered_layers_map: Incomplete
    is_inited: bool
    def __init__(self) -> None: ...
    @classmethod
    def is_supported_layer(cls, layer): ...
    @classmethod
    def is_registered_layer(cls, layer): ...
    @classmethod
    def is_simulated_quant_layer(cls, layer): ...
    @classmethod
    def layer_info(cls, layer): ...
