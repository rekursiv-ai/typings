from typing import Any

class Unpickler:
    _objs: list[Any]
    def __init__(
        self,
        backend: Any = ...,
        keys: bool = ...,
        safe: bool = ...,
        v1_decode: bool = ...,
        on_missing: str = ...,
        handle_readonly: bool = ...,
    ) -> None: ...
    def restore(self, obj: object, reset: bool = ..., classes: Any = ...) -> Any: ...
    def _restore(self, obj: object) -> Any: ...
    def _restore_id(self, obj: dict[str, Any]) -> object: ...
