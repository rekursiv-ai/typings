from collections.abc import Awaitable, Callable
from typing import Literal, overload

__all__ = [
    "RTCConfiguration",
    "RTCDataChannel",
    "RTCIceServer",
    "RTCPeerConnection",
    "RTCSessionDescription",
]

class RTCIceServer:
    def __init__(
        self,
        urls: str | list[str],
        username: str | None = None,
        credential: str | None = None,
    ) -> None: ...

class RTCConfiguration:
    def __init__(self, iceServers: list[RTCIceServer] | None = None) -> None: ...

class RTCSessionDescription:
    sdp: str
    type: str
    def __init__(self, sdp: str, type: str) -> None: ...

class RTCDataChannel:
    @property
    def readyState(self) -> str: ...
    def send(self, data: bytes | str) -> None: ...
    def close(self) -> None: ...
    @overload
    def on(
        self,
        event: Literal["message"],
        f: Callable[[bytes | str], None],
    ) -> Callable[[bytes | str], None]: ...
    @overload
    def on(
        self,
        event: Literal["close"],
        f: Callable[[], None],
    ) -> Callable[[], None]: ...

class RTCPeerConnection:
    def __init__(self, configuration: RTCConfiguration | None = None) -> None: ...
    @property
    def connectionState(self) -> str: ...
    @property
    def localDescription(self) -> RTCSessionDescription: ...
    async def createAnswer(self) -> RTCSessionDescription: ...
    async def setLocalDescription(
        self,
        sessionDescription: RTCSessionDescription,
    ) -> None: ...
    async def setRemoteDescription(
        self,
        sessionDescription: RTCSessionDescription,
    ) -> None: ...
    async def close(self) -> None: ...
    @overload
    def on(
        self,
        event: Literal["datachannel"],
        f: Callable[[RTCDataChannel], None],
    ) -> Callable[[RTCDataChannel], None]: ...
    @overload
    def on(
        self,
        event: Literal["connectionstatechange"],
        f: Callable[[], None] | Callable[[], Awaitable[None]],
    ) -> Callable[[], None] | Callable[[], Awaitable[None]]: ...
