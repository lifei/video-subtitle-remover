from .gate import BaseGate as BaseGate, GShardGate as GShardGate, NaiveGate as NaiveGate, SwitchGate as SwitchGate
from .grad_clip import ClipGradForMOEByGlobalNorm as ClipGradForMOEByGlobalNorm
from .moe_layer import MoELayer as MoELayer

ClipGradByGlobalNorm = ClipGradForMOEByGlobalNorm
