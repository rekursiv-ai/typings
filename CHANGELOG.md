# Changelog

All notable typings changes are documented here. This project follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## 0.1.10 - 2026-10-26

### Changed

- The bashlex stubs type the parser, its AST nodes and their fields.
- The YAML stubs type composition and node values.

## 0.1.9 - 2026-10-23

### Changed

- The httpx2 `QueryParams` stub is a `Mapping[str, str]`, with `__iter__` and
  `__len__`, and `get` defaults to `None`.

## 0.1.8 - 2026-10-23

### Removed

- `rekursiv-ai-typeshed`, the patched standard-library stubs. Neither ty nor
  pyrefly needs them; cast a numeric `**` with `float(...)` instead.

## 0.1.7 - 2026-10-21

### Changed

- Stubs for h5py `Dataset.chunks` and starlette's `TestClient.websocket_connect`
  with its `WebSocketTestSession`.
- The `typecheck` group requires `rekursiv-ai-typeshed` 0.1.6 or later.

## 0.1.6 - 2026-10-20

### Changed

- Stubs for the Torch device, the LBFGS step closure, and alias values.

## 0.1.5 - 2026-10-17

### Changed

- Publishes to PyPI through a trusted publisher, as every other package does.

## 0.1.4 - 2026-10-17

### Changed

- `rekursiv-ai-typeshed` README title is `typeshed🛖`.
- Stubs for `pyarrow` file streams and `torch.distributed.checkpoint.state_dict`.

## 0.1.3 - 2026-10-17

### Changed

- Both packages now share one version.
- Rewrote both READMEs.
- `rekursiv-ai-typeshed` lists its repository and classifiers on PyPI.

## 0.1.0 - 2026-10-17

### Added

- `rekursiv-ai-typings`: hand-written stubs for 72 libraries, each shipped as
  its PEP 561 `<pkg>-stubs` package; partial trees marked `partial`.
- `rekursiv-ai-typeshed`: the checkers' stdlib with `int`/`float` `**`
  returning `float`, published as an sdist.
