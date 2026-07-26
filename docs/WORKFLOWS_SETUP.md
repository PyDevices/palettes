# GitHub Actions setup

Workflow files live in `.github/workflows/`. Org secrets used by publish:

- `TESTPYPI_API_TOKEN`
- `MICROPYTHON_LIB_DEPLOY_TOKEN`

PATs that push workflow YAML need the **`workflow`** scope.

## Setup status

| # | Task | Status |
|---|------|--------|
| 1 | Push workflow YAML to `.github/workflows/` | Done |
| 2 | Publish v0.0.3 → micropython-lib + TestPyPI + MIP | Done |
| 3 | Read the Docs → [palettes.readthedocs.io](https://palettes.readthedocs.io/) | Done |
| 4 | GitHub Pages → [pydevices.github.io/palettes](https://pydevices.github.io/palettes/) | Done |

### Read the Docs (one-time, completed)

1. Sign in at https://readthedocs.org with the PyDevices GitHub org account.
2. **Import a Project** → `PyDevices/palettes`.
3. Confirm `.readthedocs.yaml` at repo root (MkDocs, Python 3.13).
4. Default version `latest` → public URL `https://palettes.readthedocs.io/`.

### GitHub Pages (one-time, completed)

The **Deploy Pages site** workflow pushes `web/` to the `gh-pages` branch.
Pages is enabled from **Settings → Pages → Deploy from branch → `gh-pages` / root**.

Target URL: https://pydevices.github.io/palettes/

## Republish a release

Bump the semver (TestPyPI rejects duplicate versions and burned filenames):

```bash
./scripts/publish_release_tag.sh X.Y.Z --push
```

Or Actions → **Publish micropython-lib** → Run workflow.

Current TestPyPI release: **`palettes` 0.0.3** ([project page](https://test.pypi.org/project/palettes/0.0.3/)).
