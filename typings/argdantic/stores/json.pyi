from pathlib import Path

from argdantic.stores.base import BaseSettingsStore
from pydantic_settings import BaseSettings

class JsonSettingsStore(BaseSettingsStore):
    def __init__(
        self,
        path: str | Path,
        *,
        encoding: str = ...,
        include: set[str] | None = ...,
        exclude: set[str] | None = ...,
        by_alias: bool = ...,
        exclude_unset: bool = ...,
        exclude_defaults: bool = ...,
        exclude_none: bool = ...,
    ) -> None: ...
    def __call__(self, settings: BaseSettings) -> None: ...
