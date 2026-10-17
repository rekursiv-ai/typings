from typing import Any

from google.auth import transport

class Request(transport.Request):
    def __init__(self, session: Any | None = ...) -> None: ...
