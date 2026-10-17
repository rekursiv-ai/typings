from typing import Any

from torch import nn

"""
Copyright (c) 2019-present NAVER Corp.
MIT License
"""

class double_conv(nn.Module):
    def __init__(self, in_ch, mid_ch, out_ch) -> None: ...
    def forward(self, x): ...

class CRAFT(nn.Module):
    def __init__(self, pretrained=..., freeze=...) -> None: ...
    def forward(self, x) -> tuple[Any, Any]: ...
    def __call__(self, *args: Any, **kwargs: Any) -> tuple[Any, Any]: ...
