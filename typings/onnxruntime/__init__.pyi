from collections.abc import Mapping, Sequence
from enum import Enum
from typing import Any

class ONNXRuntimeError(Exception): ...

class GraphOptimizationLevel(Enum):
    ORT_DISABLE_ALL: GraphOptimizationLevel

class SessionOptions:
    enable_profiling: bool
    graph_optimization_level: GraphOptimizationLevel
    profile_file_prefix: str
    intra_op_num_threads: int
    inter_op_num_threads: int

    def __init__(self) -> None: ...

class NodeArg:
    @property
    def name(self) -> str: ...
    @property
    def shape(self) -> list[int | str | None]: ...
    @property
    def type(self) -> str: ...

class InferenceSession:
    def __init__(
        self,
        path_or_bytes: str | bytes,
        sess_options: SessionOptions | None = None,
        providers: Sequence[str] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def get_inputs(self) -> list[NodeArg]: ...
    def get_outputs(self) -> list[NodeArg]: ...
    def run(
        self,
        output_names: Sequence[str] | None,
        input_feed: Mapping[str, Any],
    ) -> list[Any]: ...
    def end_profiling(self) -> str: ...

def get_available_providers() -> list[str]: ...
