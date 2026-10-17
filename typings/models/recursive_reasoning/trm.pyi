from typing import Any

from pydantic import BaseModel
from torch import Tensor, nn

class TinyRecursiveReasoningModel_ACTV1Config(BaseModel):
    def __init__(self, **data: Any) -> None: ...

class TinyRecursiveReasoningModel_ACTV1(nn.Module):
    config: TinyRecursiveReasoningModel_ACTV1Config
    def __init__(
        self,
        config_dict: dict[str, Any] | TinyRecursiveReasoningModel_ACTV1Config,
    ) -> None: ...
    @property
    def puzzle_emb(self) -> nn.Module: ...
    def initial_carry(self, batch: dict[str, Tensor]) -> Any: ...
    def forward(
        self,
        carry: Any,
        batch: dict[str, Tensor],
    ) -> tuple[Any, dict[str, Tensor]]: ...
    def __call__(self, *args: Any, **kwargs: Any) -> tuple[Any, dict[str, Tensor]]: ...
