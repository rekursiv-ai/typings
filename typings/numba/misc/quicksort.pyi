from collections.abc import Callable, Sequence
from typing import Literal, Protocol, TypeVar, overload

from numpy.typing import NDArray

import numpy as np

_Scalar = TypeVar("_Scalar", bound=np.generic)
_Value = TypeVar("_Value")

class _Sort(Protocol):
    @overload
    def run_quicksort(self, values: NDArray[_Scalar], /) -> NDArray[_Scalar]: ...
    @overload
    def run_quicksort(self, values: list[_Value], /) -> list[_Value]: ...

class _ArraySort(Protocol):
    def run_quicksort(self, values: NDArray[_Scalar], /) -> NDArray[_Scalar]: ...

class _ArrayArgsort(Protocol):
    def run_quicksort(self, values: NDArray[np.generic], /) -> NDArray[np.intp]: ...

class _ListArgsort(Protocol):
    def run_quicksort(
        self,
        values: Sequence[object] | NDArray[np.generic],
        /,
    ) -> list[int]: ...

class _RowsArgsort(Protocol):
    # A multidimensional is_np_array run returns its original input array.
    def run_quicksort(
        self,
        values: NDArray[_Scalar],
        /,
    ) -> NDArray[_Scalar] | NDArray[np.intp] | list[int]: ...

@overload
def make_py_quicksort(
    lt: Callable[..., object] | None = None,
    *,
    is_argsort: Literal[False] = False,
    is_list: bool = False,
    is_np_array: Literal[False] = False,
) -> _Sort: ...
@overload
def make_py_quicksort(
    lt: Callable[..., object] | None = None,
    *,
    is_argsort: Literal[False] = False,
    is_list: bool = False,
    is_np_array: Literal[True],
) -> _ArraySort: ...
@overload
def make_py_quicksort(
    lt: Callable[..., object] | None = None,
    *,
    is_argsort: Literal[True],
    is_list: Literal[False] = False,
    is_np_array: Literal[False] = False,
) -> _ArrayArgsort: ...
@overload
def make_py_quicksort(
    lt: Callable[..., object] | None = None,
    *,
    is_argsort: Literal[True],
    is_list: Literal[True],
    is_np_array: Literal[False] = False,
) -> _ListArgsort: ...
@overload
def make_py_quicksort(
    lt: Callable[..., object] | None = None,
    *,
    is_argsort: Literal[True],
    is_list: bool = False,
    is_np_array: Literal[True],
) -> _RowsArgsort: ...
@overload
def make_py_quicksort(
    lt: Callable[..., object] | None = None,
    *,
    is_argsort: bool = False,
    is_list: bool = False,
    is_np_array: bool = False,
) -> _Sort | _ArraySort | _ArrayArgsort | _ListArgsort | _RowsArgsort: ...
