from sklearn.utils._array_api import (
    device as device,
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.deprecation import deprecated as deprecated
from sklearn.utils.sparsefuncs import sparse_matmul_to_dense as sparse_matmul_to_dense
from sklearn.utils.sparsefuncs_fast import csr_row_norms as csr_row_norms
from sklearn.utils.validation import (
    check_array as check_array,
    check_random_state as check_random_state,
)

def squared_norm(x): ...
def row_norms(X, squared: bool = False): ...
def fast_logdet(A): ...
def density(w): ...
def safe_sparse_dot(a, b, *, dense_output: bool = False): ...
def randomized_range_finder(
    A,
    *,
    size,
    n_iter,
    power_iteration_normalizer: str = "auto",
    random_state=None,
): ...
def randomized_svd(
    M,
    n_components,
    *,
    n_oversamples: int = 10,
    n_iter: str = "auto",
    power_iteration_normalizer: str = "auto",
    transpose: str = "auto",
    flip_sign: bool = True,
    random_state=None,
    svd_lapack_driver: str = "gesdd",
): ...
def weighted_mode(a, w, *, axis: int = 0): ...
def cartesian(arrays, out=None): ...
def svd_flip(u, v, u_based_decision: bool = True): ...
def softmax(X, copy: bool = True): ...
def make_nonnegative(X, min_value: int = 0): ...
def stable_cumsum(arr, axis=None, rtol: float = 1e-05, atol: float = 1e-08): ...
def safe_sqr(X, *, copy: bool = True): ...
