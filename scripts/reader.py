#!/usr/bin/env python3
"""Builds dist/reader.html: every skill file on one page with a sidebar. Needs pandoc."""
import html, pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "sandfield-design"
FILES = [
    ("SKILL.md", "Skill", SKILL / "SKILL.md"),
    ("philosophy.md", "Philosophy", SKILL / "references" / "philosophy.md"),
    ("rules.md", "Rules", SKILL / "references" / "rules.md"),
    ("checklist.md", "Checklist", SKILL / "references" / "checklist.md"),
    ("examples.md", "Examples", SKILL / "references" / "examples.md"),
    ("themes/README.md", "Themes", SKILL / "themes" / "README.md"),
]


def to_html(md, prefix):
    out = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5", f"--id-prefix={prefix}-"],
        input=md, capture_output=True, text=True, check=True,
    ).stdout
    # pandoc renders task checkboxes only in bullet lists; also render them in numbered lists
    return re.sub(r"<li>\[ \]\s*", '<li><input type="checkbox" disabled="" />', out)


sections, nav = [], []
for path, label, f in FILES:
    md = f.read_text()
    desc = ""
    fm = re.match(r"^---\n(.*?)\n---\n", md, re.S)
    if fm:
        md = md[fm.end():]
        d = re.search(r"^description:\s*(.+)$", fm.group(1), re.M)
        desc = d.group(1) if d else ""
    sid = label.lower()
    body = to_html(md, sid)
    subs = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, re.S)
    sub_nav = "".join(f'<a class="sub" href="#{i}">{" ".join(re.sub("<[^>]+>", "", t).split())}</a>' for i, t in subs)
    nav.append(f'<a class="top" href="#{sid}">{label}</a>{sub_nav}')
    trigger = f'<p class="trigger"><strong>Triggers when:</strong> {html.escape(desc)}</p>' if desc else ""
    sections.append(f'<section id="{sid}"><p class="file">{path}</p>{trigger}{body}</section>')

version = re.search(r'"version":\s*"([^"]+)"', (ROOT / ".claude-plugin" / "plugin.json").read_text()).group(1)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sandfield Design Skill</title>
<style>
:root{{--bg:#fbfaf8;--surface:#fff;--text:#1c1b19;--muted:#6b6862;--line:#e6e2dc;--accent:#2f5d50;--accent-soft:#e7efec;--code:#f3f1ed}}
@media (prefers-color-scheme:dark){{:root{{--bg:#161615;--surface:#1f1f1d;--text:#ecebe7;--muted:#a19e97;--line:#34332f;--accent:#8cc5b3;--accent-soft:#233430;--code:#262623}}}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth;scroll-padding-top:16px}}
body{{margin:0;background:var(--bg);color:var(--text);font:16px/1.6 ui-sans-serif,-apple-system,"Segoe UI",Inter,sans-serif}}
.wrap{{display:grid;grid-template-columns:250px minmax(0,1fr);max-width:1180px;margin:0 auto}}
aside{{position:sticky;top:0;height:100vh;overflow-y:auto;padding:28px 16px 40px 24px;border-right:1px solid var(--line)}}
aside .brand{{font-weight:600;font-size:15px}}
aside .ver{{color:var(--muted);font-size:13px;margin:2px 0 20px}}
aside a{{display:block;text-decoration:none;color:var(--muted);border-radius:6px}}
aside a.top{{color:var(--text);font-weight:600;font-size:14px;padding:6px 8px;margin-top:10px}}
aside a.sub{{font-size:13.5px;padding:3px 8px 3px 18px}}
aside a:hover{{background:var(--code);color:var(--text)}}
aside a.on{{background:var(--accent-soft);color:var(--accent)}}
main{{padding:36px 48px 120px;min-width:0}}
section{{padding-bottom:40px;margin-bottom:40px;border-bottom:1px solid var(--line)}}
.file{{font:13px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted);margin:0 0 6px}}
.trigger{{background:var(--accent-soft);border-radius:8px;padding:12px 16px;font-size:14.5px}}
h1{{font-size:30px;line-height:1.2;margin:0 0 12px;letter-spacing:-.01em}}
h2{{font-size:21px;margin:40px 0 10px}}
h3{{font-size:17px;margin:26px 0 6px}}
h4{{font-size:15px;margin:20px 0 4px}}
p,li{{max-width:72ch}}
a{{color:var(--accent)}}
code{{font:.88em ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--code);padding:1px 5px;border-radius:4px}}
pre{{background:var(--code);border:1px solid var(--line);border-radius:8px;padding:14px 16px;overflow-x:auto;line-height:1.45}}
pre code{{background:none;padding:0}}
table{{width:100%;border-collapse:collapse;margin:16px 0;font-size:14.5px;display:block;overflow-x:auto}}
th,td{{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line)}}
th{{font-weight:600;color:var(--muted);font-size:13.5px}}
hr{{border:0;border-top:1px solid var(--line);margin:28px 0}}
ul,ol{{padding-left:22px}} li{{margin:4px 0}}
ul.task-list{{list-style:none;padding-left:4px}}
input[type=checkbox]{{accent-color:var(--accent);margin-right:6px}}
@media (max-width:820px){{.wrap{{display:block}}aside{{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line)}}aside a.sub{{display:none}}main{{padding:24px 16px 80px}}}}
@media print{{aside{{display:none}}.wrap{{display:block}}main{{padding:0}}}}
</style>
</head>
<body>
<div class="wrap">
<aside><div class="brand">Sandfield Design Skill</div><div class="ver">v{version} · generated from the skill files</div>{"".join(nav)}</aside>
<main>{"".join(sections)}</main>
</div>
<script>
const links=[...document.querySelectorAll('aside a')];
const map=new Map(links.map(a=>[a.getAttribute('href').slice(1),a]));
const obs=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{links.forEach(l=>l.classList.remove('on'));map.get(e.target.id)?.classList.add('on');}}}}),{{rootMargin:'0px 0px -75% 0px'}});
document.querySelectorAll('section, main h2[id]').forEach(el=>map.has(el.id)&&obs.observe(el));
</script>
</body>
</html>
"""
out = ROOT / "dist" / "reader.html"
out.parent.mkdir(exist_ok=True)
out.write_text(page)
print(f"Built {out.relative_to(ROOT)}")
