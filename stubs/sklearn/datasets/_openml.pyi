import os

__all__ = ["fetch_openml"]

type OpenmlQualitiesType = list[dict[str, str]]
type OpenmlFeaturesType = list[dict[str, str]]

class OpenMLError(ValueError): ...

def fetch_openml(
    name: str | None = None,
    *,
    version: str | int = "active",
    data_id: int | None = None,
    data_home: str | os.PathLike | None = None,
    target_column: str | list | None = "default-target",
    cache: bool = True,
    return_X_y: bool = False,
    as_frame: str | bool = "auto",
    n_retries: int = 3,
    delay: float = 1.0,
    parser: str = "auto",
    read_csv_kwargs: dict | None = None,
): ...
