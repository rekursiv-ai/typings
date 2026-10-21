from collections.abc import Sequence
from types import TracebackType
from typing import Any, Self

import httpx2

class TestClient(httpx2.Client):
    app: Any
    def __init__(
        self,
        app: Any,
        base_url: str = ...,
        *,
        follow_redirects: bool = ...,
        **kwargs: Any,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def websocket_connect(
        self,
        url: str,
        subprotocols: Sequence[str] | None = ...,
        **kwargs: object,
    ) -> WebSocketTestSession: ...

class WebSocketTestSession:
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None: ...
    def send_bytes(self, data: bytes) -> None: ...
    def receive_bytes(self) -> bytes: ...
