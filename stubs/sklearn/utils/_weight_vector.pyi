from typing import ClassVar

from _typeshed import Incomplete

__test__: dict

class WeightVector32:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    aw: Incomplete
    w: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def __reduce__(self): ...

class WeightVector64:
    __pyx_vtable__: ClassVar[PyCapsule] = ...
    aw: Incomplete
    w: Incomplete
    @classmethod
    def __init__(cls, *args, **kwargs) -> None: ...
    def __reduce__(self): ...
