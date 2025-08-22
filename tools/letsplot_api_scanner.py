"""
letsplot_api_scanner.py

Scans lets-plot.min.js for exported geoms, scales, coords, stats, bistro, and other API elements.
Generates a report and (optionally) Python stubs for missing features in ggoat.

Usage:
    python tools/letsplot_api_scanner.py [--stubs]

- Outputs a coverage report (stdout)
- With --stubs, generates Python stub functions for missing API elements
"""
import re
import sys
from pathlib import Path

# Path to lets-plot.min.js
JS_PATH = Path(__file__).parent.parent / "src/ggoat/assets/lets-plot.min.js"

# Regex patterns for API extraction (simplified for minified JS)
GEOM_PATTERN = re.compile(r'geom_([a-zA-Z0-9_]+)\s*[:=]')
SCALE_PATTERN = re.compile(r'scale_([a-zA-Z0-9_]+)\s*[:=]')
COORD_PATTERN = re.compile(r'coord_([a-zA-Z0-9_]+)\s*[:=]')
STAT_PATTERN = re.compile(r'stat_([a-zA-Z0-9_]+)\s*[:=]')
THEME_PATTERN = re.compile(r'theme_([a-zA-Z0-9_]+)\s*[:=]')
FLAVOR_PATTERN = re.compile(r'flavor_([a-zA-Z0-9_]+)\s*[:=]')
BISTRO_PATTERN = re.compile(r'(image_matrix|corr_plot|qq_plot|joint_plot|residual_plot|waterfall_plot)\s*[:=]')
GEOSPATIAL_PATTERN = re.compile(r'(geocode|maptiles)\s*[:=]')

# Optionally, scan for all exported function names
EXPORT_PATTERN = re.compile(r'exports?\.([a-zA-Z0-9_]+)\s*=')

# Helper: scan for all matches
def scan_api(js_code, pattern):
    return sorted(set(m.group(1) for m in pattern.finditer(js_code)))

# Load lets-plot.min.js
if not JS_PATH.exists():
    print(f"Error: {JS_PATH} not found.")
    sys.exit(1)
with open(JS_PATH, "r", encoding="utf-8", errors="ignore") as f:
    js_code = f.read()

# Scan for API elements
geoms = scan_api(js_code, GEOM_PATTERN)
scales = scan_api(js_code, SCALE_PATTERN)
coords = scan_api(js_code, COORD_PATTERN)
stats = scan_api(js_code, STAT_PATTERN)
themes = scan_api(js_code, THEME_PATTERN)
flavors = scan_api(js_code, FLAVOR_PATTERN)
bistro = scan_api(js_code, BISTRO_PATTERN)
geospatial = scan_api(js_code, GEOSPATIAL_PATTERN)
exports = scan_api(js_code, EXPORT_PATTERN)

# Print coverage report
print("# lets-plot.min.js API scan\n")
print(f"Geoms:      {geoms}")
print(f"Scales:     {scales}")
print(f"Coords:     {coords}")
print(f"Stats:      {stats}")
print(f"Themes:     {themes}")
print(f"Flavors:    {flavors}")
print(f"Bistro:     {bistro}")
print(f"Geospatial: {geospatial}")
print(f"Exports:    {exports}")

# Optionally, generate Python stubs for missing features
if '--stubs' in sys.argv:
    print("\n# --- Python stubs for missing features (template) ---\n")
    for kind, names in [('geom', geoms), ('scale', scales), ('coord', coords), ('stat', stats), ('theme', themes), ('flavor', flavors), ('bistro', bistro), ('geospatial', geospatial)]:
        for name in names:
            pyname = f"{kind}_{name}"
            print(f"def {pyname}(*args, **kwargs):\n    \"\"\"Stub for {pyname} (auto-generated)\"\"\"\n    raise NotImplementedError('Implement {pyname} in ggoat')\n")
