from collections.abc import Callable
from typing import Literal, Protocol

from numpy.typing import NDArray

import numpy as np

class _Argsort(Protocol):
    run_quicksort: Callable[
        [NDArray[np.float32] | NDArray[np.float64]],
        NDArray[np.int64],
    ]

def make_py_quicksort(*, is_argsort: Literal[True]) -> _Argsort: ...
