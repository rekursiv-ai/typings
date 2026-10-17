from sklearn.manifold._classical_mds import ClassicalMDS as ClassicalMDS
from sklearn.manifold._isomap import Isomap as Isomap
from sklearn.manifold._locally_linear import (
    LocallyLinearEmbedding as LocallyLinearEmbedding,
    locally_linear_embedding as locally_linear_embedding,
)
from sklearn.manifold._mds import (
    MDS as MDS,
    smacof as smacof,
)
from sklearn.manifold._spectral_embedding import (
    SpectralEmbedding as SpectralEmbedding,
    spectral_embedding as spectral_embedding,
)
from sklearn.manifold._t_sne import (
    TSNE as TSNE,
    trustworthiness as trustworthiness,
)

__all__ = [
    "MDS",
    "TSNE",
    "ClassicalMDS",
    "Isomap",
    "LocallyLinearEmbedding",
    "SpectralEmbedding",
    "locally_linear_embedding",
    "smacof",
    "spectral_embedding",
    "trustworthiness",
]
