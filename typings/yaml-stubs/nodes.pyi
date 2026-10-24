from typing import Any, ClassVar

from _typeshed import Incomplete
from yaml.error import Mark

# Any Unions: Avoid forcing the user to check for None when they know what Node was instantiated with
# Using generics may be overkill without support for default Generics
# Permissive Unions could also be useful here.
class Node:
    tag: str
    value: Incomplete
    start_mark: Mark | Any
    end_mark: Mark | Any
    def __init__(
        self,
        tag: str,
        value,
        start_mark: Mark | None,
        end_mark: Mark | None,
    ) -> None: ...

class ScalarNode(Node):
    id: ClassVar[str]
    value: str
    style: str | Any
    def __init__(
        self,
        tag: str,
        value,
        start_mark: Mark | None = None,
        end_mark: Mark | None = None,
        style: str | None = None,
    ) -> None: ...

class CollectionNode(Node):
    flow_style: bool | Any
    def __init__(
        self,
        tag: str,
        value,
        start_mark: Mark | None = None,
        end_mark: Mark | None = None,
        flow_style: bool | None = None,
    ) -> None: ...

class SequenceNode(CollectionNode):
    id: ClassVar[str]
    value: list[Node]

class MappingNode(CollectionNode):
    id: ClassVar[str]
    value: list[tuple[Node, Node]]
