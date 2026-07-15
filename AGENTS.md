# AGENTS.md — palettes

Color palette toolkit for pydisplay (`import palettes`).

## Environment

- Python venv at `.venv` — `.venv/bin/python`, `.venv/bin/ruff`
- No runtime dependencies on other pydisplay packages
- Source layout: `src/palettes/` (import name `palettes`)

## Tests and lint

```bash
.venv/bin/python -m unittest discover -s tests
.venv/bin/ruff check src tests scripts
```

## Publishing

Tag `vX.Y.Z` triggers micropython-lib sync, MIP index rebuild, and TestPyPI upload.
See `PUBLISHING.md`.

## Cursor Cloud specific instructions

The Cloud Agent update script creates the repo-root `.venv` (with `ruff`). Since
`palettes` is a source-only package (not pip-installed), the `unittest discover`
command above needs `src/` on the path — the bare command fails with
`ModuleNotFoundError: No module named 'palettes'`. Mirror CI (`env: PYTHONPATH: src`):

```bash
PYTHONPATH=src .venv/bin/python -m unittest discover -s tests
```
