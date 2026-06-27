#!/usr/bin/env python3
"""Generate a static HTML website from the XNA 4.0 spec XML files."""
import os, re, sys, html, shutil
import xml.etree.ElementTree as ET
from collections import defaultdict

SPEC_DIR = os.path.dirname(os.path.abspath(__file__))
WEB_DIR  = os.path.join(SPEC_DIR, "web")

# ── CSS ────────────────────────────────────────────────────────────────────────

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  font-size: 15px; line-height: 1.6;
  background: #1a1a2e; color: #e0e0e0;
}

a { color: #7ec8e3; text-decoration: none; }
a:hover { text-decoration: underline; color: #aad8f0; }

/* ── Layout ── */
.page-wrap { display: flex; min-height: 100vh; }

nav {
  width: 260px; min-width: 260px; background: #16213e;
  border-right: 1px solid #2a3a5c; padding: 0;
  position: sticky; top: 0; height: 100vh; overflow-y: auto;
}

main { flex: 1; padding: 32px 40px; max-width: 960px; }

/* ── Nav ── */
.nav-logo {
  display: block; padding: 18px 20px;
  font-size: 17px; font-weight: 700; color: #7ec8e3;
  border-bottom: 1px solid #2a3a5c;
}

.nav-search {
  width: 100%; padding: 8px 12px; margin: 0;
  background: #0f3460; border: none; border-bottom: 1px solid #2a3a5c;
  color: #e0e0e0; font-size: 13px;
  outline: none;
}
.nav-search::placeholder { color: #6a7a9a; }

.nav-ns { padding: 6px 12px 2px; font-size: 11px; color: #6a7a9a;
          text-transform: uppercase; letter-spacing: .08em; margin-top: 6px; }

.nav-item {
  display: flex; align-items: center; gap: 6px;
  padding: 4px 12px 4px 20px; font-size: 13px; color: #c0c8d8;
}
.nav-item:hover { background: #0f3460; color: #fff; }
.nav-item.active { background: #0f3460; color: #7ec8e3; font-weight: 600; }

.kind-badge {
  font-size: 10px; padding: 1px 5px; border-radius: 3px;
  font-weight: 700; text-transform: uppercase; min-width: 30px; text-align: center;
}
.k-class     { background: #1a4a6e; color: #7ec8e3; }
.k-struct    { background: #1a4a2e; color: #7ed8a0; }
.k-enum      { background: #4a2a1a; color: #e8a070; }
.k-interface { background: #3a1a5e; color: #c0a0e8; }
.k-delegate  { background: #4a3a1a; color: #e8d070; }

/* ── Main ── */
h1 { font-size: 28px; font-weight: 700; color: #fff; margin-bottom: 4px; }
h2 { font-size: 18px; font-weight: 600; color: #aac8e0; margin: 28px 0 10px;
     padding-bottom: 6px; border-bottom: 1px solid #2a3a5c; }
h3 { font-size: 15px; font-weight: 600; color: #c8d8e8; margin: 18px 0 6px; }

.breadcrumb { font-size: 13px; color: #6a7a9a; margin-bottom: 20px; }
.breadcrumb a { color: #6a9ab0; }

.type-meta { display: flex; gap: 10px; align-items: center; margin-bottom: 20px; }
.type-ns   { font-size: 13px; color: #6a9ab0; }

.summary-box {
  background: #16213e; border-left: 3px solid #7ec8e3;
  padding: 12px 16px; border-radius: 0 6px 6px 0; margin-bottom: 20px;
  font-size: 14px; color: #c8d8e8;
}

pre, code {
  font-family: "Cascadia Code", "Fira Code", "Consolas", monospace;
  font-size: 13px;
}
pre {
  background: #0d1b2a; border: 1px solid #2a3a5c; border-radius: 6px;
  padding: 14px 16px; overflow-x: auto; margin: 8px 0 16px;
  color: #a8c8e0; line-height: 1.5;
}

.platforms { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0; }
.platform-tag {
  background: #1a3a2e; color: #70c8a0; font-size: 12px;
  padding: 2px 8px; border-radius: 10px; border: 1px solid #2a5a3e;
}

/* ── Members table ── */
table { width: 100%; border-collapse: collapse; margin: 10px 0; }
th { text-align: left; padding: 8px 12px; background: #0f3460;
     color: #7ec8e3; font-size: 13px; font-weight: 600;
     border-bottom: 2px solid #2a3a5c; }
td { padding: 8px 12px; border-bottom: 1px solid #1e2e4a; font-size: 13px; vertical-align: top; }
tr:hover td { background: #161e30; }
td code { background: #0d1b2a; padding: 1px 5px; border-radius: 3px; font-size: 12px; }

/* ── Overloads ── */
.overload {
  background: #161e30; border: 1px solid #2a3a5c;
  border-radius: 6px; margin: 10px 0; padding: 14px 16px;
}
.overload-sig { font-size: 13px; color: #e8c870; font-weight: 600; margin-bottom: 8px; }
.overload-summary { font-size: 13px; color: #b0c0d0; margin-bottom: 8px; }

.param-list { margin: 6px 0; }
.param-row { display: flex; gap: 10px; padding: 4px 0;
             border-bottom: 1px solid #1e2e3a; font-size: 13px; }
.param-row:last-child { border-bottom: none; }
.param-name { color: #7ec8e3; min-width: 140px; font-family: monospace; }
.param-type { color: #e8a070; min-width: 160px; font-family: monospace; font-size: 12px; }
.param-desc { color: #9ab0c0; }

.returns-box { background: #1a1a0a; border: 1px solid #3a3a1a; border-radius: 4px;
               padding: 8px 12px; margin: 6px 0; font-size: 13px; color: #d0c870; }

/* ── Index ── */
.ns-section { margin-bottom: 36px; }
.ns-title { font-size: 20px; font-weight: 700; color: #7ec8e3; margin-bottom: 12px;
            padding-bottom: 8px; border-bottom: 2px solid #2a3a5c; }
.type-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 8px;
}
.type-card {
  display: flex; align-items: flex-start; gap: 10px;
  background: #16213e; border: 1px solid #2a3a5c; border-radius: 6px;
  padding: 10px 14px; transition: border-color .15s;
}
.type-card:hover { border-color: #7ec8e3; }
.type-card-name { font-weight: 600; font-size: 14px; color: #e0e8f0; display: block; }
.type-card-sum  { font-size: 12px; color: #6a8a9a; margin-top: 2px;
                  display: -webkit-box; -webkit-line-clamp: 2;
                  -webkit-box-orient: vertical; overflow: hidden; }

/* ── Search on index ── */
#search-box {
  width: 100%; padding: 10px 16px; margin-bottom: 24px; font-size: 15px;
  background: #16213e; border: 1px solid #2a3a5c; border-radius: 6px;
  color: #e0e0e0; outline: none;
}
#search-box:focus { border-color: #7ec8e3; }

/* ── Table scroll wrapper ── */
.table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; margin: 10px 0; }
.table-wrap table { margin: 0; }

/* ── Hamburger ── */
.hamburger {
  display: none; position: fixed; top: 12px; left: 12px; z-index: 200;
  background: #0f3460; border: 1px solid #2a3a5c; border-radius: 6px;
  padding: 8px 11px; cursor: pointer; color: #7ec8e3; font-size: 20px; line-height: 1;
}

.nav-overlay {
  display: none; position: fixed; inset: 0;
  background: rgba(0,0,0,.55); z-index: 99;
}

/* ── Responsive ── */
@media (max-width: 768px) {
  .hamburger { display: block; }

  nav {
    position: fixed; left: 0; top: 0; bottom: 0; z-index: 100;
    transform: translateX(-100%); transition: transform .25s ease;
    width: 280px; min-width: 0; height: 100%;
  }
  nav.open { transform: translateX(0); box-shadow: 4px 0 20px rgba(0,0,0,.5); }
  nav.open ~ .nav-overlay { display: block; }

  .page-wrap { flex-direction: column; }
  main { padding: 60px 16px 32px; max-width: 100%; }

  h1 { font-size: 22px; }
  h2 { font-size: 16px; }

  .param-row { flex-direction: column; gap: 2px; }
  .param-name, .param-type { min-width: 0; }

  .type-grid { grid-template-columns: 1fr; }

  .overload { padding: 10px 12px; }
}
"""

# ── Helpers ───────────────────────────────────────────────────────────────────

def esc(s):
    return html.escape(str(s)) if s else ""

def text(el, path, default=""):
    node = el.find(path) if el is not None else None
    return (node.text or "").strip() if node is not None else default

def cdata_text(el, path, default=""):
    """Get text content which may be CDATA."""
    node = el.find(path) if el is not None else None
    if node is None: return default
    t = (node.text or "").strip()
    return t

def platforms_html(el):
    plats = [p.text for p in el.findall("platforms/platform") if p.text]
    if not plats: return ""
    tags = "".join(f'<span class="platform-tag">{esc(p)}</span>' for p in plats)
    return f'<div class="platforms">{tags}</div>'

def syntax_html(s):
    if not s: return ""
    return f'<pre>{esc(s)}</pre>'

def params_html(el, path="parameters"):
    params = el.findall(f"{path}/parameter")
    if not params: return ""
    rows = "".join(
        f'<div class="param-row">'
        f'<span class="param-name">{esc(p.get("name",""))}</span>'
        f'<span class="param-type">{esc(p.get("type",""))}</span>'
        f'<span class="param-desc">{esc((p.text or "").strip())}</span>'
        f'</div>'
        for p in params
    )
    return f'<div class="param-list">{rows}</div>'

def kind_badge(kind):
    return f'<span class="kind-badge k-{esc(kind)}">{esc(kind)}</span>'

def nav_html(all_types, active_file=""):
    """Build sidebar nav grouped by namespace."""
    ns_groups = defaultdict(list)
    for t in all_types:
        ns_groups[t["namespace"]].append(t)

    items = []
    for ns in sorted(ns_groups):
        short_ns = ns.replace("Microsoft.Xna.Framework", "MXF")
        items.append(f'<div class="nav-ns">{esc(short_ns)}</div>')
        for t in sorted(ns_groups[ns], key=lambda x: x["name"]):
            active = ' active' if t["html_path"] == active_file else ""
            depth = "../" if "/" in active_file else ""
            href = depth + t["html_path"] if active_file else t["html_path"]
            items.append(
                f'<a class="nav-item{active}" href="{href}" data-name="{esc(t["name"].lower())}">'
                f'{kind_badge(t["kind"])}{esc(t["name"])}</a>'
            )
    return "\n".join(items)

def page(title, body, active_file, all_types, extra_head=""):
    nav = nav_html(all_types, active_file)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — XNA 4.0 API</title>
<style>{CSS}</style>
{extra_head}
</head>
<body>
<button class="hamburger" id="hamburger" aria-label="Menu">&#9776;</button>
<div class="page-wrap">
<nav id="main-nav">
  <a class="nav-logo" href="../index.html">XNA 4.0 API</a>
  <input class="nav-search" type="search" placeholder="Filter types…" id="nav-filter">
  {nav}
</nav>
<div class="nav-overlay" id="nav-overlay"></div>
<main>
{body}
</main>
</div>
<script>
(function() {{
  var ham = document.getElementById('hamburger');
  var nav = document.getElementById('main-nav');
  var overlay = document.getElementById('nav-overlay');
  function openNav() {{ nav.classList.add('open'); }}
  function closeNav() {{ nav.classList.remove('open'); }}
  ham.addEventListener('click', openNav);
  overlay.addEventListener('click', closeNav);
  document.querySelectorAll('.nav-item').forEach(function(el) {{
    el.addEventListener('click', closeNav);
  }});
  window.addEventListener('resize', function() {{
    if (window.innerWidth > 768) closeNav();
  }});
}})();
document.getElementById('nav-filter').addEventListener('input', function() {{
  var q = this.value.toLowerCase();
  document.querySelectorAll('.nav-item').forEach(function(el) {{
    el.style.display = (!q || el.dataset.name.includes(q)) ? '' : 'none';
  }});
  document.querySelectorAll('.nav-ns').forEach(function(ns) {{
    var next = ns.nextElementSibling;
    var anyVisible = false;
    while (next && next.classList.contains('nav-item')) {{
      if (next.style.display !== 'none') anyVisible = true;
      next = next.nextElementSibling;
    }}
    ns.style.display = anyVisible ? '' : 'none';
  }});
}});
document.querySelectorAll('table').forEach(function(t) {{
  var w = document.createElement('div');
  w.className = 'table-wrap';
  t.parentNode.insertBefore(w, t);
  w.appendChild(t);
}});
</script>
</body>
</html>"""

# ── Type page ─────────────────────────────────────────────────────────────────

def render_type(xml_path, rel_html, all_types):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    name      = root.get("name", "")
    kind      = root.get("kind", "")
    namespace = root.get("namespace", "")
    assembly  = root.get("assembly", "")
    base_cls  = root.get("baseClass", "")
    ifaces    = root.get("interfaces", "")
    modifier  = root.get("modifier", "")
    summary   = cdata_text(root, "summary")
    syntax    = cdata_text(root, "syntax")
    remarks   = cdata_text(root, "remarks")

    parts = [f'<div class="breadcrumb"><a href="../index.html">Index</a> › {esc(namespace)}</div>']
    parts.append(f'<h1>{esc(name)}</h1>')
    parts.append(f'<div class="type-meta">{kind_badge(kind)}'
                 f'<span class="type-ns">{esc(namespace)}</span></div>')

    if summary:
        parts.append(f'<div class="summary-box">{esc(summary)}</div>')

    # Inheritance
    inherit_parts = []
    if base_cls: inherit_parts.append(f"Base class: <code>{esc(base_cls)}</code>")
    if ifaces:   inherit_parts.append(f"Implements: <code>{esc(ifaces)}</code>")
    if modifier: inherit_parts.append(f"Modifier: <code>{esc(modifier)}</code>")
    if assembly: inherit_parts.append(f"Assembly: <code>{esc(assembly)}</code>")
    if inherit_parts:
        parts.append("<p style='font-size:13px;color:#6a8a9a;margin-bottom:16px'>" +
                     " &nbsp;·&nbsp; ".join(inherit_parts) + "</p>")

    if syntax:
        parts.append('<h2>Syntax</h2>')
        parts.append(syntax_html(syntax))

    plat = platforms_html(root)
    if plat:
        parts.append('<h2>Platforms</h2>' + plat)

    if remarks:
        parts.append(f'<h2>Remarks</h2><p style="font-size:14px;color:#b0c0d0">{esc(remarks)}</p>')

    # ── Enum members ──
    members = root.findall("members/member")
    if members:
        parts.append('<h2>Members</h2>')
        rows = "".join(
            f'<tr><td><code>{esc(m.get("name",""))}</code></td>'
            f'<td>{esc(cdata_text(m, "summary"))}</td></tr>'
            for m in members
        )
        parts.append(f'<table><tr><th>Name</th><th>Description</th></tr>{rows}</table>')

    # ── Constructors ──
    ctors = root.findall("constructors/constructor")
    if ctors:
        parts.append('<h2>Constructors</h2>')
        for c in ctors:
            sig  = c.get("signature", "")
            ssum = cdata_text(c, "summary")
            syn  = cdata_text(c, "syntax")
            rem  = cdata_text(c, "remarks")
            parts.append(f'<div class="overload">')
            parts.append(f'<div class="overload-sig">{esc(sig)}</div>')
            if ssum: parts.append(f'<div class="overload-summary">{esc(ssum)}</div>')
            if syn:  parts.append(syntax_html(syn))
            parts.append(params_html(c))
            if rem:  parts.append(f'<p style="font-size:13px;color:#9aabbb">{esc(rem)}</p>')
            parts.append(platforms_html(c))
            parts.append('</div>')

    # ── Properties ──
    props = root.findall("properties/property")
    if props:
        parts.append('<h2>Properties</h2>')
        rows = "".join(
            f'<tr><td><code>{esc(p.get("name",""))}</code></td>'
            f'<td><code>{esc(p.get("type",""))}</code></td>'
            f'<td>{esc(p.get("access",""))}</td>'
            f'<td>{"✓" if p.get("isStatic")=="true" else ""}</td>'
            f'<td>{esc(cdata_text(p,"summary"))}</td></tr>'
            for p in props
        )
        parts.append(f'<table><tr><th>Name</th><th>Type</th><th>Access</th>'
                     f'<th>Static</th><th>Description</th></tr>{rows}</table>')

    # ── Methods ──
    methods = root.findall("methods/method")
    if methods:
        parts.append('<h2>Methods</h2>')
        for m in methods:
            mname  = m.get("name","")
            msum   = cdata_text(m, "summary")
            is_s   = m.get("isStatic") == "true"
            static = " <small style='color:#6a8a9a'>[static]</small>" if is_s else ""
            parts.append(f'<h3>{esc(mname)}{static}</h3>')
            if msum: parts.append(f'<p style="font-size:13px;color:#9ab0c0;margin-bottom:6px">{esc(msum)}</p>')
            for ov in m.findall("overloads/overload"):
                sig   = ov.get("signature","")
                osum  = cdata_text(ov, "summary")
                osyn  = cdata_text(ov, "syntax")
                oret  = cdata_text(ov, "returns")
                orem  = cdata_text(ov, "remarks")
                parts.append('<div class="overload">')
                parts.append(f'<div class="overload-sig">{esc(sig)}</div>')
                if osum: parts.append(f'<div class="overload-summary">{esc(osum)}</div>')
                if osyn: parts.append(syntax_html(osyn))
                parts.append(params_html(ov))
                if oret: parts.append(f'<div class="returns-box">Returns: {esc(oret)}</div>')
                if orem: parts.append(f'<p style="font-size:13px;color:#9aabbb">{esc(orem)}</p>')
                parts.append(platforms_html(ov))
                parts.append('</div>')

    # ── Fields ──
    fields = root.findall("fields/field")
    if fields:
        parts.append('<h2>Fields</h2>')
        rows = "".join(
            f'<tr><td><code>{esc(f.get("name",""))}</code></td>'
            f'<td><code>{esc(f.get("type",""))}</code></td>'
            f'<td>{"✓" if f.get("isStatic")=="true" else ""}</td>'
            f'<td>{"✓" if f.get("isReadOnly")=="true" else ""}</td>'
            f'<td>{esc(cdata_text(f,"summary"))}</td></tr>'
            for f in fields
        )
        parts.append(f'<table><tr><th>Name</th><th>Type</th><th>Static</th>'
                     f'<th>ReadOnly</th><th>Description</th></tr>{rows}</table>')

    # ── Events ──
    events = root.findall("events/event")
    if events:
        parts.append('<h2>Events</h2>')
        rows = "".join(
            f'<tr><td><code>{esc(ev.get("name",""))}</code></td>'
            f'<td><code>{esc(ev.get("type",""))}</code></td>'
            f'<td>{esc(cdata_text(ev,"summary"))}</td></tr>'
            for ev in events
        )
        parts.append(f'<table><tr><th>Name</th><th>Type</th><th>Description</th></tr>{rows}</table>')

    # ── Delegate params/returns ──
    if kind == "delegate":
        dparams = root.findall("parameters/parameter")
        if dparams:
            parts.append('<h2>Parameters</h2>')
            parts.append(params_html(root))
        dret = cdata_text(root, "returns")
        if dret:
            parts.append(f'<h2>Return Value</h2>'
                         f'<div class="returns-box">{esc(dret)}</div>')

    title = f"{name} {kind.capitalize()}"
    return page(title, "\n".join(parts), rel_html, all_types)

# ── Index page ────────────────────────────────────────────────────────────────

def render_index(all_types):
    ns_groups = defaultdict(list)
    for t in all_types:
        ns_groups[t["namespace"]].append(t)

    parts = [
        '<h1>XNA 4.0 API Reference</h1>',
        f'<p style="color:#6a8a9a;margin-bottom:24px">{len(all_types)} types across '
        f'{len(ns_groups)} namespaces</p>',
        '<input id="search-box" type="search" placeholder="Search types…">',
    ]

    for ns in sorted(ns_groups):
        types = sorted(ns_groups[ns], key=lambda x: x["name"])
        parts.append(f'<div class="ns-section" data-ns="{esc(ns.lower())}">')
        parts.append(f'<div class="ns-title">{esc(ns)}</div>')
        parts.append('<div class="type-grid">')
        for t in types:
            parts.append(
                f'<a class="type-card" href="{esc(t["html_path"])}" '
                f'data-name="{esc(t["name"].lower())}">'
                f'{kind_badge(t["kind"])}'
                f'<div><span class="type-card-name">{esc(t["name"])}</span>'
                f'<span class="type-card-sum">{esc(t["summary"])}</span></div>'
                f'</a>'
            )
        parts.append('</div></div>')

    search_js = """
<script>
document.getElementById('search-box').addEventListener('input', function() {
  var q = this.value.toLowerCase();
  document.querySelectorAll('.type-card').forEach(function(el) {
    el.style.display = (!q || el.dataset.name.includes(q)) ? '' : 'none';
  });
  document.querySelectorAll('.ns-section').forEach(function(ns) {
    var any = Array.from(ns.querySelectorAll('.type-card'))
                   .some(function(c) { return c.style.display !== 'none'; });
    ns.style.display = (!q || any) ? '' : 'none';
  });
});
</script>
"""
    nav = nav_html(all_types, "index.html")
    body = "\n".join(parts) + search_js
    # Build index page (nav href is relative from root)
    result = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>XNA 4.0 API Reference</title>
<style>{CSS}</style>
</head>
<body>
<button class="hamburger" id="hamburger" aria-label="Menu">&#9776;</button>
<div class="page-wrap">
<nav id="main-nav">
  <a class="nav-logo" href="index.html">XNA 4.0 API</a>
  <input class="nav-search" type="search" placeholder="Filter types…" id="nav-filter">
  {nav}
</nav>
<div class="nav-overlay" id="nav-overlay"></div>
<main>
{body}
</main>
</div>
<script>
(function() {{
  var ham = document.getElementById('hamburger');
  var nav = document.getElementById('main-nav');
  var overlay = document.getElementById('nav-overlay');
  function openNav() {{ nav.classList.add('open'); }}
  function closeNav() {{ nav.classList.remove('open'); }}
  ham.addEventListener('click', openNav);
  overlay.addEventListener('click', closeNav);
  document.querySelectorAll('.nav-item').forEach(function(el) {{
    el.addEventListener('click', closeNav);
  }});
  window.addEventListener('resize', function() {{
    if (window.innerWidth > 768) closeNav();
  }});
}})();
document.getElementById('nav-filter').addEventListener('input', function() {{
  var q = this.value.toLowerCase();
  document.querySelectorAll('.nav-item').forEach(function(el) {{
    el.style.display = (!q || el.dataset.name.includes(q)) ? '' : 'none';
  }});
  document.querySelectorAll('.nav-ns').forEach(function(ns) {{
    var next = ns.nextElementSibling;
    var anyVisible = false;
    while (next && next.classList.contains('nav-item')) {{
      if (next.style.display !== 'none') anyVisible = true;
      next = next.nextElementSibling;
    }}
    ns.style.display = anyVisible ? '' : 'none';
  }});
}});
</script>
</body>
</html>"""
    return result

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    index_xml = os.path.join(SPEC_DIR, "index.xml")
    if not os.path.exists(index_xml):
        print("ERROR: index.xml not found"); sys.exit(1)

    # Collect all types from index.xml
    tree = ET.parse(index_xml)
    root = tree.getroot()

    all_types = []
    for ns_el in root.findall("namespace"):
        ns = ns_el.get("name", "")
        for ref in ns_el.findall("type-ref"):
            name     = ref.get("name", "")
            kind     = ref.get("kind", "")
            rel_path = ref.get("file", "")   # e.g. "Microsoft.Xna.Framework/BoundingBox.xml"
            summary  = cdata_text(ref, "summary")
            # HTML output path mirrors XML path with .html extension
            html_path = rel_path.replace(".xml", ".html")
            all_types.append({
                "name":      name,
                "kind":      kind,
                "namespace": ns,
                "rel_path":  rel_path,
                "html_path": html_path,
                "summary":   summary,
            })

    print(f"Found {len(all_types)} types in index.xml")

    # Create web dir
    if os.path.exists(WEB_DIR):
        shutil.rmtree(WEB_DIR)
    os.makedirs(WEB_DIR)

    # Generate type pages
    ok = 0; fail = 0
    for t in all_types:
        xml_path  = os.path.join(SPEC_DIR, t["rel_path"])
        out_path  = os.path.join(WEB_DIR,  t["html_path"])
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        try:
            html_content = render_type(xml_path, t["html_path"], all_types)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            ok += 1
        except Exception as ex:
            print(f"  ERR {t['name']}: {ex}")
            fail += 1

    # Generate index
    with open(os.path.join(WEB_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index(all_types))

    print(f"Done: {ok} type pages + index.html → {WEB_DIR}")
    if fail: print(f"  {fail} errors")

if __name__ == "__main__":
    main()
