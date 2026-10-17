from sklearn.metrics.cluster import mutual_info_score as mutual_info_score
from sklearn.neighbors import (
    KDTree as KDTree,
    NearestNeighbors as NearestNeighbors,
)
from sklearn.preprocessing import scale as scale
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.multiclass import (
    check_classification_targets as check_classification_targets,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_array as check_array,
    check_X_y as check_X_y,
)

def mutual_info_regression(
    X,
    y,
    *,
    discrete_features: str = "auto",
    n_neighbors: int = 3,
    copy: bool = True,
    random_state=None,
    n_jobs=None,
): ...
def mutual_info_classif(
    X,
    y,
    *,
    discrete_features: str = "auto",
    n_neighbors: int = 3,
    copy: bool = True,
    random_state=None,
    n_jobs=None,
): ...
