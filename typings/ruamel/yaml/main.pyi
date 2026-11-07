from pathlib import Path
from typing import IO

from ruamel.yaml.constructor import BaseConstructor
from ruamel.yaml.nodes import Node

class YAML:
    def __init__(
        self,
        *,
        typ: str | list[str] | None = ...,
        pure: bool = ...,
    ) -> None: ...
    @property
    def constructor(self) -> BaseConstructor: ...
    def compose(
        self,
        stream: str | bytes | Path | IO[str] | IO[bytes],
    ) -> Node | None: ...
    def load(self, stream: str | bytes | Path | IO[str] | IO[bytes]) -> object: ...
