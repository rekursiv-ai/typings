from collections.abc import Callable
from types import ModuleType

__all__ = ["get_xp"]

def get_xp(xp: ModuleType) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
