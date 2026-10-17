from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator,
    ClassNamePrefixFeaturesOutMixin,
    OneToOneFeatureMixin,
    TransformerMixin,
)
from sklearn.preprocessing._encoders import OneHotEncoder as OneHotEncoder

__all__ = [
    "Binarizer",
    "KernelCenterer",
    "MaxAbsScaler",
    "MinMaxScaler",
    "Normalizer",
    "OneHotEncoder",
    "PowerTransformer",
    "QuantileTransformer",
    "RobustScaler",
    "StandardScaler",
    "add_dummy_feature",
    "binarize",
    "maxabs_scale",
    "minmax_scale",
    "normalize",
    "power_transform",
    "quantile_transform",
    "robust_scale",
    "scale",
]

def scale(
    X,
    *,
    axis: int = 0,
    with_mean: bool = True,
    with_std: bool = True,
    copy: bool = True,
): ...

class MinMaxScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    feature_range: Incomplete
    copy: Incomplete
    clip: Incomplete
    def __init__(
        self,
        feature_range=(0, 1),
        *,
        copy: bool = True,
        clip: bool = False,
    ) -> None: ...
    def fit(self, X, y=None): ...
    n_samples_seen_: Incomplete
    scale_: Incomplete
    min_: Incomplete
    data_min_: Incomplete
    data_max_: Incomplete
    data_range_: Incomplete
    def partial_fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

def minmax_scale(X, feature_range=(0, 1), *, axis: int = 0, copy: bool = True): ...

class StandardScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    with_mean: Incomplete
    with_std: Incomplete
    copy: Incomplete
    def __init__(
        self,
        *,
        copy: bool = True,
        with_mean: bool = True,
        with_std: bool = True,
    ) -> None: ...
    def fit(self, X, y=None, sample_weight=None): ...
    n_samples_seen_: Incomplete
    mean_: Incomplete
    var_: Incomplete
    scale_: Incomplete
    def partial_fit(self, X, y=None, sample_weight=None): ...
    def transform(self, X, copy=None): ...
    def inverse_transform(self, X, copy=None): ...
    def __sklearn_tags__(self): ...

class MaxAbsScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    copy: Incomplete
    clip: Incomplete
    def __init__(self, *, copy: bool = True, clip: bool = False) -> None: ...
    def fit(self, X, y=None): ...
    n_samples_seen_: Incomplete
    max_abs_: Incomplete
    scale_: Incomplete
    def partial_fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

def maxabs_scale(X, *, axis: int = 0, copy: bool = True): ...

class RobustScaler(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    with_centering: Incomplete
    with_scaling: Incomplete
    quantile_range: Incomplete
    unit_variance: Incomplete
    copy: Incomplete
    def __init__(
        self,
        *,
        with_centering: bool = True,
        with_scaling: bool = True,
        quantile_range=(25.0, 75.0),
        copy: bool = True,
        unit_variance: bool = False,
    ) -> None: ...
    center_: Incomplete
    scale_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

def robust_scale(
    X,
    *,
    axis: int = 0,
    with_centering: bool = True,
    with_scaling: bool = True,
    quantile_range=(25.0, 75.0),
    copy: bool = True,
    unit_variance: bool = False,
): ...
def normalize(
    X,
    norm: str = "l2",
    *,
    axis: int = 1,
    copy: bool = True,
    return_norm: bool = False,
): ...

class Normalizer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    norm: Incomplete
    copy: Incomplete
    def __init__(self, norm: str = "l2", *, copy: bool = True) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X, copy=None): ...
    def __sklearn_tags__(self): ...

def binarize(X, *, threshold: float = 0.0, copy: bool = True): ...

class Binarizer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    threshold: Incomplete
    copy: Incomplete
    def __init__(self, *, threshold: float = 0.0, copy: bool = True) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X, copy=None): ...
    def __sklearn_tags__(self): ...

class KernelCenterer(ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator):
    K_fit_rows_: Incomplete
    K_fit_all_: Incomplete
    def fit(self, K, y=None): ...
    def transform(self, K, copy: bool = True): ...
    def __sklearn_tags__(self): ...

def add_dummy_feature(X, value: float = 1.0): ...

class QuantileTransformer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    n_quantiles: Incomplete
    output_distribution: Incomplete
    ignore_implicit_zeros: Incomplete
    subsample: Incomplete
    random_state: Incomplete
    copy: Incomplete
    def __init__(
        self,
        *,
        n_quantiles: int = 1000,
        output_distribution: str = "uniform",
        ignore_implicit_zeros: bool = False,
        subsample: int = 10000,
        random_state=None,
        copy: bool = True,
    ) -> None: ...
    n_quantiles_: Incomplete
    references_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

def quantile_transform(
    X,
    *,
    axis: int = 0,
    n_quantiles: int = 1000,
    output_distribution: str = "uniform",
    ignore_implicit_zeros: bool = False,
    subsample=...,
    random_state=None,
    copy: bool = True,
): ...

class PowerTransformer(OneToOneFeatureMixin, TransformerMixin, BaseEstimator):
    method: Incomplete
    standardize: Incomplete
    copy: Incomplete
    def __init__(
        self,
        method: str = "yeo-johnson",
        *,
        standardize: bool = True,
        copy: bool = True,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def fit_transform(self, X, y=None): ...
    def transform(self, X): ...
    def inverse_transform(self, X): ...
    def __sklearn_tags__(self): ...

def power_transform(
    X,
    method: str = "yeo-johnson",
    *,
    standardize: bool = True,
    copy: bool = True,
): ...
