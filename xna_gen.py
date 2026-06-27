#!/usr/bin/env python3
"""XNA 4.0 spec XML generator — one namespace per invocation."""
import re, os, sys, argparse, html as _html, xml.sax.saxutils as sax, xml.etree.ElementTree as ET
from collections import defaultdict

HTML_DIR = "/rv/tmp/xna_learn.microsoft.com/https___learn.microsoft.com_en-us_previous-versions_windows_xna_bb200104(v=xnagamestudio.41)/learn.microsoft.com/en-us/previous-versions/windows/xna/"
SPEC_DIR = os.path.dirname(os.path.abspath(__file__)) + "/"

SKIP_TEXT = ["This browser is no longer supported","Upgrade to Microsoft Edge",
             "Namespace","Assembly","Platforms","public ","protected ","internal ",
             "private ","See Also","Xbox 360"]

# Handle both plain and Generic variants
TYPE_SUFFIXES = {
    " Class": "class", " Structure": "struct", " Enumeration": "enum",
    " Interface": "interface", " Delegate": "delegate",
    " Generic Class": "class", " Generic Structure": "struct",
    " Generic Interface": "interface", " Generic Delegate": "delegate",
    " Generic Enumeration": "enum",
}

def read(p): return open(p, encoding="utf-8", errors="ignore").read()
def strip(s): return re.sub(r'<[^>]+>','',s)
def clean(s): return re.sub(r'\s+',' ',strip(s)).strip()

def get_h1(c):
    m = re.search(r'<h1[^>]*>(.*?)</h1>',c,re.DOTALL)
    return clean(m.group(1)) if m else ""

def get_ns(c):
    m = re.search(r'Namespace:.*?>(Microsoft\.Xna[^<\s]+)',c,re.DOTALL)
    return m.group(1).rstrip('.,') if m else ""

def get_summary(c):
    for m in re.finditer(r'<p[^>]*>(.*?)</p>',c,re.DOTALL):
        t = clean(m.group(1))
        if len(t)>=10 and not any(t.startswith(x) for x in SKIP_TEXT): return t
    return ""

def get_syntax(c):
    # Skip VB.NET (starts with ') and C++/CLI (starts with 'public:')
    for m in re.finditer(r'<pre[^>]*>(.*?)</pre>',c,re.DOTALL):
        txt = strip(m.group(1)).strip()
        if txt.startswith("'") or txt.startswith('Public ') or txt.startswith('public:'):
            continue
        if txt:
            return txt
    return ""

def get_remarks(c):
    m = re.search(r'<h2[^>]*id="remarks"[^>]*>.*?</h2>(.*?)(?=<h2|$)',c,re.DOTALL)
    return clean(re.sub(r'<[^>]+>',' ',m.group(1))) if m else ""

def get_platforms(c):
    m = re.search(r'<h2[^>]*id="platforms"[^>]*>.*?</h2>\s*<p[^>]*>(.*?)</p>',c,re.DOTALL)
    return [p.strip() for p in strip(m.group(1)).split(',') if p.strip()] if m else []

def get_returns(c):
    m = re.search(r'<h4[^>]*id="return-value"[^>]*>.*?</h4>\s*<p[^>]*>(.*?)</p>',c,re.DOTALL)
    return clean(m.group(1)) if m else ""

def get_params(c):
    m = re.search(r'<h4[^>]*id="parameters"[^>]*>.*?</h4>(.*?)(?=<h[24]|$)',c,re.DOTALL)
    if not m: return []
    # Decode HTML entities in syntax so Nullable&lt;Rectangle&gt; → Nullable<Rectangle>
    syn = _html.unescape(get_syntax(c)); tmap = {}
    for line in syn.split('\n'):
        line = line.strip().rstrip(',)').rstrip()
        tm = re.match(r'^(?:(?:ref|out|params)\s+)?([A-Za-z][\w<>\[\]?,\s]*?)\s+(\w+)\s*$', line)
        if tm:
            tmap[tm.group(2)] = tm.group(1).strip()
    params = []
    for li in re.findall(r'<li>(.*?)</li>',m.group(1),re.DOTALL):
        nm = re.search(r'<em>(.*?)</em>',li)
        if not nm: continue
        pn = clean(nm.group(1))
        # Primary: type from anchor link, incl. generic args e.g. Nullable<Rectangle>
        type_lnk = re.search(r'Type:\s*<a[^>]*>([^<]+)</a>((?:\s*&lt;\s*(?:<a[^>]*>[^<]+</a>|[\w.]+)\s*&gt;)?)', li)
        if type_lnk:
            base = clean(type_lnk.group(1))
            generic_raw = type_lnk.group(2).strip()
            if generic_raw:
                inner = _html.unescape(re.sub(r'<[^>]+>','',generic_raw)).strip('<>').strip()
                pt = f"{base}<{inner}>" if inner else base
            else:
                pt = base
        else:
            # Secondary: plain-text "Type: TypeName" or fall back to tmap
            li_plain = re.sub(r'<[^>]+>',' ', li)
            type_txt = re.search(r'Type:\s+([A-Za-z][\w<>\[\]?]*)', li_plain)
            pt = type_txt.group(1) if type_txt else tmap.get(pn,'Object')
        # Description: remove <em>name</em> and strip leading "Type: ..." prefix
        li_no_em = li.replace(nm.group(0), '')
        pd = clean(re.sub(r'<[^>]+>',' ', li_no_em))
        pd = re.sub(r'^[,\s]*(?:Type:\s*\S+\s*)', '', pd).strip()
        params.append((pn, pt, pd))
    return params

def get_enum_members(c):
    tbl = re.search(r'<table[^>]*>(.*?)</table>',c,re.DOTALL)
    if not tbl: return []
    SKIP = {'Member name','Description','','\xa0','&nbsp;'}
    out = []
    for row in re.findall(r'<tr[^>]*>(.*?)</tr>',tbl.group(1),re.DOTALL):
        cells = [clean(x).replace('&nbsp;',' ').replace('&amp;','&').strip()
                 for x in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>',row,re.DOTALL)]
        cells = [cc for cc in cells if cc]
        if len(cells)>=2 and cells[0] not in SKIP:
            out.append((cells[0], cells[1]))
    return out

def prop_access(syn):
    return 'get;set' if ('set;' in syn and 'get;' in syn) else ('set' if 'set;' in syn else 'get')

def e(t): return sax.escape(str(t)) if t else ""
def cdata(t): t=str(t).replace("]]>","]]]]><![CDATA[>"); return f"<![CDATA[{t}]]>"

def plat_xml(lines, plats, ind):
    if plats:
        lines.append(f'{ind}<platforms>')
        for p in plats: lines.append(f'{ind}  <platform>{e(p)}</platform>')
        lines.append(f'{ind}</platforms>')

def classify_page(h1):
    for sfx, kind in TYPE_SUFFIXES.items():
        if h1.endswith(sfx):
            return ('type', h1[:-len(sfx)].strip(), kind, None, None)
    # Constructor: type name may contain dots (nested types)
    m = re.match(r'^([\w.]+)\s+Constructor(?:\s+\((.*)\))?$', h1)
    if m: return ('member', m.group(1), 'constructor', '__ctor__', m.group(2))
    # Member: type name may contain dots; greedy match takes all but last segment
    m = re.match(r'^([\w.]+)\.([\w]+)\s+(Property|Method|Field|Event)(?:\s+\((.*)\))?$', h1)
    if m: return ('member', m.group(1), m.group(3).lower(), m.group(2), m.group(4))
    return None

def extract_prop_type(syn, pname):
    m = re.search(r'public(?:\s+static)?\s+(\S+)\s+'+re.escape(pname), syn)
    return m.group(1) if m else 'Object'

def extract_field_type(syn, fname):
    m = re.search(r'public(?:\s+(?:static|const|readonly|new))*\s+(\S+)\s+'+re.escape(fname), syn)
    return m.group(1) if m else 'Object'

def extract_method_return(syn, mname):
    m = re.search(r'public(?:\s+(?:static|override|virtual|new|abstract))*\s+(\S+)\s+'+re.escape(mname), syn)
    return m.group(1) if m else 'void'

def extract_event_type(syn, ename):
    m = re.search(r'event\s+(\S+)\s+'+re.escape(ename), syn)
    return m.group(1) if m else 'EventHandler'

def build_ctor_sig(type_name, params):
    if not params: return f'{type_name}()'
    return f'{type_name}({", ".join(pt for _,pt,_ in params)})'

def gen_xml(type_name, kind, ns, main_c, members):
    asm_m = re.search(r'Assembly:.*?>(Microsoft\.Xna[^<\s(]+)',main_c,re.DOTALL)
    assembly = asm_m.group(1).rstrip('.,') if asm_m else ns

    syn_main = get_syntax(main_c)
    base_class = None; interfaces = None
    if ':' in syn_main:
        after = syn_main.split(':',1)[1].strip()
        parts = [p.strip() for p in after.split(',')]
        ifaces = []
        for p in parts:
            p = p.split()[0] if p.split() else p
            if p.startswith('I') or (kind in ('struct','enum') and p):
                ifaces.append(p)
            elif kind == 'class' and not base_class and not p.startswith('I'):
                base_class = p
            else:
                ifaces.append(p)
        if ifaces: interfaces = ', '.join(ifaces)

    ctors  = defaultdict(list)
    props  = {}
    meths  = defaultdict(list)
    mlist  = {}
    flds   = {}
    evts   = {}

    for (mk, mn, sig, c) in members:
        if mk == 'constructor':
            ctors[sig or ''].append(c)
        elif mk == 'property':
            props.setdefault(mn, c)
        elif mk == 'method':
            if sig is None: mlist[mn] = c
            else: meths[mn].append((sig, c))
        elif mk == 'field':
            flds.setdefault(mn, c)
        elif mk == 'event':
            evts.setdefault(mn, c)

    out = []
    out.append('<?xml version="1.0" encoding="UTF-8"?>')
    out.append('<xna-type xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
    out.append('          xsi:noNamespaceSchemaLocation="../../xna.xsd"')
    a = f'name="{e(type_name)}" kind="{kind}"'
    a += f'\n          namespace="{e(ns)}"'
    a += f'\n          assembly="{e(assembly)}"'
    if base_class: a += f'\n          baseClass="{e(base_class)}"'
    if interfaces: a += f'\n          interfaces="{e(interfaces)}"'
    out.append(f'          {a}>')
    out.append(f'  <summary>{cdata(get_summary(main_c))}</summary>')
    out.append(f'  <syntax>{cdata(syn_main)}</syntax>')
    r = get_remarks(main_c)
    if r: out.append(f'  <remarks>{cdata(r)}</remarks>')
    plat_xml(out, get_platforms(main_c), '  ')

    if kind == 'enum':
        out.append('  <members>')
        for mn, md in get_enum_members(main_c):
            out.append(f'    <member name="{e(mn)}"><summary>{cdata(md)}</summary></member>')
        out.append('  </members>')
    elif kind == 'delegate':
        # Delegates use <parameters> and <returns>, not class sections
        ps = get_params(main_c)
        if ps:
            out.append('  <parameters>')
            for pn,pt,pd in ps:
                out.append(f'    <parameter name="{e(pn)}" type="{e(pt)}">{cdata(pd)}</parameter>')
            out.append('  </parameters>')
        oret = get_returns(main_c)
        if oret: out.append(f'  <returns>{cdata(oret)}</returns>')
    else:
        # class / struct / interface
        out.append('  <constructors>')
        for sk, contents in ctors.items():
            for c in contents:
                ps = get_params(c)
                sig_str = f'{type_name}({sk})' if sk else build_ctor_sig(type_name, ps)
                out.append(f'    <constructor signature="{e(sig_str)}">')
                out.append(f'      <summary>{cdata(get_summary(c))}</summary>')
                out.append(f'      <syntax>{cdata(get_syntax(c))}</syntax>')
                if ps:
                    out.append('      <parameters>')
                    for pn,pt,pd in ps:
                        out.append(f'        <parameter name="{e(pn)}" type="{e(pt)}">{cdata(pd)}</parameter>')
                    out.append('      </parameters>')
                rr = get_remarks(c)
                if rr: out.append(f'      <remarks>{cdata(rr)}</remarks>')
                plat_xml(out, get_platforms(c), '      ')
                out.append('    </constructor>')
        out.append('  </constructors>')

        out.append('  <properties>')
        for pn in sorted(props):
            c = props[pn]; syn = get_syntax(c); acc = prop_access(syn)
            pt = extract_prop_type(syn, pn)
            is_s = 'public static' in syn
            a2 = f'name="{e(pn)}" type="{e(pt)}" access="{acc}"'
            if is_s: a2 += ' isStatic="true"'
            out.append(f'    <property {a2}>')
            out.append(f'      <summary>{cdata(get_summary(c))}</summary>')
            out.append(f'      <syntax>{cdata(syn)}</syntax>')
            rr = get_remarks(c)
            if rr: out.append(f'      <remarks>{cdata(rr)}</remarks>')
            plat_xml(out, get_platforms(c), '      ')
            out.append('    </property>')
        out.append('  </properties>')

        out.append('  <methods>')
        all_method_names = sorted(set(list(meths.keys()) + list(mlist.keys())))
        for mn in all_method_names:
            ovs = meths.get(mn, [])
            lc = mlist.get(mn, ovs[0][1] if ovs else None)
            if not lc: continue
            ms = get_summary(lc)
            rt = 'void'; is_s = False
            if ovs:
                fs = get_syntax(ovs[0][1])
                rt = extract_method_return(fs, mn)
                is_s = 'public static' in fs or 'public static' in get_syntax(lc)
            a3 = f'name="{e(mn)}" returnType="{e(rt)}"'
            if is_s: a3 += ' isStatic="true"'
            out.append(f'    <method {a3}>')
            out.append(f'      <summary>{cdata(ms)}</summary>')
            out.append('      <overloads>')
            for sig, c in ovs:
                ps = get_params(c); oret = get_returns(c); ore = get_remarks(c)
                sig_str = f'{mn}({sig})' if sig else f'{mn}()'
                out.append(f'        <overload signature="{e(sig_str)}">')
                out.append(f'          <summary>{cdata(get_summary(c))}</summary>')
                out.append(f'          <syntax>{cdata(get_syntax(c))}</syntax>')
                if ps:
                    out.append('          <parameters>')
                    for pn,pt,pd in ps:
                        out.append(f'            <parameter name="{e(pn)}" type="{e(pt)}">{cdata(pd)}</parameter>')
                    out.append('          </parameters>')
                if oret: out.append(f'          <returns>{cdata(oret)}</returns>')
                if ore: out.append(f'          <remarks>{cdata(ore)}</remarks>')
                plat_xml(out, get_platforms(c), '          ')
                out.append('        </overload>')
            if not ovs:
                c = lc; ps = get_params(c); oret = get_returns(c); ore = get_remarks(c)
                out.append(f'        <overload signature="{e(mn)}()">')
                out.append(f'          <summary>{cdata(get_summary(c))}</summary>')
                out.append(f'          <syntax>{cdata(get_syntax(c))}</syntax>')
                if ps:
                    out.append('          <parameters>')
                    for pn,pt,pd in ps:
                        out.append(f'            <parameter name="{e(pn)}" type="{e(pt)}">{cdata(pd)}</parameter>')
                    out.append('          </parameters>')
                if oret: out.append(f'          <returns>{cdata(oret)}</returns>')
                if ore: out.append(f'          <remarks>{cdata(ore)}</remarks>')
                plat_xml(out, get_platforms(c), '          ')
                out.append('        </overload>')
            out.append('      </overloads>')
            out.append('    </method>')
        out.append('  </methods>')

        out.append('  <fields>')
        for fn in sorted(flds):
            c = flds[fn]; syn = get_syntax(c)
            ft = extract_field_type(syn, fn)
            is_s = 'static' in syn; is_ro = 'readonly' in syn or 'const' in syn
            a4 = f'name="{e(fn)}" type="{e(ft)}"'
            if is_s: a4 += ' isStatic="true"'
            if is_ro: a4 += ' isReadOnly="true"'
            out.append(f'    <field {a4}>')
            out.append(f'      <summary>{cdata(get_summary(c))}</summary>')
            if syn: out.append(f'      <syntax>{cdata(syn)}</syntax>')
            rr = get_remarks(c)
            if rr: out.append(f'      <remarks>{cdata(rr)}</remarks>')
            plat_xml(out, get_platforms(c), '      ')
            out.append('    </field>')
        out.append('  </fields>')

        out.append('  <events>')
        for en in sorted(evts):
            c = evts[en]; syn = get_syntax(c)
            et = extract_event_type(syn, en)
            out.append(f'    <event name="{e(en)}" type="{e(et)}">')
            out.append(f'      <summary>{cdata(get_summary(c))}</summary>')
            if syn: out.append(f'      <syntax>{cdata(syn)}</syntax>')
            rr = get_remarks(c)
            if rr: out.append(f'      <remarks>{cdata(rr)}</remarks>')
            plat_xml(out, get_platforms(c), '      ')
            out.append('    </event>')
        out.append('  </events>')

    out.append('</xna-type>')
    return "\n".join(out)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--namespace', required=True)
    p.add_argument('--skip', nargs='*', default=[])
    args = p.parse_args()
    ns = args.namespace
    skip = set(args.skip)

    print(f"[{ns}] Scanning HTML files...")
    seen = {}
    for fname in os.listdir(HTML_DIR):
        if not (fname.endswith('.html') or fname.endswith('.htm')): continue
        base = re.sub(r'-2\.(html|htm)$', r'.\1', fname)
        if '-2.' in fname or base not in seen:
            seen[base] = fname

    type_pages = {}
    member_map = defaultdict(list)

    for base, fname in seen.items():
        fpath = os.path.join(HTML_DIR, fname)
        content = read(fpath)
        h1 = get_h1(content)
        file_ns = get_ns(content)
        if file_ns != ns or not h1: continue
        result = classify_page(h1)
        if not result: continue
        page_type, type_name, kind_or_mk, member_name, sig = result
        if page_type == 'type':
            type_pages.setdefault(type_name, (kind_or_mk, content))
        else:
            member_map[type_name].append((kind_or_mk, member_name, sig, content))

    print(f"[{ns}] Found {len(type_pages)} types")
    out_dir = os.path.join(SPEC_DIR, ns)
    os.makedirs(out_dir, exist_ok=True)

    ok = 0; fail = 0
    for type_name in sorted(type_pages):
        if type_name in skip:
            print(f"  SKIP {type_name}")
            continue
        kind, main_c = type_pages[type_name]
        members = member_map.get(type_name, [])
        try:
            xml = gen_xml(type_name, kind, ns, main_c, members)
            out_path = os.path.join(out_dir, f"{type_name}.xml")
            with open(out_path,'w',encoding='utf-8') as f: f.write(xml)
            ET.parse(out_path)
            print(f"  OK  {type_name} ({kind}, {len(members)} member pages)")
            ok += 1
        except Exception as ex:
            print(f"  ERR {type_name}: {ex}")
            fail += 1

    print(f"[{ns}] Done: {ok} OK, {fail} errors")
    return fail

if __name__ == '__main__':
    sys.exit(main())
