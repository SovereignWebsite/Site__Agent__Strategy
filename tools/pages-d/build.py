# d.strategy's page generator: renders the markdown sources in tools/pages-d/sources/ into pages under site/accounts/d/,
# inside the shell of site/accounts/d/index.html (its head, style, family credit, header and footer).
# Run: python3 tools/pages-d/build.py   then the repository's checks (.github/ci/), then commit signed.
# The sources were moved here from PrompTugal__News__Website board/team/strategy.d/ (24 Nov 2026); edit them here.
import html, json, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SRC = os.path.join(HERE, 'sources')
OLD = 'https://github.com/PrompTugal/PrompTugal__News__Website/blob/dev/board/team/strategy.d/'
BASE = 'https://strategy.agents.sovereignweb.site/'

PAGES = [
    # (source, json or None, path under site/, title, description)
    ('map-decision-making.md', 'map-decision-making.json', 'accounts/d/maps/decision-making/',
     'Map 1: decision-making', 'A Wardley map of decision-making across Dinis Cruz\'s estate: the decision-making framework as a product, from codified thinking to signed answers.'),
    ('map-estate.md', 'map-estate.json', 'accounts/d/maps/estate/',
     'Map 2: the estate', 'A Wardley map of Dinis Cruz\'s estate: Sovereign Website first, one chain of trust under every area.'),
    ('map-sovereign-website.md', 'map-sovereign-website.json', 'accounts/d/maps/sovereign-website/',
     'Map 4: Sovereign Website', 'A Wardley map of Sovereign Website: the owner, the visitor and the partner, against 31 players read from public pages.'),
    ('strategy-platform-sites.md', None, 'accounts/d/strategy/platform-sites/',
     'Strategy: platform sites, B to C to B, and partners', 'Better interfaces on platforms people already use, run in the browser on the user\'s own key, each showing its agents and policies.'),
    ('strategy-wardley-maps-site.md', None, 'accounts/d/strategy/wardley-maps-site/',
     'Strategy: the Wardley Maps site', 'The Wardley Maps site and frameworks as a product: maps with history, made from sourced data and kept current by agents.'),
    ('brief-deciding-in-your-area.md', None, 'accounts/d/briefs/deciding-in-your-area/',
     'Brief: deciding in your area', 'A two-minute context brief for any agent about to decide something: is it mine, is it reserved, is the context there.'),
]
LINKS = {  # old relative targets in the sources -> new pages
    '2026-11-22-decision-making': '/accounts/d/maps/decision-making/',
    '2026-11-22-the-estate': '/accounts/d/maps/estate/',
    '2026-11-22-sovereign-website': '/accounts/d/maps/sovereign-website/',
    'platform-sites-b2c2b': '/accounts/d/strategy/platform-sites/',
    'wardley-maps-site': '/accounts/d/strategy/wardley-maps-site/',
}

shell = open(os.path.join(ROOT, 'site/accounts/d/index.html')).read()
HEAD, rest = shell.split('<main id="main">', 1)
FOOT = rest[rest.index('<footer>'):]

def link_target(u):
    if re.match(r'^(https?:|mailto:|#|/)', u):
        return u
    for k, v in LINKS.items():
        if k in u:
            return v
    return OLD + u.lstrip('./')

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', lambda m: '<code>' + m.group(1) + '</code>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lambda m: f'<a href="{html.escape(link_target(html.unescape(m.group(2))), quote=True)}">{m.group(1)}</a>', s)
    s = re.sub(r'(?<![\w"=/])(https?://[^\s<)]+[^\s<).,;:])', r'<a href="\1">\1</a>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*\s][^*]*)\*(?![\w*])', r'<em>\1</em>', s)
    return s

def render(md):
    lines = md.split('\n'); out = []; i = 0
    h1 = None
    def lst(i, indent):
        tag = 'ol' if re.match(r'\s*\d+\.\s', lines[i]) else 'ul'
        buf = [f'<{tag}>']
        while i < len(lines):
            m = re.match(r'^(\s*)(?:[-*]|\d+\.)\s+(.*)$', lines[i])
            if not m or len(m.group(1)) < indent:
                break
            if len(m.group(1)) > indent:
                sub, i = lst(i, len(m.group(1)))
                buf[-1] = buf[-1][:-5] + sub + '</li>'
                continue
            buf.append('<li>' + inline(m.group(2)) + '</li>'); i += 1
        buf.append(f'</{tag}>')
        return ''.join(buf), i
    while i < len(lines):
        l = lines[i]
        if not l.strip():
            i += 1; continue
        if l.startswith('```'):
            j = i + 1; code = []
            while j < len(lines) and not lines[j].startswith('```'):
                code.append(lines[j]); j += 1
            out.append('<pre>' + html.escape('\n'.join(code)) + '</pre>'); i = j + 1; continue
        m = re.match(r'^(#{1,4})\s+(.*)$', l)
        if m:
            n = len(m.group(1))
            if n == 1 and h1 is None:
                h1 = m.group(2); i += 1; continue
            n = max(2, n)
            out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); i += 1; continue
        if l.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            body = [r for r in rows[1:] if not all(re.match(r'^:?-{2,}:?$', c) for c in r)]
            t = ['<div class="wrap"><table><thead><tr>'] + [f'<th scope="col">{inline(c)}</th>' for c in rows[0]] + ['</tr></thead><tbody>']
            for r in body:
                t.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            out.append(''.join(t) + '</tbody></table></div>'); continue
        if l.startswith('>'):
            q = []
            while i < len(lines) and lines[i].startswith('>'):
                q.append(lines[i].lstrip('> ').rstrip()); i += 1
            out.append('<blockquote><p>' + inline(' '.join(q)) + '</p></blockquote>'); continue
        if re.match(r'^\s*(?:[-*]|\d+\.)\s+', l):
            s, i = lst(i, len(re.match(r'^(\s*)', l).group(1))); out.append(s); continue
        p = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,4}\s|```|\||>|\s*(?:[-*]|\d+\.)\s)', lines[i]):
            p.append(lines[i].strip()); i += 1
        out.append('<p>' + inline(' '.join(p)) + '</p>')
    return h1, '\n'.join(out)

def page(path, title, desc, body):
    h = HEAD
    h = re.sub(r'<title>.*?</title>', f'<title>{html.escape(title)}</title>', h)
    for attr in ('name="description"', 'property="og:description"', 'name="twitter:description"'):
        h = re.sub(r'(<meta ' + attr + r' content=")[^"]*', lambda m: m.group(1) + html.escape(desc, quote=True), h)
    for attr in ('property="og:title"', 'name="twitter:title"'):
        h = re.sub(r'(<meta ' + attr + r' content=")[^"]*', lambda m: m.group(1) + html.escape(title, quote=True), h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + BASE + path, h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + BASE + path, h)
    h = h.replace(' aria-current="page"', '')
    return h + '<main id="main">\n' + body + '\n' + FOOT

for src, data, path, title, desc in PAGES:
    md = open(os.path.join(SRC, src)).read()
    h1, body = render(md)
    crumbs = '<p class="crumbs"><a href="/">Strategy</a> / <a href="/accounts/d/">Account D</a></p>'
    mark = '<div class="mark">d.strategy, account D</div>'
    extra = ''
    out_dir = os.path.join(ROOT, 'site', path)
    os.makedirs(out_dir, exist_ok=True)
    if data:
        shutil.copyfile(os.path.join(SRC, data), os.path.join(out_dir, 'map.json'))
        extra = '<p>The same map as data: <a href="map.json">map.json</a> (visibility and evolution from 0 to 1, links, movements). A draft, <span class="tag prop">Proposal</span>.</p>'
    moved = f'<p>Moved here from PrompTugal__News__Website on 24 November 2026; the history before that is in <a href="{OLD}">board/team/strategy.d/</a>.</p>'
    body = f'{crumbs}\n{mark}\n<h1>{html.escape(title)}</h1>\n{extra}\n{body}\n{moved}'
    open(os.path.join(out_dir, 'index.html'), 'w').write(page(path, title, desc, body))
    print('wrote', path)
