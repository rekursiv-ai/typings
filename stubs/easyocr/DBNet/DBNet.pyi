from typing import Any

from numpy import ndarray
from numpy.typing import NDArray
from torch import Tensor, dtype

class DBNet:
    def __init__(
        self,
        backbone=...,
        weight_dir=...,
        weight_name=...,
        initialize_model=...,
        dynamic_import_relative_path=...,
        device=...,
        verbose=...,
    ) -> None: ...
    def set_relative_import_path(self, configs, dynamic_import_relative_path): ...
    def load_weight(self, weight_path) -> None: ...
    def construct_model(self, config) -> None: ...
    def initialize_model(self, model_config, weight_path) -> None: ...
    def get_cv2_image(
        self,
        image,
    ) -> (
        ndarray[Any, dtype[Any]]
        | ndarray[_Shape, dtype[Any]]
        | ndarray[_AnyShape, dtype[Any]]
    ): ...
    def resize_image(self, img, detection_size=...) -> tuple[Any, tuple[Any, Any]]: ...
    def image_array2tensor(self, image) -> Tensor: ...
    def normalize_image(self, image): ...
    def load_image(
        self,
        image_path,
        detection_size=...,
    ) -> tuple[Tensor, tuple[Any, Any]]: ...
    def load_images(
        self,
        images,
        detection_size=...,
    ) -> tuple[Tensor, tuple[Any, ...]]: ...
    def hmap2bbox(
        self,
        image_tensor,
        original_shapes,
        hmap,
        text_threshold=...,
        bbox_min_score=...,
        bbox_min_size=...,
        max_candidates=...,
        as_polygon=...,
    ) -> tuple[tuple[Any, ...], tuple[Any, ...]]: ...
    def binarize(self, tensor, threshold): ...
    def polygons_from_bitmap(
        self,
        hmap,
        segmentation,
        dest_width,
        dest_height,
        bbox_min_score=...,
        bbox_min_size=...,
        max_candidates=...,
    ) -> tuple[list[Any], list[Any]]: ...
    def boxes_from_bitmap(
        self,
        hmap,
        segmentation,
        dest_width,
        dest_height,
        bbox_min_score=...,
        bbox_min_size=...,
        max_candidates=...,
    ) -> tuple[list[list[list[int]]], _Array[tuple[int], floating[_32Bit]]]: ...
    def unclip(self, box, unclip_ratio=...) -> NDArray[Any]: ...
    def get_mini_boxes(self, contour) -> tuple[list[Any], float]: ...
    def box_score_fast(self, hmap, box_) -> float: ...
    def image2hmap(self, image_tensor) -> Any: ...
    def inference(
        self,
        image,
        text_threshold=...,
        bbox_min_score=...,
        bbox_min_size=...,
        max_candidates=...,
        detection_size=...,
        as_polygon=...,
        return_scores=...,
    ) -> tuple[tuple[Any, ...], tuple[Any, ...]] | tuple[Any, ...]: ...
