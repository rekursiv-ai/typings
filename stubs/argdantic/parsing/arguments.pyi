from abc import ABC, abstractmethod
from argparse import ArgumentParser
from collections import abc, deque
from collections.abc import Iterator, Mapping, Sequence
from enum import Enum
from typing import (
    Any,
    Literal,
)

from argdantic.parsing.actions import Action

registry = ...
cli_types: dict[str, tuple[Any, str]] = ...
cli_default = ...

class ActionTracker:
    def __init__(self, action_class: type[Action]) -> None: ...
    def __call__(self, option_strings: Sequence[str], dest: str, **kwargs) -> Any: ...
    def is_set(self) -> bool: ...

class MultiActionTracker(ActionTracker):
    def __init__(self, trackers: list[ActionTracker]) -> None: ...
    def is_set(self) -> bool: ...

class Argument(ABC):
    def __init__(
        self,
        *field_names: str,
        identifier: str,
        field_type: type[Any],
        default: Any = ...,
        required: bool = ...,
        description: str | None = ...,
    ) -> None: ...
    @abstractmethod
    def build(self, parser: ArgumentParser) -> ActionTracker: ...
    def build_internal(
        self,
        parser: ArgumentParser,
        *,
        action: type[Action],
        **optional_fields: Any,
    ) -> ActionTracker: ...

class PrimitiveArgument(Argument):
    def build(self, parser: ArgumentParser) -> ActionTracker: ...

@registry.register(bool)
class FlagArgument(Argument):
    def build(self, parser: ArgumentParser) -> ActionTracker: ...

@registry.register(
    list,
    tuple,
    set,
    frozenset,
    range,
    deque,
    abc.Sequence,
    abc.Iterable,
)
class MultipleArgument(Argument):
    def build(self, parser: ArgumentParser) -> ActionTracker: ...

@registry.register(Literal, Enum)
class ChoiceArgument(Argument):
    def __contains__(self, item: Any) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __next__(self) -> Any: ...
    def __len__(self) -> int: ...
    def convert(self, name: Any) -> Any: ...
    def build(self, parser: ArgumentParser) -> ActionTracker: ...

@registry.register(dict, dict, Mapping)
class DictArgument(Argument):
    def build(self, parser: ArgumentParser) -> ActionTracker: ...
