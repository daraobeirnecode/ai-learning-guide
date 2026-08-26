---
title: "Master Codex Guide — The 20 Starter Prompts & Skills"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 04 — The 20 Starter Prompts & Skills

Codex's equivalent of the Claude skill library: **twenty versioned prompt templates** for Inish Labs work. Use them three ways: paste into `codex exec "..."`, pipe from file, or (⚠️ if your build supports it) mirror into `~/.codex/prompts/` as `/commands`. Each names its **profile**. Replace `[BRACKETS]`; the safety clauses are part of the template — don't trim them.

Every template inherits the global AGENTS.md contract: end with *what changed / files / tests run / risks / next step*.

---

## A. Orientation & review (profile: `safe` or `review`)

**1. `orient`** — *"Summarize this repo: purpose, architecture, entry points, how to run tests, and the three files that matter most. Make no changes."*

**2. `diff-review`** — *"Review the current git diff. Report every real issue with confidence + severity: correctness first, then security, then maintainability. Fix nothing. Do not expand scope. If the diff is clean, say so plainly."* (The second half of the Claude↔Codex cross-review.)

**3. `second-opinion`** — *"Read WORK-ORDER.md and the current diff (written by another AI agent). Independently assess: does the implementation satisfy the order? What would you have done differently and why? What's the one risk you'd fix before shipping? Make no changes."*

**4. `security-pass`** — *"Read-only security review of [path]: secrets in code, injection surfaces, unvalidated input at boundaries, anything bound to 0.0.0.0, permissive CORS. Report with file:line. No fixes."*

**5. `test-gap`** — *"Map test coverage against actual behavior in [module]: list the untested paths that could break silently, ranked by blast radius. Output a numbered test plan, no code."*

## B. Bounded implementation (profile: `builder`, usually `--full-auto`)

**6. `work-order`** — *"Read WORK-ORDER.md. Implement exactly what it specifies — nothing more. Run [test command] until green. Do not commit. Then report per the completion checklist."* (The heart of the pair pattern.)

**7. `python-script`** — *"Create scripts/[name].py: python3.12, typed, uv-compatible, a --dry-run mode, no secrets (read config from env), and a usage example in the docstring. [Task]. Run it in dry-run to prove it works."*

**8. `n8n-code-node`** — *"Write an n8n Code node: input via $input.first().json (or $input.all() — state which), return [{ json: ... }], no external deps. Task: [transform]. Include 3 test payloads and expected outputs as a comment."* (Your established template, kept.)

**9. `fastapi-endpoint`** — *"Add [route] to the FastAPI app following the existing router pattern: Pydantic in/out models, typed, tested with the same fixtures style as tests/. Run pytest. Do not commit."*

**10. `test-backfill`** — *"Write tests only — do not modify source. Cover the plan in TEST-PLAN.md (or the gaps you identify in [module]). Match the repo's existing test idiom. Run them; report pass/fail honestly."*

**11. `refactor-safe`** — *"Refactor [target] for [goal: clarity/duplication/typing]. Behavior must not change: run the test suite before and after and show both outputs. Small commits-worth of change only; stop and report if the tests were already red."*

**12. `bugfix`** — *"Bug: [symptom]. Expected: [behavior]. Reproduction: [steps/test]. Evidence: [log/trace]. Find the root cause FIRST and state it; then fix minimally; then add the regression test. Do not refactor around it."* (Your Bug/Expected/Repro/Evidence template, kept.)

## C. GIS + AI delivery (profile: `builder`)

**13. `geopandas-loader`** — *"Write a loader for [dataset]: GeoPandas read → reproject to EPSG:4326 → geometry validity fixes → stage table → atomic promote, idempotent re-runs. Follow the existing loaders' pattern in scripts/. Dry-run against the sample file in samples/."*

**14. `arcpy-migrate`** — *"Migrate [script.py] from ArcPy to GeoPandas/Shapely/PostGIS. Preserve behavior: build a paired test comparing outputs on the sample data with numeric tolerance [x]. Flag anything with no clean OSS equivalent instead of faking it. License-check any new dependency (flag GPL/AGPL)."* (The $9,500-Sprint engine.)

**15. `postgis-query`** — *"Write and explain the PostGIS SQL for: [question]. Use ST_ functions over Python loops; include the EXPLAIN and the index it needs. Read-only — run against the dev DB via the postgres MCP."*

**16. `spatial-op-port`** — *"Implement OP_REGISTRY op [name] per the contract in ops/near.py: typed input schema, provenance dict, tests. The op does [spatial behavior]. Run pytest tests/unit/ops/."*

## D. Business & content support (profile: `builder` / `safe`)

**17. `client-discovery-proto`** — *"Read client-brief.md. Produce: (1) an n8n workflow outline for their top pain, (2) the Code node from template #8 for the judgment step, (3) a QA checklist, (4) a handoff SOP in plain English. Mock data only — no external APIs."* (Your HVAC worked example, generalized.)

**18. `integrator-review`** — *"Act as a professional systems integrator reviewing this client prototype: where will it break at 10× volume, what's unclear in the handoff SOP, what would you refuse to ship? Report only."*

**19. `landing-polish`** — *"Polish this Vite/Astro page for production: semantic HTML, responsive at 360/768/1440, dark-mode audit, remove dead code, Lighthouse ≥95. Do not change the copy — it's brand-controlled. Run the build."*

**20. `runbook`** — *"Generate RUNBOOK.md for this repo from what's actually here (compose files, scripts, Makefile): what runs, how to start/stop/update it, where logs live, the 5 most likely failures and their fixes. Plain English, for a competent non-author."*

---

## Using the library

- **Store canonically** in the repo at `prompts/codex/` (and mirror to `~/.codex/prompts/` ⚠️ if supported) — versioned, reviewable, improvable like code.
- **Compose:** a full Codex working session is usually `1 → 6 → 2` (orient → work-order → self-review) — exactly the 7-step ritual from doc 02.
- **The three-times rule applies here too:** third time you type a variation of the same instruction, it becomes template #21.

---

*Next: [05 Ten Tutorials](05%20Ten%20Tutorials.md).*
