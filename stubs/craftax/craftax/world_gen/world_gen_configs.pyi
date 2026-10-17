from typing import Any

class SmoothGenConfig:
    def __getattr__(self, name: str) -> Any: ...

class DungeonConfig:
    def __getattr__(self, name: str) -> Any: ...

OVERWORLD_CONFIG: SmoothGenConfig
GNOMISH_MINES_CONFIG: SmoothGenConfig
TROLL_MINES_CONFIG: SmoothGenConfig
FIRE_LEVEL_CONFIG: SmoothGenConfig
ICE_LEVEL_CONFIG: SmoothGenConfig
BOSS_LEVEL_CONFIG: SmoothGenConfig
DUNGEON_CONFIG: DungeonConfig
SEWER_CONFIG: DungeonConfig
VAULTS_CONFIG: DungeonConfig
