"""Placeholder source for the hand-written `aiortc` stubs.

aiortc is an opt-in extra no package depends on: trackinizer imports it under
`TYPE_CHECKING` and loads it lazily only where a user installed it. Without the
wheel, basedpyright's `reportMissingModuleSource` fires on that import -- a
diagnostic about the environment, not the code.

This placeholder satisfies source resolution. Types still come from the
adjacent `.pyi` (stubs win over source), so nothing here mirrors the real API.
`typings` is on `extraPaths` so this file is found; it is never on the runtime
`sys.path`.
"""
