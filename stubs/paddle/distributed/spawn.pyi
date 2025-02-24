from _typeshed import Incomplete
from paddle.base import core as core
from paddle.device import get_device as get_device
from paddle.distributed.cloud_utils import get_cluster_and_pod as get_cluster_and_pod
from paddle.distributed.fleet.cloud_utils import use_paddlecloud as use_paddlecloud
from paddle.distributed.fleet.launch import get_cluster_from_args as get_cluster_from_args
from paddle.distributed.fleet.launch_utils import DeviceMode as DeviceMode, block_windows_and_macos as block_windows_and_macos, check_backend as check_backend
from paddle.distributed.utils.launch_utils import get_host_name_ip as get_host_name_ip
from paddle.framework import set_flags as set_flags

class ParallelEnvArgs:
    cluster_node_ips: Incomplete
    node_ip: Incomplete
    use_paddlecloud: Incomplete
    started_port: Incomplete
    print_config: bool
    selected_devices: Incomplete
    def __init__(self) -> None: ...

class MultiprocessContext:
    error_queues: Incomplete
    return_queues: Incomplete
    processes: Incomplete
    sentinels: Incomplete
    def __init__(self, processes, error_queues, return_queues) -> None: ...
    def join(self, timeout: Incomplete | None = None): ...

def spawn(func, args=(), nprocs: int = -1, join: bool = True, daemon: bool = False, **options): ...
