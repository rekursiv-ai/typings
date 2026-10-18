from collections.abc import Iterator, Sequence
from os import PathLike
from typing import Literal, Self

from pyarrow import Schema, Table

import pyarrow as pa

class ColumnChunkMetaData:
    compression: str

class RowGroupMetaData:
    num_rows: int

    def column(self, i: int) -> ColumnChunkMetaData: ...

class FileMetaData:
    num_rows: int
    num_row_groups: int
    created_by: str

    def row_group(self, i: int) -> RowGroupMetaData: ...

class ParquetFile:
    schema_arrow: Schema
    metadata: FileMetaData
    num_row_groups: int

    def __init__(self, source: str | PathLike[str]) -> None: ...
    def read_row_group(self, i: int) -> Table: ...
    def read(
        self,
        columns: Sequence[str] | None = None,
        use_threads: bool = True,
        use_pandas_metadata: bool = False,
    ) -> Table: ...
    def iter_batches(
        self,
        batch_size: int = 65536,
        row_groups: Sequence[int] | None = None,
        columns: Sequence[str] | None = None,
        use_threads: bool = True,
        use_pandas_metadata: bool = False,
    ) -> Iterator[pa.RecordBatch]: ...

class ParquetWriter:
    def __init__(self, where: str | PathLike[str], schema: Schema) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: object, **kwargs: object) -> Literal[False]: ...
    def write_table(self, table: Table, row_group_size: int | None = None) -> None: ...
    def close(self) -> None: ...

def read_table(
    source: str | PathLike[str],
    *,
    columns: Sequence[str] | None = ...,
) -> Table: ...
def read_metadata(where: str | PathLike[str]) -> FileMetaData: ...
def write_table(
    table: Table,
    where: str | PathLike[str],
    row_group_size: int | None = None,
    *,
    compression: str | dict[str, str] = "snappy",
) -> None: ...
