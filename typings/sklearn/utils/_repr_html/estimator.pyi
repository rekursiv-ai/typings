from _typeshed import Incomplete
from sklearn import config_context as config_context

class _IDCounter:
    prefix: Incomplete
    count: int
    def __init__(self, prefix) -> None: ...
    def get_id(self): ...

class _VisualBlock:
    kind: Incomplete
    estimators: Incomplete
    dash_wrapped: Incomplete
    name_caption: Incomplete
    doc_link_label: Incomplete
    names: Incomplete
    name_details: Incomplete
    def __init__(
        self,
        kind,
        estimators,
        *,
        names=None,
        name_details=None,
        name_caption=None,
        doc_link_label=None,
        dash_wrapped: bool = True,
    ) -> None: ...

def estimator_html_repr(estimator): ...
