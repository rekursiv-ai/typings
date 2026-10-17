from craftax.craftax.craftax_state import EnvState
from jax import Array

def log_achievements_to_info(
    state: EnvState,
    done: bool | Array,
) -> dict[str, Array]: ...
