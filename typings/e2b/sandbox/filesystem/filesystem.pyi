from datetime import datetime
from enum import Enum

class FileType(Enum):
    FILE = "file"
    DIR = "dir"
    SYMLINK = "symlink"

class WriteInfo:
    name: str
    type: FileType | None
    path: str

class EntryInfo(WriteInfo):
    size: int
    mode: int
    permissions: str
    owner: str
    group: str
    modified_time: datetime
    symlink_target: str | None
