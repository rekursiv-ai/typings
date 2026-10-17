from jax import Array

class Space:
    def sample(self, key: Array) -> Array: ...
    def contains(self, x: Array) -> Array: ...

class Discrete(Space):
    n: int
    shape: tuple[int, ...]
    dtype: object

    def __init__(self, num_categories: int) -> None: ...

class Box(Space):
    low: Array | float
    high: Array | float
    shape: tuple[int, ...]
    dtype: object

    def __init__(
        self,
        low: Array | float,
        high: Array | float,
        shape: tuple[int, ...],
        dtype: object = ...,
    ) -> None: ...
