from datetime import datetime

from google.auth import transport

class Credentials:
    token: str | None
    expiry: datetime | None

    @property
    def valid(self) -> bool: ...
    @property
    def expired(self) -> bool: ...
    def refresh(self, request: transport.Request) -> None: ...
    def apply(self, headers: dict[str, str], token: str | None = ...) -> None: ...
