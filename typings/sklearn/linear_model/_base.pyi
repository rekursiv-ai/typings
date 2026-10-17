from abc import ABCMeta, abstractmethod

from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassifierMixin as ClassifierMixin,
    MultiOutputMixin as MultiOutputMixin,
    RegressorMixin as RegressorMixin,
)
from sklearn.utils import (
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils._array_api import (
    get_namespace as get_namespace,
    get_namespace_and_device as get_namespace_and_device,
    indexing_dtype as indexing_dtype,
    supported_float_dtypes as supported_float_dtypes,
)
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils._seq_dataset import (
    ArrayDataset32 as ArrayDataset32,
    ArrayDataset64 as ArrayDataset64,
    CSRDataset32 as CSRDataset32,
    CSRDataset64 as CSRDataset64,
)
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.sparsefuncs import mean_variance_axis as mean_variance_axis
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

SPARSE_INTERCEPT_DECAY: float

def make_dataset(X, y, sample_weight, random_state=None): ...

class LinearModel(BaseEstimator, metaclass=ABCMeta):
    @abstractmethod
    def fit(self, X, y): ...
    def predict(self, X): ...

class LinearClassifierMixin(ClassifierMixin):
    def decision_function(self, X): ...
    def predict(self, X): ...

class SparseCoefMixin:
    coef_: Incomplete
    def densify(self): ...
    def sparsify(self): ...

class LinearRegression(MultiOutputMixin, RegressorMixin, LinearModel):
    fit_intercept: Incomplete
    copy_X: Incomplete
    tol: Incomplete
    n_jobs: Incomplete
    positive: Incomplete
    def __init__(
        self,
        *,
        fit_intercept: bool = True,
        copy_X: bool = True,
        tol: float = 1e-06,
        n_jobs=None,
        positive: bool = False,
    ) -> None: ...
    coef_: Incomplete
    def fit(self, X, y, sample_weight=None): ...
    def __sklearn_tags__(self): ...
