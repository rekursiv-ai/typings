from typing import Any

from argdantic.sources.base import FileBaseSettingsSource, FileSettingsSourceBuilder
from pydantic.fields import FieldInfo
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

class YamlFileLoader(FileBaseSettingsSource):
    def get_field_value(
        self,
        field: FieldInfo,
        field_name: str,
    ) -> tuple[Any, str, bool]: ...
    def __call__(self) -> dict[str, Any]: ...

class YamlSettingsSource(FileSettingsSourceBuilder):
    def __call__(
        self,
        settings_cls: type[BaseSettings],
    ) -> PydanticBaseSettingsSource: ...
