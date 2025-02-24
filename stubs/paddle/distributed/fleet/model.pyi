from .base.topology import ParallelMode as ParallelMode
from .meta_parallel import PipelineLayer as PipelineLayer, PipelineParallel as PipelineParallel, PipelineParallelWithInterleave as PipelineParallelWithInterleave, PipelineParallelWithInterleaveFthenB as PipelineParallelWithInterleaveFthenB, SegmentParallel as SegmentParallel, ShardingParallel as ShardingParallel, TensorParallel as TensorParallel
from paddle.distributed import fleet as fleet

def distributed_model(model): ...
