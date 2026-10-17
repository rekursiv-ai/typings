from sklearn.utils._param_validation import (
    StrOptions as StrOptions,
    validate_params as validate_params,
)

def compute_class_weight(class_weight, *, classes, y, sample_weight=None): ...
def compute_sample_weight(class_weight, y, *, indices=None): ...
