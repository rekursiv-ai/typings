from collections.abc import Sequence

class Hook:
    id: str
    alias: str
    entry: str
    args: Sequence[str]
    stages: Sequence[str]
