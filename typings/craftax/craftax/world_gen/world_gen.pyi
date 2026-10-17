from craftax.craftax.craftax_state import EnvParams, EnvState, StaticEnvParams
from craftax.craftax.world_gen.world_gen_configs import SmoothGenConfig
from jax import Array

def generate_smoothworld(
    rng: Array,
    static_params: StaticEnvParams,
    player_position: Array,
    config: SmoothGenConfig,
    params: EnvParams,
) -> tuple[Array, Array, Array, Array, Array]: ...
def generate_world(
    rng: Array,
    params: EnvParams,
    static_params: StaticEnvParams,
) -> EnvState: ...
