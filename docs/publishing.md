# Publishing and releases

How a published GitHub Release becomes versioned **`pydevices-palettes`**
artifacts on [TestPyPI](https://test.pypi.org/project/pydevices-palettes/) and
the unprefixed **`palettes`** package in the PyDevices MIP index.

## Pipeline

```text
published GitHub Release vX.Y.Z
  publish-release-packages.yml
    ├─ shared build + clean import test
    ├─ API-token upload → TestPyPI
    └─ exact ref → serialized PyDevices/mip queue → Pages artifact
```

## Version numbers

Format: **`0.0.x`** semver until promoted. TestPyPI rejects duplicate versions and
rejects filenames that were previously uploaded then deleted (even under a
different project name).

Update and commit `VERSION`, then create and publish a GitHub Release whose tag
is exactly `vX.Y.Z`. To retry a failed channel, manually run
`publish-release-packages.yml` with that same tag.

The TestPyPI distribution is **`pydevices-palettes`**. Its import and MIP package remain **`palettes`**.

## Authentication

TestPyPI uses the existing `TESTPYPI_API_TOKEN`, owned by `bdbarnett`, while
the PyDevices TestPyPI organization request is pending. The existing
`MICROPYTHON_LIB_DEPLOY_TOKEN` dispatches the central MIP queue.

## Install from TestPyPI

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pydevices-palettes
```

## MIP install

```python
mip.install("palettes", index="https://PyDevices.github.io/mip")
```

`palettes` is independent of the `pydevices` and `pydevices-desktop`
meta-packages.
