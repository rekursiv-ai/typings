from jax import Array
from jax._src.sharding_impls import (
    NamedSharding,
    PartitionSpec as P,
)
from jax._src.typing import DTypeLike

def categorical(
    key: Array,
    logits: Array,
    axis: int = -1,
    shape: tuple[int, ...] | None = None,
    replace: bool = True,
    mode: str | None = None,
    *,
    out_sharding: NamedSharding | P | None = None,
) -> Array: ...
def fold_in(key: Array, data: int | Array) -> Array: ...
def PRNGKey(seed: int) -> Array: ...
def key(seed: int) -> Array: ...
def split(key: Array, num: int | tuple[int, ...] = 2) -> Array: ...
def uniform(
    key: Array,
    shape: tuple[int, ...] = (),
    dtype: DTypeLike | type | None = None,
    minval: float | Array = 0.0,
    maxval: float | Array = 1.0,
) -> Array: ...
def randint(
    key: Array,
    shape: tuple[int, ...],
    minval: int | Array,
    maxval: int | Array,
    dtype: DTypeLike | type | None = None,
) -> Array: ...
def choice(
    key: Array,
    a: int | Array,
    shape: tuple[int, ...] = (),
    replace: bool = True,
    p: Array | None = None,
) -> Array: ...
def permutation(
    key: Array,
    x: int | Array,
    axis: int = 0,
    independent: bool = False,
) -> Array: ...
def normal(
    key: Array,
    shape: tuple[int, ...] = (),
    dtype: DTypeLike | type | None = None,
) -> Array: ...
