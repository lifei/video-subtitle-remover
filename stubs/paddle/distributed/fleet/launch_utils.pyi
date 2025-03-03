from _typeshed import Incomplete
from paddle import framework as framework

logger: Incomplete

class DistributeMode:
    COLLECTIVE: int
    PS: int
    PS_HETER: int

class DeviceMode:
    UNKNOWN: int
    CPU: int
    GPU: int
    KUNLUN: int
    XPU: int

class Cluster:
    job_server: Incomplete
    pods: Incomplete
    hdfs: Incomplete
    job_stage_flag: Incomplete
    def __init__(self, hdfs) -> None: ...
    def __eq__(self, cluster): ...
    def __ne__(self, cluster): ...
    def update_pods(self, cluster) -> None: ...
    def trainers_nranks(self): ...
    def pods_nranks(self): ...
    def trainers_endpoints(self): ...
    def world_device_ids(self): ...
    def pods_endpoints(self): ...
    def get_pod_by_id(self, pod_id): ...

class JobServer:
    endpoint: Incomplete
    def __init__(self) -> None: ...
    def __eq__(self, j): ...
    def __ne__(self, j): ...

class Trainer:
    accelerators: Incomplete
    endpoint: Incomplete
    stage: Incomplete
    def __init__(self) -> None: ...
    def __eq__(self, t): ...
    def __ne__(self, t): ...
    def rank(self): ...

class Pod:
    id: Incomplete
    addr: Incomplete
    port: Incomplete
    trainers: Incomplete
    servers: Incomplete
    workers: Incomplete
    coordinators: Incomplete
    heter_workers: Incomplete
    accelerators: Incomplete
    device_mode: Incomplete
    def __init__(self) -> None: ...
    def __eq__(self, pod): ...
    def __ne__(self, pod): ...
    def parse_response(self, res_pods) -> None: ...
    def rank(self): ...
    def get_visible_accelerators(self): ...

def get_logger(log_level: int = 20, name: str = 'root'): ...
def get_cluster(node_ips, node_ip, trainer_endpoints, device_mode, devices_per_proc): ...
def terminate_local_procs(procs) -> None: ...
def get_host_name_ip(): ...
def add_arguments(argname, type, default, help, argparser, **kwargs) -> None: ...
def find_free_ports(num): ...
def get_ports(num, offset): ...
def pretty_print_envs(envs, header: Incomplete | None = None): ...

class TrainerProc:
    proc: Incomplete
    log_fn: Incomplete
    log_offset: Incomplete
    rank: Incomplete
    local_rank: Incomplete
    cmd: Incomplete
    def __init__(self) -> None: ...

def run_with_coverage(*args): ...
def start_local_trainers(cluster, pod, training_script, training_script_args, log_dir: Incomplete | None = None, envs: Incomplete | None = None): ...
def pull_worker_log(tp) -> None: ...
def watch_local_trainers(procs, nranks): ...
def get_gpus(gpus): ...
def get_xpus(xpus): ...
def get_device_mode(backend): ...
def get_device_proc_info(args): ...
def direct_start(args) -> None: ...
def get_custom_endpoints(origin_endpoints, offset: int = 0): ...
def get_mapped_cluster_without_rank_mapping(node_ips, node_ip, trainer_endpoints, device_mode, node_ranks): ...
def get_mapped_cluster_from_args_without_rank_mapping(args, device_mode): ...
def get_mapped_cluster_with_rank_mapping(node_ips, node_ip, trainer_endpoints, device_mode, node_ranks, node_rank_mappings): ...
def get_mapped_cluster_from_args_with_rank_mapping(args, device_mode): ...

class ParameterServerLauncher:
    args: Incomplete
    distribute_mode: Incomplete
    with_coordinator: bool
    server_num: int
    worker_num: int
    heter_worker_num: int
    coordinator_num: int
    server_endpoints: str
    server_endpoints_ips: Incomplete
    server_endpoints_port: Incomplete
    worker_endpoints: str
    worker_endpoints_ips: Incomplete
    worker_endpoints_port: Incomplete
    heter_worker_endpoints: str
    heter_worker_endpoints_ips: Incomplete
    heter_worker_endpoints_port: Incomplete
    coordinator_endpoints: str
    coordinator_endpoints_ips: Incomplete
    coordinator_endpoints_port: Incomplete
    is_local: bool
    current_node_ip: str
    stage_trainer_num: Incomplete
    stage_heter_map: Incomplete
    stage_list: Incomplete
    stage_device_map: Incomplete
    stage_num: int
    def __init__(self, args, distribute_mode) -> None: ...
    stage_heter_trainer_num: Incomplete
    http_port: Incomplete
    node_ips: Incomplete
    node_rank: Incomplete
    def get_role_endpoints(self, args) -> None: ...
    gloo_rendezvous_dir: Incomplete
    procs: Incomplete
    cmds: Incomplete
    log_fns: Incomplete
    def start_ps(self) -> None: ...
    def start_pod_server(self, args, pod) -> None: ...
    def start_pod_worker(self, args, pod) -> None: ...
    def start_pod_coordinator(self, args, pod) -> None: ...
    def start_pod_heter_worker(self, args, pod) -> None: ...

def check_backend(backend) -> None: ...
def block_windows_and_macos(backend) -> None: ...
def get_backend_by_compile_flag(): ...
