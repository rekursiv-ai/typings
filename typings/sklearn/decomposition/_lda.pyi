from _typeshed import Incomplete
from sklearn.base import (
    BaseEstimator as BaseEstimator,
    ClassNamePrefixFeaturesOutMixin as ClassNamePrefixFeaturesOutMixin,
    TransformerMixin as TransformerMixin,
)
from sklearn.utils import (
    check_random_state as check_random_state,
    gen_batches as gen_batches,
    gen_even_slices as gen_even_slices,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)
from sklearn.utils.validation import (
    check_is_fitted as check_is_fitted,
    check_non_negative as check_non_negative,
    validate_data as validate_data,
)

EPS: Incomplete

class LatentDirichletAllocation(
    ClassNamePrefixFeaturesOutMixin,
    TransformerMixin,
    BaseEstimator,
):
    n_components: Incomplete
    doc_topic_prior: Incomplete
    topic_word_prior: Incomplete
    learning_method: Incomplete
    learning_decay: Incomplete
    learning_offset: Incomplete
    max_iter: Incomplete
    batch_size: Incomplete
    evaluate_every: Incomplete
    total_samples: Incomplete
    perp_tol: Incomplete
    mean_change_tol: Incomplete
    max_doc_update_iter: Incomplete
    n_jobs: Incomplete
    verbose: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_components: int = 10,
        *,
        doc_topic_prior=None,
        topic_word_prior=None,
        learning_method: str = "batch",
        learning_decay: float = 0.7,
        learning_offset: float = 10.0,
        max_iter: int = 10,
        batch_size: int = 128,
        evaluate_every: int = -1,
        total_samples: float = 1000000.0,
        perp_tol: float = 0.1,
        mean_change_tol: float = 0.001,
        max_doc_update_iter: int = 100,
        n_jobs=None,
        verbose: int = 0,
        random_state=None,
    ) -> None: ...
    def __sklearn_tags__(self): ...
    def partial_fit(self, X, y=None): ...
    bound_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X, *, normalize: bool = True): ...
    def fit_transform(self, X, y=None, *, normalize: bool = True): ...
    def score(self, X, y=None): ...
    def perplexity(self, X, sub_sampling: bool = False): ...
