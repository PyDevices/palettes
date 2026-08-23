# Palette Gallery

A visual reference and interactive explorer for all built-in color palette families in `palettes`.

| Family | Class | Key | Primary Use Case |
|:---|:---|:---|:---|
| **Color Wheel** | `WheelPalette` | `"wheel"` | Continuous color ramps, hue sweeps, rainbows, circular gauges |
| **Material Design** | `MDPalette` | `"material_design"` | Modern UI widget theming, semantic status colors, contrast shades |
| **Color Cube** | `CubePalette` | `"cube"` | Quantized 8, 27, 64, or 125 color spaces for dithering and Retro UIs |
| **Windows-16** | `Palette` | `"default"` | Standard named 16-color ANSI/Windows retro palette |

---

## 💻 Live Palette Explorer

Adjust the palette parameters below and click **▶ Run** to see the colors render live in your browser:

<div class="pydevices-live-demo">
  <div class="demo-editor-pane">
    <textarea class="code-editor">
from palettes import get_palette
from displaydev.auto import AutoDisplay

display = AutoDisplay(width=320, height=240, canvas_id=CANVAS_ID)
display.fill(0x0000)

# Try changing name to "cube", "default", or "material_design"
palette = get_palette("wheel", color_depth=16, length=320, saturation=1.0)

# Render a full-screen vertical sweep
for x in range(display.width):
    display.fill_rect(x, 0, 1, display.height, palette[x])

display.show()
print(f"Rendered {len(palette)} colors from the wheel palette!")
    </textarea>
    <div class="demo-controls">
      <button class="run-btn" disabled>▶ Run</button>
      <button class="reset-btn">↺ Reset</button>
      <span class="demo-status">Initializing Python…</span>
    </div>
    <pre class="demo-output"></pre>
  </div>
  <div class="demo-canvas-pane">
    <canvas id="canvas_palette_gallery" width="320" height="240" tabindex="0"></canvas>
  </div>
</div>

---

## 1. Color Wheel (`"wheel"`)

`WheelPalette` generates an evenly spaced rainbow ramp by stepping through HSV hues while maintaining constant saturation and value.

![Color Wheel Preview](images/palette_wheel.png)

```python
from palettes import get_palette

# 256-step wheel at full saturation
wheel = get_palette("wheel", color_depth=16, length=256, saturation=1.0)

# Access color at index
color_50 = wheel[50]
```

### Parameters
* `length` (int): Number of steps around the hue circle (default `256`).
* `saturation` (float): Color saturation between `0.0` (grayscale) and `1.0` (vibrant, default `1.0`).
* `value` (float): Brightness multiplier between `0.0` and `1.0` (default `1.0`).
* `color_depth` (int): Bit depth (`16` for RGB565, `24` for RGB888, `32` for ARGB8888).
* `swapped` (bool): If `True`, swap bytes in 16-bit RGB565 for SPI display hardware.

---

## 2. Material Design (`"material_design"`)

`MDPalette` provides Google's Material Design color palette with 19 distinct color families, each containing shades from `50` (lightest) to `900` (deepest), plus accent shades (`A100`–`A700`).

![Material Design Preview](images/palette_material.png)

```python
from palettes import get_palette

# Get the blue palette family
blue = get_palette("material_design", color_depth=16, color_name="blue")

header_bg = blue["500"]  # Primary brand color
card_bg   = blue["50"]   # Light tint background
accent_fg = blue["A400"] # Vivid accent
```

### Available Color Families
`red`, `pink`, `purple`, `deep_purple`, `indigo`, `blue`, `light_blue`, `cyan`, `teal`, `green`, `light_green`, `lime`, `yellow`, `amber`, `orange`, `deep_orange`, `brown`, `grey`, `blue_grey`.

---

## 3. Color Cube (`"cube"`)

`CubePalette` divides the RGB color space into equal steps along each axis ($N \times N \times N$).

![Color Cube Preview](images/palette_cube.png)

| Cube Size | Total Colors | Steps per Channel (R, G, B) | Typical Use |
|:---|:---|:---|:---|
| **8** | 8 | 2 steps (0, 255) | 3-bit primary colors |
| **27** | 27 | 3 steps (0, 127, 255) | Ultra-compact retro UIs |
| **64** | 64 | 4 steps (0, 85, 170, 255) | 6-bit color quantization |
| **125** | 125 | 5 steps (0, 64, 128, 191, 255) | High-fidelity dithering |

```python
cube = get_palette("cube", color_depth=16, length=64)
```

---

## 4. Named Windows-16 (`"default"`)

The standard 16-color ANSI/Windows palette accessible by name or integer index.

![Windows-16 Preview](images/palette_win16.png)

```python
from palettes import get_palette

win16 = get_palette("default", color_depth=16)

black   = win16["black"]   # 0x0000
red     = win16["red"]     # 0x8000
green   = win16["green"]   # 0x0400
blue    = win16["blue"]    # 0x0010
yellow  = win16["yellow"]  # 0x8400
white   = win16["white"]   # 0xFFFF
```
