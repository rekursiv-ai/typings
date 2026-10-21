import abc

from ...base import BaseImage
from ...._types import Box
from ....main import ActiveWithNeighbors

class QRModuleDrawer(abc.ABC, metaclass=abc.ABCMeta):
    needs_neighbors: bool = False
    img: BaseImage
    def initialize(self, img: BaseImage) -> None: ...
    @abc.abstractmethod
    def drawrect(self, box: Box, is_active: bool | ActiveWithNeighbors) -> None: ...
