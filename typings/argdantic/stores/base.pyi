from abc import ABC, abstractmethod
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings

type SettingsStoreCallable = Callable[[BaseSettings | BaseModel], None]

class BaseSettingsStore(ABC):
    def __init__(
        self,
        path: str | Path,
        *,
        mode: Literal["python", "json"] = ...,
        encoding: str = ...,
        include: set[str] | None = ...,
        exclude: set[str] | None = ...,
        by_alias: bool = ...,
        exclude_unset: bool = ...,
        exclude_defaults: bool = ...,
        exclude_none: bool = ...,
    ) -> None: ...
    @abstractmethod
    def __call__(self, settings: BaseSettings) -> None: ...
