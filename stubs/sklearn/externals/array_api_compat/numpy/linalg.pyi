from _typeshed import Incomplete
from numpy.linalg import (
    LinAlgError as LinAlgError,
    cond as cond,
    det as det,
    eig as eig,
    eigvals as eigvals,
    eigvalsh as eigvalsh,
    inv as inv,
    lstsq as lstsq,
    matrix_power as matrix_power,
    multi_dot as multi_dot,
    norm as norm,
    tensorinv as tensorinv,
    tensorsolve as tensorsolve,
)

from ._aliases import (
    matmul as matmul,
    matrix_transpose as matrix_transpose,
    tensordot as tensordot,
    vecdot as vecdot,
)
from ._typing import Array

__all__ = [
    "EighResult",
    "LinAlgError",
    "QRResult",
    "SVDResult",
    "SlogdetResult",
    "cholesky",
    "cond",
    "cross",
    "det",
    "diagonal",
    "eig",
    "eigh",
    "eigvals",
    "eigvalsh",
    "inv",
    "lstsq",
    "matmul",
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
    "svd",
    "svdvals",
    "tensordot",
    "tensorinv",
    "tensorsolve",
    "trace",
    "vecdot",
    "vector_norm",
]

cross: Incomplete
outer: Incomplete
EighResult: Incomplete
QRResult: Incomplete
SlogdetResult: Incomplete
SVDResult: Incomplete
eigh: Incomplete
qr: Incomplete
slogdet: Incomplete
svd: Incomplete
cholesky: Incomplete
matrix_rank: Incomplete
pinv: Incomplete
matrix_norm: Incomplete
svdvals: Incomplete
diagonal: Incomplete
trace: Incomplete

def solve(x1: Array, x2: Array, /) -> Array: ...

vector_norm: Incomplete
