from collections.abc import Callable, Collection, Iterable, Iterator, Sequence
from typing import IO, Any, Literal, Self

from lark.exceptions import UnexpectedInput
from lark.lexer import Lexer, TerminalDef, Token
from lark.tree import ParseTree
from lark.utils import TextOrSlice

class PostLex:
    always_accept: Iterable[str]
    def process(self, stream: Iterator[Token]) -> Iterator[Token]: ...

class LarkOptions:
    start: list[str]
    debug: bool
    strict: bool
    propagate_positions: bool | str
    maybe_placeholders: bool
    cache: bool | str
    cache_grammar: bool
    regex: bool
    g_regex_flags: int
    keep_all_tokens: bool
    parser: str
    lexer: str
    ambiguity: Literal["auto", "resolve", "explicit", "forest"]
    postlex: PostLex | None
    priority: Literal["auto", "normal", "invert"] | None
    lexer_callbacks: dict[str, Callable[[Token], Token]]
    use_bytes: bool
    ordered_sets: bool
    source_path: str | None
    def __init__(self, options_dict: dict[str, Any]) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

class Lark:
    source_path: str
    source_grammar: str
    options: LarkOptions
    lexer: Lexer
    terminals: Collection[TerminalDef]
    def __init__(self, grammar: str | IO[str], **options: Any) -> None: ...
    @classmethod
    def open(
        cls,
        grammar_filename: str,
        rel_to: str | None = ...,
        **options: Any,
    ) -> Self: ...
    @classmethod
    def open_from_package(
        cls,
        package: str,
        grammar_path: str,
        search_paths: Sequence[str] = ...,
        **options: Any,
    ) -> Self: ...
    @classmethod
    def load(cls, f: IO[bytes]) -> Self: ...
    def save(self, f: IO[bytes], exclude_options: Collection[str] = ...) -> None: ...
    def lex(self, text: TextOrSlice, dont_ignore: bool = ...) -> Iterator[Token]: ...
    def get_terminal(self, name: str) -> TerminalDef: ...
    # Upstream types `text` as `Union[AnyStr, TextSlice[AnyStr], Any]`; the bare
    # `AnyStr` leaves the parameter unsolved and the whole method partially
    # unknown at every call site.
    def parse(
        self,
        text: str,
        start: str | None = ...,
        on_error: Callable[[UnexpectedInput], bool] | None = ...,
    ) -> ParseTree: ...
