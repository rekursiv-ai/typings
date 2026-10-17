from typing import Any

from argdantic.sources.base import FileBaseSettingsSource
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

DEFAULT_SOURCE_FIELD = ...

class DynamicFileSource(PydanticBaseSettingsSource):
    def __init__(
        self,
        settings_cls: type[BaseSettings],
        source_cls: type[FileBaseSettingsSource],
        init_kwargs: dict[str, Any],
        required: bool,
        field_name: str | None = ...,
    ) -> None: ...
    def get_field_value(self, field: Any, field_name: str) -> tuple[Any, str, bool]: ...
    def __call__(self) -> dict[str, Any]: ...

def from_file(
    loader: type[FileBaseSettingsSource],
    use_field: str | None = ...,
    required: bool = ...,
):  # -> Callable[..., type[DynamicSourceSettings]]:
    ...
