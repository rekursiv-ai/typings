from argparse import ArgumentParser, Namespace
from collections.abc import Callable, Iterable
from typing import Any, Generic, TypeVar

from argdantic.parsing import Argument
from argdantic.stores import SettingsStoreCallable
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings.sources import PydanticBaseSettingsSource

type SettingSourceCallable = Callable[[type[BaseSettings]], PydanticBaseSettingsSource]
ParserType = TypeVar("ParserType", bound=ArgParser)

class Command:
    def __init__(
        self,
        callback: Callable,
        arguments: Iterable[Argument],
        model_class: type[BaseModel],
        name: str,
        description: str | None = ...,
        singleton: bool = ...,
        stores: list[SettingsStoreCallable] | None = ...,
        delimiter: str = ...,
    ) -> None: ...
    def __call__(self, args: Namespace) -> Any: ...
    def build(self, parser: ArgumentParser) -> None: ...

class ArgParser(Generic[ParserType]):
    def __init__(
        self,
        name: str | None = ...,
        description: str | None = ...,
        force_group: bool = ...,
        delimiter: str = ...,
        internal_delimiter: str = ...,
        subcommand_meta: str = ...,
    ) -> None: ...
    def __call__(self, args: Namespace | None = ...) -> Any: ...
    def command(
        self,
        name: str | None = ...,
        help: str | None = ...,
        sources: list[SettingSourceCallable] | None = ...,
        stores: list[SettingsStoreCallable] | None = ...,
        singleton: bool = ...,
    ) -> Callable: ...
    def add_parser(self, parser: ParserType, name: str | None = ...) -> None: ...
