# rekursiv-ai-typings

[![PyPI version](https://img.shields.io/pypi/v/rekursiv-ai-typings.svg)](https://pypi.org/project/rekursiv-ai-typings/)
[![CI](https://github.com/rekursiv-ai/typings/actions/workflows/package-validation.yml/badge.svg?branch=main)](https://github.com/rekursiv-ai/typings/actions/workflows/package-validation.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](pyproject.toml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/discord/1530237005311639592?logo=discord&logoColor=white&label=Discord&color=5865F2)](https://discord.gg/2GZFPPvCqn)

Hand-written type stubs for third-party libraries that ship no types, or ship
types loose enough to fail `basedpyright` and `ty` in strict mode.

## Quick Start

```bash
# Mac:
#   # Required for quick install.
#   brew install uv

# Ubuntu/Debian:
#   # Required for quick install.
#   sudo apt-get install -y curl
#   curl -LsSf https://astral.sh/uv/install.sh | sh

uv add --dev rekursiv-ai-typings

# Alternatively: python -m pip install rekursiv-ai-typings
```

Each `typings/<pkg>/` installs as the PEP 561 stub-only package `<pkg>-stubs`.
Both checkers find those in site-packages on their own, so installing the
wheel is the whole setup.

## Example

```python
import yaml

data = yaml.safe_load("a: 1")
reveal_type(data)  # object, not Any
```

## Features

### Override one library

A project's own stubs win. Put them under the project's `stubPath`, named the
same way:

```text
typings/<pkg>-stubs/__init__.pyi
```

```toml
[tool.basedpyright]
stubPath = "typings"

[tool.ty.environment]
extra-paths = ["typings"]
```

Name the directory `<pkg>-stubs`, not `<pkg>`: ty ignores a local
`typings/<pkg>/` while an installed `<pkg>-stubs` exists.

### Partial stubs

A tree that stubs only some of a library's modules (`fastapi`, `starlette`,
`lxml`, `curl_cffi`, `lark`, `optax`, `sklearn`, `torch`) carries a `py.typed`
reading `partial`, so the checkers take the remaining modules from the library
itself.

### Placeholder sources

`triton` is a linux-only wheel. Where it is absent, basedpyright reports
`reportMissingModuleSource` on every `import triton`, and an inline
suppression is then flagged unnecessary on linux. The wheel therefore also
installs the `triton` tree, `.py` placeholders included, at
`.venv/share/rekursiv-ai-typings/triton`. Add its parent to `extraPaths`:

```toml
[tool.basedpyright]
extraPaths = [".venv/share/rekursiv-ai-typings"]
```

Types still come from `triton-stubs`; the placeholders only satisfy source
resolution.

### Patched standard library

`rekursiv-ai-typeshed`, in `typeshed/`, is the companion package: the
checkers' bundled stdlib stubs with `int`/`float` `**` returning `float`
instead of `Any`. It needs one path per checker; see `typeshed/README.md`.
