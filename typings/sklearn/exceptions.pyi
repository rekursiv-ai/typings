from _typeshed import Incomplete

__all__ = [
    "ConvergenceWarning",
    "DataConversionWarning",
    "DataDimensionalityWarning",
    "EfficiencyWarning",
    "EstimatorCheckFailedWarning",
    "FitFailedWarning",
    "NotFittedError",
    "PositiveSpectrumWarning",
    "SkipTestWarning",
    "UndefinedMetricWarning",
    "UnsetMetadataPassedError",
]

class UnsetMetadataPassedError(ValueError):
    unrequested_params: Incomplete
    routed_params: Incomplete
    def __init__(self, *, message, unrequested_params, routed_params) -> None: ...

class NotFittedError(ValueError, AttributeError): ...
class ConvergenceWarning(UserWarning): ...
class DataConversionWarning(UserWarning): ...
class DataDimensionalityWarning(UserWarning): ...
class EfficiencyWarning(UserWarning): ...
class FitFailedWarning(RuntimeWarning): ...
class SkipTestWarning(UserWarning): ...
class UndefinedMetricWarning(UserWarning): ...
class PositiveSpectrumWarning(UserWarning): ...

class InconsistentVersionWarning(UserWarning):
    estimator_name: Incomplete
    current_sklearn_version: Incomplete
    original_sklearn_version: Incomplete
    def __init__(
        self,
        *,
        estimator_name,
        current_sklearn_version,
        original_sklearn_version,
    ) -> None: ...

class EstimatorCheckFailedWarning(UserWarning):
    estimator: Incomplete
    check_name: Incomplete
    exception: Incomplete
    status: Incomplete
    expected_to_fail: Incomplete
    expected_to_fail_reason: Incomplete
    def __init__(
        self,
        *,
        estimator,
        check_name: str,
        exception: Exception,
        status: str,
        expected_to_fail: bool,
        expected_to_fail_reason: str,
    ) -> None: ...
