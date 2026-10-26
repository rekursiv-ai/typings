from typing import Any, NamedTuple, Protocol

class TransformInitFn(Protocol):
    def __call__[T](self, params: T) -> OptState: ...

class TransformUpdateFn(Protocol):
    def __call__[T](
        self,
        updates: T,
        state: OptState,
        params: T | None = None,
    ) -> tuple[T, OptState]: ...

class GradientTransformation(NamedTuple):
    init: TransformInitFn
    update: TransformUpdateFn

class GradientTransformationExtraArgs(GradientTransformation):
    update: Any

type EmptyState = Any
type OptState = object
type Params = Any
type Updates = Any
type ScalarOrSchedule = float | Any
type Schedule = Any
type TransformUpdateExtraArgsFn = Any
type MaskOrFn = Any

def identity() -> GradientTransformation: ...
def set_to_zero() -> GradientTransformation: ...
def stateless(*args: Any, **kwargs: Any) -> GradientTransformation: ...
def stateless_with_tree_map(*args: Any, **kwargs: Any) -> GradientTransformation: ...
