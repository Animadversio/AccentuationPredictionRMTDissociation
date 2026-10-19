"""Revise Figure 1A, preserving the v7 B--F panels and canvas size.

Run with system Python (matplotlib). PDF composition uses the bundled pypdf
runtime if pypdf is unavailable in the current interpreter. Labels remain
native text in SVG and embedded TrueType text in PDF for Illustrator editing.
"""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/figures/cosyne2027_figure1_workflow'
OUT.mkdir(parents=True, exist_ok=True)
(ROOT / 'output/pdf').mkdir(parents=True, exist_ok=True)
os.environ.setdefault('MPLCONFIGDIR', '/private/tmp/cosyne2027-figure1-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

plt.rcParams.update({
    'font.family': 'DejaVu Sans', 'pdf.fonttype': 42,
    'ps.fonttype': 42, 'svg.fonttype': 'none', 'text.parse_math': False,
})
W, H, CUT = 522.0, 128.16, 88.5
fig = plt.figure(figsize=(W / 72, H / 72))
ax = fig.add_axes((0, 0, 1, 1))
ax.set(xlim=(0, W), ylim=(0, H))
ax.axis('off')
ax.text(1.044, H * .995, 'A  Fit–optimize–test paradigm',
        fontsize=7.1, weight='bold', va='top')

steps = [
    ('1  Record neural data', ['Natural images and',
                              'neural responses {(xᵢ, yᵢ)}'], '#e4eef4'),
    ('2  Fit encoding model', ['Ridge regression with',
                              'cross-validated layer and penalty selection'], '#eee7f3'),
    ('3  Feature accentuation', ['x ← x₀; regularized updates',
                                'x ← x ± η∇ₓ fₘ(x)',
                                'until fₘ(x*) = r*'], '#f9e9db'),
    ('4  Test neural control', ['Record neural responses to',
                               'each model’s accentuated',
                               'images x*'], '#e5f0e8'),
]
labels = []
for xfrac, (title, lines, color) in zip([.006, .257, .508, .759], steps):
    x, w = xfrac * W, .230 * W
    ax.add_patch(FancyBboxPatch(
        (x, 90.0), w, 29.0,
        boxstyle='round,pad=0.24,rounding_size=1.5',
        lw=.45, ec='#8a8a8a', fc=color))
    labels.append((ax.text(x + w/2, 113.8, title, fontsize=6.3,
                          weight='bold', ha='center', va='center'), x, w))
    centers = [101.5, 95.8] if len(lines) == 2 else [104.6, 98.9, 93.2]
    for y, line in zip(centers, lines):
        labels.append((ax.text(x + w/2, y, line, fontsize=5.35,
                              ha='center', va='center'), x, w))
for xfrac in [.239, .490, .741]:
    x = xfrac * W
    ax.annotate('', xy=(x + .016*W, 104.5), xytext=(x, 104.5),
                arrowprops={'arrowstyle': '-|>', 'lw': .65,
                            'mutation_scale': 6, 'color': '#555555'})

# Catch accidental text overflow without horizontal scaling or font outlines.
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
for label, x, w in labels:
    bb = label.get_window_extent(renderer).transformed(ax.transData.inverted())
    assert x + 1 < bb.x0 and bb.x1 < x + w - 1, label.get_text()
    assert 90 < bb.y0 and bb.y1 < 119, label.get_text()
overlay = OUT / 'figure1A_overlay.pdf'
fig.savefig(overlay, facecolor='white')
svg = OUT / 'cosyne2027_figure1A_editable.svg'
fig.savefig(svg, facecolor='white')
plt.close(fig)

# SVG's top-left viewBox crops off the unused lower canvas, retaining <text>.
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
tree = ET.parse(svg)
root = tree.getroot()
root.set('height', f'{H-CUT:g}pt')
root.set('viewBox', f'0 0 {W:g} {H-CUT:g}')
tree.write(svg, encoding='utf-8', xml_declaration=True)
assert len(root.findall('.//{http://www.w3.org/2000/svg}text')) == 15

compose = r'''
from pathlib import Path
from copy import deepcopy
import shutil, sys
from pypdf import PdfReader, PdfWriter, Transformation
from pypdf.generic import RectangleObject
root, out = map(Path, sys.argv[1:])
base = PdfReader(root/'CoSyNe2027/figures/cosyne2027_v7_experiment_dense.pdf').pages[0]
overlay = PdfReader(out/'figure1A_overlay.pdf').pages[0]
assert tuple(map(float, base.mediabox)) == (0.0, 0.0, 522.0, 128.16)
overlay.cropbox = RectangleObject((0, 88.5, 522, 128.16))
base.merge_page(overlay)
writer = PdfWriter(); writer.add_page(base)
full = root/'CoSyNe2027/figures/cosyne2027_figure1_workflow.pdf'
with full.open('wb') as f: writer.write(f)
shutil.copy2(full, root/'output/pdf'/full.name)
panel = deepcopy(overlay)
panel.add_transformation(Transformation().translate(0, -88.5))
panel.mediabox = RectangleObject((0, 0, 522, 39.66))
panel.cropbox = RectangleObject((0, 0, 522, 39.66))
writer = PdfWriter(); writer.add_page(panel)
with (root/'output/pdf/cosyne2027_figure1A_editable.pdf').open('wb') as f:
    writer.write(f)
'''
try:
    import pypdf
    python = sys.executable
except ImportError:
    python = str(Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3')
subprocess.run([python, '-c', compose, str(ROOT), str(OUT)], check=True)
shutil.copy2(svg, ROOT / 'CoSyNe2027/figures' / svg.name)
shutil.copy2(ROOT / 'output/pdf/cosyne2027_figure1A_editable.pdf',
             ROOT / 'CoSyNe2027/figures/cosyne2027_figure1A_editable.pdf')
print('Wrote revised full Figure 1 PDF and editable Figure 1A PDF/SVG.')
