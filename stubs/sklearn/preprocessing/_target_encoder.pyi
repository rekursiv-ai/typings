from _typeshed import Incomplete
from sklearn.base import OneToOneFeatureMixin as OneToOneFeatureMixin
from sklearn.preprocessing._encoders import _BaseEncoder
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.multiclass import type_of_target as type_of_target
from sklearn.utils.validation import (
    check_consistent_length as check_consistent_length,
    check_is_fitted as check_is_fitted,
)

class TargetEncoder(OneToOneFeatureMixin, _BaseEncoder):
    categories: Incomplete
    smooth: Incomplete
    target_type: Incomplete
    cv: Incomplete
    shuffle: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        categories: str = "auto",
        target_type: str = "auto",
        smooth: str = "auto",
        cv: int = 5,
        shuffle: bool = True,
        random_state=None,
    ) -> None: ...
    def fit(self, X, y): ...
    def fit_transform(self, X, y): ...
    def transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
    def __sklearn_tags__(self): ...
