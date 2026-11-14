# Mediclaimswala — MVP landing page redesign

Date: 2026-11-15 · Status: draft for approval · Owner: techteam (for client demo, morning of 2026-11-16)

## Intent and why

The client sees an MVP of the Mediclaimswala landing page tomorrow morning. The current page
(`mediclaimswala-website.html`) works, but it is built from the patterns that make a page read as
AI-generated: gradient hero, pill badges, icon-topped card grids, soft shadows on everything, a dotted
texture, placeholder stats and star-rated placeholder testimonials. For a business whose whole offer is
"trust us with your rejected claim", looking generated is the main risk.

Goal of the redesign: a visitor holding a rejection letter should feel, in five seconds, that real
experts read letters like theirs line by line, and know how to start (free review, WhatsApp).

Product truth comes from `MEDICLAIMSWALA_CONTEXT.md` (business, audiences, compliance guardrails,
working rules). That file stays authoritative.

## Goals

- A hero that is trustworthy and clearly from the medical-insurance world, built around **a rejection
  letter being reviewed by experts** (user's decision; the team stays anonymous, no names or photos).
- One coherent visual world across the whole page (user picked a full redesign, not hero-only).
- A designed footer, referencing typographic / large-type footers on footer.design (the user wrote
  "footer.site"; that domain does not exist).
- Everything that works today keeps working: EN/हिंदी toggle, WhatsApp links with prefilled text, the
  case-review form with validation that opens WhatsApp, reason picker feeding the form, dark mode,
  reduced motion, mobile Call/WhatsApp bar.

## Non-goals (for this MVP)

- No backend, form service, analytics, SEO files, privacy/terms pages, hosting or multi-page site.
  (Those are roadmap items in the context file.)
- No new real content the client hasn't given (fees, numbers, testimonials, address, email).

## Anti-goals (failure even if it "works")

- Any invented proof: stats, testimonials, star ratings, insurer logos, case counts, "trusted by".
- Any promise of approval or recovery, in copy, alt text or meta.
- Any page that looks like a template: centred hero over a gradient, icon cards in rows, pill badges,
  eyebrow labels, 01/02/03 numbering, glass blur, shadows on resting cards.
- A letter that imitates a real insurer's name, logo or letterhead.

## Constraints

- Single static HTML file, inline CSS and vanilla JS, no build step, no new JS libraries. Google Fonts
  only. Must open from the file system and from any static host.
- Brand kept: navy `#0B3C5D` (trust/headings), green `#1FA67A` / `#13805C` (resolution), amber
  `#F5A623` (the one action colour), Poppins for display, Inter for text, Noto Sans Devanagari for
  Hindi, the shield logo and "Mediclaims" + "wala" two-colour wordmark, light + dark themes.
- Every user-facing string exists in English and Hindi (`data-i18n` + `HI` dictionary).
- Mobile first, tested at 360px; tap targets ≥ 44px; visible focus; `prefers-reduced-motion` honoured;
  content visible without JS.
- The original file stays untouched as the demo fallback. The new page is `index.html`.

## Approaches considered

1. **Full redesign in one new look** — new hero, new footer, every section re-composed. Most work,
   one coherent page. **Picked by the user.**
2. New hero + footer, middle sections only cleaned up — faster, but old card-grid layouts would sit
   between two new pieces; the seam shows in a demo.
3. Hero only — quickest; the template look returns on the first scroll. Advised against.

## Visual direction (decided)

Dealt by the taste skill (`.taste-skill/direction.json`, seed 1873956158): **"The printed annual"** —
the page laid out like a well-edited printed report. A fixed column line at ~42% of the width
organises everything: headings and body hang from it; the zone left of it holds small side notes or
stays empty. Sections alternate between text pages on white/paper and full-bleed flat colour pages
(navy, mint, green) carrying one large thing. Brand palette and fonts kept (`--keep palette,type`).

**The idea:** on this page, *the insurer's rejection letter* becomes *the printed report's masthead*,
and *the experts' review* becomes *the margin notes that hang off the column line*. The reviewer's
voice (short notes, in the brand's text face, not a script font) appears beside documents throughout
the page, so the "experts read it line by line" claim is shown, not stated.

**The live thing:** the reason picker lives on the letter. The visitor picks the reason printed on
their own letter (pre-existing disease, waiting period, non-disclosure, "not medically necessary",
room-rent capping, missing documents); the letter's highlighted clause and the reviewer's margin note
change to match (data from today's `REASONS`, both languages). Works by keyboard and thumb; without JS
the default reason is shown.

House rules that apply on top (taste + hallmark + impeccable): no gradients, no shadows on things at
rest, no eyebrows or tracked caps labels, no monospace, no 01/02 index numbers (a real `<ol>` is fine),
no thin hairline dividers as decoration, no icon cards, no pills, no glass, headlines ≤ 2 lines at
every width, one `h1`, a heading on every section, equal outer margins, one button shape and radius.

## Page, section by section

Order follows the page's argument (claim → proof). Dealt blueprints adapted where the content differs;
each adaptation is noted.

1. **Header.** Plain bar: logo + wordmark, 4–5 text links, EN/हिंदी toggle, one amber action ("Free
   case review"). No blur, no pill nav. Sticky is fine.

2. **Hero — the letter under review.** *Redrawn from the dealt "two-by-two board"*, because that
   board needs photographs and a giant name, and the user chose the letter hero.
   - Left of the column line: `h1` (brand tagline family, ≤ 2 lines, e.g. "Claim rejected? Your case
     isn't closed."), one supporting sentence saying plainly what Mediclaimswala does, the amber
     primary action and a WhatsApp secondary action. All visible at 1280×800 and at 360px.
   - Right of the line, large: a realistic claim-decision letter drawn in HTML/CSS (paper, generic
     letterhead "Sample Health Insurance Co. Ltd." or similar, policy no., claim no., date, a
     repudiation paragraph). Marked clearly as a sample. The clause matching the picked reason is
     highlighted; a reviewer note sits in the margin next to it saying what we check.
   - Reason picker attached to the letter ("What does your letter say?"), replacing today's separate
     `#reasons` section. The picked reason still feeds the WhatsApp form message.
   - Trust line under the actions (no pills): free first review, Hindi and English, confidential —
     as plain text.
   - Phone: headline, sentence and action first; the letter below at full width; picker as a
     scrollable row or 2-column grid of real buttons.

3. **How it works.** Dealt "Many into one": one diagram made of a repeated shape instead of arrows —
   scattered papers on the left (the visitor's documents), pulled into a tight band in the middle (our
   review), leaving as an ordered stack on the right (the filed case / resolution). Today's four steps
   sit under it as a real `<ol>` aligned to the diagram (4 columns instead of the blueprint's 3).
   Phone: diagram runs top to bottom, steps beside it.

4. **Services (what we do).** The dealt "paragraph with picture words" cannot hold six services within
   the statement-size limit, so the builder takes the closest alternative from the taste library
   (`draw.mjs --alternatives features`) that holds six named services as a typographic list — name
   large, one line of description — with no icons and no cards. Content from today's six services.

5. **Why Mediclaimswala (about).** Dealt "wide photo, colour tile, facts", adapted: the photo slot
   becomes a second document (e.g. a policy schedule or discharge summary with reviewer marks on it);
   the colour tile carries who we help (families, seniors and their children, employees, HR teams,
   hospitals); the "facts" pairs become the four value points (insider expertise, end-to-end, honest
   advice, data stays private). **The `[X]+` stats are removed.**

6. **Fees.** Dealt "plans as a large table" does not fit (there is one offer, and the fee model is not
   decided). Builder uses a full-bleed colour page with one large statement — "Your first case review
   is free." — plus the two true lines (full fee in writing before we start; no hidden charges) and the
   action. The `[Fee model …]` placeholder is removed. **Testimonials section removed** (no real
   testimonials exist; placeholders and stars would read as fake).

7. **FAQ.** Dealt "answers as reading text": all six Q&As set as continuous reading text in two
   columns, question as a run-in in the medium weight, no accordion, no icons. One column on phones.
   The "ask us on WhatsApp" link stays.

8. **Contact.** Dealt "sentence, portrait, two links" says no form, but the form is product function,
   so it stays: closing sentence and direct links (call, WhatsApp) on the left of the line, the
   case-review form on the right, same fields, validation and WhatsApp hand-off as today.
   `[your email]` and `[Office address]` placeholders are hidden until the client gives them.

9. **Footer.** Dealt "columns above, wordmark below", matching the large-type footers on
   footer.design: inverted ground (navy / near-black navy), small columns at the top (contact, pages,
   languages, disclaimer), and the wordmark "Mediclaimswala" fitted edge to edge at the bottom in the
   brand's two colours. On phones the wordmark stacks as "Mediclaims" / "wala". Disclaimer kept
   verbatim. The last section may slide away to uncover it (sticky reveal) if it doesn't fight the
   mobile action bar.

10. **Floating WhatsApp (desktop) and Call/WhatsApp bar (mobile)** kept, restyled to the new world
    (flat, no glow).

## Imagery

No photographs in this MVP. The open collections searched (Openverse/Wikimedia) only offer off-topic
or risky images (named hospitals that would imply affiliation). The documents are the pictures:
the rejection letter, a policy schedule, a hospital bill or discharge summary, drawn in HTML/CSS/SVG
in one consistent flat paper language, large and legible. This knowingly waives the taste skill's
"four real photographs" floor; the waiver and reason go in the report. Real photos (office, team
hands, documents) can replace slots after the client provides them.

## Motion

- Signature move: the letter opens in once (clip-path shutter, ~1.1s) and the highlight sweeps across
  the clause; the margin note settles in after it. Changing the reason replays only the highlight
  and note.
- Section parts enter once on scroll (heading, text, document), staggered, transform/opacity only.
- Feedback on every control (hover, press, focus) — consistent across buttons, links, reason buttons,
  language toggle, WhatsApp button.
- Reduced motion: no travel, content shown immediately. Content visible with JS off.

## Copy rules

Reuse today's copy and Hindi wherever it fits. New strings (letter sample text, reviewer notes per
reason, trust line, footer columns) are written in both languages. No guaranteed outcomes. Sample
letter text uses realistic but fictional names and numbers.

## Verification (how we'll know it's ready)

- Taste `inspect.mjs` at 1440 / 768 / 390: 0 FAIL, except the photo-floor check, which is waived
  on purpose (see Imagery) and explained in the report; every WARN fixed or defended. Hallmark
  `sloplint --render`: 0 FAIL. Impeccable `detect`: findings fixed or justified.
- Playwright click-through: language toggle (all strings switch, WhatsApp links update), reason picker
  (letter + note change, reason reaches the WhatsApp message), form (3 errors on empty submit; valid
  submit builds the same WhatsApp text as today), mobile bar, 360px with no horizontal scroll.
- Screenshots reviewed at desktop and phone in light and dark.

## Decisions made by the assistant (please check)

- New file `index.html`; original kept as fallback.
- Testimonials and `[X]` stats removed rather than shown as placeholders.
- Email and address placeholders hidden for the demo.
- Fictional "Sample …" insurer on the letter, visibly marked as a sample.
- Services and fees sections deviate from the dealt blueprints (reasons above).

## Left to the builder

Exact sample-letter wording and clause numbers, reviewer-note wording per reason (drafted from
`REASONS`), the document drawings, spacing and type steps within the brand fonts, the services
alternative blueprint, motion timing, and the How-it-works diagram's shape.
