# Changelog

All notable typings changes are documented here. This project follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

Both packages in this repository, `rekursiv-ai-typings` and
`rekursiv-ai-typeshed`, share one version and one release tag.

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
