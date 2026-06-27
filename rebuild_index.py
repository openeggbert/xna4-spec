#!/usr/bin/env python3
"""Rebuild index.xml from all generated type XML files."""
import os, re, xml.etree.ElementTree as ET
import xml.sax.saxutils as sax

SPEC_DIR = "/rv/tmp/xna_learn.microsoft.com/spec/"
INDEX_PATH = os.path.join(SPEC_DIR, "index.xml")

def e(t): return sax.escape(str(t)) if t else ""
def cdata(t): t=str(t).replace("]]>","]]]]><![CDATA[>"); return f"<![CDATA[{t}]]>"

# Collect all types grouped by namespace
ns_map = {}  # ns -> {'assembly': str, 'types': [(name, kind, relpath, summary)]}

for root, dirs, files in os.walk(SPEC_DIR):
    dirs.sort()
    for f in sorted(files):
        if not f.endswith('.xml') or f == 'index.xml':
            continue
        path = os.path.join(root, f)
        rel = os.path.relpath(path, SPEC_DIR)
        try:
            doc = ET.parse(path)
            xna = doc.getroot()
            name = xna.get('name')
            kind = xna.get('kind')
            ns = xna.get('namespace')
            assembly = xna.get('assembly', ns)
            summary_el = xna.find('summary')
            summary = (summary_el.text or '').strip() if summary_el is not None else ''
            if not name or not kind or not ns:
                continue
            if ns not in ns_map:
                ns_map[ns] = {'assembly': assembly, 'types': []}
            ns_map[ns]['types'].append((name, kind, rel, summary))
        except Exception as ex:
            print(f"WARN: {path}: {ex}")

# Namespace order (stable)
NS_ORDER = [
    "Microsoft.Xna.Framework",
    "Microsoft.Xna.Framework.Graphics",
    "Microsoft.Xna.Framework.Graphics.PackedVector",
    "Microsoft.Xna.Framework.Audio",
    "Microsoft.Xna.Framework.Input",
    "Microsoft.Xna.Framework.Input.Touch",
    "Microsoft.Xna.Framework.Media",
    "Microsoft.Xna.Framework.Net",
    "Microsoft.Xna.Framework.Storage",
    "Microsoft.Xna.Framework.Content",
    "Microsoft.Xna.Framework.GamerServices",
    "Microsoft.Xna.Framework.Design",
    "Microsoft.Xna.Framework.Content.Pipeline",
    "Microsoft.Xna.Framework.Content.Pipeline.Audio",
    "Microsoft.Xna.Framework.Content.Pipeline.Graphics",
    "Microsoft.Xna.Framework.Content.Pipeline.Processors",
    "Microsoft.Xna.Framework.Content.Pipeline.Serialization.Compiler",
    "Microsoft.Xna.Framework.Content.Pipeline.Serialization.Intermediate",
    "Microsoft.Xna.Framework.Content.Pipeline.Tasks",
]

out = []
out.append('<?xml version="1.0" encoding="UTF-8"?>')
out.append('<xna-index version="4.0">')

ordered = [ns for ns in NS_ORDER if ns in ns_map]
remaining = sorted(n for n in ns_map if n not in ordered)

total = 0
for ns in ordered + remaining:
    info = ns_map[ns]
    out.append(f'  <namespace name="{e(ns)}" assembly="{e(info["assembly"])}">')
    for name, kind, relpath, summary in sorted(info['types'], key=lambda x: x[0]):
        out.append(f'    <type-ref name="{e(name)}" kind="{kind}" file="{e(relpath)}">')
        out.append(f'      <summary>{cdata(summary)}</summary>')
        out.append(f'    </type-ref>')
        total += 1
    out.append('  </namespace>')

out.append('</xna-index>')

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')

print(f"Rebuilt index.xml: {total} types across {len(ns_map)} namespaces")
for ns in ordered + remaining:
    print(f"  {len(ns_map[ns]['types']):3d}  {ns}")
