from bashlex import ast

def parse(
    s: str,
    strictmode: bool = ...,
    expansionlimit: int | None = ...,
    convertpos: bool = ...,
) -> list[ast.node]: ...

parsesingle = ...
split = ...
