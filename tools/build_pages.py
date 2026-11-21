"""Build the service and guide pages from content/en.py and content/hi.py.

Run from the repo root:   python tools/build_pages.py
It writes public/<slug>.html, public/hi/<slug>.html and public/sitemap.xml. Commit the output:
Cloudflare serves public/ as it is, with no build step on its side.
"""
import html
import importlib.util
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / 'public'
SITE = 'https://mediclaimswala.in'
WA = '918502967063'

LOGO = ('<svg viewBox="0 0 100 120" aria-hidden="true"><path d="M50 4 L92 18 V58 C92 86 74 106 50 116 C26 106 8 86 8 58 V18 Z" fill="var(--heading)"/>'
        '<rect x="42" y="30" width="16" height="56" rx="3" fill="var(--ground)"/><rect x="22" y="50" width="56" height="16" rx="3" fill="var(--ground)"/>'
        '<circle cx="78" cy="92" r="20" fill="var(--green)" stroke="var(--ground)" stroke-width="5"/>'
        '<path d="M68 92 L75 99 L89 85" fill="none" stroke="var(--ground)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
ARROW = ('<svg viewBox="0 0 24 24"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
WA_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.25-.12-1.47-.72-1.7-.8s-.39-.12-.56.13-.64.8-.79.96-.29.19-.54.06a6.7 6.7 0 0 1-3.3-2.9c-.25-.43.25-.4.71-1.33a.45.45 0 0 0-.02-.42c-.06-.12-.56-1.35-.77-1.85s-.41-.42-.56-.43h-.48a.92.92 0 0 0-.67.31 2.8 2.8 0 0 0-.87 2.08 4.9 4.9 0 0 0 1 2.6 11.2 11.2 0 0 0 4.3 3.8c1.6.69 2.2.75 3 .63a2.6 2.6 0 0 0 1.7-1.2 2.1 2.1 0 0 0 .15-1.2c-.06-.1-.23-.17-.48-.29z"/></svg>')
PHONE_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>')


def load(lang):
    path = ROOT / 'content' / f'{lang}.py'
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(f'content_{lang}', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def esc(s):
    return html.escape(s, quote=True)


def prefix(lang):
    return '/hi/' if lang == 'hi' else '/'


def home(lang):
    return '/?lang=hi' if lang == 'hi' else '/'


def wa_link(text):
    return f'https://wa.me/{WA}?text={quote(text)}'


def btn(href, label):
    return f'<a class="btn" href="{href}"><span>{esc(label)}</span><span class="arr" aria-hidden="true">{ARROW}</span></a>'


def btn_wa(text, label):
    return (f'<a class="btn-line" href="{wa_link(text)}" target="_blank" rel="noopener">{WA_ICON}'
            f'<span>{esc(label)}</span><span class="chev" aria-hidden="true"></span></a>')


def render(mod, page, langs):
    ui, lang = mod.UI, mod.UI['lang']
    pages = mod.PAGES
    by_slug = {p['slug']: p for p in pages}
    slug = page['slug']
    url = SITE + prefix(lang) + slug
    h = home(lang)
    other = ui['other_lang']
    has_other = other in langs

    body = page['body']
    if lang == 'hi':  # internal links stay inside the Hindi pages
        body = re.sub(r'href="/(' + '|'.join(re.escape(s) for s in by_slug) + r')"', r'href="/hi/\1"', body)

    current = ' aria-current="page"'
    menu = ''.join(
        f'<li><a href="{prefix(lang)}{p["slug"]}"{current if p["slug"] == slug else ""}>{esc(p["nav"])}</a></li>'
        for p in pages)
    header = f'''<header class="top"><div class="wrap">
  <a class="brand" href="{h}" aria-label="Mediclaimswala home">{LOGO}<span>Mediclaims<span class="w">wala</span></span></a>
  <nav class="nav" aria-label="Main">
    <details class="menu"><summary>{esc(ui["services"])}</summary><ul>{menu}</ul></details>
    <a href="{h}#how">{esc(ui["how"])}</a><a href="{h}#fees">{esc(ui["fees"])}</a><a href="{h}#faq">{esc(ui["faq"])}</a>
  </nav>
  {f'<a class="lang-link" href="{prefix(other)}{slug}" hreflang="{other}" lang="{other}">{esc(ui["other_label"])}</a>' if has_other else ''}
  {btn(h + "#contact", ui["cta_short"])}
</div></header>'''

    if page.get('fee', True):
        side = (f'<h2>{esc(ui["fee_t"])}</h2><p>{esc(ui["fee_p"])}</p>'
                f'<ul>{"".join(f"<li>{esc(x)}</li>" for x in ui["fee_li"])}</ul>')
    else:
        side = f'<h2>{esc(page["side_t"])}</h2><p>{esc(page["side_p"])}</p>'
    side += btn(h + '#contact', ui['cta_review'])
    side += f'<a class="side-wa" href="{wa_link(page["wa"])}" target="_blank" rel="noopener">{WA_ICON}<span>{esc(ui["cta_wa"])}</span></a>'

    faq = ''.join(f'<details name="faq"{" open" if i == 0 else ""}><summary><span>{esc(q)}</span><i aria-hidden="true"></i></summary><p>{esc(a)}</p></details>'
                  for i, (q, a) in enumerate(page['faq']))
    related = ''.join(f'<li><a href="{prefix(lang)}{s}"><span>{esc(by_slug[s]["nav"])}</span><span class="chev" aria-hidden="true"></span></a></li>'
                      for s in page['related'])

    svc_links = ''.join(f'<li><a href="{prefix(lang)}{p["slug"]}">{esc(p["nav"])}</a></li>' for p in pages if p['kind'] == 'service')
    guide_links = ''.join(f'<li><a href="{prefix(lang)}{p["slug"]}">{esc(p["nav"])}</a></li>' for p in pages if p['kind'] == 'guide')
    footer = f'''<footer><div class="wrap">
  <div class="f-cols">
    <div><h2>{esc(ui["f_talk"])}</h2><ul><li><a href="tel:+918502967063">+91 85029 67063</a></li><li><a href="{wa_link(ui["wa_default"])}" target="_blank" rel="noopener">{esc(ui["cta_wa"])}</a></li><li>{esc(ui["b2"])}</li></ul></div>
    <div><h2>{esc(ui["services"])}</h2><ul>{svc_links}</ul></div>
    <div><h2>{esc(ui["f_help"])}</h2><ul>{guide_links}<li><a href="{h}#how">{esc(ui["how"])}</a></li><li><a href="{h}#fees">{esc(ui["fees"])}</a></li><li><a href="{h}#faq">{esc(ui["faq"])}</a></li></ul></div>
    <div><h2>{esc(ui["f_legal"])}</h2><ul><li><a href="/privacy">{esc(ui["privacy"])}</a></li><li><a href="/terms">{esc(ui["terms"])}</a></li></ul></div>
  </div>
  <p class="disc">{esc(ui["disclaimer"])}</p>
  <p>© 2026 Mediclaimswala</p>
</div></footer>'''

    reviewed_iso, reviewed_text = mod.REVIEWED
    in_lang = 'hi-IN' if lang == 'hi' else 'en-IN'
    main_node = ({'@type': 'Service', '@id': url + '#service', 'name': page['nav'], 'description': page['description'],
                  'serviceType': 'Health insurance claim consultancy', 'url': url, 'areaServed': {'@type': 'Country', 'name': 'India'},
                  'availableLanguage': ['English', 'Hindi'], 'provider': {'@id': SITE + '/#business'}}
                 if page['kind'] == 'service' else
                 {'@type': 'Article', '@id': url + '#article', 'headline': page['h1'], 'description': page['description'],
                  'inLanguage': in_lang, 'datePublished': reviewed_iso, 'dateModified': reviewed_iso, 'mainEntityOfPage': url,
                  'author': {'@type': 'Organization', 'name': 'Mediclaimswala', 'url': SITE + '/'}, 'publisher': {'@id': SITE + '/#business'}})
    if page['kind'] == 'service' and page.get('fee', True):
        main_node['offers'] = {'@type': 'Offer', 'description': ui['fee_p']}
    graph = [
        {'@type': 'WebPage', '@id': url, 'url': url, 'name': page['title'], 'description': page['description'], 'inLanguage': in_lang,
         'dateModified': reviewed_iso, 'isPartOf': {'@id': SITE + '/#website'}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': ui['home'], 'item': SITE + h},
            {'@type': 'ListItem', 'position': 2, 'name': page['nav'], 'item': url}]},
        main_node,
        {'@type': 'FAQPage', '@id': url + '#faq', 'mainEntity': [
            {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in page['faq']]},
    ]
    ld = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':'))

    alternates = f'<link rel="alternate" hreflang="en-IN" href="{SITE}/{slug}">\n'
    if 'hi' in langs:
        alternates += f'<link rel="alternate" hreflang="hi-IN" href="{SITE}/hi/{slug}">\n'
    alternates += f'<link rel="alternate" hreflang="x-default" href="{SITE}/{slug}">'
    preload = ('/assets/fonts/noto-sans-devanagari-devanagari-400-TuG7UU.woff2' if lang == 'hi' else '/assets/fonts/zodiak-700.woff2')

    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(page["title"])}</title>
<meta name="description" content="{esc(page["description"])}">
<link rel="canonical" href="{url}">
{alternates}
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#FFFFFF">
<meta property="og:type" content="{"article" if page["kind"] == "guide" else "website"}">
<meta property="og:site_name" content="Mediclaimswala">
<meta property="og:locale" content="{ui["locale"]}">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(page["h1"])}">
<meta property="og:description" content="{esc(page["description"])}">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/assets/favicon-96.png" type="image/png" sizes="96x96">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="{preload}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts.css">
<link rel="stylesheet" href="/assets/page.css">
<script type="application/ld+json">{ld}</script>
<meta name="facebook-domain-verification" content="emebk17k6oy4ffzmbfv1mu7yinuczq">
<script src="/assets/pixel.js" async></script>
</head>
<body class="g">
<noscript><img height="1" width="1" style="display:none" alt="" src="https://www.facebook.com/tr?id=1520687953209029&amp;ev=PageView&amp;noscript=1"></noscript>
<a class="skip" href="#main">{esc(ui["skip"])}</a>
{header}
<main id="main">
<section class="g-hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="{h}">{esc(ui["home"])}</a></li><li><a href="{h}#services">{esc(ui["services"] if page["kind"] == "service" else ui["guides"])}</a></li><li><span aria-current="page">{esc(page["nav"])}</span></li></ol></nav>
  <h1>{esc(page["h1"])}</h1>
  <p class="short"><strong>{esc(ui["in_short"])}</strong> {esc(page["short"])}</p>
  <div class="ctas">{btn(h + "#contact", ui["cta_review"])}{btn_wa(page["wa"], ui["cta_wa"])}</div>
</div></section>
<div class="wrap g-body">
  <article class="prose">{body}
<p class="reviewed">{esc(ui["reviewed"])}: <time datetime="{reviewed_iso}">{esc(reviewed_text)}</time>. {esc(ui["note"])}</p>
  </article>
  <aside class="g-side"><div class="fee-card">{side}</div></aside>
</div>
<section class="g-faq"><div class="wrap"><h2>{esc(ui["faq_t"])}</h2><div class="faq-list">{faq}</div></div></section>
<section class="g-rel"><div class="wrap"><h2>{esc(ui["related_t"])}</h2><ul class="rel">{related}</ul></div></section>
<section class="g-band"><div class="wrap"><h2>{esc(ui["band_t"])}</h2><p>{esc(ui["band_p"])}</p><div class="ctas">{btn(h + "#contact", ui["cta_review"])}{btn_wa(page["wa"], ui["cta_wa"])}</div></div></section>
</main>
{footer}
<div class="mbar"><a class="m-call" href="tel:+918502967063">{PHONE_ICON}<span>{esc(ui["call"])}</span></a><a class="m-wa" href="{wa_link(page["wa"])}" target="_blank" rel="noopener">{WA_ICON}<span>{esc(ui["cta_wa"])}</span></a></div>
<script src="/assets/nav.js" defer></script>
</body>
</html>
'''


def check(mod):
    """Self-check: every related slug and every internal body link points at a page that exists."""
    slugs = {p['slug'] for p in mod.PAGES}
    for p in mod.PAGES:
        assert set(p['related']) <= slugs, (p['slug'], p['related'])
        for target in re.findall(r'href="/([^"#?]*)"', p['body']):
            assert target in slugs or target in ('', 'privacy', 'terms'), (p['slug'], target)
        assert '—' not in p['body'] + p['short'] and '–' not in p['body'] + p['short'], p['slug']


def sitemap(mods):
    en = mods['en']
    lastmod = en.REVIEWED[0]
    rows = [f'  <url><loc>{SITE}/</loc><lastmod>{lastmod}</lastmod></url>']
    for p in en.PAGES:
        for lang in mods:
            alts = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}-IN" href="{SITE}{prefix(l)}{p["slug"]}"/>' for l in mods)
            rows.append(f'  <url><loc>{SITE}{prefix(lang)}{p["slug"]}</loc><lastmod>{lastmod}</lastmod>{alts}</url>')
    rows += [f'  <url><loc>{SITE}/privacy</loc><lastmod>2026-11-15</lastmod></url>',
             f'  <url><loc>{SITE}/terms</loc><lastmod>2026-11-15</lastmod></url>']
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + '\n'.join(rows) + '\n</urlset>\n')


def main():
    mods = {l: m for l in ('en', 'hi') if (m := load(l))}
    if 'hi' in mods:
        assert [p['slug'] for p in mods['hi'].PAGES] == [p['slug'] for p in mods['en'].PAGES], 'hi.py pages must match en.py'
    written = []
    for lang, mod in mods.items():
        check(mod)
        out_dir = PUB / ('hi' if lang == 'hi' else '')
        out_dir.mkdir(exist_ok=True)
        for page in mod.PAGES:
            target = out_dir / f'{page["slug"]}.html'
            target.write_text(render(mod, page, mods), encoding='utf-8', newline='\n')
            written.append(target.relative_to(ROOT).as_posix())
    (PUB / 'sitemap.xml').write_text(sitemap(mods), encoding='utf-8', newline='\n')
    print('\n'.join(written + ['public/sitemap.xml']))


if __name__ == '__main__':
    main()
