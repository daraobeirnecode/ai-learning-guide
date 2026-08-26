---
title: "Master Claude Guide — The 20 Starter Skills"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 04 — The 20 Starter Skills

Twenty skills purpose-built for Inish Labs work, ready to scaffold into `~/.claude/skills/` (personal, marked **P**) or the relevant repo's `.claude/skills/` (project, marked **R**). Two are written out in full as the pattern; the rest are specs — build each with `skill-creator` the first time you actually need it (*the three-times rule decides the order, not this list*).

**Install the foundation first:** `/plugin install anthropic-skills` (docx, pdf, pptx, xlsx, schedule, skill-creator).

---

## A. Infrastructure & delivery (the money-makers)

**1. `provision-client`** (R: infra repo) — Snapshot-clone a new client box on Hetzner, re-key secrets via SOPS, join Tailscale, compose up, smoke-test. Args: `[slug] [starter|pro]`. `allowed-tools: Bash(hcloud *), Bash(ssh *)`; `model: claude-fable-5`; `disable-model-invocation: true` (manual only — it spends money). *Full example in doc 03 §4.*

**2. `deploy-stack`** (R) — The `make up` ritual with verification: sync repo → decrypt secrets → compose up → healthchecks → status table. Fails loudly on any `0.0.0.0` binding.

**3. `snapshot-before`** (R) — Pre-change safety: quiesce → `hcloud server create-image` → resume → report snapshot ID + rollback command. Hook-paired: refuse risky ops without it.

**4. `backup-verify`** (R) — Run backup.sh now, then **restore into a throwaway container and prove tables exist**. Scheduled quarterly via the `schedule` skill.

**5. `audit-box`** (R) — Security sweep: public-port scan (`ss -tlnp` filter), backup freshness, disk %, pinned-tag drift, LiteLLM budget status. Output: pass/fail table. `context: fork`.

**6. `n8n-workflow`** (R) — Author/modify an n8n workflow as JSON against the catalog conventions (Postgres-backed, error-branch mandatory, credentials by name never value), import via CLI, run once, show execution log. Args: `[workflow-name]`.

**7. `hermes-skillpack`** (R) — Scaffold a Hermes skill for a client profile (MEMORY/SOUL conventions from your agent files), wire to LiteLLM key, test one task.

## B. GIS + AI delivery

**8. `spatial-op`** (R: gis repo) — Add a typed op to `OP_REGISTRY` (schema, provenance, tests) following `ops/near.py`. Enforces *the LLM never writes raw SQL*. `paths: platform/src/ops/**`.

**9. `layer-ingest`** (R) — Stage→QA→promote a spatial file into PostGIS: reproject to 4326, geometry validity, embed descriptors (Voyage), register in catalog. Args: `[file] [layer-name]`.

**10. `gis-health-audit`** (R) — The $1,500–3,500 product as a skill: read-only crawl of an ArcGIS org/open-data portal → stale/broken/metadata-risk inventory → client-ready PDF (via `pdf` skill). `agent: Explore` for the crawl.

**11. `arcpy-triage`** (P) — The Sprint's engine: classify an ArcPy codebase's scripts into migrate-clean / migrate-hard / leave, with effort estimates — the $9,500 deliverable's skeleton. `model: claude-opus-4-8`.

**12. `demo-seed`** (R) — Seed DEMO with a named city's open data (out-of-state list only — hard-coded guard), build the 311 Pulse page, verify tiles render.

## C. Business operations (dogfooding)

**13. `weekly-briefing`** (P) — Your own Monday brief: pipeline (CRM table), MRR, Langfuse cost/client, content calendar, top-3 actions. Runs via `schedule` every Monday 7am.

**14. `proposal`** (P) — Generate the ≤2-page, 3-option proposal from a discovery-call note, prices pulled from `03 Service Catalog & Pricing` — never invented. Args: `[client] [notes-file]`. Output: docx via `docx` skill.

**15. `invoice-chase`** (P) — Read Wave/Stripe exports, draft polite escalating reminders for >14/30/45-day invoices. `disable-model-invocation: true`.

**16. `client-value-report`** (P) — The retention weapon: monthly per-client report (workflows run, hours saved, spend vs cap) from n8n + Langfuse data, in brand voice.

## D. Content & brand

**17. `brand-check`** (P) — The guardrail: scan any draft for the 8 banned words, employer references, first-person-singular slips, and vague claims; return violations + rewrites. Stack it: `/brand-check /linkedin-post`.

**18. `linkedin-post`** (P) — Draft Mon/Wed/Fri posts from a vault artifact per the 9 templates in `08 Marketing Material` — concrete number + screenshot prompt + one CTA. Args: `[artifact-path] [mon|wed|fri]`.

**19. `case-study`** (P) — Turn an engagement's notes into the 5-beat case study (Situation → Did → Found → Changed → **Learned-confession**), 400–600 words, `/work` MDX + PDF.

**20. `seo-essay`** (P) — Expand a vault doc into a 1,500-word `/writing` essay in the editorial voice, with the target query in title + headings. Feeds the website's SEO program.

---

## Worked example #2 (business-side pattern — `proposal`)

```markdown
---
name: proposal
description: Generate an Inish Labs client proposal (2 pages, 3 options) from
  discovery-call notes. Use after any discovery call.
argument-hint: "[client-name] [path-to-notes]"
allowed-tools: Read, Write, Bash(pandoc *)
---
## Price card (authoritative — never invent a number)
!`sed -n '/## Service/,/## Quoting/p' "docs/pricing.md"`

# Steps
1. Read $1. Extract: pain (their words), systems named, timeline, budget signals.
2. Build 3 options (A diagnostic / B build / C build+retainer) using ONLY prices above.
3. Render via the docx skill from ${CLAUDE_SKILL_DIR}/template.docx.
4. Include the what-you-keep isolation paragraph verbatim from 07 Website Content.
5. Terms: 50% upfront, 7-day validity. Flag anything out-of-catalog for manual pricing.
```

## Build order (first month)

Week 1: **17, 18** (content engine — daily use) · Week 2: **2, 5, 13** (ops) · Week 3: **6, 14** (first client motions) · Week 4: **1, 3, 4** (delivery). The rest when their third repetition arrives.

---

*Next: [05 Ten Tutorials](05%20Ten%20Tutorials.md) — where you build several of these hands-on.*
