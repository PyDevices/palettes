# Publishing and releases

How changes in this repo become versioned **`pydevices-palettes`** CPython wheels on [TestPyPI](https://test.pypi.org/project/pydevices-palettes/) and unprefixed **`palettes`** MicroPython packages on [mip gh-pages](https://PyDevices.github.io/mip).

## Pipeline

```text
palettes (commit on main)
  ./scripts/publish_release_tag.sh X.Y.Z --push
           │
           ▼
publish-mip.yml
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

The TestPyPI distribution is **`pydevices-palettes`**. Its import and MIP package remain **`palettes`**.

## Secrets

Requires repository authentication secrets for package uploads and index syncing.

## Install from TestPyPI

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pydevices-palettes
```

## MIP install

```python
mip.install("palettes", index="https://PyDevices.github.io/mip")
```

`palettes` is **not** part of `pydevices-bundle`.
