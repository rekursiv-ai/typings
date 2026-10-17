from abc import ABC, abstractmethod
from pathlib import Path

from pydantic_settings import BaseSettings, PydanticBaseSettingsSource
from pydantic_settings.sources import (
    DotEnvSettingsSource as PydanticEnvSource,
    DotenvType,
)

class SettingsSourceBuilder(ABC):
    @abstractmethod
    def __call__(
        self,
        settings_cls: type[BaseSettings],
    ) -> PydanticBaseSettingsSource: ...

class FileSettingsSourceBuilder(SettingsSourceBuilder):
    def __init__(self, path: str | Path) -> None: ...

class FileBaseSettingsSource(PydanticBaseSettingsSource):
    def __init__(self, settings_cls: type[BaseSettings], path: str | Path) -> None: ...

class PydanticMultiEnvSource(PydanticEnvSource): ...

class EnvSettingsSource(SettingsSourceBuilder):
    def __init__(
        self,
        env_file: DotenvType | None,
        env_file_encoding: str | None = ...,
        env_nested_delimiter: str | None = ...,
        env_prefix: str = ...,
        env_case_sensitive: bool = ...,
    ) -> None: ...
    def __call__(
        self,
        settings_cls: type[BaseSettings],
    ) -> PydanticBaseSettingsSource: ...

class SecretsSettingsSource(SettingsSourceBuilder):
    def __init__(
        self,
        secrets_dir: str | Path | None,
        case_sensitive: bool = ...,
        env_prefix: str = ...,
    ) -> None: ...
    def __call__(
        self,
        settings_cls: type[BaseSettings],
    ) -> PydanticBaseSettingsSource: ...
