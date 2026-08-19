# palettes

**Pure-Python, zero-dependency color palette toolkit**

`palettes` provides pre-computed, display-ready and integer-indexed color lookup tables for any Python environment. It has **zero dependencies** on any other PyDevices library or external package, running identically on **MicroPython**, **CircuitPython**, **CPython (desktop/server)**, and **PyScript (Web)**.

### Universal Color Tooling
While `palettes` integrates seamlessly with PyDevices displays, it is a standalone utility useful for **any Python project** needing easy-to-access named and indexed palettes, including:
- **Embedded & Hardware**: RGB565 displays, addressable LEDs / NeoPixels, status indicators.
- **Terminal & CLI Tools**: ANSI terminal formatting, logs, status alerts.
- **Data & Charts**: Consistent categorical and sequential color mapping.
- **Theme Engines**: Swappable UI color palettes with human-readable color names.


---

## Palette Types & Previews

### 1. Color Wheel (`"wheel"`)
Generates a smooth, continuous HSV-based color spectrum. Ideal for color pickers, circular progress rings, and continuous gradient animations:

```python
from palettes import get_palette

# 360-step full saturation color wheel (16-bit RGB565)
wheel = get_palette(name="wheel", length=360, saturation=1.0, color_depth=16)
color = wheel[180]  # get color at hue angle 180°
```

![Color Wheel Preview](https://raw.githubusercontent.com/PyDevices/palettes/main/docs/images/palette_wheel.png)

---

### 2. Material Design (`"material_design"`)
A curated collection of modern UI colors based on Google's Material Design palette:

```python
material = get_palette(name="material_design", color_depth=16)
primary_color = material[0]
color_name = material.color_name(0)  # e.g., "Red 500"
```

![Material Design Preview](https://raw.githubusercontent.com/PyDevices/palettes/main/docs/images/palette_material.png)

---

### 3. Color Cube (`"cube"`)
A structured 3D RGB color cube mapped into a discrete indexed palette. Excellent for retro imaging and color-space mapping:

```python
cube = get_palette(name="cube", size=5, color_depth=16)
```

![Color Cube Preview](https://raw.githubusercontent.com/PyDevices/palettes/main/docs/images/palette_cube.png)

---

### 4. Named Windows-16 (`"default"`)
The classic 16 standard system colors:

```python
win16 = get_palette(name="default", color_depth=16)
navy = win16[1]  # Black, Navy, Blue, Green, Teal, Lime, Cyan, etc.
```

![Windows-16 Preview](https://raw.githubusercontent.com/PyDevices/palettes/main/docs/images/palette_win16.png)

---

## Quick Start: Painting on a Display

```python
import board_config
from palettes import get_palette

display_drv = board_config.display_drv
palette = get_palette(name="wheel", length=display_drv.width, color_depth=16)

# Draw a full-width color spectrum band
for x in range(display_drv.width):
    display_drv.fill_rect(x, 0, 1, 40, palette[x])

display_drv.show()
```

---

## Installation

```python
import mip
mip.install("palettes", index="https://PyDevices.github.io/mip")
```

```bash
pip install -i https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ pydevices-palettes
```

Full options: [docs/index.md](docs/index.md).

## Links & Demos

- [Documentation](https://palettes.readthedocs.io)
- [Source Code](https://github.com/PyDevices/palettes)
- [PyScript Live Demos](https://pydevices.github.io/pydevices-examples/pyscript/) (`palettes_demo.py`)
- Related: [pydevices](https://github.com/PyDevices/pydevices), [pdwidgets](https://github.com/PyDevices/pdwidgets), [pydevices-examples](https://github.com/PyDevices/pydevices-examples)

## License

MIT — see [LICENSE](LICENSE).

