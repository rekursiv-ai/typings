from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.metrics.pairwise import (
    KERNEL_PARAMS as KERNEL_PARAMS,
    PAIRWISE_KERNEL_FUNCTIONS as PAIRWISE_KERNEL_FUNCTIONS,
    pairwise_kernels as pairwise_kernels,
)
from sklearn.utils import check_random_state as check_random_state
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.extmath import safe_sparse_dot as safe_sparse_dot
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    validate_data as validate_data,
)

class PolynomialCountSketch(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    BaseEstimator,
):
    gamma: Incomplete
    degree: Incomplete
    coef0: Incomplete
    n_components: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        *,
        gamma: float = 1.0,
        degree: int = 2,
        coef0: int = 0,
        n_components: int = 100,
        random_state=None,
    ) -> None: ...
    indexHash_: Incomplete
    bitHash_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...

class RBFSampler(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    gamma: Incomplete
    n_components: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        *,
        gamma: float = 1.0,
        n_components: int = 100,
        random_state=None,
    ) -> None: ...
    random_weights_: Incomplete
    random_offset_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...

class SkewedChi2Sampler(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    BaseEstimator,
):
    skewedness: Incomplete
    n_components: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        *,
        skewedness: float = 1.0,
        n_components: int = 100,
        random_state=None,
    ) -> None: ...
    random_weights_: Incomplete
    random_offset_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...

class AdditiveChi2Sampler(TransformerMixin, BaseEstimator):
    sample_steps: Incomplete
    sample_interval: Incomplete
    def __init__(self, *, sample_steps: int = 2, sample_interval=None) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
    def __sklearn_tags__(self): ...

class Nystroem(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    kernel: Incomplete
    gamma: Incomplete
    coef0: Incomplete
    degree: Incomplete
    kernel_params: Incomplete
    n_components: Incomplete
    random_state: Incomplete
    n_jobs: Incomplete
    def __init__(
        self,
        kernel: str = "rbf",
        *,
        gamma=None,
        coef0=None,
        degree=None,
        kernel_params=None,
        n_components: int = 100,
        random_state=None,
        n_jobs=None,
    ) -> None: ...
    normalization_: Incomplete
    components_: Incomplete
    component_indices_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...
