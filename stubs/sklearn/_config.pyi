from collections.abc import Generator
from contextlib import contextmanager as contextmanager

def get_config(): ...
def set_config(
    assume_finite=None,
    working_memory=None,
    print_changed_only=None,
    display=None,
    pairwise_dist_chunk_size=None,
    enable_cython_pairwise_dist=None,
    array_api_dispatch=None,
    transform_output=None,
    enable_metadata_routing=None,
    skip_parameter_validation=None,
) -> None: ...
@contextmanager
def config_context(
    *,
    assume_finite=None,
    working_memory=None,
    print_changed_only=None,
    display=None,
    pairwise_dist_chunk_size=None,
    enable_cython_pairwise_dist=None,
    array_api_dispatch=None,
    transform_output=None,
    enable_metadata_routing=None,
    skip_parameter_validation=None,
) -> Generator[None]: ...
