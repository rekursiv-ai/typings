from typing import Any

from sklearn.preprocessing import MultiLabelBinarizer as MultiLabelBinarizer
from sklearn.utils import (
    Bunch as Bunch,
    check_array as check_array,
    check_random_state as check_random_state,
)
from sklearn.utils._param_validation import (
    Interval as Interval,
    StrOptions as StrOptions,
    validate_params as validate_params,
)
from sklearn.utils.random import (
    sample_without_replacement as sample_without_replacement,
)

import numpy as np
import numpy.typing as npt

def make_classification(
    n_samples: int = 100,
    n_features: int = 20,
    *,
    n_informative: int = 2,
    n_redundant: int = 2,
    n_repeated: int = 0,
    n_classes: int = 2,
    n_clusters_per_class: int = 2,
    weights: Any = None,
    flip_y: float = 0.01,
    class_sep: float = 1.0,
    hypercube: bool = True,
    shift: float = 0.0,
    scale: float = 1.0,
    shuffle: bool = True,
    random_state: Any = None,
    return_X_y: bool = True,
) -> tuple[npt.NDArray[np.float64], npt.NDArray[np.int64]]: ...
def make_multilabel_classification(
    n_samples: int = 100,
    n_features: int = 20,
    *,
    n_classes: int = 5,
    n_labels: int = 2,
    length: int = 50,
    allow_unlabeled: bool = True,
    sparse: bool = False,
    return_indicator: str = "dense",
    return_distributions: bool = False,
    random_state=None,
): ...
def make_hastie_10_2(n_samples: int = 12000, *, random_state=None): ...
def make_regression(
    n_samples: int = 100,
    n_features: int = 100,
    *,
    n_informative: int = 10,
    n_targets: int = 1,
    bias: float = 0.0,
    effective_rank=None,
    tail_strength: float = 0.5,
    noise: float = 0.0,
    shuffle: bool = True,
    coef: bool = False,
    random_state=None,
): ...
def make_circles(
    n_samples: int = 100,
    *,
    shuffle: bool = True,
    noise=None,
    random_state=None,
    factor: float = 0.8,
): ...
def make_moons(
    n_samples: int = 100,
    *,
    shuffle: bool = True,
    noise=None,
    random_state=None,
): ...
def make_blobs(
    n_samples: int = 100,
    n_features: int = 2,
    *,
    centers=None,
    cluster_std: float = 1.0,
    center_box=(-10.0, 10.0),
    shuffle: bool = True,
    random_state=None,
    return_centers: bool = False,
): ...
def make_friedman1(
    n_samples: int = 100,
    n_features: int = 10,
    *,
    noise: float = 0.0,
    random_state=None,
): ...
def make_friedman2(n_samples: int = 100, *, noise: float = 0.0, random_state=None): ...
def make_friedman3(n_samples: int = 100, *, noise: float = 0.0, random_state=None): ...
def make_low_rank_matrix(
    n_samples: int = 100,
    n_features: int = 100,
    *,
    effective_rank: int = 10,
    tail_strength: float = 0.5,
    random_state=None,
): ...
def make_sparse_coded_signal(
    n_samples,
    *,
    n_components,
    n_features,
    n_nonzero_coefs,
    random_state=None,
): ...
def make_sparse_uncorrelated(
    n_samples: int = 100,
    n_features: int = 10,
    *,
    random_state=None,
): ...
def make_spd_matrix(n_dim, *, random_state=None): ...
def make_sparse_spd_matrix(
    n_dim: int = 1,
    *,
    alpha: float = 0.95,
    norm_diag: bool = False,
    smallest_coef: float = 0.1,
    largest_coef: float = 0.9,
    sparse_format=None,
    random_state=None,
): ...
def make_swiss_roll(
    n_samples: int = 100,
    *,
    noise: float = 0.0,
    random_state=None,
    hole: bool = False,
): ...
def make_s_curve(n_samples: int = 100, *, noise: float = 0.0, random_state=None): ...
def make_gaussian_quantiles(
    *,
    mean=None,
    cov: float = 1.0,
    n_samples: int = 100,
    n_features: int = 2,
    n_classes: int = 3,
    shuffle: bool = True,
    random_state=None,
): ...
def make_biclusters(
    shape,
    n_clusters,
    *,
    noise: float = 0.0,
    minval: int = 10,
    maxval: int = 100,
    shuffle: bool = True,
    random_state=None,
): ...
def make_checkerboard(
    shape,
    n_clusters,
    *,
    noise: float = 0.0,
    minval: int = 10,
    maxval: int = 100,
    shuffle: bool = True,
    random_state=None,
): ...
