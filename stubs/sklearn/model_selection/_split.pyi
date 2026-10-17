from abc import ABCMeta, abstractmethod
from collections.abc import Generator
from typing import Any

from _typeshed import Incomplete
from sklearn.utils.metadata_routing import _MetadataRequester

__all__ = [
    "BaseCrossValidator",
    "GroupKFold",
    "GroupShuffleSplit",
    "KFold",
    "LeaveOneGroupOut",
    "LeaveOneOut",
    "LeavePGroupsOut",
    "LeavePOut",
    "PredefinedSplit",
    "RepeatedKFold",
    "RepeatedStratifiedKFold",
    "ShuffleSplit",
    "StratifiedGroupKFold",
    "StratifiedKFold",
    "StratifiedShuffleSplit",
    "check_cv",
    "train_test_split",
]

class _UnsupportedGroupCVMixin:
    def split(self, X, y=None, groups=None): ...

class GroupsConsumerMixin(_MetadataRequester): ...

class BaseCrossValidator(_MetadataRequester, metaclass=ABCMeta):
    def split(self, X, y=None, groups=None) -> Generator[Incomplete]: ...
    @abstractmethod
    def get_n_splits(self, X=None, y=None, groups=None): ...

class LeaveOneOut(_UnsupportedGroupCVMixin, BaseCrossValidator):
    def get_n_splits(self, X, y=None, groups=None): ...

class LeavePOut(_UnsupportedGroupCVMixin, BaseCrossValidator):
    p: Incomplete
    def __init__(self, p) -> None: ...
    def get_n_splits(self, X, y=None, groups=None): ...

class _BaseKFold(BaseCrossValidator, metaclass=ABCMeta):
    n_splits: Incomplete
    shuffle: Incomplete
    random_state: Incomplete
    @abstractmethod
    def __init__(self, n_splits, *, shuffle, random_state): ...
    def split(self, X, y=None, groups=None) -> Generator[Incomplete]: ...
    def get_n_splits(self, X=None, y=None, groups=None): ...

class KFold(_UnsupportedGroupCVMixin, _BaseKFold):
    def __init__(
        self,
        n_splits: int = 5,
        *,
        shuffle: bool = False,
        random_state=None,
    ) -> None: ...

class GroupKFold(GroupsConsumerMixin, _BaseKFold):
    def __init__(
        self,
        n_splits: int = 5,
        *,
        shuffle: bool = False,
        random_state=None,
    ) -> None: ...
    def split(self, X, y=None, groups=None): ...

class StratifiedKFold(_BaseKFold):
    def __init__(
        self,
        n_splits: int = 5,
        *,
        shuffle: bool = False,
        random_state=None,
    ) -> None: ...
    def split(self, X, y, groups=None): ...

class StratifiedGroupKFold(GroupsConsumerMixin, _BaseKFold):
    def __init__(
        self,
        n_splits: int = 5,
        shuffle: bool = False,
        random_state=None,
    ) -> None: ...

class TimeSeriesSplit(_BaseKFold):
    max_train_size: Incomplete
    test_size: Incomplete
    gap: Incomplete
    def __init__(
        self,
        n_splits: int = 5,
        *,
        max_train_size=None,
        test_size=None,
        gap: int = 0,
    ) -> None: ...
    def split(self, X, y=None, groups=None): ...

class LeaveOneGroupOut(GroupsConsumerMixin, BaseCrossValidator):
    def get_n_splits(self, X=None, y=None, groups=None): ...
    def split(self, X, y=None, groups=None): ...

class LeavePGroupsOut(GroupsConsumerMixin, BaseCrossValidator):
    n_groups: Incomplete
    def __init__(self, n_groups) -> None: ...
    def get_n_splits(self, X=None, y=None, groups=None): ...
    def split(self, X, y=None, groups=None): ...

class _RepeatedSplits(_MetadataRequester, metaclass=ABCMeta):
    cv: Incomplete
    n_repeats: Incomplete
    random_state: Incomplete
    cvargs: Incomplete
    def __init__(
        self,
        cv,
        *,
        n_repeats: int = 10,
        random_state=None,
        **cvargs,
    ) -> None: ...
    def split(self, X, y=None, groups=None) -> Generator[Incomplete]: ...
    def get_n_splits(self, X=None, y=None, groups=None): ...

class RepeatedKFold(_UnsupportedGroupCVMixin, _RepeatedSplits):
    def __init__(
        self,
        *,
        n_splits: int = 5,
        n_repeats: int = 10,
        random_state=None,
    ) -> None: ...

class RepeatedStratifiedKFold(_UnsupportedGroupCVMixin, _RepeatedSplits):
    def __init__(
        self,
        *,
        n_splits: int = 5,
        n_repeats: int = 10,
        random_state=None,
    ) -> None: ...
    def split(self, X, y, groups=None): ...

class BaseShuffleSplit(_MetadataRequester, metaclass=ABCMeta):
    n_splits: Incomplete
    test_size: Incomplete
    train_size: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        n_splits: int = 10,
        *,
        test_size=None,
        train_size=None,
        random_state=None,
    ) -> None: ...
    def split(self, X, y=None, groups=None) -> Generator[Incomplete]: ...
    def get_n_splits(self, X=None, y=None, groups=None): ...

class ShuffleSplit(_UnsupportedGroupCVMixin, BaseShuffleSplit):
    def __init__(
        self,
        n_splits: int = 10,
        *,
        test_size=None,
        train_size=None,
        random_state=None,
    ) -> None: ...

class GroupShuffleSplit(GroupsConsumerMixin, BaseShuffleSplit):
    def __init__(
        self,
        n_splits: int = 5,
        *,
        test_size=None,
        train_size=None,
        random_state=None,
    ) -> None: ...
    def split(self, X, y=None, groups=None): ...

class StratifiedShuffleSplit(BaseShuffleSplit):
    def __init__(
        self,
        n_splits: int = 10,
        *,
        test_size=None,
        train_size=None,
        random_state=None,
    ) -> None: ...
    def split(self, X, y, groups=None): ...

class PredefinedSplit(BaseCrossValidator):
    test_fold: Incomplete
    unique_folds: Incomplete
    def __init__(self, test_fold) -> None: ...
    def split(self, X=None, y=None, groups=None): ...
    def get_n_splits(self, X=None, y=None, groups=None): ...

class _CVIterableWrapper(BaseCrossValidator):
    cv: Incomplete
    def __init__(self, cv) -> None: ...
    def get_n_splits(self, X=None, y=None, groups=None): ...
    def split(self, X=None, y=None, groups=None) -> Generator[Incomplete]: ...

def check_cv(cv: int = 5, y=None, *, classifier: bool = False): ...
def train_test_split(
    *arrays: Any,
    test_size: Any = None,
    train_size: Any = None,
    random_state: Any = None,
    shuffle: bool = True,
    stratify: Any = None,
) -> list[Any]: ...
