from collections import OrderedDict
from typing import Any

from torch import nn

import torch

def copyStateDict(state_dict) -> OrderedDict[Any, Any]: ...
def test_net(
    canvas_size,
    mag_ratio,
    net,
    image,
    text_threshold,
    link_threshold,
    low_text,
    poly,
    device,
    estimate_num_chars=...,  # noqa: PT028 -- Mirrors upstream fixture defaults.
) -> tuple[list[Any], list[Any]]: ...
def get_detector(
    trained_model: str,
    device: torch.device | str = ...,
    quantize: bool = ...,
    cudnn_benchmark: bool = ...,
) -> nn.Module: ...
def get_textbox(
    detector,
    image,
    canvas_size,
    mag_ratio,
    text_threshold,
    link_threshold,
    low_text,
    poly,
    device,
    optimal_num_chars=...,
    **kwargs,
) -> list[Any]: ...
