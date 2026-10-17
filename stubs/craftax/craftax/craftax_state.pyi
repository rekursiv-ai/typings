from dataclasses import dataclass
from typing import Self

from jax import Array

@dataclass
class Inventory:
    wood: Array
    stone: Array
    coal: Array
    iron: Array
    diamond: Array
    sapling: Array
    pickaxe: Array
    sword: Array
    bow: Array
    arrows: Array
    armour: Array
    torches: Array
    ruby: Array
    sapphire: Array
    potions: Array
    books: Array

    def replace(self, **updates: object) -> Self: ...

@dataclass
class Mobs:
    position: Array
    health: Array
    mask: Array
    attack_cooldown: Array
    type_id: Array

    def replace(self, **updates: object) -> Self: ...

@dataclass
class EnvState:
    map: Array
    item_map: Array
    mob_map: Array
    light_map: Array
    down_ladders: Array
    up_ladders: Array
    chests_opened: Array
    monsters_killed: Array
    player_position: Array
    player_level: Array
    player_direction: Array
    player_health: Array
    player_food: Array
    player_drink: Array
    player_energy: Array
    player_mana: Array
    is_sleeping: bool | Array
    is_resting: bool | Array
    player_recover: Array
    player_hunger: Array
    player_thirst: Array
    player_fatigue: Array
    player_recover_mana: Array
    player_xp: Array
    player_dexterity: Array
    player_strength: Array
    player_intelligence: Array
    inventory: Inventory
    melee_mobs: Mobs
    passive_mobs: Mobs
    ranged_mobs: Mobs
    mob_projectiles: Mobs
    mob_projectile_directions: Array
    player_projectiles: Mobs
    player_projectile_directions: Array
    growing_plants_positions: Array
    growing_plants_age: Array
    growing_plants_mask: Array
    potion_mapping: Array
    learned_spells: Array
    sword_enchantment: Array
    bow_enchantment: Array
    armour_enchantments: Array
    boss_progress: Array
    boss_timesteps_to_spawn_this_round: Array
    light_level: Array
    achievements: Array
    state_rng: Array
    timestep: Array
    fractal_noise_angles: tuple[
        Array | None,
        Array | None,
        Array | None,
        Array | None,
    ] = ...

    def replace(self, **updates: object) -> Self: ...

@dataclass
class EnvParams:
    max_timesteps: int = ...
    day_length: int = ...
    always_diamond: bool = ...
    mob_despawn_distance: int = ...
    max_attribute: int = ...
    god_mode: bool = ...
    fractal_noise_angles: tuple[
        Array | None,
        Array | None,
        Array | None,
        Array | None,
    ] = ...

    def replace(self, **updates: object) -> Self: ...

@dataclass
class StaticEnvParams:
    map_size: tuple[int, int] = ...
    num_levels: int = ...
    max_melee_mobs: int = ...
    max_passive_mobs: int = ...
    max_growing_plants: int = ...
    max_ranged_mobs: int = ...
    max_mob_projectiles: int = ...
    max_player_projectiles: int = ...

    def replace(self, **updates: object) -> Self: ...
