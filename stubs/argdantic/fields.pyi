from collections.abc import Sequence
from typing import Any

def ArgField(
    *names: Sequence[str] | None,
    default: Any | None = ...,
    description: str | None = ...,
    **extra: Any,
) -> Any: ...
