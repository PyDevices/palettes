# GitHub Actions setup

Workflow files live in `.github/workflows/`. Org secrets used by publish:

- `TESTPYPI_API_TOKEN`
- `MICROPYTHON_LIB_DEPLOY_TOKEN`

PATs that push workflow YAML need the **`workflow`** scope.

## Manual follow-up status

| # | Task | Status |
|---|------|--------|
| 1 | Push workflow YAML to `.github/workflows/` | Done |
| 2 | Publish v0.0.1 → micropython-lib + TestPyPI + MIP | **Pending** (tag push) |
| 3 | Read the Docs → `palettes.readthedocs.io` | **Pending** (admin) |
| 4 | Enable GitHub Pages (`gh-pages` branch) | **Pending** (admin) |

### #3 Read the Docs (one-time)

1. Sign in at https://readthedocs.org with the PyDevices GitHub org account.
2. **Import a Project** → `PyDevices/palettes`.
3. Confirm `.readthedocs.yaml` at repo root (MkDocs, Python 3.13).
4. Default version `latest` → public URL `https://palettes.readthedocs.io/`.

### #4 GitHub Pages (one-time)

The **Deploy Pages site** workflow pushes `web/` to the `gh-pages` branch. Enable
the site in repo settings:

**Settings → Pages → Deploy from branch → `gh-pages` / root**

Target URL: https://pydevices.github.io/palettes/

To republish a release:

```bash
./scripts/publish_release_tag.sh 0.0.1 --push
```

Or Actions → **Publish micropython-lib** → Run workflow.
