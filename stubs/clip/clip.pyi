from collections.abc import Callable

import torch

from .model import CLIP

__all__ = ["available_models", "load", "tokenize"]

def available_models() -> list[str]: ...
def load(
    name: str,
    device: str | torch.device = ...,
    jit: bool = ...,
    download_root: str = ...,
) -> tuple[CLIP, Callable[..., torch.Tensor]]: ...
def tokenize(
    texts: str | list[str],
    context_length: int = ...,
    truncate: bool = ...,
) -> torch.Tensor: ...
