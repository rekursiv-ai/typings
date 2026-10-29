from asyncio import AbstractEventLoop
from collections.abc import Awaitable, Callable

__all__ = ["register", "unregister"]

__version__: str

def register(
    callback: Callable[[], Awaitable[object] | object],
    *,
    loop: AbstractEventLoop | None = None,
) -> None: ...
def unregister(
    callback: Callable[[], Awaitable[object] | object],
    *,
    loop: AbstractEventLoop | None = None,
) -> None: ...
