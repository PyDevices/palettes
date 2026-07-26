# Publishing and releases

How changes in this repo become versioned **`palettes`** wheels on [TestPyPI](https://test.pypi.org/project/palettes/) and MIP packages on [micropython-lib gh-pages](https://PyDevices.github.io/micropython-lib/mip/PyDevices).

## Pipeline

```text
palettes (commit on main)
  ./scripts/publish_release_tag.sh X.Y.Z --push
           │
           ▼
publish-micropython-lib.yml
  sync → micropython/palettes/
  hatch + twine → TestPyPI
  rebuild mip/PyDevices → gh-pages
```

## Version numbers

Format: **`0.0.x`** semver until promoted. TestPyPI rejects duplicate versions and
rejects filenames that were previously uploaded then deleted (even under a
different project name).

```bash
./scripts/publish_release_tag.sh X.Y.Z --push
```

Current release: **`palettes` 0.0.3** on [TestPyPI](https://test.pypi.org/project/palettes/0.0.3/).

## Secrets (repository or org)

| Secret | Purpose |
|--------|---------|
| `TESTPYPI_API_TOKEN` | TestPyPI upload |
| `MICROPYTHON_LIB_DEPLOY_TOKEN` | PAT with `contents:write` on PyDevices/micropython-lib |

## Install from TestPyPI

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ palettes
```

## MIP install

```python
mip.install("palettes", index="https://PyDevices.github.io/micropython-lib/mip/PyDevices")
```

`palettes` is **not** part of `pydisplay-bundle`.
