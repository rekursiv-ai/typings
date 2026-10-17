from enum import Enum
from typing import Any

from _typeshed import Incomplete

__all__ = ["NUMPY_VERSION", "Backend"]

NUMPY_VERSION: Incomplete

class Backend(Enum):
    ARRAY_API_STRICT = "array_api_strict"
    ARRAY_API_STRICTEST = "array_api_strict:strictest"
    NUMPY = "numpy"
    NUMPY_READONLY = "numpy:readonly"
    CUPY = "cupy"
    TORCH = "torch"
    TORCH_GPU = "torch:gpu"
    DASK = "dask.array"
    SPARSE = "sparse"
    JAX = "jax.numpy"
    JAX_GPU = "jax.numpy:gpu"
    @property
    def modname(self) -> str: ...
    def like(self, *others: Backend) -> bool: ...
    def pytest_param(self) -> Any: ...
