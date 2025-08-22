"""
letsplot_api_autogen.py

Scans lets-plot.min.js and génère automatiquement des wrappers Python pour chaque fonction lets-plot détectée (geoms, scales, coords, stats, thèmes, bistro, geospatial, etc.).

- Génère un rapport de couverture.
- Génère des wrappers Python (avec docstring, signature générique, et TODO pour les cas complexes).
- Pour les cas connus complexes (ex: facet_wrap, facet_grid), ajoute un commentaire d'avertissement/TODO.

Usage :
    python tools/letsplot_api_autogen.py --out <dossier_cible>
"""
import re
import sys
from pathlib import Path

JS_PATH = Path(__file__).parent.parent / "src/ggoat/assets/lets-plot.min.js"
DEFAULT_OUT = Path(__file__).parent.parent / "src/ggoat/autogen"

PATTERNS = {
    'geom': re.compile(r'geom_([a-zA-Z0-9_]+)\s*[:=]'),
    'scale': re.compile(r'scale_([a-zA-Z0-9_]+)\s*[:=]'),
    'coord': re.compile(r'coord_([a-zA-Z0-9_]+)\s*[:=]'),
    'stat': re.compile(r'stat_([a-zA-Z0-9_]+)\s*[:=]'),
    'theme': re.compile(r'theme_([a-zA-Z0-9_]+)\s*[:=]'),
    'flavor': re.compile(r'flavor_([a-zA-Z0-9_]+)\s*[:=]'),
    'bistro': re.compile(r'(image_matrix|corr_plot|qq_plot|joint_plot|residual_plot|waterfall_plot)\s*[:=]'),
    'geospatial': re.compile(r'(geocode|maptiles)\s*[:=]'),
}

COMPLEX = {'facet_wrap', 'facet_grid', 'joint_plot', 'residual_plot', 'waterfall_plot', 'image_matrix', 'corr_plot', 'geocode', 'maptiles'}

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
api = {kind: scan_api(js_code, pat) for kind, pat in PATTERNS.items()}

# Génération des wrappers Python
def gen_wrapper(kind, name):
    pyname = f"{kind}_{name}"
    doc = f"Wrapper auto-généré pour {pyname} (lets-plot)."
    if name in COMPLEX:
        todo = f"# TODO: Implémentation manuelle recommandée pour {pyname} (cas complexe)"
    else:
        todo = ""
    return f"def {pyname}(*args, **kwargs):\n    \"\"\"{doc}\"\"\"\n    {todo}\n    # ...\n    raise NotImplementedError('Auto-generated: implémenter {pyname}')\n"

# Création du dossier de sortie
def ensure_outdir(outdir):
    outdir.mkdir(parents=True, exist_ok=True)

# Génération des fichiers
def main():
    outdir = DEFAULT_OUT
    if '--out' in sys.argv:
        idx = sys.argv.index('--out')
        if idx+1 < len(sys.argv):
            outdir = Path(sys.argv[idx+1])
    ensure_outdir(outdir)
    print(f"# lets-plot API auto-generation\n# Dossier de sortie: {outdir}\n")
    for kind, names in api.items():
        fname = outdir / f"{kind}s_autogen.py"
        with open(fname, "w", encoding="utf-8") as f:
            f.write(f""""""
Auto-generated wrappers for lets-plot {kind}s
Do not edit manually. Regenerate with letsplot_api_autogen.py
"""""")
            for name in names:
                f.write("\n" + gen_wrapper(kind, name))
        print(f"- {fname} : {len(names)} fonctions générées")

if __name__ == "__main__":
    main()
