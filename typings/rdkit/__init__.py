"""Placeholder source for the hand-written `rdkit` stubs.

RDKit is installed only in the isolated CASMI preparation interpreters, never in
the project environment, so basedpyright's `reportMissingModuleSource` would fire on
every import of it. This placeholder satisfies source resolution. Types come from the
adjacent `.pyi` (stubs win over source), so nothing here mirrors the real API.
`typings` is on `extraPaths` so this file is found; it is never on the runtime
`sys.path`.
"""
