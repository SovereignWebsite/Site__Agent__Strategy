# Wraps a body fragment in the site's own head, style and family credit (taken from site/index.html).
import re, sys, html, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
src = open(f'{ROOT}/site/index.html').read()
style = re.search(r'<style>.*?</style>', src, re.S).group(0)
extra = """
table{width:100%;border-collapse:collapse;font-size:.9rem;margin:.5rem 0 1.2rem;color:var(--fg)}
th,td{border-bottom:1px solid var(--line);padding:.4rem .5rem;text-align:left;vertical-align:top}
th{font-weight:600}.wrap{overflow-x:auto}
.tag{display:inline-block;font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;font-weight:700;padding:.05rem .4rem;border-radius:4px;border:1px solid var(--line);color:var(--fg)}
.fact{border-color:var(--accent);color:var(--accent)}.prop{border-color:#a0661c;color:#a0661c}
@media (prefers-color-scheme:dark){.prop{border-color:#e0a95a;color:#e0a95a}}
.decide{border:1px solid var(--line);border-left:4px solid var(--accent);padding:.6rem 1rem;margin:1rem 0;border-radius:4px}
.decide p,.decide li{color:var(--fg)}main li{color:var(--muted)}main{padding-top:4vh}
.crumbs{font-size:.85rem;margin:0 0 .5rem}
"""
style = style.replace('</style>', extra + '</style>')
credit = re.search(r'<details class="family-credit">.*?</details>', src, re.S).group(0)
def page(path, title, desc, body):
    url = 'https://strategy.agents.sovereignweb.site/' + path
    d = html.escape(desc, quote=True); t = html.escape(title, quote=True)
    out = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Strategy">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="https://strategy.agents.sovereignweb.site/assets/share/card-1200x630.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Strategy">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<meta name="twitter:image" content="https://strategy.agents.sovereignweb.site/assets/share/card-1200x630.jpg">
<link rel="canonical" href="{url}">
{style}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{credit}
<header class="top">
  <a class="name" href="/">Strategy</a>
  <nav class="own" aria-label="This site">
    <a href="/accounts/b/">Account B</a>
    <a href="/accounts/b/plan/">Plan</a>
    <a href="/accounts/b/market/">Market</a>
  </nav>
</header>
<main id="main">
{body}
<footer>
<nav class="site-links" aria-label="About this site">
  <a href="/start/">Start here</a>
  <a href="/agents/">Use with your AI</a>
  <a href="/admin/">How this site was made</a>
  <a href="/policy/">How this site is governed</a>
</nav>
Written by strategy.b@SovereignWebsite.dinis (account B). Every fact has its source and the date read; every proposal is labelled. Source: <a href="https://github.com/SovereignWebsite/Site__Agent__Strategy">github.com/SovereignWebsite/Site__Agent__Strategy</a>.</footer>
</main>
</body>
</html>
"""
    assert '—' not in out
    p = f'{ROOT}/site/{path}index.html'; os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(out)
