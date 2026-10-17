from collections.abc import Generator

from _typeshed import Incomplete
from sklearn import config_context as config_context
from sklearn.exceptions import DataConversionWarning as DataConversionWarning
from sklearn.metrics._pairwise_distances_reduction import ArgKmin as ArgKmin
from sklearn.preprocessing import normalize as normalize
from sklearn.utils import (
    check_array as check_array,
    gen_batches as gen_batches,
    gen_even_slices as gen_even_slices,
)
from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
)
from sklearn.utils._chunking import get_chunk_n_rows as get_chunk_n_rows
from sklearn.utils._missing import is_scalar_nan as is_scalar_nan
from sklearn.utils._param_validation import (
    Hidden as Hidden,
    Interval as Interval,
    MissingValues as MissingValues,
    Options as Options,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.extmath import (
    row_norms as row_norms,
    safe_sparse_dot as safe_sparse_dot,
)
from sklearn.utils.fixes import (
    parse_version as parse_version,
    sp_base_version as sp_base_version,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import check_non_negative as check_non_negative

def check_pairwise_arrays(
    X,
    Y,
    *,
    precomputed: bool = False,
    dtype: str = "infer_float",
    accept_sparse: str = "csr",
    ensure_all_finite: bool = True,
    ensure_2d: bool = True,
    copy: bool = False,
): ...
def check_paired_arrays(X, Y): ...
def euclidean_distances(
    X,
    Y=None,
    *,
    Y_norm_squared=None,
    squared: bool = False,
    X_norm_squared=None,
): ...
def nan_euclidean_distances(
    X,
    Y=None,
    *,
    squared: bool = False,
    missing_values=...,
    copy: bool = True,
): ...
def pairwise_distances_argmin_min(
    X,
    Y,
    *,
    axis: int = 1,
    metric: str = "euclidean",
    metric_kwargs=None,
): ...
def pairwise_distances_argmin(
    X,
    Y,
    *,
    axis: int = 1,
    metric: str = "euclidean",
    metric_kwargs=None,
): ...
def haversine_distances(X, Y=None): ...
def manhattan_distances(X, Y=None): ...
def cosine_distances(X, Y=None): ...
def paired_euclidean_distances(X, Y): ...
def paired_manhattan_distances(X, Y): ...
def paired_cosine_distances(X, Y): ...

PAIRED_DISTANCES: Incomplete

def paired_distances(X, Y, *, metric: str = "euclidean", **kwds): ...
def linear_kernel(X, Y=None, dense_output: bool = True): ...
def polynomial_kernel(X, Y=None, degree: int = 3, gamma=None, coef0: int = 1): ...
def sigmoid_kernel(X, Y=None, gamma=None, coef0: int = 1): ...
def rbf_kernel(X, Y=None, gamma=None): ...
def laplacian_kernel(X, Y=None, gamma=None): ...
def cosine_similarity(X, Y=None, dense_output: bool = True): ...
def additive_chi2_kernel(X, Y=None): ...
def chi2_kernel(X, Y=None, gamma: float = 1.0): ...

PAIRWISE_DISTANCE_FUNCTIONS: Incomplete

def distance_metrics(): ...
def pairwise_distances_chunked(
    X,
    Y=None,
    *,
    reduce_func=None,
    metric: str = "euclidean",
    n_jobs=None,
    working_memory=None,
    **kwds,
) -> Generator[Incomplete]: ...
def pairwise_distances(
    X,
    Y=None,
    metric: str = "euclidean",
    *,
    n_jobs=None,
    ensure_all_finite: bool = True,
    **kwds,
): ...

PAIRWISE_BOOLEAN_FUNCTIONS: Incomplete
PAIRWISE_KERNEL_FUNCTIONS: Incomplete

def kernel_metrics(): ...

KERNEL_PARAMS: Incomplete

def pairwise_kernels(
    X,
    Y=None,
    metric: str = "linear",
    *,
    filter_params: bool = False,
    n_jobs=None,
    **kwds,
): ...
