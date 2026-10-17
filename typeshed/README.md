# typeshed🛖

Standard-library stubs for `ty` and `basedpyright`, patched so that `x ** 0.5`
is a `float` rather than `Any`.

Both checkers bundle typeshed, which says `int.__pow__` and `float.__pow__`
return `Any`. If you enable `reportAny`, every `**` in your code becomes a
warning. Neither checker lets you patch a single stdlib file, so this package
installs a full patched copy of the stdlib stubs for each checker. The copy is
built from whichever `ty` and `basedpyright` you have installed, so it always
matches them.

## Install

```bash
uv add --dev rekursiv-ai-typeshed
```

## Configure

Point each checker at its copy in `pyproject.toml`:

```toml
[tool.basedpyright]
typeshedPath = ".venv/share/rekursiv-ai-typeshed/basedpyright"

[tool.ty.environment]
typeshed = ".venv/share/rekursiv-ai-typeshed/ty"
```
