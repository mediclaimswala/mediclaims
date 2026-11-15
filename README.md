# Mediclaimswala website

Landing page for [mediclaimswala.in](https://mediclaimswala.in): help with rejected, short-paid and delayed health insurance claims in India. English and Hindi, static HTML, no build step.

## What is where

| Path | What it is |
| --- | --- |
| `public/` | **The website.** Everything Cloudflare publishes. |
| `public/index.html` | Home page (inline CSS for a fast first paint). |
| `public/privacy.html`, `public/terms.html`, `public/404.html` | Legal pages and the not-found page. |
| `public/<service>.html`, `public/hi/<service>.html` | Service and guide pages in English and Hindi. **Generated, don't edit by hand** (see below). |
| `content/en.py`, `content/hi.py` | The text of the service and guide pages. Edit these. |
| `tools/build_pages.py` | Builds the service and guide pages and `sitemap.xml` from `content/`. |
| `public/assets/main.js` | Language switch, rejection-reason letter, scroll effects, the case-review form. |
| `public/assets/motion.js`, `public/assets/nav.js` | Motion (motion.dev) springs for section reveals; closes the Services menu. |
| `public/assets/fonts/` | Self-hosted Zodiak (Fontshare), Poppins, Inter and Noto Sans Devanagari. |
| `public/_headers`, `public/_redirects` | Cloudflare security headers, caching and the favicon route. |
| `public/robots.txt`, `public/sitemap.xml`, `public/llms.txt` | For search engines and AI assistants. |

## Editing the service and guide pages

Change the text in `content/en.py` (and the same page in `content/hi.py`), then run `python tools/build_pages.py` from the repo root and commit both the content and the generated `public/` files. The script checks that every internal link points at a real page. When the facts are re-checked, update `REVIEWED` in both content files.
| `docs/` | Design notes. Not published. |
| `mediclaimswala-website.html` | The earlier version, kept for reference. Not published. |

## Preview locally

```sh
cd public
python -m http.server 8080
```

Open http://localhost:8080. (Opening `public/index.html` straight from the folder also works.)

## Deploy on Cloudflare

The site runs as the Cloudflare Worker **`mediclaims`** (static assets, no code), connected to this repository with Workers Builds. `wrangler.jsonc` tells it to serve `public/` and to use `public/404.html` for missing pages. Every push to `main` redeploys it.

- Worker address: https://mediclaims.mediclaimswala.workers.dev (marked `noindex`; the real site is mediclaimswala.in)
- `public/_headers` and `public/_redirects` set the security headers, font caching and the favicon route.

### Vercel (temporary mirror)

`vercel.json` and `.vercelignore` at the repo root let the same `public/` folder deploy on Vercel too (`vercel --prod`). The two hosts never read each other's files: Cloudflare uses `public/_headers` and `public/_redirects`, Vercel uses `vercel.json` and skips those two. `*.vercel.app` is marked `noindex`. When Cloudflare is the only host, delete `vercel.json` and `.vercelignore`.

### Custom domain (later)

1. Pages project → **Custom domains** → add `mediclaimswala.in`, then `www.mediclaimswala.in`.
2. Redirect `www` to the bare domain: **Rules → Redirect Rules** → `www.mediclaimswala.in/*` → `https://mediclaimswala.in/${1}`, 301.
3. Keep **Rocket Loader** off (it rewrites scripts and clashes with the security policy).

## After going live

- **Google Search Console**: add `mediclaimswala.in` (DNS TXT record in Cloudflare), then submit `https://mediclaimswala.in/sitemap.xml`.
- **Google Business Profile**: set the website to `https://mediclaimswala.in`.
- **Cloudflare Web Analytics** (optional, free, no cookies): turn it on in the Pages project; the security policy already allows it.
- **Lead emails** (optional): get a free access key at web3forms.com and paste it into `LEAD_KEY` at the top of `public/assets/main.js`. Without it, leads arrive on WhatsApp only.

## Editing text

Every visible string has an English version in the HTML (`data-i18n="key"`) and a Hindi version in the `HI` list in `public/assets/main.js`. Change both.
