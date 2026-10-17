from typing import Any

from numpy.typing import NDArray

def warpCoord(Minv, pt) -> NDArray[Any]: ...
def getDetBoxes_core(
    textmap,
    linkmap,
    text_threshold,
    link_threshold,
    low_text,
    estimate_num_chars=...,
) -> tuple[list[Any], Any, list[Any]]: ...
def getPoly_core(boxes, labels, mapper, linkmap) -> list[Any]: ...
def getDetBoxes(
    textmap,
    linkmap,
    text_threshold,
    link_threshold,
    low_text,
    poly=...,
    estimate_num_chars=...,
) -> tuple[list[Any], list[Any] | list[None], list[Any]]: ...
def adjustResultCoordinates(polys, ratio_w, ratio_h, ratio_net=...) -> NDArray[Any]: ...
