from _typeshed import Incomplete

__all__ = ['FleetUtil', 'GPUPSUtil']

class FleetUtil:
    def __init__(self, mode: str = 'pslib') -> None: ...
    def rank0_print(self, s) -> None: ...
    def rank0_info(self, s) -> None: ...
    def rank0_error(self, s) -> None: ...
    def set_zero(self, var_name, scope=..., place=..., param_type: str = 'int64') -> None: ...
    def print_global_auc(self, scope=..., stat_pos: str = '_generated_var_2', stat_neg: str = '_generated_var_3', print_prefix: str = '') -> None: ...
    def get_global_auc(self, scope=..., stat_pos: str = '_generated_var_2', stat_neg: str = '_generated_var_3'): ...
    def load_fleet_model_one_table(self, table_id, path) -> None: ...
    def load_fleet_model(self, path, mode: int = 0) -> None: ...
    def save_fleet_model(self, path, mode: int = 0) -> None: ...
    def write_model_donefile(self, output_path, day, pass_id, xbox_base_key, hadoop_fs_name, hadoop_fs_ugi, hadoop_home: str = '$HADOOP_HOME', donefile_name: str = 'donefile.txt') -> None: ...
    def write_xbox_donefile(self, output_path, day, pass_id, xbox_base_key, data_path, hadoop_fs_name, hadoop_fs_ugi, monitor_data={}, hadoop_home: str = '$HADOOP_HOME', donefile_name: Incomplete | None = None) -> None: ...
    def write_cache_donefile(self, output_path, day, pass_id, key_num, hadoop_fs_name, hadoop_fs_ugi, hadoop_home: str = '$HADOOP_HOME', donefile_name: str = 'sparse_cache.meta', **kwargs) -> None: ...
    def load_model(self, output_path, day, pass_id) -> None: ...
    def save_model(self, output_path, day, pass_id) -> None: ...
    def save_batch_model(self, output_path, day) -> None: ...
    def save_delta_model(self, output_path, day, pass_id) -> None: ...
    def save_xbox_base_model(self, output_path, day) -> None: ...
    def save_cache_model(self, output_path, day, pass_id, mode: int = 1, **kwargs): ...
    def save_cache_base_model(self, output_path, day, **kwargs): ...
    def pull_all_dense_params(self, scope, program) -> None: ...
    def save_paddle_inference_model(self, executor, scope, program, feeded_vars, target_vars, output_path, day, pass_id, hadoop_fs_name, hadoop_fs_ugi, hadoop_home: str = '$HADOOP_HOME', save_combine: bool = True) -> None: ...
    def save_paddle_params(self, executor, scope, program, model_name, output_path, day, pass_id, hadoop_fs_name, hadoop_fs_ugi, hadoop_home: str = '$HADOOP_HOME', var_names: Incomplete | None = None, save_combine: bool = True) -> None: ...
    def get_last_save_xbox_base(self, output_path, hadoop_fs_name, hadoop_fs_ugi, hadoop_home: str = '$HADOOP_HOME'): ...
    def get_last_save_xbox(self, output_path, hadoop_fs_name, hadoop_fs_ugi, hadoop_home: str = '$HADOOP_HOME'): ...
    def get_last_save_model(self, output_path, hadoop_fs_name, hadoop_fs_ugi, hadoop_home: str = '$HADOOP_HOME'): ...
    def get_online_pass_interval(self, days, hours, split_interval, split_per_pass, is_data_hourly_placed): ...
    def get_global_metrics(self, scope=..., stat_pos_name: str = '_generated_var_2', stat_neg_name: str = '_generated_var_3', sqrerr_name: str = 'sqrerr', abserr_name: str = 'abserr', prob_name: str = 'prob', q_name: str = 'q', pos_ins_num_name: str = 'pos', total_ins_num_name: str = 'total'): ...
    def print_global_metrics(self, scope=..., stat_pos_name: str = '_generated_var_2', stat_neg_name: str = '_generated_var_3', sqrerr_name: str = 'sqrerr', abserr_name: str = 'abserr', prob_name: str = 'prob', q_name: str = 'q', pos_ins_num_name: str = 'pos', total_ins_num_name: str = 'total', print_prefix: str = '') -> None: ...
    def program_type_trans(self, prog_dir, prog_fn, is_text): ...
    def load_program(self, model_filename, is_text): ...
    def draw_from_program_file(self, model_filename, is_text, output_dir, output_filename) -> None: ...
    def draw_from_program(self, program, output_dir, output_name) -> None: ...
    def check_two_programs(self, config): ...
    def check_vars_and_dump(self, config): ...
    def parse_program_proto(self, prog_path, is_text, output_dir) -> None: ...

class GPUPSUtil(FleetUtil):
    def __init__(self, fs_client: Incomplete | None = None) -> None: ...
    def init(self, fs_name, fs_user, fs_passwd, fs_conf) -> None: ...
    def set_fsclient(self, fs_client) -> None: ...
    def get_last_save_xbox_base(self, output_path): ...
    def get_last_save_xbox(self, output_path): ...
    def get_last_save_model(self, output_path): ...
    def write_model_donefile(self, output_path, day, pass_id, xbox_base_key, donefile_name: str = 'donefile.txt') -> None: ...
    def write_xbox_donefile(self, output_path, day, pass_id, xbox_base_key, data_path, hadoop_fs_name, hadoop_fs_ugi, monitor_data={}, hadoop_home: str = '$HADOOP_HOME', donefile_name: Incomplete | None = None) -> None: ...
    def write_cache_donefile(self, output_path, day, pass_id, key_num, donefile_name: str = 'sparse_cache.meta', **kwargs) -> None: ...
