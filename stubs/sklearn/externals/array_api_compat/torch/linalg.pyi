from torch import outer as outer
from torch.linalg import *

from ._aliases import (
    matmul as matmul,
    matrix_transpose as matrix_transpose,
    tensordot as tensordot,
)
from ._typing import Array, DType
from ..common._typing import JustFloat, JustInt

__all__ = [
    "LinAlgError",
    "cholesky",
    "cholesky_ex",
    "common_notes",
    "cond",
    "cross",
    "det",
    "diagonal",
    "eig",
    "eigh",
    "eigvals",
    "eigvalsh",
    "householder_product",
    "inv",
    "inv_ex",
    "ldl_factor",
    "ldl_factor_ex",
    "ldl_solve",
    "lstsq",
    "lu",
    "lu_factor",
    "lu_factor_ex",
    "lu_solve",
    "matmul",
    "matrix_exp",
    "matrix_norm",
    "matrix_power",
    "matrix_rank",
    "matrix_transpose",
    "multi_dot",
    "norm",
    "outer",
    "pinv",
    "qr",
    "slogdet",
    "solve",
    "solve_ex",
    "solve_triangular",
    "svd",
    "svdvals",
    "tensordot",
    "tensorinv",
    "tensorsolve",
    "trace",
    "vander",
    "vecdot",
    "vector_norm",
]

def cross(x1: Array, x2: Array, /, *, axis: int = -1) -> Array: ...
def vecdot(x1: Array, x2: Array, /, *, axis: int = -1, **kwargs) -> Array: ...
def solve(x1: Array, x2: Array, /, **kwargs) -> Array: ...
def trace(x: Array, /, *, offset: int = 0, dtype: DType | None = None) -> Array: ...
def vector_norm(
    x: Array,
    /,
    *,
    axis: int | tuple[int, ...] | None = None,
    keepdims: bool = False,
    ord: JustInt | JustFloat = 2,
    **kwargs,
) -> Array: ...

# Names in __all__ with no definition:
#   LinAlgError
#   cholesky
#   cholesky_ex
#   common_notes
#   cond
#   det
#   diagonal
#   eig
#   eigh
#   eigvals
#   eigvalsh
#   householder_product
#   inv
#   inv_ex
#   ldl_factor
#   ldl_factor_ex
#   ldl_solve
#   lstsq
#   lu
#   lu_factor
#   lu_factor_ex
#   lu_solve
#   matrix_exp
#   matrix_norm
#   matrix_power
#   matrix_rank
#   multi_dot
#   norm
#   pinv
#   qr
#   slogdet
#   solve_ex
#   solve_triangular
#   svd
#   svdvals
#   tensorinv
#   tensorsolve
#   vander
