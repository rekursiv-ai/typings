# ruff: noqa: N999 -- Mirrors the upstream module name; renaming breaks every import.
from collections.abc import Iterable

from rdkit.Chem import Mol

def GenMACCSKeys(mol: Mol) -> Iterable[int]: ...
