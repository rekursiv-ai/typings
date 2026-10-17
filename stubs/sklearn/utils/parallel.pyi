from _typeshed import Incomplete
from sklearn._config import (
    config_context as config_context,
    get_config as get_config,
)

import joblib

class Parallel(joblib.Parallel):
    def __call__(self, iterable): ...

def delayed(function): ...

class _FuncWrapper:
    function: Incomplete
    def __init__(self, function) -> None: ...
    config: Incomplete
    warning_filters: Incomplete
    def with_config_and_warning_filters(self, config, warning_filters): ...
    def __call__(self, *args, **kwargs): ...
