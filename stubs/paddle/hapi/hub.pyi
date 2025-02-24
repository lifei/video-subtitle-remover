from _typeshed import Incomplete
from paddle.utils.download import get_path_from_url as get_path_from_url

DEFAULT_CACHE_DIR: str
VAR_DEPENDENCY: str
MODULE_HUBCONF: str
HUB_DIR: Incomplete

def list(repo_dir, source: str = 'github', force_reload: bool = False): ...
def help(repo_dir, model, source: str = 'github', force_reload: bool = False): ...
def load(repo_dir, model, source: str = 'github', force_reload: bool = False, **kwargs): ...
