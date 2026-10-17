from _typeshed import Incomplete
from sklearn.base import BaseEstimator, OneToOneFeatureMixin, TransformerMixin
from sklearn.feature_extraction._stop_words import (
    ENGLISH_STOP_WORDS as ENGLISH_STOP_WORDS,
)

__all__ = [
    "ENGLISH_STOP_WORDS",
    "CountVectorizer",
    "HashingVectorizer",
    "TfidfTransformer",
    "TfidfVectorizer",
    "strip_accents_ascii",
    "strip_accents_unicode",
    "strip_tags",
]

def strip_accents_unicode(s): ...
def strip_accents_ascii(s): ...
def strip_tags(s): ...

class _VectorizerMixin:
    def decode(self, doc): ...
    def build_preprocessor(self): ...
    def build_tokenizer(self): ...
    def get_stop_words(self): ...
    def build_analyzer(self): ...

class HashingVectorizer(
    TransformerMixin,
    _VectorizerMixin,
    BaseEstimator,
    auto_wrap_output_keys=None,
):
    input: Incomplete
    encoding: Incomplete
    decode_error: Incomplete
    strip_accents: Incomplete
    preprocessor: Incomplete
    tokenizer: Incomplete
    analyzer: Incomplete
    lowercase: Incomplete
    token_pattern: Incomplete
    stop_words: Incomplete
    n_features: Incomplete
    ngram_range: Incomplete
    binary: Incomplete
    norm: Incomplete
    alternate_sign: Incomplete
    dtype: Incomplete
    def __init__(
        self,
        *,
        input: str = "content",
        encoding: str = "utf-8",
        decode_error: str = "strict",
        strip_accents=None,
        lowercase: bool = True,
        preprocessor=None,
        tokenizer=None,
        stop_words=None,
        token_pattern: str = "(?u)\\b\\w\\w+\\b",  # noqa: S107 -- default value mirrors upstream; stub is never executed
        ngram_range=(1, 1),
        analyzer: str = "word",
        n_features=...,
        binary: bool = False,
        norm: str = "l2",
        alternate_sign: bool = True,
        dtype=...,
    ) -> None: ...
    def partial_fit(self, X, y=None): ...
    def fit(self, X, y=None): ...
    def transform(self, X): ...
    def fit_transform(self, X, y=None): ...
    def __sklearn_tags__(self): ...

class CountVectorizer(_VectorizerMixin, BaseEstimator):
    input: Incomplete
    encoding: Incomplete
    decode_error: Incomplete
    strip_accents: Incomplete
    preprocessor: Incomplete
    tokenizer: Incomplete
    analyzer: Incomplete
    lowercase: Incomplete
    token_pattern: Incomplete
    stop_words: Incomplete
    max_df: Incomplete
    min_df: Incomplete
    max_features: Incomplete
    ngram_range: Incomplete
    vocabulary: Incomplete
    binary: Incomplete
    dtype: Incomplete
    def __init__(
        self,
        *,
        input: str = "content",
        encoding: str = "utf-8",
        decode_error: str = "strict",
        strip_accents=None,
        lowercase: bool = True,
        preprocessor=None,
        tokenizer=None,
        stop_words=None,
        token_pattern: str = "(?u)\\b\\w\\w+\\b",  # noqa: S107 -- default value mirrors upstream; stub is never executed
        ngram_range=(1, 1),
        analyzer: str = "word",
        max_df: float = 1.0,
        min_df: int = 1,
        max_features=None,
        vocabulary=None,
        binary: bool = False,
        dtype=...,
    ) -> None: ...
    def fit(self, raw_documents, y=None): ...
    vocabulary_: Incomplete
    def fit_transform(self, raw_documents, y=None): ...
    def transform(self, raw_documents): ...
    def inverse_transform(self, X): ...
    def get_feature_names_out(self, input_features=None): ...
    def __sklearn_tags__(self): ...

class TfidfTransformer(
    OneToOneFeatureMixin,
    TransformerMixin,
    BaseEstimator,
    auto_wrap_output_keys=None,
):
    norm: Incomplete
    use_idf: Incomplete
    smooth_idf: Incomplete
    sublinear_tf: Incomplete
    def __init__(
        self,
        *,
        norm: str = "l2",
        use_idf: bool = True,
        smooth_idf: bool = True,
        sublinear_tf: bool = False,
    ) -> None: ...
    idf_: Incomplete
    def fit(self, X, y=None): ...
    def transform(self, X, copy: bool = True): ...
    def __sklearn_tags__(self): ...

class TfidfVectorizer(CountVectorizer):
    norm: Incomplete
    use_idf: Incomplete
    smooth_idf: Incomplete
    sublinear_tf: Incomplete
    def __init__(
        self,
        *,
        input: str = "content",
        encoding: str = "utf-8",
        decode_error: str = "strict",
        strip_accents=None,
        lowercase: bool = True,
        preprocessor=None,
        tokenizer=None,
        analyzer: str = "word",
        stop_words=None,
        token_pattern: str = "(?u)\\b\\w\\w+\\b",  # noqa: S107 -- default value mirrors upstream; stub is never executed
        ngram_range=(1, 1),
        max_df: float = 1.0,
        min_df: int = 1,
        max_features=None,
        vocabulary=None,
        binary: bool = False,
        dtype=...,
        norm: str = "l2",
        use_idf: bool = True,
        smooth_idf: bool = True,
        sublinear_tf: bool = False,
    ) -> None: ...
    @property
    def idf_(self): ...
    @idf_.setter
    def idf_(self, value) -> None: ...
    def fit(self, raw_documents, y=None): ...
    def fit_transform(self, raw_documents, y=None): ...
    def transform(self, raw_documents): ...
    def __sklearn_tags__(self): ...
