# Narrow overlay for arcengine: only the surface loop uses, with no ``Any``.
#
# arcengine ships ``py.typed`` but annotates ``ActionInput.data`` as
# ``dict[str, Any]``, ``reasoning`` as ``Any``, and returns an untagged
# ``FrameData | FrameDataRaw`` from ``perform_action``.  This stub shadows the
# package for the checkers, so any name absent here is a type error by design.

from collections.abc import Mapping
from enum import Enum, auto
from typing import Literal, overload

import numpy as np
import pydantic

MAX_REASONING_BYTES: int

class BlockingMode(Enum):
    NOT_BLOCKED = auto()
    BOUNDING_BOX = auto()
    PIXEL_PERFECT = auto()

class InteractionMode(Enum):
    TANGIBLE = auto()
    INTANGIBLE = auto()
    INVISIBLE = auto()
    REMOVED = auto()

# ``str, Enum`` and NOT ``StrEnum``: upstream declares the former, and the two
# differ in the one place a reader would trust this line -- ``str(state)`` and
# ``f"{state}"`` render ``"GameState.WIN"`` here, where ``StrEnum`` renders
# ``"WIN"``. Equality against the bare value holds either way, so declaring
# ``StrEnum`` buys a silently wrong interpolation. Read the value via ``.value``.
class GameState(str, Enum):  # noqa: UP042 -- mirrors upstream; see comment above
    NOT_PLAYED = "NOT_PLAYED"
    NOT_FINISHED = "NOT_FINISHED"
    WIN = "WIN"
    GAME_OVER = "GAME_OVER"

class SimpleAction(pydantic.BaseModel):
    game_id: str = ...

class ComplexAction(pydantic.BaseModel):
    game_id: str = ...
    x: int = ...
    y: int = ...

class GameAction(Enum):
    # Upstream declares ``(id, model)`` tuples but rewrites ``_value_`` to the
    # bare id in ``__init__``, so ``.value`` is an int at runtime.  Mirroring
    # the tuples here would type ``from_id(action.value)`` as an error.
    RESET = 0
    ACTION1 = 1
    ACTION2 = 2
    ACTION3 = 3
    ACTION4 = 4
    ACTION5 = 5
    ACTION6 = 6
    ACTION7 = 7
    action_type: type[SimpleAction | ComplexAction]
    action_data: SimpleAction | ComplexAction
    def is_simple(self) -> bool: ...
    def is_complex(self) -> bool: ...
    @classmethod
    def from_id(cls, action_id: int) -> GameAction: ...
    @classmethod
    def from_name(cls, name: str) -> GameAction: ...

class ActionInput(pydantic.BaseModel):
    id: GameAction = ...
    data: Mapping[str, int] = ...
    reasoning: object | None = ...

class FrameData(pydantic.BaseModel):
    game_id: str = ...
    frame: list[list[list[int]]] = ...
    state: GameState = ...
    levels_completed: int = ...
    win_levels: int = ...
    action_input: ActionInput = ...
    guid: str | None = ...
    full_reset: bool = ...
    available_actions: list[int] = ...
    def is_empty(self) -> bool: ...

class FrameDataRaw(pydantic.BaseModel):
    game_id: str = ...
    state: GameState = ...
    levels_completed: int = ...
    win_levels: int = ...
    action_input: ActionInput = ...
    guid: str | None = ...
    full_reset: bool = ...
    available_actions: list[int] = ...
    @property
    def frame(self) -> list[np.ndarray[tuple[int, int], np.dtype[np.int8]]]: ...
    @frame.setter
    def frame(
        self,
        value: list[np.ndarray[tuple[int, int], np.dtype[np.int8]]],
    ) -> None: ...
    def is_empty(self) -> bool: ...

class Sprite:
    pixels: np.ndarray[tuple[int, int], np.dtype[np.int8]]
    def __init__(
        self,
        pixels: list[list[int]] | np.ndarray[tuple[int, int], np.dtype[np.int8]],
        name: str | None = None,
        x: int = 0,
        y: int = 0,
        layer: int = 0,
        scale: int = 1,
        rotation: int = 0,
        mirror_ud: bool = False,
        mirror_lr: bool = False,
        blocking: BlockingMode = ...,
        interaction: InteractionMode | None = None,
        visible: bool = True,
        collidable: bool = True,
        tags: list[str] = [],
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def x(self) -> int: ...
    @property
    def y(self) -> int: ...
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def layer(self) -> int: ...
    @property
    def tags(self) -> list[str]: ...
    @property
    def is_visible(self) -> bool: ...
    def set_position(self, x: int, y: int) -> Sprite: ...
    def collides_with(self, other: Sprite, ignoreMode: bool = False) -> bool: ...
    def render(self) -> np.ndarray[tuple[int, int], np.dtype[np.int8]]: ...

class PlaceableArea:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        x_scale: int = 1,
        y_scale: int = 1,
    ) -> None: ...

class Level:
    def __init__(
        self,
        sprites: list[Sprite] | None = None,
        grid_size: tuple[int, int] | None = None,
        data: dict[str, object] = {},
        name: str = "Level",
        placeable_areas: list[PlaceableArea] | None = None,
    ) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def grid_size(self) -> tuple[int, int] | None: ...
    def get_data(self, key: str) -> object: ...
    def get_sprites(self) -> list[Sprite]: ...
    def clone(self) -> Level: ...
    # Upstream types this ``dict[str, Any]``; narrowed here since callers must
    # narrow every value on read regardless (see
    # ``arcengine_torch/spine/extract.py``'s ``_json_safe_data``).
    _data: dict[str, object]

class RenderableUserDisplay:
    def render_interface(
        self,
        frame: np.ndarray[tuple[int, int], np.dtype[np.int8]],
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int8]]: ...

class Camera:
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 64,
        height: int = 64,
        background: int = 5,
        letter_box: int = 5,
        interfaces: list[RenderableUserDisplay] = [],
    ) -> None: ...
    @property
    def x(self) -> int: ...
    @x.setter
    def x(self, value: int) -> None: ...
    @property
    def y(self) -> int: ...
    @y.setter
    def y(self, value: int) -> None: ...
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def background(self) -> int: ...
    @property
    def letter_box(self) -> int: ...
    # Both used by ``arcengine_torch/spine/oracle.py``'s ``_sprite_only_render``,
    # which reproduces ``Camera.render`` minus the game's interface passes --
    # the exact split the offline probes (``probe_render_split.py``) measured.
    def _raw_render(
        self,
        sprites: list[Sprite],
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int8]]: ...
    def _calculate_scale_and_offset(self) -> tuple[int, int, int]: ...

class ARCBaseGame:
    def __init__(
        self,
        game_id: str,
        levels: list[Level],
        camera: Camera | None = None,
        debug: bool = False,
        win_score: int = 1,
        available_actions: list[int] = [1, 2, 3, 4, 5, 6],
        seed: int = 0,
    ) -> None: ...
    @overload
    def perform_action(
        self,
        action_input: ActionInput,
        raw: Literal[True],
    ) -> FrameDataRaw: ...
    @overload
    def perform_action(
        self,
        action_input: ActionInput,
        raw: Literal[False] = False,
    ) -> FrameData: ...
    def step(self) -> None: ...
    @property
    def game_id(self) -> str: ...
    @property
    def current_level(self) -> Level: ...
    @property
    def camera(self) -> Camera: ...
    @property
    def level_index(self) -> int: ...
    def set_level(self, index: int) -> None: ...
    def level_reset(self) -> None: ...
    # Both hold every level, cloned independently at construction;
    # ``arcengine_torch/spine/extract.py`` reproduces the exact
    # reset/level-entry sequence ``base_game.py`` itself uses (clone from
    # ``_clean_levels``, then ``set_level``) rather than reading
    # ``_clean_levels`` directly, since a level's ``on_set_level`` hook can
    # mutate it (``tr87``'s fixed-seed rotation setup).
    _clean_levels: list[Level]
    _levels: list[Level]
    # Zeroed by ``set_level`` (full reset, level reset, AND level advance --
    # not only an explicit RESET action); ``arcengine_torch/spine/
    # lifecycle_test.py`` reads this to prove ``reset_is_full``'s documented
    # contract against a live engine. No public accessor.
    _action_count: int
    # ``arcengine_torch/spine/lifecycle_test.py`` reads/sets this to check
    # and arrange ``handle_reset``'s WIN branch against a live engine. No
    # public accessor.
    _state: GameState
