from ruamel.yaml.nodes import Node

class BaseConstructor:
    def construct_document(self, node: Node) -> object: ...
