from sklearn.metrics import (
    check_scoring as check_scoring,
    get_scorer_names as get_scorer_names,
)
from sklearn.utils import (
    Bunch as Bunch,
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils._param_validation import (
    HasMethods as HasMethods,
    Integral as Integral,
    Interval as Interval,
    RealNotInt as RealNotInt,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.parallel import (
    Parallel as Parallel,
    delayed as delayed,
)

def permutation_importance(
    estimator,
    X,
    y,
    *,
    scoring=None,
    n_repeats: int = 5,
    n_jobs=None,
    random_state=None,
    sample_weight=None,
    max_samples: float = 1.0,
): ...
