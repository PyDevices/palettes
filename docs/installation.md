# Installation

## MicroPython (MIP)

```python
import mip
mip.install("palettes", index="https://PyDevices.github.io/micropython-lib/mip/PyDevices")
```

## CircuitPython / copy install

Copy the `palettes/` package folder onto `sys.path`.

## CPython (TestPyPI)

```bash
pip install \
  -i https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  palettes
```

## PyScript

Add to the example header:

```python
# pyscript mip: palettes
# pyodide wheels: pydevices-palettes
```

The pydisplay gallery generator adds these when examples import `palettes`.
