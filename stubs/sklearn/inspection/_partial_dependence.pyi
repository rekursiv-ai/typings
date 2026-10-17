__all__ = ["partial_dependence"]

def partial_dependence(
    estimator,
    X,
    features,
    *,
    sample_weight=None,
    categorical_features=None,
    feature_names=None,
    response_method: str = "auto",
    percentiles=(0.05, 0.95),
    grid_resolution: int = 100,
    custom_values=None,
    method: str = "auto",
    kind: str = "average",
): ...
