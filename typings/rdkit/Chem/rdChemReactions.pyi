# ruff: noqa: N999 -- Mirrors the upstream module name; renaming breaks every import.
from rdkit.Chem import Mol

class ChemicalReaction:
    def RunReactants(
        self,
        reactants: tuple[Mol, ...],
    ) -> tuple[tuple[Mol, ...], ...]: ...

def ReactionFromSmarts(SMARTS: str) -> ChemicalReaction: ...
