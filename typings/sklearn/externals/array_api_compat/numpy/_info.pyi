from numpy import complex128, dtype, float64, intp

from ._typing import Device, DType

__all__ = ["__array_namespace_info__"]

class __array_namespace_info__:
    __module__: str
    def capabilities(self): ...
    def default_device(self): ...
    def default_dtypes(
        self,
        *,
        device: Device | None = None,
    ) -> dict[str, dtype[intp | float64 | complex128]]: ...
    def dtypes(
        self,
        *,
        device: Device | None = None,
        kind: str | tuple[str, ...] | None = None,
    ) -> dict[str, DType]: ...
    def devices(self) -> list[Device]: ...
