from collections.abc import Iterable, Mapping
from typing import Protocol

class _RawBody(Protocol):
    def stream(self, **kwargs: object) -> Iterable[bytes]: ...

class AWSResponse:
    def __init__(
        self,
        url: str,
        status_code: int,
        headers: Mapping[str, str],
        raw: _RawBody,
    ) -> None: ...
