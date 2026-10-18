from .tokenization_utils_base import PreTrainedTokenizerBase

class TokenizersBackend(PreTrainedTokenizerBase):
    def __init__(self, *args: object, **kwargs: object) -> None: ...
