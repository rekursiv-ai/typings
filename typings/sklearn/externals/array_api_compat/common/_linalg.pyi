from typing import Literal, NamedTuple

from ._aliases import (
    matmul as matmul,
    matrix_transpose as matrix_transpose,
    tensordot as tensordot,
    vecdot as vecdot,
)
from ._typing import Array, DType, JustFloat, JustInt, Namespace

__all__ = [
    "EighResult",
    "QRResult",
    "SVDResult",
    "SlogdetResult",
    "cholesky",
    "cross",
    "diagonal",
    "eigh",
    "matmul",
    "matrix_norm",
    "matrix_rank",
    "matrix_transpose",
    "outer",
    "pinv",
    "qr",
    "slogdet",
    "svd",
    "svdvals",
    "tensordot",
    "trace",
    "vecdot",
    "vector_norm",
]

def cross(
    x1: Array,
    x2: Array,
    /,
    xp: Namespace,
    *,
    axis: int = -1,
    **kwargs: object,
) -> Array: ...
def outer(x1: Array, x2: Array, /, xp: Namespace, **kwargs: object) -> Array: ...

class EighResult(NamedTuple):
    eigenvalues: Array
    eigenvectors: Array

class QRResult(NamedTuple):
    Q: Array
    R: Array

class SlogdetResult(NamedTuple):
    sign: Array
    logabsdet: Array

class SVDResult(NamedTuple):
    U: Array
    S: Array
    Vh: Array

def eigh(x: Array, /, xp: Namespace, **kwargs: object) -> EighResult: ...
def qr(
    x: Array,
    /,
    xp: Namespace,
    *,
    mode: Literal["reduced", "complete"] = "reduced",
    **kwargs: object,
) -> QRResult: ...
def slogdet(x: Array, /, xp: Namespace, **kwargs: object) -> SlogdetResult: ...
def svd(
    x: Array,
    /,
    xp: Namespace,
    *,
    full_matrices: bool = True,
    **kwargs: object,
) -> SVDResult: ...
def cholesky(
    x: Array,
    /,
    xp: Namespace,
    *,
    upper: bool = False,
    **kwargs: object,
) -> Array: ...
def matrix_rank(
    x: Array,
    /,
    xp: Namespace,
    *,
    rtol: float | Array | None = None,
    **kwargs: object,
) -> Array: ...
def pinv(
    x: Array,
    /,
    xp: Namespace,
    *,
    rtol: float | Array | None = None,
    **kwargs: object,
) -> Array: ...
def matrix_norm(
    x: Array,
    /,
    xp: Namespace,
    *,
    keepdims: bool = False,
    ord: Literal[1, 2, -1, -2, "fro", "nuc"] | JustFloat | None = "fro",
) -> Array: ...
def svdvals(x: Array, /, xp: Namespace) -> Array | tuple[Array, ...]: ...
def vector_norm(
    x: Array,
    /,
    xp: Namespace,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
    ord: JustInt | JustFloat = 2,
) -> Array: ...
def diagonal(
    x: Array,
    /,
    xp: Namespace,
    *,
    offset: int = 0,
    **kwargs: object,
) -> Array: ...
def trace(
    x: Array,
    /,
    xp: Namespace,
    *,
    offset: int = 0,
    dtype: DType | None = None,
    **kwargs: object,
) -> Array: ...
