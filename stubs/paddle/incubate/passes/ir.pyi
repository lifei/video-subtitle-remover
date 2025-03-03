import paddle
from ...base import core as core, unique_name as unique_name
from ...base.framework import OpProtoHolder as OpProtoHolder
from _typeshed import Incomplete
from paddle.base.proto import framework_pb2 as framework_pb2, pass_desc_pb2 as pass_desc_pb2

base_path: Incomplete

class RegisterPassHelper:
    def __init__(self, pass_pairs, pass_type: str = '', input_specs={}) -> None: ...
    def SerializeMultiPassDesc(self): ...

class PassDesc:
    class AttrHelper:
        def __init__(self, obj, name, element_index: Incomplete | None = None) -> None: ...
        def __getitem__(self, index): ...
        def __sub__(self, value): ...
        def __add__(self, value): ...
        def Mod(self, value): ...
        def Size(self): ...
        def EQ(self, value) -> None: ...
        def MappedPattern(self, var: Incomplete | None = None, op: Incomplete | None = None, index: int = 0, name: Incomplete | None = None, element_index: Incomplete | None = None): ...
    class VarHelper(paddle.static.Variable):
        def __init__(self, *args, **kwargs) -> None: ...
        def __getattr__(self, name): ...
        def Attr(self, name): ...
    class OpHelper:
        def __init__(self, type: Incomplete | None = None) -> None: ...
        def __getattr__(self, name): ...
        def __call__(self, *args, **kwargs): ...
        def Init(self) -> None: ...
        def Attr(self, name): ...
        def SetAttr(self, name, value) -> None: ...
        def Output(self, name): ...
        def Outputs(self): ...
        def SetOutputs(self, **kwargs) -> None: ...
    OP: Incomplete

def RegisterPass(function: Incomplete | None = None, input_specs={}): ...
