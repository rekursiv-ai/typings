from typing import Any

class Pickler:
    keys: bool
    _objs: dict[int, int]
    def __init__(
        self,
        unpicklable: bool = ...,
        make_refs: bool = ...,
        max_depth: int | None = ...,
        backend: Any = ...,
        keys: bool = ...,
        warn: bool = ...,
        max_iter: int | None = ...,
        numeric_keys: bool = ...,
        use_decimal: bool = ...,
        use_base85: bool = ...,
        fail_safe: Any = ...,
        include_properties: bool = ...,
        handle_readonly: bool = ...,
        original_object: Any = ...,
    ) -> None: ...
    def flatten(self, obj: object, reset: bool = ...) -> Any: ...
    def _flatten(self, obj: object) -> Any: ...
    def _flatten_obj_instance(self, obj: object) -> Any: ...
    def _flatten_key_value_pair(
        self,
        k: object,
        v: object,
        data: dict[str, Any],
    ) -> dict[str, Any]: ...
    def _flatten_string_key_value_pair(
        self,
        k: object,
        v: object,
        data: dict[str, Any],
    ) -> dict[str, Any]: ...
    def _flatten_non_string_key_value_pair(
        self,
        k: object,
        v: object,
        data: dict[str, Any],
    ) -> dict[str, Any]: ...
    def _escape_key(self, k: object) -> str: ...
    def _pickle_warning(self, obj: object) -> None: ...
