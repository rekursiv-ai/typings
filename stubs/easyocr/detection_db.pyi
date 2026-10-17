from typing import Any

from numpy import ndarray
from torch import dtype

def test_net(
    image,
    detector,
    threshold=...,  # noqa: PT028 -- Mirrors upstream fixture defaults.
    bbox_min_score=...,  # noqa: PT028 -- Mirrors upstream fixture defaults.
    bbox_min_size=...,  # noqa: PT028 -- Mirrors upstream fixture defaults.
    max_candidates=...,  # noqa: PT028 -- Mirrors upstream fixture defaults.
    canvas_size=...,  # noqa: PT028 -- Mirrors upstream fixture defaults.
    poly=...,  # noqa: PT028 -- Mirrors upstream fixture defaults.
    device=...,  # noqa: PT028 -- Mirrors upstream fixture defaults.
) -> tuple[Any, Any]: ...
def get_detector(
    trained_model,
    backbone=...,
    device=...,
    quantize=...,
    cudnn_benchmark=...,
) -> DBNet: ...
def get_textbox(
    detector,
    image,
    canvas_size=...,
    poly=...,
    threshold=...,
    bbox_min_score=...,
    bbox_min_size=...,
    max_candidates=...,
    device=...,
    **kwargs,
) -> list[list[ndarray[tuple[int], dtype[signedinteger[_32Bit]]]]]: ...
