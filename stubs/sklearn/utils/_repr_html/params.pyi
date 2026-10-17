from collections import UserDict

from _typeshed import Incomplete
from sklearn.externals._numpydoc import docscrape as docscrape
from sklearn.utils._repr_html.base import ReprHTMLMixin as ReprHTMLMixin

class ParamsDict(ReprHTMLMixin, UserDict):
    non_default: Incomplete
    estimator_class: Incomplete
    doc_link: Incomplete
    def __init__(
        self,
        *,
        params=None,
        non_default=...,
        estimator_class=None,
        doc_link: str = "",
    ) -> None: ...
