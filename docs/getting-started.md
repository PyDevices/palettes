# Getting started

## Setup

Install from [micropython-lib MIP](installation.md) or [TestPyPI](installation.md):

```python
import mip
mip.install("palettes", index="https://PyDevices.github.io/micropython-lib/mip/PyDevices")
```

Development clone — put `src/` on `PYTHONPATH` or copy `src/palettes/` to your device.

## Basic usage

```python
from palettes import get_palette

palette = get_palette(name="wheel", length=256, saturation=1.0)
display_drv.fill_rect(0, 0, 10, 10, palette[0])
```

## Palette types

| `name` | Class | Notes |
|--------|-------|-------|
| `"default"` | `Palette` | Windows 16-color named set |
| `"wheel"` | `WheelPalette` | HSV wheel; `length`, `saturation` kwargs |
| `"cube"` | `CubePalette` | RGB cube; `size` kwarg (2–5) |
| `"material_design"` | `MDPalette` | Material Design swatches |

## Examples

Palette demos remain in [pydisplay `src/examples/`](https://github.com/PyDevices/pydisplay/tree/main/src/examples):

- `palettes_demo.py` — cycles wheel, cube, and material palettes
- `graphics_simpletest.py`, `feathers.py`, and others use `get_palette()` for colors

PyScript installs `palettes` at runtime via `# pyscript mip: palettes`.
