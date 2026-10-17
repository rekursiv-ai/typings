from _typeshed import Incomplete
from sklearn.decomposition._base import _BasePCA
from sklearn.utils import (
    gen_batches as gen_batches,
    metadata_routing as metadata_routing,
)
from sklearn.utils._param_validation import Interval as Interval
from sklearn.utils.extmath import svd_flip as svd_flip
from sklearn.utils.validation import validate_data as validate_data

class IncrementalPCA(_BasePCA):
    n_components: Incomplete
    whiten: Incomplete
    copy: Incomplete
    batch_size: Incomplete
    def __init__(
        self,
        n_components=None,
        *,
        whiten: bool = False,
        copy: bool = True,
        batch_size=None,
    ) -> None: ...
    components_: Incomplete
    n_samples_seen_: int
    mean_: float
    var_: float
    singular_values_: Incomplete
    explained_variance_: Incomplete
    explained_variance_ratio_: Incomplete
    noise_variance_: Incomplete
    batch_size_: Incomplete
    def fit(self, X, y=None): ...
    n_components_: Incomplete
    def partial_fit(self, X, y=None, check_input: bool = True): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...
