from typing import ClassVar

from _typeshed import Incomplete
from yaml.error import Mark

# The scanner marks every token it yields; a token built by hand may have none.
class Token:
    start_mark: Mark | None
    end_mark: Mark | None
    def __init__(self, start_mark, end_mark) -> None: ...

class DirectiveToken(Token):
    id: ClassVar[str]
    name: Incomplete
    value: Incomplete
    def __init__(self, name, value, start_mark, end_mark) -> None: ...

class DocumentStartToken(Token):
    id: ClassVar[str]

class DocumentEndToken(Token):
    id: ClassVar[str]

class StreamStartToken(Token):
    id: ClassVar[str]
    encoding: Incomplete
    def __init__(self, start_mark=None, end_mark=None, encoding=None) -> None: ...

class StreamEndToken(Token):
    id: ClassVar[str]

class BlockSequenceStartToken(Token):
    id: ClassVar[str]

class BlockMappingStartToken(Token):
    id: ClassVar[str]

class BlockEndToken(Token):
    id: ClassVar[str]

class FlowSequenceStartToken(Token):
    id: ClassVar[str]

class FlowMappingStartToken(Token):
    id: ClassVar[str]

class FlowSequenceEndToken(Token):
    id: ClassVar[str]

class FlowMappingEndToken(Token):
    id: ClassVar[str]

class KeyToken(Token):
    id: ClassVar[str]

class ValueToken(Token):
    id: ClassVar[str]

class BlockEntryToken(Token):
    id: ClassVar[str]

class FlowEntryToken(Token):
    id: ClassVar[str]

class AliasToken(Token):
    id: ClassVar[str]
    value: str
    def __init__(self, value, start_mark, end_mark) -> None: ...

class AnchorToken(Token):
    id: ClassVar[str]
    value: str
    def __init__(self, value, start_mark, end_mark) -> None: ...

class TagToken(Token):
    id: ClassVar[str]
    value: Incomplete
    def __init__(self, value, start_mark, end_mark) -> None: ...

class ScalarToken(Token):
    id: ClassVar[str]
    value: Incomplete
    plain: Incomplete
    style: Incomplete
    def __init__(self, value, plain, start_mark, end_mark, style=None) -> None: ...
