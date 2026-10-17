from typing import NamedTuple

import textwrap

from _typeshed import Incomplete

__all__ = ["simple_separated_format", "tabulate", "tabulate_formats"]

class Line(NamedTuple):
    begin: Incomplete
    hline: Incomplete
    sep: Incomplete
    end: Incomplete

class DataRow(NamedTuple):
    begin: Incomplete
    sep: Incomplete
    end: Incomplete

class TableFormat(NamedTuple):
    lineabove: Incomplete
    linebelowheader: Incomplete
    linebetweenrows: Incomplete
    linebelow: Incomplete
    headerrow: Incomplete
    datarow: Incomplete
    padding: Incomplete
    with_header_hide: Incomplete

tabulate_formats: Incomplete

from typing import Any  # noqa: E402 -- Mirrors upstream module layout.

def simple_separated_format(separator: str) -> str: ...
def tabulate(
    tabular_data: Any,
    headers: Any = (),
    tablefmt: str = "simple",
    floatfmt: Any = ...,
    intfmt: Any = ...,
    numalign: Any = ...,
    stralign: Any = ...,
    missingval: Any = ...,
    showindex: str = "default",
    disable_numparse: bool = False,
    colglobalalign: Any = None,
    colalign: Any = None,
    preserve_whitespace: bool = False,
    maxcolwidths: Any = None,
    headersglobalalign: Any = None,
    headersalign: Any = None,
    rowalign: Any = None,
    maxheadercolwidths: Any = None,
    break_long_words: Any = ...,
    break_on_hyphens: Any = ...,
) -> str: ...

class JupyterHTMLStr(str):
    @property
    def str(self): ...

class _CustomTextWrap(textwrap.TextWrapper):
    max_lines: Incomplete
    def __init__(self, *args, **kwargs) -> None: ...
