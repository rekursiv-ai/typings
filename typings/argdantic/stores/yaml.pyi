from argdantic.stores.base import BaseSettingsStore
from pydantic_settings import BaseSettings

class YamlSettingsStore(BaseSettingsStore):
    def __call__(self, settings: BaseSettings) -> None: ...
