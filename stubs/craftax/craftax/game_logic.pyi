from craftax.craftax.craftax_state import EnvParams, EnvState, StaticEnvParams
from craftax.craftax.util.game_logic_utils import (
    calculate_light_level as calculate_light_level,
)
from jax import Array

def is_game_over(
    state: EnvState,
    params: EnvParams,
    static_env_params: StaticEnvParams,
) -> Array: ...
def update_plants_with_eat(
    state: EnvState,
    plant_position: Array,
    static_params: StaticEnvParams,
) -> Array: ...
def do_action(
    rng: Array,
    state: EnvState,
    action: int | Array,
    static_params: StaticEnvParams,
) -> EnvState: ...
def do_crafting(state: EnvState, action: int | Array) -> EnvState: ...
def place_block(
    state: EnvState,
    action: int | Array,
    static_params: StaticEnvParams,
) -> EnvState: ...
def update_mobs(
    rng: Array,
    state: EnvState,
    params: EnvParams,
    static_params: StaticEnvParams,
) -> EnvState: ...
def update_player_intrinsics(
    state: EnvState,
    action: int | Array,
    static_params: StaticEnvParams,
) -> EnvState: ...
def update_plants(state: EnvState, static_params: StaticEnvParams) -> EnvState: ...
def move_player(
    state: EnvState,
    action: int | Array,
    params: EnvParams,
) -> EnvState: ...
def spawn_mobs(
    state: EnvState,
    rng: Array,
    params: EnvParams,
    static_params: StaticEnvParams,
) -> EnvState: ...
def shoot_projectile(
    state: EnvState,
    action: int | Array,
    static_params: StaticEnvParams,
) -> EnvState: ...
def cast_spell(
    state: EnvState,
    action: int | Array,
    static_params: StaticEnvParams,
) -> EnvState: ...
def drink_potion(state: EnvState, action: int | Array) -> EnvState: ...
def read_book(rng: Array, state: EnvState, action: int | Array) -> EnvState: ...
def enchant(rng: Array, state: EnvState, action: int | Array) -> EnvState: ...
def boss_logic(state: EnvState, static_params: StaticEnvParams) -> EnvState: ...
def calculate_inventory_achievements(state: EnvState) -> EnvState: ...
def level_up_attributes(
    state: EnvState,
    action: int | Array,
    params: EnvParams,
) -> EnvState: ...
def craftax_step(
    rng: Array,
    state: EnvState,
    action: int | Array,
    params: EnvParams,
    static_params: StaticEnvParams,
) -> tuple[EnvState, Array]: ...
