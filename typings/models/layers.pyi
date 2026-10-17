from typing import Any

from torch import Tensor, nn

import torch

type CosSin = tuple[Tensor, Tensor] | None

class CastedLinear(nn.Module):
    weight: nn.Parameter
    bias: nn.Parameter | None
    def __init__(self, in_features: int, out_features: int, bias: bool) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Tensor: ...

class CastedEmbedding(nn.Module):
    embedding_weight: nn.Parameter
    cast_to: torch.dtype
    def __init__(
        self,
        num_embeddings: int,
        embedding_dim: int,
        init_std: float,
        cast_to: torch.dtype,
    ) -> None: ...
    def forward(self, input: Tensor) -> Tensor: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Tensor: ...

class RotaryEmbedding(nn.Module):
    cos_cached: Tensor
    sin_cached: Tensor
    def __init__(
        self,
        dim: int,
        max_position_embeddings: int,
        base: float,
        device: torch.device | None = ...,
    ) -> None: ...
    def forward(self) -> tuple[Tensor, Tensor]: ...
    def __call__(self, *args: Any, **kwargs: Any) -> tuple[Tensor, Tensor]: ...

class Attention(nn.Module):
    qkv_proj: CastedLinear
    o_proj: CastedLinear
    def __init__(
        self,
        hidden_size: int,
        head_dim: int,
        num_heads: int,
        num_key_value_heads: int,
        causal: bool = ...,
    ) -> None: ...
    def forward(self, cos_sin: CosSin, hidden_states: Tensor) -> Tensor: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Tensor: ...

class LinearSwish(nn.Module):
    linear: CastedLinear
    reverse: bool
    def __init__(self, hidden_size: int, reverse: bool = ...) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Tensor: ...

class SwiGLU(nn.Module):
    gate_up_proj: CastedLinear
    down_proj: CastedLinear
    def __init__(self, hidden_size: int, expansion: float) -> None: ...
    def forward(self, x: Tensor) -> Tensor: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Tensor: ...

def rms_norm(hidden_states: Tensor, variance_epsilon: float) -> Tensor: ...
