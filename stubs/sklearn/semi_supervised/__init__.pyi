from sklearn.semi_supervised._label_propagation import (
    LabelPropagation as LabelPropagation,
    LabelSpreading as LabelSpreading,
)
from sklearn.semi_supervised._self_training import (
    SelfTrainingClassifier as SelfTrainingClassifier,
)

__all__ = ["LabelPropagation", "LabelSpreading", "SelfTrainingClassifier"]
