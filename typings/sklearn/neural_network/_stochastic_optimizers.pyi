from _typeshed import Incomplete

class BaseOptimizer:
    learning_rate_init: Incomplete
    learning_rate: Incomplete
    def __init__(self, learning_rate_init: float = 0.1) -> None: ...
    def update_params(self, params, grads) -> None: ...
    def iteration_ends(self, time_step) -> None: ...
    def trigger_stopping(self, msg, verbose): ...

class SGDOptimizer(BaseOptimizer):
    lr_schedule: Incomplete
    momentum: Incomplete
    nesterov: Incomplete
    power_t: Incomplete
    velocities: Incomplete
    def __init__(
        self,
        params,
        learning_rate_init: float = 0.1,
        lr_schedule: str = "constant",
        momentum: float = 0.9,
        nesterov: bool = True,
        power_t: float = 0.5,
    ) -> None: ...
    learning_rate: Incomplete
    def iteration_ends(self, time_step) -> None: ...
    def trigger_stopping(self, msg, verbose): ...

class AdamOptimizer(BaseOptimizer):
    beta_1: Incomplete
    beta_2: Incomplete
    epsilon: Incomplete
    t: int
    ms: Incomplete
    vs: Incomplete
    def __init__(
        self,
        params,
        learning_rate_init: float = 0.001,
        beta_1: float = 0.9,
        beta_2: float = 0.999,
        epsilon: float = 1e-08,
    ) -> None: ...
