---
title: "Website and Webmap Generation Procedures"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Website and Webmap Generation Procedures

This note consolidates the website/webmap build methods currently documented as Hermes/primary-agent and gis-agent skills. It is intended as a reviewable command-center note, not a replacement for the source skills.

## Source skills / procedural memory

General website skills in primary-agent:

- `/Users/yourname/.hermes/profiles/example-agent/skills/software-development/modern-website-stack/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/software-development/nextjs-product-website-builder/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/software-development/conversion-landing-page-builder/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/software-development/frontend-polish-and-design-system/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/software-development/website-quality-gates/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/creative/claude-design/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/creative/popular-web-designs/SKILL.md`

GIS/webmap skills in gis-agent:

- `/Users/yourname/.hermes/profiles/example-agent/skills/gis/premium-gis-product-app-builder/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/gis/nextjs-gis-web-app-stack/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/gis/open-source-gis-stack-builder/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/gis/esri-claude-code-app-builder/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/gis/client-ready-gis-offers/SKILL.md`
- `/Users/yourname/.hermes/profiles/example-agent/skills/devops/github-vercel-gis-publishing/SKILL.md`

Related Obsidian sources already found:

- `33 Skills/popular-web-designs.md`
- `33 Skills/open-source-gis-stack-builder.md`
- `05 AI Systems/GIS/GIS Products to Sell.md`
- `05 AI Systems/GIS/GIS Application Portfolio Configuration Strategy.md`
- `03 Learning/AI Learning/Claude/Multi Agent Guide/arcgis-web-dev.md`

## One-screen decision tree

Use the smallest stack that genuinely ships the job:

1. **One-off visual artifact / concept / option board**
   - Use: self-contained HTML/CSS/JS.
   - Best for: mockups, comparison pages, interactive explainers, quick prototypes, design boards, decks.
   - Source skills: `claude-design`, `popular-web-designs`.

2. **Conversion landing page / offer page**
   - Use: Astro for content-led pages, Next.js for product/app-adjacent pages, or one-off HTML for quick drafts.
   - Best for: service offers, SaaS waitlists, client acquisition, business idea tests.
   - Source skills: `conversion-landing-page-builder`, `modern-website-stack`.

3. **Content/marketing/documentation website**
   - Use: Astro + TypeScript + Tailwind, with React islands only when needed.
   - Best for: blogs, documentation, portfolios, static marketing websites, content libraries.
   - Source skill: `modern-website-stack`.

4. **Product website / SaaS shell / dashboard app**
   - Use: Next.js App Router + React + TypeScript + Tailwind + shadcn/ui.
   - Best for: multi-route apps, dashboards, forms, route handlers, metadata, Vercel deployments.
   - Source skill: `nextjs-product-website-builder`.

5. **Simple GIS/webmap demo**
   - Use: Vite + ArcGIS Maps SDK CDN/AMD for Esri demos, or Vite + MapLibre/OpenLayers/Leaflet for open-source demos.
   - Best for: portfolio maps, public-data demos, browser-only spatial tools.
   - Source skills: `esri-claude-code-app-builder`, `open-source-gis-stack-builder`.

6. **Premium multi-page GIS product app**
   - Use: Next.js GIS stack + product framing + deliberate cartographic design.
   - Best for: client demos, GIS product labs, portfolio case-study sites, civic intelligence products.
   - Source skills: `premium-gis-product-app-builder`, `nextjs-gis-web-app-stack`, `client-ready-gis-offers`.

7. **Open enterprise GIS agent stack**
   - Use: VPS + PostGIS + QGIS + FastAPI + MapLibre/OpenLayers + controlled Hermes/n8n automation.
   - Best for: showing enterprise-style GIS workflows without claiming ArcGIS Enterprise parity.
   - Source skill: `open-source-gis-stack-builder`.

8. **Published GitHub/Vercel GIS project**
   - Use: GitHub repo + README + build verification + Vercel/static deployment.
   - Best for: public/private portfolio demos and client-review URLs.
   - Source skill: `github-vercel-gis-publishing`.

---

# Procedure 1 — One-off HTML artifact / visual concept

## Use when

- You need a fast preview before building a real repo.
- The deliverable is a design board, option comparison, interactive explainer, small deck, prototype, or dashboard concept.
- Visual hierarchy and interaction matter more than clean production architecture.

## Default output

A complete local `.html` file with embedded CSS and JavaScript, openable directly in a browser.

## Procedure

1. Define the artifact purpose in one sentence.
2. Gather any existing brand/repo/context if available.
3. Choose the format: static option board, clickable prototype, component lab, HTML deck, or interactive report/explainer.
4. Pick a visual direction.
5. If the user wants a known look, load `popular-web-designs` and choose a template such as Linear, Stripe, Vercel, Notion, Supabase, Sentry, or a GIS/data-app reference.
6. Define design tokens: background, foreground, muted text, borders, accent, radius, shadow, typography.
7. Write a self-contained HTML file.
8. Serve locally if needed:
   ```bash
   python3 -m http.server 8877 --bind 127.0.0.1
   ```
9. Open in browser and check console/errors/visual layout.
10. Save path and summary for review.

## Quality gates

- File exists and opens.
- No obvious JavaScript console errors.
- Primary viewport visually checked.
- Mobile checked if it is a public/website-like artifact.
- No private data, tokens, local usernames, or client identifiers included unless intentionally supplied for private review.

## Prompt template

```text
Create a self-contained HTML artifact for [purpose].
Audience: [who reviews/uses it].
Visual direction: [style or reference].
Include: [sections/interactions].
Use sample data only and label it as sample.
Verify locally in browser before reporting the file path.
```

---

# Procedure 2 — Conversion landing page / offer page

## Use when

- The page must persuade someone to book, buy, sign up, request a demo, join a waitlist, or understand an offer quickly.
- Good for AI/GIS service offers, side-business ideas, SaaS concepts, consulting packages, or client-demo wrappers.

## Choose stack

- **One-off HTML** for fast copy/design exploration.
- **Astro** for a lightweight content/marketing site.
- **Next.js** when the landing page belongs to a larger product/app or needs server-side forms/routes.

## Landing page brief

Fill this before writing the page:

```text
Audience:
Pain:
Promise:
Mechanism:
Proof:
CTA:
Risk reversal:
```

## Recommended section order

1. Header/nav with one clear CTA.
2. Hero: specific audience + outcome + concrete visual.
3. Problem/cost of status quo.
4. Solution mechanism in 3–4 concrete steps.
5. Proof: screenshot, demo, case example, credentials, methodology, or honest substitute.
6. Features-to-benefits grid.
7. Use cases / who it is for / who it is not for.
8. Offer/pricing/next step.
9. FAQ and objection handling.
10. Final CTA.

## Procedure

1. Write the landing page brief.
2. Choose one visual direction and a different visual recipe than recent similar sites.
3. Draft copy with concrete nouns/verbs; avoid generic AI/SaaS filler.
4. Build the page in the chosen stack.
5. Add real screenshots/workflow diagrams/map previews when available.
6. Add metadata: title, description, Open Graph if public.
7. Verify mobile hero and CTA.
8. Run quality gates before calling it done.

## Quality gates

- One audience is obvious above the fold.
- Headline says an outcome, not just a product category.
- CTA is specific and repeated consistently.
- No fake testimonials or unverified claims.
- Mobile CTA is easy to tap.
- Build passes if in a repo.
- Secret/privacy scan passes before commit/deploy.

## Prompt template

```text
Build a conversion landing page for [offer].
Audience: [buyer/persona].
Pain: [problem].
Promise: [outcome].
Mechanism: [how it works].
Proof available: [screenshots/data/demo/none].
Primary CTA: [exact action].
Choose the smallest stack that fits and run website quality gates.
```

---

# Procedure 3 — Astro content / marketing / documentation website

## Use when

- The site is mostly content, marketing, docs, portfolio, blog, or reference material.
- SEO and static performance matter.
- Interactivity is limited to a few islands.

## Default stack

- Astro
- TypeScript
- Tailwind CSS
- React islands only when needed
- Sitemap for public sites
- Markdown/MDX content collections for repeatable content

## New project commands

```bash
npm create astro@latest my-site
cd my-site
npx astro add tailwind react sitemap
npm install lucide-react motion zod
npm install -D prettier prettier-plugin-astro
```

## Recommended structure

```text
src/pages/
src/layouts/
src/components/
src/content/
src/styles/global.css
public/
```

## Procedure

1. Define the content model: pages, posts, case studies, docs, or portfolio items.
2. Define the site promise and navigation.
3. Choose design posture and tokens.
4. Create layouts first: base layout, content layout, landing layout.
5. Create reusable components: hero, CTA, feature grid, content card, footer.
6. Add content collections if repeatable content exists.
7. Add metadata, sitemap, and clean URLs.
8. Build and preview.

## Quality gates

- `npm run build` passes.
- Key pages render with correct metadata.
- Navigation works on mobile.
- No broken internal links in the main nav/footer.
- Images/assets are optimized enough for static hosting.
- No secrets/private data in public content.

## Prompt template

```text
Build an Astro content/marketing site for [topic/business/project].
Content types: [pages/posts/case studies/docs].
Audience: [reader/buyer].
Primary action: [CTA].
Design direction: [reference or posture].
Use Markdown/MDX collections where useful and verify build + mobile nav.
```

---

# Procedure 4 — Next.js product website / SaaS shell / dashboard app

## Use when

- The site needs multiple routes, app-like interactions, server routes, forms, auth later, dashboards, metadata, or Vercel app deployment.
- Good for SaaS product pages, internal tools, client portals, AI/GIS dashboards, app shells.

## Default stack

- Next.js App Router
- React
- TypeScript
- Tailwind CSS
- shadcn/ui + Radix primitives
- Lucide icons
- Zod for validation
- Vitest for pure logic
- Playwright for key browser journeys when useful

## New project commands

```bash
npx create-next-app@latest my-site --ts --tailwind --eslint --app --src-dir --import-alias '@/*'
cd my-site
npx shadcn@latest init
npx shadcn@latest add button card input textarea badge tabs accordion dropdown-menu sheet dialog table skeleton sonner
npm install lucide-react zod @tanstack/react-query motion
npm install -D vitest @testing-library/react @testing-library/jest-dom playwright
```

## Recommended structure

```text
src/app/
  layout.tsx
  page.tsx
  (marketing)/
  (app)/dashboard/page.tsx
  api/.../route.ts
src/components/
  ui/
  marketing/
  app-shell/
  forms/
  charts/
src/lib/
  env.ts
  validations.ts
  metadata.ts
  utils.ts
  data/
public/
```

## Server/client rules

- Pages and layouts are Server Components by default.
- Use Client Components for browser APIs, local state, charts, maps, editors, drag/drop, command palettes, and dialogs with state.
- Keep client wrappers narrow.
- Do not pass secrets, DB clients, or server-only objects into Client Components.
- Validate route params, forms, and API bodies with Zod.

## Procedure

1. Inspect existing repo if one exists.
2. Confirm package manager and scripts.
3. Define route structure and app groups.
4. Build design tokens/layout before pages.
5. Implement marketing pages and app/dashboard pages separately.
6. Add forms/API routes only after the data contract is clear.
7. Add loading/empty/error states.
8. Run build/lint/type/test where configured.
9. Browser-check desktop and mobile.

## Quality gates

- Route structure is coherent.
- Server/client boundaries are intentional.
- Build passes.
- Lint/type/test status is reported honestly.
- Dashboard answers “what should I do next?” not just “look at these cards.”
- Browser screenshot/inspection confirms visual quality at mobile and desktop.

## Prompt template

```text
Build a Next.js product website/app for [product/workflow].
Routes needed: [home, dashboard, map, settings, etc.].
Audience: [user].
Primary workflow: [task].
Data: [static sample/public API/private later].
Use App Router, TypeScript, Tailwind, shadcn/ui, and run quality gates before reporting.
```

---

# Procedure 5 — Frontend polish / design-system upgrade

## Use when

- A site works but looks generic, unfinished, inconsistent, or AI-made.
- Webmaps/pages are starting to look the same.
- The task is “make it modern/professional/premium” without changing core functionality.

## Procedure

1. Inventory current UI files: global CSS, Tailwind/theme config, layout, shared components, key pages.
2. Inspect the current page in browser if possible.
3. Choose a design posture: editorial trust, premium SaaS, developer-tool dark, civic utility, playful creator, luxury minimal, data-dense cockpit, or map/data-first.
4. Write a variation recipe: typography, color world, surface style, motion level, CTA/action language, and for maps: basemap, symbology, legend, popup/detail pattern, mobile behavior.
5. Centralize tokens using CSS custom properties or Tailwind theme conventions.
6. Apply typography scale, spacing rhythm, states, and responsive rules.
7. Remove AI-design slop: too many gradients, random icons/emoji, weak contrast gray text, generic cards, fake metrics, repeated dark SaaS look across unrelated sites.
8. Browser-check desktop, tablet-ish, and mobile widths.

## Quality gates

- Design posture is named and consistently applied.
- Variation recipe is visible in the plan/README or notes.
- Tokens are centralized.
- Buttons/cards/forms have hover/focus/disabled states.
- Mobile layout is visually checked.
- Browser review shows no obvious clipping, overlap, or placeholder slop.

## Prompt template

```text
Polish this website/webmap without changing the core functionality.
Current issue: [generic/unfinished/mobile/map overlays/etc.].
Choose a differentiated visual recipe first.
Fix tokens, typography, spacing, states, responsive layout, and map/page-specific UI.
Run browser verification at desktop and mobile widths.
```

---

# Procedure 6 — Simple Esri ArcGIS JS portfolio webmap

## Use when

- the operator wants a standalone portfolio mapping application using Esri services or ArcGIS-familiar workflows.
- The app should be a static/Vercel-friendly demo, not an ArcGIS Online/Enterprise Web Experience item.

## Default stack

- Vite
- ArcGIS Maps SDK for JavaScript via CDN AMD `require`
- Plain JavaScript or light TypeScript if project demands it
- CSS in `src/style.css` or `style.css`
- README with local/dev/deploy/data notes

## Important convention

For the operator’s simple ArcGIS JS portfolio apps, default to **Vite + ArcGIS JS SDK via CDN AMD `require`**, not npm/ESM, unless explicitly asked.

Template CDN shape:

```html
<link rel="stylesheet" href="https://js.arcgis.com/4.34/esri/themes/light/main.css">
<script src="https://js.arcgis.com/4.34/"></script>
```

Template JS shape:

```javascript
require([
  "esri/Map",
  "esri/views/MapView",
  "esri/layers/FeatureLayer"
], function (Map, MapView, FeatureLayer) {
  // Complete app code here.
});
```

## Discovery / viability procedure

1. Identify the public data source before coding.
2. Prefer public hosted `FeatureServer`/`MapServer` endpoints for Esri portfolio demos.
3. Validate read-only endpoint details: service metadata, layer metadata, count query, sample records, geometry type, spatial reference, date/filter fields, domains/coded values, and CORS suitability.
4. Validate temporal fields empirically; do not assume date fields are populated or recent.
5. For large layers, default to safe recent/category/status filters.
6. Pause for approval at phase boundaries if the concept/data/build/deploy scope is unclear.

## Build procedure

1. Scaffold Vite app.
2. Add `index.html`, `main.js`, CSS, `vite.config.js`, and README.
3. Add ArcGIS map, view, layers, popups, legend, filters.
4. Use a product promise, not just “show points on a map.”
5. Add data source/caveat section in README and/or page.
6. Run build and browser QA.

## Responsive map rules

- Desktop overlay panels can use map padding, but mobile must preserve usable map area.
- On phone widths, heavy KPI/filter panels should move into document flow or collapse.
- Check horizontal overflow at about 390px.
- Make renderer and legend use the same category rules.

## Quality gates

- Public data source validated.
- Build passes.
- Map loads with no fatal console errors.
- Legend matches actual renderer/symbology.
- Mobile map is usable.
- README explains data source and caveats.
- No private ArcGIS service/token/credential in client code.

## Prompt template

```text
Build a standalone Vite + ArcGIS Maps SDK portfolio app.
Use public data only: [service URL or search target].
First validate metadata, fields, count, samples, geometry, dates, filters, and CORS.
Then build a productized webmap with a clear user/workflow, legend parity, responsive layout, README, build verification, and browser QA.
```

---

# Procedure 7 — Open-source webmap demo

## Use when

- the operator wants a non-Esri frontend stack or open-source GIS demo.
- The app can use public data, static data, PMTiles, or public ArcGIS REST as a read-only source.

## Stack selection

- **MapLibre GL JS**: vector tiles, basemap styling, PMTiles, polished modern web maps.
- **OpenLayers**: GIS controls, projections, WMS/WFS/OGC, heavier geospatial workflows.
- **Leaflet**: simple markers/GeoJSON, quick MVPs, minimal complexity.
- **deck.gl**: high-volume GPU visualization, temporal/point-cloud/large visual analysis.

Data prep/storage:

- GeoJSON for small demos only.
- FlatGeobuf / GeoParquet for efficient file-based data.
- PMTiles for static deployable vector/raster tiles.
- DuckDB spatial for local analytical SQL.
- PostGIS or Supabase/PostGIS for serious multi-user apps.

## Procedure

1. Identify use case: visualization, ETL, analysis, editing, routing, tiles, or AI/GIS workflow.
2. Pick the smallest map engine that ships the demo.
3. Validate data source and license/attribution.
4. If using public ArcGIS REST with an open-source frontend, label it honestly as “open-source client stack consuming public ArcGIS REST data.”
5. Keep browser-rendered records bounded unless full paging/performance has been tested.
6. Build Vite app with chosen map engine.
7. Add filters, legend, popups/detail panels, source notes, and performance-safe defaults.
8. Run build and browser QA.

## Public ArcGIS REST data procedure for open-source maps

1. Validate service/layer metadata, fields, count, geometry, spatial reference, CORS, and realistic filters.
2. Query aggregate stats separately using REST stats/grouping where supported.
3. Fetch a safe display subset by default.
4. For full filtered datasets, inspect pagination support and page conservatively.
5. Convert to GeoJSON only for small/bounded data; otherwise precompute PMTiles/FlatGeobuf/GeoParquet/cached API.
6. Always report total matching records separately from mapped/geocoded records.

## Quality gates

- Build passes.
- Data is size-appropriate for browser/static hosting.
- README explains client stack, basemap, data source, and caveats.
- No private API keys/tokens in diffs.
- Browser QA checks map load, interactions, mobile layout, and console errors.

## Prompt template

```text
Build an open-source GIS webmap demo for [use case].
Compare MapLibre/OpenLayers/Leaflet/deck.gl and choose the smallest suitable stack.
Use public/static data only unless approved.
Document client stack, basemap, data source, caveats, and deployment path.
Run build + browser QA.
```

---

# Procedure 8 — Premium multi-page GIS product app

## Use when

- The goal is not just a map but a client-ready GIS/data product.
- The app needs routes, dashboard, map explorer, report pages, methodology, case studies, or app shell.
- Good for portfolio demos, client acquisition, productized civic/spatial tools, and GIS product labs.

## Default stack

- Next.js App Router
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- Lucide icons
- MapLibre for open-source mapping
- ArcGIS Maps SDK when Esri/Enterprise workflows matter
- Recharts or ECharts
- Zod
- Vitest/Playwright where useful
- Vercel for hosting

## Product promise

Do not code until this is specific:

```text
This app helps [persona] [do task] by combining [spatial/data source] with [workflow/insight] in [format].
```

## Visual recipe required

```markdown
## Visual Recipe
- Design posture:
- Typography:
- Color world:
- Cartography:
- Surface style:
- Primary action language:
- Anti-repeat note:
```

## App archetypes

1. **GIS product landing page + live demo** — Home, demo, use cases, data/methodology, implementation, contact/next step.
2. **Civic intelligence dashboard** — `/`, `/dashboard`, `/map`, `/neighborhoods` or `/districts`, `/methodology`, `/export`.
3. **Site-selection / parcel intelligence app** — `/`, `/search`, `/map`, `/sites/[id]`, `/compare`, `/report`.
4. **Operations triage workspace** — `/queue`, `/map`, `/records/[id]`, `/trends`, `/settings`.
5. **Analytical story/report site** — Executive summary, map story chapters, charts, methodology, download/share.

## Recommended route architecture

```text
app/
  layout.tsx
  page.tsx
  dashboard/page.tsx
  map/page.tsx
  datasets/page.tsx
  reports/page.tsx
  methodology/page.tsx
components/
  map/
  ui/
  charts/
  layout/
lib/
  gis/
  data/
  scoring/
  validation/
public/
  data/
```

## Map architecture

Keep map engine code separate from product logic:

```text
components/map/
  MapShell.tsx
  MapLibreMap.tsx
  ArcGISMap.tsx
  LayerManager.tsx
  Legend.tsx
  PopupPanel.tsx
lib/gis/
  layer-schema.ts
  map-events.ts
  geojson.ts
  projections.ts
  arcgis-adapter.ts
  maplibre-adapter.ts
```

## Procedure

1. Define persona, decision/workflow, and product promise.
2. Pick app archetype and routes.
3. Select map engine deliberately.
4. Define visual recipe and cartographic recipe.
5. Validate data source and caveats.
6. Build shell, navigation, and pages before detailed map work.
7. Build map components with SSR-safe client wrappers.
8. Add charts/tables/reports with source notes.
9. Add methodology/data caveat page.
10. Add README with adaptation-to-client section.
11. Run build, tests, browser QA, mobile QA, secret scan.
12. If deployed, verify live URL.

## Next.js map pitfall

In newer Next.js/Turbopack-style setups, do not directly use `next/dynamic(..., { ssr: false })` inside a Server Component page. Put the dynamic map import in a small Client Component wrapper, then import that wrapper from the Server Component page.

## Quality gates

A premium GIS app is not done until:

1. Product promise is visible in app or README.
2. Pages/routes support the workflow.
3. Data source and caveats are explicit.
4. Visual direction is deliberate and different from recent similar apps.
5. Build passes.
6. Browser console has no fatal errors.
7. Mobile layout is checked.
8. Secret scan passes.
9. If deployed, live URL is verified.
10. For portfolio/case-study sites, app inventory is cross-checked against known repos/deployments.

## Prompt template

```text
Build a premium multi-page GIS product app for [persona/workflow].
Product promise: [sentence].
Archetype: [landing+demo/civic dashboard/site selection/ops triage/story site].
Map engine: [MapLibre/ArcGIS Maps SDK].
Data source: [public/static/client later].
Create a visual recipe and anti-repeat note before coding.
Use Next.js App Router, TypeScript, Tailwind, shadcn/ui, map abstraction, methodology page, README, quality gates, mobile/browser QA, and secret scan.
```

---

# Procedure 9 — GIS portfolio / case-study product lab

## Use when

- the operator wants a single website aggregating multiple GIS apps, Vercel demos, repositories, or case studies.
- The goal is a client-facing product lab rather than another map demo.

## Default structure

```text
src/app/page.tsx
src/app/apps/page.tsx
src/app/apps/[slug]/page.tsx
src/app/stack/page.tsx
src/app/methodology/page.tsx
src/lib/apps.ts
```

Use `src/lib/apps.ts` as the typed source of truth for app metadata and long-form writeups.

## Case study should include

- audience,
- problem,
- workflow,
- usefulness,
- architecture,
- stack,
- public data,
- caveats,
- future direction,
- live app/repo CTAs,
- iframe preview when public-safe.

## Procedure

1. Inventory candidate apps from local app folders, GitHub repos, Vercel projects, README files, prior notes/work logs.
2. Compare visible app list against known app families: safety, development/planning, budget/money, business/site selection, permits, homelessness/engagement, crime trends, 311/service requests, neighborhood vitality/civic assets.
3. Build/update typed content source first.
4. Generate app index and detail routes from the content source.
5. Add stack/methodology page explaining common architecture and caveats.
6. Verify index and at least one new detail page locally and live if deployed.

## Quality gates

- App inventory cross-checked.
- Dynamic index and detail routes use a central source of truth.
- Each case study has live/repo links or labels why unavailable.
- Browser QA covers `/`, `/apps`, and at least one `/apps/<slug>` route.
- Mobile nav/cards/iframes do not overflow.

## Prompt template

```text
Create/update a GIS portfolio product-lab site.
Inventory known apps from local folders, GitHub, Vercel, READMEs, and notes.
Use Next.js with src/lib/apps.ts as source of truth.
Create app index, detail pages, stack page, methodology page, and client-facing CTAs.
Verify local build, browser routes, mobile containment, and deployed URL if publishing.
```

---

# Procedure 10 — Client-ready GIS offer package

## Use when

- A GIS/webmap demo should become a sellable offer, not just a technical experiment.
- Useful for the operator’s goal of practical revenue from Hermes + n8n + GIS automation.

## Offer template

```markdown
## Client Offer
- Buyer/persona:
- Pain point:
- Outcome:
- Demo app:
- Data needed from client:
- Automation/GIS components:
- Setup fee idea:
- Monthly support/hosting idea:
- Risks/limitations:
- Next sales step:
```

Keep pricing as draft ranges/placeholders unless explicitly asked for a proposal.

## Strong offer types

1. **Civic Service Pulse** — City/public works/311 operations dashboard + map + priority queue + weekly digest.
2. **Planning & Development Watch** — Permits/projects map + detail pages + new project alerts.
3. **Site Selection Screener** — Search + map + scorecard + compare + report.
4. **Infrastructure / Utility Network Explainer** — Trace result map + plain-English summary + exportable packet.
5. **Public Data Story Site** — Editorial story + maps/charts + recurring data refresh/briefings.
6. **Open Enterprise GIS Agent Stack** — PostGIS/QGIS/API/web map/AI-agent demo with controlled permissions.

## Procedure

1. Start from a working or planned demo.
2. Identify buyer/persona and pain.
3. Define outcome and business value.
4. Add “How this could be adapted for a client” section: replace public demo data with client data, add authenticated staff-only views, connect alerts/reports through n8n/email/Teams/Slack, add scheduled refresh and QA checks, package hosting/monitoring/support.
5. Add sales next step: live demo, fit call, pilot, audit, or sample report.
6. Make limitations and data caveats explicit.

## Quality gates

- One-sentence buyer outcome is visible.
- Demo has live URL or screenshot path if available.
- README/site explains stack/data sources/caveats.
- Offer does not overclaim production readiness.
- Next sales step is concrete.

## Prompt template

```text
Turn this GIS/webmap app into a client-ready offer.
App/demo: [name/path/URL].
Buyer: [persona].
Pain/outcome: [details].
Add offer structure, adaptation path, automation add-ons, risks, maintenance model, and next sales step.
Do not invent exact pricing as fact.
```

---

# Procedure 11 — Open enterprise GIS agent stack

## Use when

- The goal is to demonstrate open-source enterprise GIS capability, not just a frontend map.
- Best for GIS managers, civic data teams, utilities, consultants, and planning/public works analysts.

## Positioning

Do not claim full ArcGIS Enterprise parity. Position this as enterprise GIS building blocks:

- PostGIS system of record,
- QGIS analyst desktop access,
- FastAPI controlled workflow API,
- MapLibre/OpenLayers web map,
- vector tiles/OGC publishing,
- scheduled automation,
- backups/ops,
- AI agents for safe spatial SQL, QA, reports, and briefings.

## Recommended MVP stack

- VPS: Ubuntu + Docker Compose + Caddy/Nginx HTTPS.
- Database: PostgreSQL/PostGIS with `source`, `staging`, `analysis`, `ai_results`, `reports` schemas.
- GIS desktop: QGIS connecting via SSH tunnel to VPS PostGIS.
- Publishing: Martin or `pg_tileserv` first; GeoServer later if WMS/WFS administration matters.
- API: FastAPI endpoints for health, schema inspection, guarded read SQL, and controlled save-to-results.
- Agent: Hermes on VPS through controlled API/DB roles.
- Automation: cron/n8n after the core loop works.

## Guardrails

- Never expose Postgres publicly by default.
- Never give the agent `postgres`/admin credentials.
- Use read/write roles with narrow schemas.
- Block destructive AI-generated SQL: `DROP`, `DELETE`, `UPDATE`, `ALTER`, `TRUNCATE`, broad `CREATE`, multi-statement SQL.
- Require explicit `LIMIT` during exploration.
- Generated AI outputs become GIS layers only through a controlled save endpoint.

## Procedure

1. Define the demo workflow: question → validated SQL/API → result layer → web/QGIS visibility → report/brief.
2. Define schemas, roles, and allowed operations.
3. Build Docker Compose for PostGIS, API, tile service, web app, reverse proxy.
4. Load safe public/sample data.
5. Build FastAPI guard endpoints.
6. Build web map connected to tiles/API.
7. Configure QGIS connection via SSH tunnel/VPN.
8. Add Hermes/n8n automation only after controlled API works.
9. Document backups, monitoring, and rollback.

## Quality gates

- No database admin credentials exposed to agents or frontend.
- Public internet exposes only intended HTTPS endpoints.
- API blocks destructive SQL and multi-statements.
- QGIS and web app see the same approved output layer.
- README explains what this is and is not.

## Prompt template

```text
Design/build an open enterprise GIS agent stack demo.
Goal: [workflow].
Use PostGIS, QGIS, FastAPI, MapLibre/OpenLayers, tile publishing, controlled Hermes/n8n automation.
Do not claim ArcGIS Enterprise parity.
Define roles/schemas/guardrails first, then scaffold Docker/API/web app, then verify with sample data.
```

---

# Procedure 12 — GitHub + Vercel publishing for website/GIS projects

## Use when

- A website, webmap, static report, or GIS app needs a repo and/or deployment URL.

## Safety rules

- Default GitHub repos to private unless explicitly public.
- Do not commit `.env`, API keys, ArcGIS tokens, Portal credentials, Vercel tokens, `.vercel`, `node_modules`, or build outputs unless intentionally safe.
- Production deploys require explicit approval unless the operator directly asked to publish/deploy.
- Public apps must not depend on private/on-prem services unless explicitly approved or mocked.

## Preflight commands

```bash
git --version
gh --version || true
HOME=/Users/yourname gh auth status || true
HOME=/Users/yourname vercel --version || true
HOME=/Users/yourname vercel whoami || true
npm --version
```

For the operator’s local CLI auth, prefix auth-dependent commands with:

```bash
HOME=/Users/yourname
```

## Repo standards

Minimum files:

- `README.md` with purpose, stack, local setup, data sources, and deployment URL.
- `.gitignore` with `node_modules`, `dist`, `.env*`, `.vercel`, OS/editor cruft.
- `package.json` scripts: `dev`, `build`, `preview` or relevant framework equivalents.
- Public data attribution/license notes.

Set repo-local Git identity before first commit:

```bash
GH_ID=$(HOME=/Users/yourname gh api user --jq '.id')
git config user.name "Example Operator"
git config user.email "${GH_ID}[EMAIL REDACTED]"
```

## Typical GitHub flow

```bash
git status
git init -b main  # only if not already a repo
git add .
git diff --cached --stat
git diff --cached
# inspect for secrets, then commit
git commit -m "feat: scaffold web app"
HOME=/Users/yourname gh repo create <repo-name> --private --source . --push
```

## Vercel static/Vite flow

```bash
npm install
npm run build
HOME=/Users/yourname vercel --yes
HOME=/Users/yourname vercel inspect <deployment-url-or-alias>
```

Vercel settings for Vite:

- Framework preset: Vite.
- Build command: `npm run build`.
- Output directory: `dist`.
- Install command: `npm install` or `npm ci` depending on lockfile.

## Vercel Next.js flow

```bash
npm run lint
npm run build
npm run dev -- -H 127.0.0.1 -p 3020
# Browser-check /, /apps, and at least one dynamic route.
HOME=/Users/yourname vercel --yes
HOME=/Users/yourname vercel inspect <deployment-url-or-alias>
```

## Quality gates

- Build passes before deployment.
- Required env var names are documented without values.
- Secret scan passes.
- Live URL is opened and checked after deployment.
- Console errors and mobile layout checked on live site when public-facing.
- Final report includes repo URL, deployment URL, checks, and caveats.

## Prompt template

```text
Publish this website/webmap project to GitHub and Vercel.
Repo privacy: [private/public].
Deployment target: [preview/production].
Run auth checks, build, secret scan, repo hygiene, commit, push, deploy, inspect, and browser-check the live URL.
Do not print or commit secrets.
```

---

# Universal website/webmap quality gate

Run these before saying any website or webmap is done.

## Command gates

Inspect `package.json` and run only configured scripts:

```bash
npm install                # if dependencies are missing/outdated for this checkout
npm run lint               # if configured
npm run typecheck          # if configured
npm run test -- --run      # if configured and compatible
npm run build
```

If lint/type/test are not configured, say so honestly.

## Browser gates

1. Start dev/preview server.
2. Wait for readiness using logs or HTTP check.
3. Check desktop and mobile widths.
4. Check key routes.
5. Test primary CTA/form/menu/map interaction.
6. Check browser console errors.
7. Use visual/screenshot review if available.

## Accessibility basics

- One logical `h1` per page.
- Headings ordered semantically.
- Buttons/links have accessible names.
- Inputs have labels.
- Focus states visible.
- Color contrast readable.
- Keyboard reaches nav/dialogs/forms/menus.
- Images have meaningful alt text or empty alt when decorative.
- Motion respects `prefers-reduced-motion`.

## Public-page SEO basics

- Title and meta description.
- Open Graph metadata when relevant.
- Canonical URL if known.
- Sitemap/robots for content sites when appropriate.
- Critical marketing copy not hidden entirely behind client-only rendering unless intentional.

## Secret/privacy gate

Before commit/deploy:

```bash
git status --short
git diff -- . ':(exclude)package-lock.json' ':(exclude)pnpm-lock.yaml' ':(exclude)yarn.lock'
```

Scan changed files for real token/key patterns. Do not preserve or print secret values.

## Final report format

```text
Done — built/updated [site/app].
Checks:
- build: pass/fail
- lint/type/test: pass/not configured/fail
- browser: desktop + mobile checked / limited because ...
- secrets: no obvious changed-file secrets found
Files changed: ...
URL/path: ...
Next: ...
```

---

# Review checklist for the operator

When reviewing this note, decide:

- Should this stay in `00 Inbox` or move to `05 AI Systems/GIS/` as a durable playbook?
- Should gis-agent be the default agent/profile for all GIS webmap builds?
- Should primary-agent keep general website work while gis-agent handles GIS product apps?
- Which item types should become templates/snippets in future repos?
- Which build types should be offered as $5k–$10k MRR packages first?

Suggested first packaged offers to explore:

1. Civic Service Pulse.
2. Planning & Development Watch.
3. Site Selection Screener.
4. Public Data Story Site.
5. Open Enterprise GIS Agent Stack.
