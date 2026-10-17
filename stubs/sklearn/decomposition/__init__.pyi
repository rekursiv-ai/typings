from sklearn.decomposition._dict_learning import (
    DictionaryLearning as DictionaryLearning,
    MiniBatchDictionaryLearning as MiniBatchDictionaryLearning,
    SparseCoder as SparseCoder,
    dict_learning as dict_learning,
    dict_learning_online as dict_learning_online,
    sparse_encode as sparse_encode,
)
from sklearn.decomposition._factor_analysis import FactorAnalysis as FactorAnalysis
from sklearn.decomposition._fastica import (
    FastICA as FastICA,
    fastica as fastica,
)
from sklearn.decomposition._incremental_pca import IncrementalPCA as IncrementalPCA
from sklearn.decomposition._kernel_pca import KernelPCA as KernelPCA
from sklearn.decomposition._lda import (
    LatentDirichletAllocation as LatentDirichletAllocation,
)
from sklearn.decomposition._nmf import (
    NMF as NMF,
    MiniBatchNMF as MiniBatchNMF,
    non_negative_factorization as non_negative_factorization,
)
from sklearn.decomposition._pca import PCA as PCA
from sklearn.decomposition._sparse_pca import (
    MiniBatchSparsePCA as MiniBatchSparsePCA,
    SparsePCA as SparsePCA,
)
from sklearn.decomposition._truncated_svd import TruncatedSVD as TruncatedSVD
from sklearn.utils.extmath import randomized_svd as randomized_svd

__all__ = [
    "NMF",
    "PCA",
    "DictionaryLearning",
    "FactorAnalysis",
    "FastICA",
    "IncrementalPCA",
    "KernelPCA",
    "LatentDirichletAllocation",
    "MiniBatchDictionaryLearning",
    "MiniBatchNMF",
    "MiniBatchSparsePCA",
    "SparseCoder",
    "SparsePCA",
    "TruncatedSVD",
    "dict_learning",
    "dict_learning_online",
    "fastica",
    "non_negative_factorization",
    "randomized_svd",
    "sparse_encode",
]
