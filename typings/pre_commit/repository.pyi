from pre_commit.hook import Hook
from pre_commit.store import Store

def all_hooks(root_config: dict[str, object], store: Store) -> tuple[Hook, ...]: ...
