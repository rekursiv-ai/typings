from collections.abc import Iterator, Mapping, MutableMapping
from types import TracebackType
from typing import Any, Self

from numpy import bytes_, dtype, generic, object_

__version__: str

def string_dtype(
    encoding: str = ...,
    length: int | None = ...,
) -> dtype[object_ | bytes_]: ...

class Dataset:
    @property
    def name(self) -> str | None: ...
    shape: tuple[int, ...]
    @property
    def chunks(self) -> tuple[int, ...] | None: ...
    dtype: dtype[generic]
    attrs: MutableMapping[str, object]
    def __getitem__(self, key: Any) -> Any: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __len__(self) -> int: ...
    def resize(self, size: tuple[int, ...] | int, axis: int | None = ...) -> None: ...

class Group(Mapping[str, Group | Dataset]):
    @property
    def name(self) -> str | None: ...
    def __getitem__(self, key: str) -> Group | Dataset: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def create_dataset(
        self,
        name: str,
        shape: Any = ...,
        dtype: Any = ...,
        data: Any = ...,
        **kwargs: Any,
    ) -> Dataset: ...
    def create_group(self, name: str) -> Group: ...
    attrs: MutableMapping[str, object]

class File(Group):
    def __init__(
        self,
        name: Any,
        mode: str = ...,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def close(self) -> None: ...
