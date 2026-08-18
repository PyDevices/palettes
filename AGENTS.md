# AGENTS.md — palettes

Color palette toolkit for PyDevices (`import palettes`).

## Environment

- Python venv at `.venv` — `.venv/bin/python`, `.venv/bin/ruff`
- No runtime dependencies on other PyDevices packages
- Source layout: `lib/palettes/` (import name `palettes`)

## Tests and lint

```bash
.venv/bin/python -m unittest discover -s tests
.venv/bin/ruff check lib tests scripts
```

## Publishing

Commit `VERSION=X.Y.Z` and publish GitHub Release `vX.Y.Z`. The import and MIP
name stay `palettes`; the TestPyPI distribution is `pydevices-palettes`.
Procedure: [.github/docs/publishing-automation.md](https://github.com/PyDevices/.github/blob/main/docs/publishing-automation.md).

## Cursor Cloud specific instructions

The Cloud Agent update script creates the repo-root `.venv` (with `ruff`). Since
`palettes` is a source-only package (not pip-installed), the `unittest discover`
command above needs `lib/` on the path — the bare command fails with
`ModuleNotFoundError: No module named 'palettes'`. Mirror CI (`env: PYTHONPATH: lib`):

```bash
PYTHONPATH=lib .venv/bin/python -m unittest discover -s tests
```
