from collections.abc import Sequence
from typing import Literal

from torch.fft import *

from ._typing import Array

__all__ = [
    "Tensor",
    "fft",
    "fft2",
    "fftfreq",
    "fftn",
    "fftshift",
    "hfft",
    "ifft",
    "ifft2",
    "ifftn",
    "ifftshift",
    "ihfft",
    "irfft",
    "irfft2",
    "irfftn",
    "rfft",
    "rfft2",
    "rfftfreq",
    "rfftn",
]

def fftn(
    x: Array,
    /,
    *,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
    **kwargs,
) -> Array: ...
def ifftn(
    x: Array,
    /,
    *,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
    **kwargs,
) -> Array: ...
def rfftn(
    x: Array,
    /,
    *,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
    **kwargs,
) -> Array: ...
def irfftn(
    x: Array,
    /,
    *,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: Literal["backward", "ortho", "forward"] = "backward",
    **kwargs,
) -> Array: ...
def fftshift(
    x: Array,
    /,
    *,
    axes: int | Sequence[int] | None = None,
    **kwargs,
) -> Array: ...
def ifftshift(
    x: Array,
    /,
    *,
    axes: int | Sequence[int] | None = None,
    **kwargs,
) -> Array: ...

# Names in __all__ with no definition:
#   Tensor
#   fft
#   fft2
#   fftfreq
#   hfft
#   ifft
#   ifft2
#   ihfft
#   irfft
#   irfft2
#   rfft
#   rfft2
#   rfftfreq
