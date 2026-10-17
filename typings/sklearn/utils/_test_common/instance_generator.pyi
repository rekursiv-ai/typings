from _typeshed import Incomplete
from sklearn import (
    clone as clone,
    config_context as config_context,
)
from sklearn.calibration import CalibratedClassifierCV as CalibratedClassifierCV
from sklearn.cluster import (
    HDBSCAN as HDBSCAN,
    AffinityPropagation as AffinityPropagation,
    AgglomerativeClustering as AgglomerativeClustering,
    Birch as Birch,
    BisectingKMeans as BisectingKMeans,
    FeatureAgglomeration as FeatureAgglomeration,
    KMeans as KMeans,
    MeanShift as MeanShift,
    MiniBatchKMeans as MiniBatchKMeans,
    SpectralBiclustering as SpectralBiclustering,
    SpectralClustering as SpectralClustering,
    SpectralCoclustering as SpectralCoclustering,
)
from sklearn.compose import ColumnTransformer as ColumnTransformer
from sklearn.covariance import (
    GraphicalLasso as GraphicalLasso,
    GraphicalLassoCV as GraphicalLassoCV,
)
from sklearn.cross_decomposition import (
    CCA as CCA,
    PLSSVD as PLSSVD,
    PLSCanonical as PLSCanonical,
    PLSRegression as PLSRegression,
)
from sklearn.decomposition import (
    NMF as NMF,
    PCA as PCA,
    DictionaryLearning as DictionaryLearning,
    FactorAnalysis as FactorAnalysis,
    FastICA as FastICA,
    IncrementalPCA as IncrementalPCA,
    KernelPCA as KernelPCA,
    LatentDirichletAllocation as LatentDirichletAllocation,
    MiniBatchDictionaryLearning as MiniBatchDictionaryLearning,
    MiniBatchNMF as MiniBatchNMF,
    MiniBatchSparsePCA as MiniBatchSparsePCA,
    SparseCoder as SparseCoder,
    SparsePCA as SparsePCA,
    TruncatedSVD as TruncatedSVD,
)
from sklearn.discriminant_analysis import (
    LinearDiscriminantAnalysis as LinearDiscriminantAnalysis,
)
from sklearn.dummy import DummyClassifier as DummyClassifier
from sklearn.ensemble import (
    AdaBoostClassifier as AdaBoostClassifier,
    AdaBoostRegressor as AdaBoostRegressor,
    BaggingClassifier as BaggingClassifier,
    BaggingRegressor as BaggingRegressor,
    ExtraTreesClassifier as ExtraTreesClassifier,
    ExtraTreesRegressor as ExtraTreesRegressor,
    GradientBoostingClassifier as GradientBoostingClassifier,
    GradientBoostingRegressor as GradientBoostingRegressor,
    HistGradientBoostingClassifier as HistGradientBoostingClassifier,
    HistGradientBoostingRegressor as HistGradientBoostingRegressor,
    IsolationForest as IsolationForest,
    RandomForestClassifier as RandomForestClassifier,
    RandomForestRegressor as RandomForestRegressor,
    RandomTreesEmbedding as RandomTreesEmbedding,
    StackingClassifier as StackingClassifier,
    StackingRegressor as StackingRegressor,
    VotingClassifier as VotingClassifier,
    VotingRegressor as VotingRegressor,
)
from sklearn.exceptions import SkipTestWarning as SkipTestWarning
from sklearn.experimental import enable_halving_search_cv as enable_halving_search_cv
from sklearn.feature_selection import (
    RFE as RFE,
    RFECV as RFECV,
    SelectFdr as SelectFdr,
    SelectFromModel as SelectFromModel,
    SelectKBest as SelectKBest,
    SequentialFeatureSelector as SequentialFeatureSelector,
)
from sklearn.frozen import FrozenEstimator as FrozenEstimator
from sklearn.kernel_approximation import (
    Nystroem as Nystroem,
    PolynomialCountSketch as PolynomialCountSketch,
    RBFSampler as RBFSampler,
    SkewedChi2Sampler as SkewedChi2Sampler,
)
from sklearn.linear_model import (
    ARDRegression as ARDRegression,
    BayesianRidge as BayesianRidge,
    ElasticNet as ElasticNet,
    ElasticNetCV as ElasticNetCV,
    GammaRegressor as GammaRegressor,
    HuberRegressor as HuberRegressor,
    LarsCV as LarsCV,
    Lasso as Lasso,
    LassoCV as LassoCV,
    LassoLars as LassoLars,
    LassoLarsCV as LassoLarsCV,
    LassoLarsIC as LassoLarsIC,
    LinearRegression as LinearRegression,
    LogisticRegression as LogisticRegression,
    LogisticRegressionCV as LogisticRegressionCV,
    MultiTaskElasticNet as MultiTaskElasticNet,
    MultiTaskElasticNetCV as MultiTaskElasticNetCV,
    MultiTaskLasso as MultiTaskLasso,
    MultiTaskLassoCV as MultiTaskLassoCV,
    OrthogonalMatchingPursuitCV as OrthogonalMatchingPursuitCV,
    PassiveAggressiveClassifier as PassiveAggressiveClassifier,
    PassiveAggressiveRegressor as PassiveAggressiveRegressor,
    Perceptron as Perceptron,
    PoissonRegressor as PoissonRegressor,
    QuantileRegressor as QuantileRegressor,
    RANSACRegressor as RANSACRegressor,
    Ridge as Ridge,
    RidgeClassifier as RidgeClassifier,
    SGDClassifier as SGDClassifier,
    SGDOneClassSVM as SGDOneClassSVM,
    SGDRegressor as SGDRegressor,
    TheilSenRegressor as TheilSenRegressor,
    TweedieRegressor as TweedieRegressor,
)
from sklearn.manifold import (
    MDS as MDS,
    TSNE as TSNE,
    Isomap as Isomap,
    LocallyLinearEmbedding as LocallyLinearEmbedding,
    SpectralEmbedding as SpectralEmbedding,
)
from sklearn.mixture import (
    BayesianGaussianMixture as BayesianGaussianMixture,
    GaussianMixture as GaussianMixture,
)
from sklearn.model_selection import (
    FixedThresholdClassifier as FixedThresholdClassifier,
    GridSearchCV as GridSearchCV,
    HalvingGridSearchCV as HalvingGridSearchCV,
    HalvingRandomSearchCV as HalvingRandomSearchCV,
    RandomizedSearchCV as RandomizedSearchCV,
    TunedThresholdClassifierCV as TunedThresholdClassifierCV,
)
from sklearn.multiclass import (
    OneVsOneClassifier as OneVsOneClassifier,
    OneVsRestClassifier as OneVsRestClassifier,
    OutputCodeClassifier as OutputCodeClassifier,
)
from sklearn.multioutput import (
    ClassifierChain as ClassifierChain,
    MultiOutputClassifier as MultiOutputClassifier,
    MultiOutputRegressor as MultiOutputRegressor,
    RegressorChain as RegressorChain,
)
from sklearn.neighbors import (
    KernelDensity as KernelDensity,
    KNeighborsClassifier as KNeighborsClassifier,
    KNeighborsRegressor as KNeighborsRegressor,
    KNeighborsTransformer as KNeighborsTransformer,
    NeighborhoodComponentsAnalysis as NeighborhoodComponentsAnalysis,
    RadiusNeighborsTransformer as RadiusNeighborsTransformer,
)
from sklearn.neural_network import (
    BernoulliRBM as BernoulliRBM,
    MLPClassifier as MLPClassifier,
    MLPRegressor as MLPRegressor,
)
from sklearn.pipeline import (
    FeatureUnion as FeatureUnion,
    Pipeline as Pipeline,
)
from sklearn.preprocessing import (
    KBinsDiscretizer as KBinsDiscretizer,
    OneHotEncoder as OneHotEncoder,
    SplineTransformer as SplineTransformer,
    StandardScaler as StandardScaler,
    TargetEncoder as TargetEncoder,
)
from sklearn.random_projection import (
    GaussianRandomProjection as GaussianRandomProjection,
    SparseRandomProjection as SparseRandomProjection,
)
from sklearn.semi_supervised import (
    LabelPropagation as LabelPropagation,
    LabelSpreading as LabelSpreading,
    SelfTrainingClassifier as SelfTrainingClassifier,
)
from sklearn.svm import (
    SVC as SVC,
    SVR as SVR,
    LinearSVC as LinearSVC,
    LinearSVR as LinearSVR,
    NuSVC as NuSVC,
    NuSVR as NuSVR,
    OneClassSVM as OneClassSVM,
)
from sklearn.tree import (
    DecisionTreeClassifier as DecisionTreeClassifier,
    DecisionTreeRegressor as DecisionTreeRegressor,
)
from sklearn.utils import all_estimators as all_estimators
from sklearn.utils._tags import get_tags as get_tags
from sklearn.utils._testing import SkipTest as SkipTest
from sklearn.utils.fixes import (
    parse_version as parse_version,
    sp_base_version as sp_base_version,
)

CROSS_DECOMPOSITION: Incomplete
rng: Incomplete
INIT_PARAMS: Incomplete
PER_ESTIMATOR_CHECK_PARAMS: dict
SKIPPED_ESTIMATORS: Incomplete
PER_ESTIMATOR_XFAIL_CHECKS: Incomplete
linear_svr_not_thread_safe: str
