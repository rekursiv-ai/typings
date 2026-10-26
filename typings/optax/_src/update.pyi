from optax._src.base import Params

def apply_updates[T](params: T, updates: T) -> T: ...
def incremental_update(
    new_tensors: Params,
    old_tensors: Params,
    step_size: float,
) -> Params: ...
def periodic_update(
    new_tensors: Params,
    old_tensors: Params,
    steps: int,
    update_period: int,
) -> Params: ...
