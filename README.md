# WMM2025

WMM2025 World Magnetic Model...in simple, object-oriented Python.
Tested on Linux, Mac and Windows.
Most C compilers work.
At this time Visual Studio is not supported since MSVC doesn't export function symbols without additional headers,
which is typically done with something like SWIG.

![image](./src/wmm2025/tests/incldecl.png)

## Install

for the latest release from PyPi:

```sh
python -m pip install wmm2025
```

Optionally, to get the cutting-edge development version:

```sh
git clone https://github.com/Navigraph/wmm2025

python -m pip install -e wmm2025
```

This Python wrapper of WMM2025 uses our build-on-run technique.
The first time you use WMM2025, you will see messages from the Meson build system and your C compiler.


## Usage

an example script

```sh
python RunWMM2025.py
```

or as a Python module:

```python
import wmm2025

mag = wmm2025.wmm(glat, glon, alt_km, yeardec)
```

## Reference

* WMM2025 [inclination map](https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2025/WMM2025_I_MERC.pdf)
* WMM2025 [declination map](https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2025/WMM2025_D_MERC.pdf)
