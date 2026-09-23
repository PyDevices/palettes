"""Freeze the palettes package from its canonical source tree.

A firmware build that wants palettes frozen includes this file from its own
freeze manifest -- for example micropython-pydevices'
``manifests/pygraphics.py``, which includes ``../../palettes/manifest.py``.
"""

if 0:

    def package(*args, **kwargs):
        pass

    def module(*args, **kwargs):
        pass


package("palettes", base_path="./lib", opt=3)  # type: ignore[name-defined]  # noqa: PGH003
