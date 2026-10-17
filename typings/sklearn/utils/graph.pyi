from sklearn.metrics.pairwise import pairwise_distances as pairwise_distances
from sklearn.utils._param_validation import (
    Integral as Integral,
    Interval as Interval,
    validate_params as validate_params,
)

def single_source_shortest_path_length(graph, source, *, cutoff=None): ...
