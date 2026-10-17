from collections.abc import Callable

from jax import Array

def interpolant(value: Array) -> Array: ...
def generate_perlin_noise_2d(
    rng: Array,
    shape: tuple[int, int],
    res: tuple[int, int],
    interpolant: Callable[[Array], Array] = ...,
    override_angles: Array | None = ...,
) -> Array: ...
def generate_fractal_noise_2d(
    rng: Array,
    shape: tuple[int, int],
    res: tuple[int, int],
    octaves: int = ...,
    persistence: float = ...,
    lacunarity: int = ...,
    interpolant: Callable[[Array], Array] = ...,
    override_angles: Array | None = ...,
) -> Array: ...
