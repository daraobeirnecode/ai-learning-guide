---
title: "R08 — Web App Dev Capability: Style Bundles, _state, Diversity Eval, MapLibre + Leaflet Scaffolds"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# R08 — Web App Dev Capability

This runbook gives the agent end-to-end web-app scaffolding for GIS apps. It binds the app-scaffold skills from R05-skills-library-bootstrap to gis-agent's 10 style bundles (per Hermes for GIS App Dev — 50 Ideas and Plan v2), wires `gis-apps/_state/`, and turns on the diversity eval that prevents the agent from producing samey output.

We finish by walking through a real MapLibre scaffold and a real Leaflet scaffold end-to-end.

---

## 1. gis-agent's 10 style bundles

The bundles are pre-built design tokens + map-style JSON + component snippets. Each bundle is a self-contained `bundle.json` plus assets under `gis-apps/_bundles/<slug>/`.

```
bundles/
  mercator-clean/         # default, neutral, business-grade
  mercator-noir/          # dark mode, dense data
  mercator-sandstone/     # warm, environment + heritage
  mercator-aqua/          # marine, hydrology
  mercator-cargo/         # logistics, ports, supply chain
  mercator-fieldwork/     # high-contrast for field tablets
  mercator-civic/         # local government, citizen-facing
  mercator-academic/      # publications, journals, monochrome accent
  mercator-pitch/         # demo decks and sales conversations
  mercator-tactical/      # operations center, real-time
```

Each `bundle.json` declares: color palette, typography, basemap style URL or PMTiles path, marker/symbol set, legend style, and a list of compatible map libraries (`maplibre`, `leaflet`, `openlayers`).

Install:

```
cd /opt/gis-agent
sudo -u gisagent rsync -av kit/gis-apps/_bundles/ gis-apps/_bundles/
ls gis-apps/_bundles | wc -l
```

**Expected output:** `10`.

**Verification gate:** every bundle has a `bundle.json` that validates against `gis-apps/_bundles/bundle.schema.json`.

**Rollback if:** a bundle fails schema — block deployment; bundles are load-bearing inputs.

---

## 2. The style-bundle-picker skill

The picker is its own small skill `style-bundle-pick` that selects a bundle for a given brief. It uses three signals:

1. The brief's domain (logistics, citizen, marine, etc.) keyword-matches against bundle tags.
2. The customer's `MEMORY.md` may pin a default (e.g. an agency might pin `mercator-civic`).
3. The diversity eval (section 5) penalizes bundles used recently.

It is wired in:

```
sudo -u gisagent bin/agent skills wire \
  --skill style-bundle-pick \
  --bind-to web-app-scaffold-maplibre,web-app-scaffold-leaflet
```

This makes the picker run before either scaffold skill, returning the chosen bundle as a structured input.

**Verification gate:** `bin/agent --profile gis-app-dev --task "scaffold a map for Acme Logistics"` logs `style-bundle-pick -> mercator-cargo` (or another reasoned choice).

---

## 3. `gis-apps/_state/` — the agent's working memory for apps

Every scaffolded app gets a sibling `_state/` folder under `gis-apps/`. The agent owns it.

```
gis-apps/
  acme-logistics-map/
    src/
    index.html
    package.json
    vite.config.ts
    README.md
    _state/
      bundle.lock          # which bundle was picked, why, and a hash of its contents
      brief.md             # the original natural-language brief
      diversity.json       # diversity scores at scaffold time
      decisions.md         # narrative log of choices the agent made
      next-steps.md        # the agent's TODO list for the next session
```

The state folder is what lets the agent come back to an app a week later and continue work coherently. It is the agent's per-app memory.

**Verification gate:** any scaffold run creates the four state files.

**Rollback if:** `_state/` is missing — the scaffold skill aborts. Treat as a bug.

---

## 4. The diversity eval

Without this, an LLM-driven scaffolder picks the same look-and-feel repeatedly. The diversity eval scores a candidate scaffold against the last N (default 5) scaffolds and refuses to ship a near-duplicate.

Scoring:

- 30%: bundle similarity (categorical with adjacency).
- 30%: dominant color delta in screenshot (rendered headless via Playwright).
- 20%: layout similarity (hashed component tree).
- 20%: copy similarity (cosine over README + index.html text).

```
sudo -u gisagent bin/agent eval diversity \
  --candidate gis-apps/acme-logistics-map \
  --baseline gis-apps/_state/_history/last5/
```

A candidate scoring < 0.35 against the average of the last 5 is rejected; the scaffold skill retries with a different bundle and a `diversity_pressure` flag in the prompt.

**Verification gate:** running the eval against an obvious clone returns < 0.35; against a deliberately different scaffold returns > 0.6.

**Rollback if:** the eval falsely rejects good output — raise the threshold to 0.30 and instrument why. Do not turn the eval off; it is the bulwark against samey output.

---

## 5. Walkthrough: scaffold a MapLibre app end-to-end

Brief: "Build a MapLibre app that shows port congestion for Acme Logistics. Use the customer's PMTiles of vessel positions."

```
cd /opt/gis-agent
sudo -u gisagent bin/agent \
  --profile gis-app-dev \
  --task "Scaffold a MapLibre app for Acme Logistics port congestion, using vessels.pmtiles from /opt/gis-agent/data/customer/acme/"
```

What the agent does, in order:

1. Loads `profiles/gis-app-dev/MEMORY.md` (gis-agent defaults from R06-memory-system).
2. Calls `style-bundle-pick` -> `mercator-cargo` (matches logistics keywords).
3. Calls `web-app-scaffold-maplibre`:
   - Initializes `gis-apps/acme-logistics-map/` with Vite + TypeScript.
   - Pulls `maplibre-gl@^4` and `pmtiles@^3` from the templates installed in R03-open-source-gis-stack.
   - Writes `src/map.ts` with the gis-agent-cargo style applied, the PMTiles protocol registered, and a vessel-density circle layer.
   - Generates a `README.md` and a `_state/decisions.md` explaining choices.
4. Runs `npm run build` (sandboxed).
5. Renders a Playwright screenshot to `_state/screenshot.png`.
6. Runs the diversity eval. Score 0.71 against last 5. Passes.
7. Writes `_state/next-steps.md`: legend, time slider, mobile breakpoint.

**Expected output:** a fully working MapLibre app under `gis-apps/acme-logistics-map/` with a working build.

**Verification gate:** `cd gis-apps/acme-logistics-map && npm run preview` opens a working map.

**Rollback if:** the build fails — the scaffold skill rolls back the directory and logs the build error. Re-run with `--retry-with-debug`.

---

## 6. Walkthrough: scaffold a Leaflet app end-to-end

Brief: "Quick prototype: Leaflet map of pothole reports from a citizens-portal feed."

```
sudo -u gisagent bin/agent \
  --profile gis-app-dev \
  --task "Scaffold a Leaflet prototype showing pothole reports from https://data.example.gov/potholes.geojson"
```

What the agent does:

1. `style-bundle-pick` -> `mercator-civic` (citizen-facing domain).
2. `web-app-scaffold-leaflet`:
   - Scaffolds `gis-apps/potholes-leaflet/` with a single `index.html`, a small JS file, Leaflet 1.9, and gis-agent-civic CSS variables.
   - Fetches the GeoJSON at build time and caches a sample under `_state/sample.geojson` for offline preview.
   - Generates simple cluster markers with `leaflet.markercluster`.
3. Diversity eval: 0.62 against the last 5 (mercator-civic was not in the recent window). Passes.
4. `_state/next-steps.md`: add a heatmap layer toggle, mobile bottom-sheet UI, source attribution.

**Expected output:** a single-page Leaflet app you can open with `python -m http.server` from `gis-apps/potholes-leaflet/` and see clustered points.

**Verification gate:** the GeoJSON fetch is sandboxed under the `net.http:data.example.gov` capability granted by the `gis-app-dev` profile.

**Rollback if:** the GeoJSON source is unreachable — the agent falls back to the cached sample and notes this in `_state/decisions.md`.

---

## 7. Tracking the last-5 history

```
gis-apps/_state/_history/last5/
  2026-06-11-acme-logistics-map/
    screenshot.png
    bundle.lock
    bundle_used.txt
  2026-06-10-citymap-tactical/
    ...
```

A trim job runs on every scaffold to keep exactly 5 entries. The diversity eval reads from here.

```
sudo -u gisagent bin/agent gis-apps history trim --keep 5
```

**Verification gate:** `ls gis-apps/_state/_history/last5/ | wc -l` returns 5 after the second-and-later scaffolds.

---

## 8. Final checklist

- [ ] 10 gis-agent bundles installed and schema-valid.
- [ ] `style-bundle-pick` is bound to both scaffold skills.
- [ ] `_state/` is created on every scaffold with all four files.
- [ ] Diversity eval rejects clones and accepts genuinely different output.
- [ ] MapLibre walkthrough builds and previews cleanly.
- [ ] Leaflet walkthrough builds and previews cleanly.
- [ ] `_history/last5/` is being maintained.

When all seven pass, the app-dev capability is live. Proceed to R09-hosting-and-deployment to put the whole stack behind Caddy + Cloudflare Tunnel.
