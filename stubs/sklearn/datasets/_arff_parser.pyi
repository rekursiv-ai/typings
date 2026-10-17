from sklearn.externals._arff import ArffSparseDataType as ArffSparseDataType
from sklearn.utils._chunking import (
    chunk_generator as chunk_generator,
    get_chunk_n_rows as get_chunk_n_rows,
)
from sklearn.utils._optional_dependencies import (
    check_pandas_support as check_pandas_support,
)
from sklearn.utils.fixes import pd_fillna as pd_fillna

def load_arff_from_gzip_file(
    gzip_file,
    parser,
    output_type,
    openml_columns_info,
    feature_names_to_select,
    target_names_to_select,
    shape=None,
    read_csv_kwargs=None,
): ...
