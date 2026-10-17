from _typeshed import Incomplete
from sklearn.base import BaseEstimator, TransformerMixin

__all__ = [
    "PatchExtractor",
    "extract_patches_2d",
    "grid_to_graph",
    "img_to_graph",
    "reconstruct_from_patches_2d",
]

def img_to_graph(img, *, mask=None, return_as=..., dtype=None): ...
def grid_to_graph(n_x, n_y, n_z: int = 1, *, mask=None, return_as=..., dtype=...): ...
def extract_patches_2d(image, patch_size, *, max_patches=None, random_state=None): ...
def reconstruct_from_patches_2d(patches, image_size): ...

class PatchExtractor(TransformerMixin, BaseEstimator):
    patch_size: Incomplete
    max_patches: Incomplete
    random_state: Incomplete
    def __init__(
        self,
        *,
        patch_size=None,
        max_patches=None,
        random_state=None,
    ) -> None: ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def __sklearn_tags__(self): ...
