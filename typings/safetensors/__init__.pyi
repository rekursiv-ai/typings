# Generated content -- partially. The structure and docstrings are produced by
# `python stub.py`. The following are hand-edited additions that must be
# re-applied after each regeneration:
#   - module-level imports (`os`, `typing`, `torch`)
#   - `__version__: str`
#   - type annotations on `TensorSpec` / `serialize` / `serialize_file` / `safe_open`
#
# TODO: once we upgrade pyo3 to >= 0.28, replace `stub.py` with a dedicated
# `tools/stub-gen` binary using `pyo3-introspection`,
# mirroring how `huggingface/tokenizers` does it (see PR #1928).
# That generator emits typed stubs directly from Rust
# signatures -- no hand-editing, no drift.

from collections.abc import Sequence
from typing import Self

import os

from torch import Tensor

__version__: str

@staticmethod
def deserialize(bytes): ...
@staticmethod
def serialize(
    tensor_dict: dict[str, TensorSpec],
    metadata: dict[str, str] | None = ...,
) -> bytes: ...
@staticmethod
def serialize_file(
    tensor_dict: dict[str, TensorSpec],
    filename: str | os.PathLike[str],
    metadata: dict[str, str] | None = ...,
) -> None: ...

class TensorSpec:
    def __init__(
        self,
        *,
        dtype: str,
        shape: Sequence[int],
        data_ptr: int,
        data_len: int,
    ) -> None: ...
    @property
    def data_len(self) -> int: ...
    @property
    def data_ptr(self) -> int: ...
    @property
    def dtype(self) -> str: ...
    @property
    def shape(self) -> list[int]: ...

class safe_open:
    def __init__(
        self,
        filename: str | os.PathLike[str],
        framework: str,
        device: str = ...,
        *,
        backend: str = ...,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        _exc_type: object,
        _exc_value: object,
        _traceback: object,
    ) -> None: ...
    def get_slice(self, name: str): ...
    def get_tensor(self, name: str) -> Tensor: ...
    def get_tensors(self): ...
    def keys(self) -> list[str]: ...
    def metadata(self) -> dict[str, str] | None: ...
    def offset_keys(self) -> list[str]: ...

class SafetensorError(Exception): ...
