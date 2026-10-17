from collections.abc import Awaitable, Callable, Coroutine
from typing import Literal, overload

from e2b.sandbox.commands.command_handle import CommandResult
from e2b.sandbox_async.commands.command_handle import AsyncCommandHandle

class Commands:
    @overload
    def run(
        self,
        cmd: str,
        background: Literal[False] | None = ...,
        envs: dict[str, str] | None = ...,
        user: str | None = ...,
        cwd: str | None = ...,
        on_stdout: Callable[[str], Awaitable[None] | None] | None = ...,
        on_stderr: Callable[[str], Awaitable[None] | None] | None = ...,
        stdin: bool | None = ...,
        timeout: float | None = ...,
        request_timeout: float | None = ...,
    ) -> Coroutine[object, object, CommandResult]: ...
    @overload
    def run(
        self,
        cmd: str,
        background: Literal[True],
        envs: dict[str, str] | None = ...,
        user: str | None = ...,
        cwd: str | None = ...,
        on_stdout: Callable[[str], Awaitable[None] | None] | None = ...,
        on_stderr: Callable[[str], Awaitable[None] | None] | None = ...,
        stdin: bool | None = ...,
        timeout: float | None = ...,
        request_timeout: float | None = ...,
    ) -> Coroutine[object, object, AsyncCommandHandle]: ...
    def connect(
        self,
        pid: int,
        timeout: float | None = ...,
        request_timeout: float | None = ...,
        on_stdout: Callable[[str], Awaitable[None] | None] | None = ...,
        on_stderr: Callable[[str], Awaitable[None] | None] | None = ...,
    ) -> Coroutine[object, object, AsyncCommandHandle]: ...
    async def send_stdin(
        self,
        pid: int,
        data: str | bytes,
        request_timeout: float | None = ...,
    ) -> None: ...
    async def close_stdin(
        self,
        pid: int,
        request_timeout: float | None = ...,
    ) -> None: ...
