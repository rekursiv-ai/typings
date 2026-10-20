# ruff: noqa: N999 -- Mirrors the upstream module name; renaming breaks every import.
from rdkit.Chem import Mol

def ComputeGasteigerCharges(mol: Mol) -> None: ...
