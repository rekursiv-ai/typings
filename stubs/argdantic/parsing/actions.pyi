from argparse import (
    Action as Action,
    ArgumentParser,
    Namespace,
)
from collections.abc import Sequence
from typing import Any

class StoreAction(Action):
    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        nargs: int | str | None = ...,
        **kwargs,
    ) -> None: ...
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: Sequence[Any] | str | None,
        option_string: str | None = ...,
    ) -> None: ...
    @property
    def specified(self) -> bool: ...

class StoreConstAction(StoreAction):
    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        const: Any,
        nargs: int | str = ...,
        **kwargs: dict,
    ) -> None: ...
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: Sequence[Any] | str | None,
        option_string: str | None = ...,
    ) -> None: ...

class StoreTrueAction(StoreConstAction):
    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        **kwargs: Any,
    ) -> None: ...

class StoreFalseAction(StoreConstAction):
    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        **kwargs: Any,
    ) -> None: ...

class AppendAction(StoreAction):
    def __init__(
        self,
        option_strings: Sequence[str],
        dest: str,
        nargs: int | str | None,
        const: Any | None = ...,
        **kargs: dict,
    ) -> None: ...
    def __call__(
        self,
        parser: ArgumentParser,
        namespace: Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = ...,
    ) -> None: ...
