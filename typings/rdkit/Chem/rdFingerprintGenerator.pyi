# ruff: noqa: N999 -- Mirrors the upstream module name; renaming breaks every import.
from collections.abc import Mapping, Sequence

from numpy.typing import NDArray

import numpy as np

from rdkit.Chem import Mol

class AtomInvariantsGenerator: ...

class AdditionalOutput:
    def __init__(self) -> None: ...
    def AllocateBitInfoMap(self) -> None: ...
    def GetBitInfoMap(self) -> Mapping[int, Sequence[tuple[int, int]]]: ...

class FingerprintGenerator64:
    def GetFingerprintAsNumPy(self, mol: Mol) -> NDArray[np.uint8]: ...
    def GetSparseCountFingerprint(
        self,
        mol: Mol,
        additionalOutput: AdditionalOutput | None = None,
    ) -> object: ...

def GetMorganFeatureAtomInvGen() -> AtomInvariantsGenerator: ...
def GetMorganGenerator(
    radius: int = 3,
    fpSize: int = 2048,
    atomInvariantsGenerator: AtomInvariantsGenerator | None = None,
) -> FingerprintGenerator64: ...
def GetRDKitFPGenerator(
    minPath: int = 1,
    maxPath: int = 7,
    fpSize: int = 2048,
) -> FingerprintGenerator64: ...
def GetAtomPairGenerator(fpSize: int = 2048) -> FingerprintGenerator64: ...
def GetTopologicalTorsionGenerator(fpSize: int = 2048) -> FingerprintGenerator64: ...
