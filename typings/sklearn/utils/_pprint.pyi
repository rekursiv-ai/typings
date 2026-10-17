import pprint

from _typeshed import Incomplete
from sklearn._config import get_config as get_config
from sklearn.base import BaseEstimator as BaseEstimator
from sklearn.utils._missing import is_scalar_nan as is_scalar_nan

class KeyValTuple(tuple): ...
class KeyValTupleParam(KeyValTuple): ...

class _EstimatorPrettyPrinter(pprint.PrettyPrinter):
    n_max_elements_to_show: Incomplete
    def __init__(
        self,
        indent: int = 1,
        width: int = 80,
        depth=None,
        stream=None,
        *,
        compact: bool = False,
        indent_at_name: bool = True,
        n_max_elements_to_show=None,
    ) -> None: ...
    def format(self, object, context, maxlevels, level): ...
