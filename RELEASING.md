# Releasing

Releases are automatic. Every push to `main` that changes a distribution's
files runs `.github/workflows/publish-pypi.yml`, which stamps a date version
(`YYYY.M.D.<run>`) and uploads to PyPI:

| Changed paths | Publishes |
|---|---|
| `typings/`, `hatch_build.py`, `pyproject.toml`, `README.md` | `rekursiv-ai-typings` (wheel + sdist) |
| `typeshed/` | `rekursiv-ai-typeshed` (sdist only) |

`rekursiv-ai-typeshed` never ships a wheel: its build copies the stdlib stubs
out of the installer's own `ty` and `basedpyright`, so a prebuilt wheel would
freeze them at the release's checker versions.

To republish without a change:

```bash
gh workflow run publish-pypi.yml --repo rekursiv-ai/typings -f packages="typings typeshed"
```

The upload authenticates with the `PYPI_API_TOKEN` secret of the `pypi`
environment. If PyPI rejects it, rotate that secret.
