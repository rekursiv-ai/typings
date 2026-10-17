from sklearn.externals.array_api_compat import is_numpy_array as is_numpy_array
from sklearn.metrics.pairwise import (
    pairwise_distances as pairwise_distances,
    pairwise_distances_chunked as pairwise_distances_chunked,
)
from sklearn.preprocessing import LabelEncoder as LabelEncoder
from sklearn.utils import (
    check_random_state as check_random_state,
    check_X_y as check_X_y,
)
from sklearn.utils._array_api import (
    get_namespace_and_device as get_namespace_and_device,
    xpx as xpx,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)

def check_number_of_labels(n_labels, n_samples) -> None: ...
def silhouette_score(
    X,
    labels,
    *,
    metric: str = "euclidean",
    sample_size=None,
    random_state=None,
    **kwds,
): ...
def silhouette_samples(X, labels, *, metric: str = "euclidean", **kwds): ...
def calinski_harabasz_score(X, labels): ...
def davies_bouldin_score(X, labels): ...
