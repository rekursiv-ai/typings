class Node:
    tag: str | None

class ScalarNode(Node):
    value: str

class CollectionNode(Node): ...

class SequenceNode(CollectionNode):
    value: list[Node]

class MappingNode(CollectionNode):
    value: list[tuple[Node, Node]]
