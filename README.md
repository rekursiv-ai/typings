# typings🏷️

[![PyPI version](https://img.shields.io/pypi/v/rekursiv-ai-typings.svg)](https://pypi.org/project/rekursiv-ai-typings/)
[![CI](https://github.com/rekursiv-ai/typings/actions/workflows/package-validation.yml/badge.svg?branch=main)](https://github.com/rekursiv-ai/typings/actions/workflows/package-validation.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](pyproject.toml)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/discord/1530237005311639592?logo=discord&logoColor=white&label=Discord&color=5865F2)](https://discord.gg/2GZFPPvCqn)

Type stubs for third-party libraries, written by hand. Some of these libraries
ship no types at all. Others ship types that `basedpyright` and `ty` reject in
strict mode.

## Quick Start

```bash
uv add --dev rekursiv-ai-typings
```

See [Install](#install) for additional details.

There is nothing to configure. Each library's stubs install as a separate
`<pkg>-stubs` package (the standard PEP 561 layout), and both checkers look for
those automatically.

## Example

```python
import yaml

data = yaml.safe_load("a: 1")
reveal_type(data)  # object, not Any
```

## Features

### Override one library

If you want your own stubs for a library instead of ours, put them in your
project and they take priority. Name the directory `<pkg>-stubs`:

```text
typings/<pkg>-stubs/__init__.pyi
```

Then tell both checkers where to look:

```toml
[tool.basedpyright]
stubPath = "typings"

[tool.ty.environment]
extra-paths = ["typings"]
```

The `-stubs` suffix matters. If you name the directory `<pkg>`, ty ignores it
and uses ours.

### Partial stubs

Some stubs cover only part of a library: `fastapi`, `starlette`, `lxml`,
`curl_cffi`, `lark`, `optax`, `sklearn`, and `torch`. Each of these is marked
partial, so for any module we don't stub, the checkers fall back to the
library's own types.

### Triton on macOS

`triton` only installs on Linux. On macOS, basedpyright reports
`reportMissingModuleSource` on every `import triton`. To fix that, this package
also installs placeholder `.py` files for triton. Add their location to
`extraPaths`:

```toml
[tool.basedpyright]
extraPaths = [".venv/share/rekursiv-ai-typings"]
```

The placeholders only make the import resolve. The types still come from our
stubs.

## Install

```bash
uv add --dev rekursiv-ai-typings
```

If you're missing `uv`,
- Mac
  ```bash
  brew install uv
  ```
- Linux
  ```bash
  sudo apt install -y curl
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

Or with pip,
```bash
python -m pip install rekursiv-ai-typings
```
