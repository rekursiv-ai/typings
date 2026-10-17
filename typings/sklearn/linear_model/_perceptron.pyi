from sklearn.linear_model._stochastic_gradient import (
    BaseSGDClassifier as BaseSGDClassifier,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
)

class Perceptron(BaseSGDClassifier):
    def __init__(
        self,
        *,
        penalty=None,
        alpha: float = 0.0001,
        l1_ratio: float = 0.15,
        fit_intercept: bool = True,
        max_iter: int = 1000,
        tol: float = 0.001,
        shuffle: bool = True,
        verbose: int = 0,
        eta0: float = 1.0,
        n_jobs=None,
        random_state: int = 0,
        early_stopping: bool = False,
        validation_fraction: float = 0.1,
        n_iter_no_change: int = 5,
        class_weight=None,
        warm_start: bool = False,
    ) -> None: ...
