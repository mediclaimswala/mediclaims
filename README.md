# Mediclaimswala website

Landing page for [mediclaimswala.in](https://mediclaimswala.in): help with rejected, short-paid and delayed health insurance claims in India. English and Hindi, static HTML, no build step.

## What is where

| Path | What it is |
| --- | --- |
| `public/` | **The website.** Everything Cloudflare publishes. |
| `public/index.html` | Home page (inline CSS for a fast first paint). |
| `public/privacy.html`, `public/terms.html`, `public/404.html` | Legal pages and the not-found page. |
| `public/assets/main.js` | Language switch, rejection-reason letter, scroll effects, the case-review form. |
| `public/assets/fonts/` | Self-hosted Poppins, Inter and Noto Sans Devanagari. |
| `public/_headers`, `public/_redirects` | Cloudflare Pages security headers, caching and the favicon route. |
| `public/robots.txt`, `public/sitemap.xml` | For search engines. |
| `docs/` | Design notes. Not published. |
| `mediclaimswala-website.html` | The earlier version, kept for reference. Not published. |

## Preview locally

```sh
cd public
python -m http.server 8080
```

Open http://localhost:8080. (Opening `public/index.html` straight from the folder also works.)

## Deploy on Cloudflare Pages

Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** → pick this repository, then:

| Setting | Value |
| --- | --- |
| Production branch | `main` |
| Framework preset | None |
| Build command | *(leave empty)* |
| Build output directory | `public` |

Every push to `main` publishes the site; other branches get preview links on `*.pages.dev` (kept out of Google by `_headers`).

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
