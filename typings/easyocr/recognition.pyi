from typing import Any

from numpy import ndarray
from torch import dtype

import torch
import torch.utils.data

def custom_mean(x): ...
def contrast_grey(img) -> tuple[Any, Any, Any]: ...
def adjust_contrast_grey(
    img,
    target=...,
) -> ndarray[_AnyShape, dtype[unsignedinteger[_8Bit]]]: ...

class NormalizePAD:
    def __init__(self, max_size, PAD_type=...) -> None: ...
    def __call__(self, img): ...

class ListDataset(torch.utils.data.Dataset):
    def __init__(self, image_list) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index) -> Image: ...

class AlignCollate:
    def __init__(
        self,
        imgH=...,
        imgW=...,
        keep_ratio_with_pad=...,
        adjust_contrast=...,
    ) -> None: ...
    def __call__(self, batch): ...

def recognizer_predict(
    model,
    converter,
    test_loader,
    batch_max_length,
    ignore_idx,
    char_group_idx,
    decoder=...,
    beamWidth=...,
    device=...,
) -> list[Any]: ...
def get_recognizer(
    recog_network,
    network_params,
    character,
    separator_list,
    dict_list,
    model_path,
    device=...,
    quantize=...,
) -> tuple[Any, CTCLabelConverter]: ...
def get_text(
    character,
    imgH,
    imgW,
    recognizer,
    converter,
    image_list,
    ignore_char=...,
    decoder=...,
    beamWidth=...,
    batch_size=...,
    contrast_ths=...,
    adjust_contrast=...,
    filter_ths=...,
    workers=...,
    device=...,
) -> list[Any]: ...
