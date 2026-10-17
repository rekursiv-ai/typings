from _typeshed import Incomplete

class _AvailableIfDescriptor:
    fn: Incomplete
    check: Incomplete
    attribute_name: Incomplete
    def __init__(self, fn, check, attribute_name) -> None: ...
    def __get__(self, obj, owner=None): ...

def available_if(check): ...
