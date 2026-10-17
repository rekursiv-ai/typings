from sklearn.gaussian_process import kernels as kernels
from sklearn.gaussian_process._gpc import (
    GaussianProcessClassifier as GaussianProcessClassifier,
)
from sklearn.gaussian_process._gpr import (
    GaussianProcessRegressor as GaussianProcessRegressor,
)

__all__ = ["GaussianProcessClassifier", "GaussianProcessRegressor", "kernels"]
