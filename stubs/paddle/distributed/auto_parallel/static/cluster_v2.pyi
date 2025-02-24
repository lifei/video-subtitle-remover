from _typeshed import Incomplete
from enum import IntEnum
from paddle.framework import core as core

class DeviceType(IntEnum):
    UNKNOWN = 0
    CPU = 1
    GPU = 2
    XPU = 3
    DCU = 5
    NIC = 6

class LinkType(IntEnum):
    UNKNOWN = 0
    LOC = 1
    SYS = 2
    PHB = 3
    PIX = 4
    PIB = 5
    NVL = 6
    NVB = 7
    NET = 8

class DeviceMesh(core.DeviceMesh):
    def __init__(self, name, mesh, dim_names: Incomplete | None = None) -> None: ...
    @property
    def mesh(self): ...
