# Integrations

How to use `palettes` alongside `pygraphics`, `pdwidgets`, and hardware display drivers.

---

## 1. Using with `pygraphics`

`palettes` provides color values directly consumable by `pygraphics.FrameBuffer` and `pygraphics.Draw`:

```python
import pygraphics
from palettes import get_palette

# 1. Create a 160x128 RGB565 FrameBuffer
w, h = 160, 128
fb = pygraphics.FrameBuffer(bytearray(w * h * 2), w, h, pygraphics.RGB565)
fb.fill(0x0000)

# 2. Get a 128-step color wheel for a smooth horizontal gradient
palette = get_palette("wheel", color_depth=16, length=h)

for y in range(h):
    fb.hline(0, y, w, palette[y])

# 3. Draw text in high-contrast white
pygraphics.text16(fb, "pygraphics", 20, 56, 0xFFFF)
```

---

## 2. Using with `pdwidgets`

`pdwidgets` uses `palettes` to theme UI components, buttons, and progress indicators:

```python
import pdwidgets as pd
from palettes import get_palette

# Material Design Teal palette for primary theme
teal = get_palette("material_design", color_depth=16, color_name="teal")
grey = get_palette("material_design", color_depth=16, color_name="grey")

screen = pd.Screen(display, bg=grey["100"])

# Theme widgets using palette tokens
app_bar = pd.Widget(screen, w=screen.width, h=32, bg=teal["700"], align=pd.ALIGN.TOP)
btn_primary = pd.Button(screen, label="Submit", bg=teal["500"], fg=0xFFFF, x=20, y=50, radius=4)
btn_cancel  = pd.Button(screen, label="Cancel", bg=grey["300"], fg=grey["900"], x=120, y=50, radius=4)
```

---

## 3. Using with Display Drivers (`displaydev`)

When drawing directly to a hardware display driver (e.g. ST7789 or ILI9341):

```python
import board_config
from palettes import get_palette

drv = board_config.display_drv

# If the SPI driver expects byte-swapped integers:
palette = get_palette("wheel", color_depth=16, length=drv.width, swapped=True)

for x in range(drv.width):
    drv.fill_rect(x, 0, 1, drv.height, palette[x])

drv.show()
```

---

## 4. Cycling Animated Palettes

Because palettes are lightweight indexable objects, animation loops can cycle colors simply by offsetting an integer index:

```python
import time
from palettes import get_palette

wheel = get_palette("wheel", color_depth=16, length=256)

offset = 0
while True:
    for i in range(16):
        color = wheel[(offset + i * 16) % 256]
        display_drv.fill_rect(i * 20, 0, 20, 240, color)
    display_drv.show()
    offset = (offset + 1) % 256
    time.sleep(0.016)  # ~60 FPS
```

---

## 🎮 Live Interactive Gallery Examples

Experience full `palettes` color gradients and animation demos live in your browser:

| Example | Description | Live PyScript Link |
|:---|:---|:---|
| **`palettes_demo`** | Comprehensive gallery showcasing all standard palettes and color bars | [**▶ Launch `palettes_demo`**](https://pydevices.github.io/pydevices-examples/pyscript/pyodide.html?modules=palettes_demo&deps=pydevices-palettes,pydevices-pygraphics) |
| **`feathers`** | Smooth multi-chromatic feather curves and color-cycling geometry | [**▶ Launch `feathers`**](https://pydevices.github.io/pydevices-examples/pyscript/pyodide.html?modules=feathers&deps=pydevices-palettes,pydevices-pygraphics) |
| **`rotations`** | Rotational color sweeps and geometric palette mapping | [**▶ Launch `rotations`**](https://pydevices.github.io/pydevices-examples/pyscript/pyodide.html?modules=rotations&deps=pydevices-palettes,pydevices-pygraphics) |
| **`scroll`** | Smooth gradient scrolling demo with palette cycling | [**▶ Launch `scroll`**](https://pydevices.github.io/pydevices-examples/pyscript/pyodide.html?modules=scroll&deps=pydevices-palettes,pydevices-pygraphics) |

