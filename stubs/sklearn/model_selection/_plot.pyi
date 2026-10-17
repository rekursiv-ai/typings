from _typeshed import Incomplete
from sklearn.model_selection._validation import (
    learning_curve as learning_curve,
    validation_curve as validation_curve,
)
from sklearn.utils._optional_dependencies import (
    check_matplotlib_support as check_matplotlib_support,
)

class _BaseCurveDisplay: ...

class LearningCurveDisplay(_BaseCurveDisplay):
    train_sizes: Incomplete
    train_scores: Incomplete
    test_scores: Incomplete
    score_name: Incomplete
    def __init__(
        self,
        *,
        train_sizes,
        train_scores,
        test_scores,
        score_name=None,
    ) -> None: ...
    def plot(
        self,
        ax=None,
        *,
        negate_score: bool = False,
        score_name=None,
        score_type: str = "both",
        std_display_style: str = "fill_between",
        line_kw=None,
        fill_between_kw=None,
        errorbar_kw=None,
    ): ...
    @classmethod
    def from_estimator(
        cls,
        estimator,
        X,
        y,
        *,
        groups=None,
        train_sizes=...,
        cv=None,
        scoring=None,
        exploit_incremental_learning: bool = False,
        n_jobs=None,
        pre_dispatch: str = "all",
        verbose: int = 0,
        shuffle: bool = False,
        random_state=None,
        error_score=...,
        fit_params=None,
        ax=None,
        negate_score: bool = False,
        score_name=None,
        score_type: str = "both",
        std_display_style: str = "fill_between",
        line_kw=None,
        fill_between_kw=None,
        errorbar_kw=None,
    ): ...

class ValidationCurveDisplay(_BaseCurveDisplay):
    param_name: Incomplete
    param_range: Incomplete
    train_scores: Incomplete
    test_scores: Incomplete
    score_name: Incomplete
    def __init__(
        self,
        *,
        param_name,
        param_range,
        train_scores,
        test_scores,
        score_name=None,
    ) -> None: ...
    def plot(
        self,
        ax=None,
        *,
        negate_score: bool = False,
        score_name=None,
        score_type: str = "both",
        std_display_style: str = "fill_between",
        line_kw=None,
        fill_between_kw=None,
        errorbar_kw=None,
    ): ...
    @classmethod
    def from_estimator(
        cls,
        estimator,
        X,
        y,
        *,
        param_name,
        param_range,
        groups=None,
        cv=None,
        scoring=None,
        n_jobs=None,
        pre_dispatch: str = "all",
        verbose: int = 0,
        error_score=...,
        fit_params=None,
        ax=None,
        negate_score: bool = False,
        score_name=None,
        score_type: str = "both",
        std_display_style: str = "fill_between",
        line_kw=None,
        fill_between_kw=None,
        errorbar_kw=None,
    ): ...
