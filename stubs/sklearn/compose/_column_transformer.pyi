from _typeshed import Incomplete
from sklearn.base import TransformerMixin
from sklearn.utils.metaestimators import _BaseComposition

__all__ = ["ColumnTransformer", "make_column_selector", "make_column_transformer"]

class ColumnTransformer(TransformerMixin, _BaseComposition):
    transformers: Incomplete
    remainder: Incomplete
    sparse_threshold: Incomplete
    n_jobs: Incomplete
    transformer_weights: Incomplete
    verbose: Incomplete
    verbose_feature_names_out: Incomplete
    force_int_remainder_cols: Incomplete
    def __init__(
        self,
        transformers,
        *,
        remainder: str = "drop",
        sparse_threshold: float = 0.3,
        n_jobs=None,
        transformer_weights=None,
        verbose: bool = False,
        verbose_feature_names_out: bool = True,
        force_int_remainder_cols: str = "deprecated",
    ) -> None: ...
    def set_output(self, *, transform=None): ...
    def get_params(self, deep: bool = True): ...
    def set_params(self, **kwargs): ...
    @property
    def named_transformers_(self): ...
    def get_feature_names_out(self, input_features=None): ...
    def fit(self, X, y=None, **params): ...
    sparse_output_: Incomplete
    def fit_transform(self, X, y=None, **params): ...
    def transform(self, X, **params): ...
    def __getitem__(self, key): ...
    def get_metadata_routing(self): ...
    def __sklearn_tags__(self): ...

def make_column_transformer(
    *transformers,
    remainder: str = "drop",
    sparse_threshold: float = 0.3,
    n_jobs=None,
    verbose: bool = False,
    verbose_feature_names_out: bool = True,
    force_int_remainder_cols: str = "deprecated",
): ...

class make_column_selector:
    pattern: Incomplete
    dtype_include: Incomplete
    dtype_exclude: Incomplete
    def __init__(
        self,
        pattern=None,
        *,
        dtype_include=None,
        dtype_exclude=None,
    ) -> None: ...
    def __call__(self, df): ...
