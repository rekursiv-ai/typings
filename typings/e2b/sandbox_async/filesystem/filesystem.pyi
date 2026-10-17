from typing import BinaryIO, Literal, TextIO

from e2b.sandbox.filesystem.filesystem import WriteInfo

class Filesystem:
    async def read(
        self,
        path: str,
        format: Literal["bytes"],
        user: str | None = ...,
        request_timeout: float | None = ...,
    ) -> bytearray: ...
    async def write(
        self,
        path: str,
        data: str | bytes | BinaryIO | TextIO,
        user: str | None = ...,
        request_timeout: float | None = ...,
    ) -> WriteInfo: ...
