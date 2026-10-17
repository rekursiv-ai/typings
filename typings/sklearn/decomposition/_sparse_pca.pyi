from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.decomposition._dict_learning import (
    MiniBatchDictionaryLearning as MiniBatchDictionaryLearning,
    dict_learning as dict_learning,
)
from sklearn.linear_model import ridge_regression as ridge_regression
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import svd_flip as svd_flip
from sklearn.utils.validation import (
    check_array as check_array,
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class _BaseSparsePCA(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    n_components: Incomplete
    alpha: Incomplete
    ridge_alpha: Incomplete
    max_iter: Incomplete
    tol: Incomplete
    method: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        alpha: int = 1,
        ridge_alpha: float = 0.01,
        max_iter: int = 1000,
        tol: float = 1e-08,
        method: str = "lars",
        n_jobs=None,
        verbose: bool = False,
        random_state=None,
    ) -> None: ...
    mean_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

class SparsePCA(_BaseSparsePCA):
    U_init: Incomplete
    V_init: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        alpha: int = 1,
        ridge_alpha: float = 0.01,
        max_iter: int = 1000,
        tol: float = 1e-08,
        method: str = "lars",
        n_jobs=None,
        U_init=None,
        V_init=None,
        verbose: bool = False,
        random_state=None,
    ) -> None: ...

class MiniBatchSparsePCA(_BaseSparsePCA):
    callback: Incomplete
    batch_size: Incomplete
    shuffle: Incomplete
    max_no_improvement: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        alpha: int = 1,
        ridge_alpha: float = 0.01,
        max_iter: int = 1000,
        callback=None,
        batch_size: int = 3,
        verbose: bool = False,
        shuffle: bool = True,
        n_jobs=None,
        method: str = "lars",
        random_state=None,
        tol: float = 0.001,
        max_no_improvement: int = 10,
    ) -> None: ...
