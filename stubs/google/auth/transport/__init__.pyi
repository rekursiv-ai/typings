from typing import Any

class Request:
    def __call__(
        self,
        url: str,
        method: str = ...,
        body: bytes | None = ...,
        headers: dict[str, str] | None = ...,
        timeout: float | None = ...,
        **kwargs: Any,
    ) -> Any: ...
