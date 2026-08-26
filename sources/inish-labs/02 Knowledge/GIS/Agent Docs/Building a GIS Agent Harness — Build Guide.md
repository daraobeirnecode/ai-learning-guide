---
title: "Building a GIS Agent Harness — Build Guide"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Building a GIS Agent Harness — Build Guide

> [!tldr]
> Part of the GIS + AI Agents — Knowledge Base MOC. The GIS-specialized sequel to Building a Harness — Engineering Guide: that note builds a generic SQL-bot harness in ~600 lines; this one specifies what changes when the domain is spatial. Seven phases, each with a definition of done. The worked target is **"Surveyor"** — a GIS analyst harness over your real stack (local PostGIS + esri-mcp + GDAL + a geocoder) that can take "find all parcels within 500m of a school, rank by assessed value, map it" and return a verified answer with a rendered map. Concepts: [GIS Agent Harness — Core Components Guide](GIS%20Agent%20Harness%20%E2%80%94%20Core%20Components%20Guide.md). Platform detail: Agent Harnesses + Open Source GIS — Integration Guide, Agent Harnesses + ESRI Platform — Integration Guide.

---

## Phase 0 — Decide what you're building (one evening)

Three viable scopes, in ascending effort:

1. **Configuration harness** — don't write a loop at all; configure Hermes/Claude Code/Codex with your GIS MCP servers and context files. 90% of the value, 5% of the work. This is Configuring Hermes, Claude Code, and Codex for GIS — Guide, and you should do it *first* regardless — it teaches you what a custom harness must beat.
2. **Custom loop harness ("Surveyor")** — your own Python loop with GIS-aware context assembly, spatial verification, and tiered permissions; calls the same MCP servers. Build this when you need behavior the off-the-shelf harnesses can't give: spatial verification as a *hard* gate, per-client deployments, embedding in a product (your example risk-scoring product/SaaS directions).
3. **Multi-agent spatial system** — planner/SQL-writer/verifier agents (AI + GIS — Comprehensive Guide §2.1's Zhang et al. pattern). Only when single-agent demonstrably fails — past a few hundred tables or for product-grade NL→SQL.

The rest of this note builds scope 2, because scope 1 is documented elsewhere and scope 3 is scope 2 plus routing.

## Phase 1 — The toolbelt (week 1)

Stand up the tool layer *before* any loop code. Target inventory (≈12 tools — small enough to fit context comfortably, components guide §3.4):

```
describe_database        list tables, geometry columns, SRIDs, row counts
describe_table           fields, types, sample values, indexes
run_select               SELECT-only, LIMIT-injected, 10s timeout, geometry→centroid/bbox by default
geocode                  bias polygon required, returns confidence + in-bounds flag
arcgis_describe_layer    (esri-mcp, shipped)
arcgis_query_layer       (esri-mcp, shipped — truncation-aware)
arcgis_portal_search     (esri-mcp, shipped)
gdal_info                file metadata
gdal_transform           reproject/convert into scratch dir only
render_map               geojson/table → PNG via headless MapLibre or QGIS render
write_scratch            results → scratch schema / scratch GDB, returns handle
submit_gp_job/check_job  async geoprocessing pair
```

Build rules: every tool description states units, CRS behavior, cost, and limits (this is prompt engineering that lives in code — Template — GIS MCP Tool Description); every query tool has a describe sibling; every write lands in scratch unless explicitly elevated. Use FastMCP for the new servers — consistent with esri-mcp and instantly reusable by all three commercial harnesses.

**Done when:** from a bare Claude Code session with only these servers configured, the school-buffer question succeeds with no hand-holding.

## Phase 2 — The loop (week 2)

Standard agentic loop (per Building a Harness — Engineering Guide §3): receive → assemble context → call model → execute tools → repeat → respond. ~300 lines of Python with the Anthropic SDK (or LiteLLM for model-agnosticism). GIS-specific deltas:

- **Context assembly is spatial:** system prompt = SOUL-style identity + the *spatial context document* (SRIDs, schema map, conventions — Template — CLAUDE.md for GIS Repos content, programmatically injected) + tool list. Refresh the schema block from `describe_database` at session start, not hardcoded — schema drift is the silent killer.
- **Geometry payload guard in the dispatcher:** before any tool result enters context, measure it; >50KB → write to scratch, substitute `{handle, feature_count, bbox, crs}`. The model gets a *reference*, not the vertices.
- **Bounded loop:** max 25 tool calls per task, max $X per task (count tokens per Token Management — Comprehensive Guide), circuit breaker on 3 consecutive tool errors.

**Done when:** the loop answers the school-buffer question end-to-end with logs showing every tool call, token count, and cost.

## Phase 3 — Permissions (week 2–3, do not skip)

Implement the four tiers from the [components guide](GIS%20Agent%20Harness%20%E2%80%94%20Core%20Components%20Guide.md) §3.6 as a dispatcher gate, not as prompt text:

```python
TIERS = {"read": auto, "scratch": auto_logged, "prod_write": require_approval, "publish": require_approval_plus_dryrun}
```

Approval = the harness pauses, surfaces the exact operation (tool, args, target, row-count estimate from a dry-run `SELECT count(*)` / `returnCountOnly`), and waits for y/n — same approval-first philosophy as primary-agent (Hermes primary-agent Configuration Recap - Replicable Agent Setup). Log every decision. The model never knows the gate exists except as a tool error saying "requires approval — ask the user."

**Done when:** an UPDATE on the parcels table is impossible without an interactive yes, *even if the model is jailbroken*, because the gate is in code.

## Phase 4 — Spatial verification (week 3)

The component that makes a GIS harness worth custom-building. After the model drafts an answer involving spatial results, the harness runs a verification pass *before* releasing it:

1. **Mechanical checks (code, free):** result CRS known; geometries valid; result bbox ⊆ jurisdiction bbox; feature count > 0 and < table total; areas/lengths within plausibility bands for the stated units; geocodes above confidence threshold and in-bounds.
2. **Render-and-look (cheap):** `render_map` the result; attach the PNG to a second model call: "Does this map plausibly show X? List anomalies." Multimodal QA catches the buffer-in-degrees class of error instantly.
3. **On failure:** loop back with the failure report injected — "verification failed: result bbox is in Kansas" — max 2 retries, then surface the failure honestly.

**Done when:** you can inject a wrong-SRID bug into a query on purpose and the harness catches it without you.

## Phase 5 — Memory and skills (week 4)

- **Durable spatial facts** (MEMORY.md-equivalent): learned schema quirks, geocoder failure patterns, "assessor table updates Mondays." Append-and-curate, like Hermes memory.
- **Skills as procedures** (Template — GIS Agent Skill (SKILL.md)): parameterized runbooks — "weekly publication refresh," "EO change-detection pipeline" (STAC search → clip → Prithvi/Clay inference → vectorize → PostGIS → render). Load on demand by description match, Hermes-style, to keep per-request context lean.
- **Provenance:** every dataset the harness writes gets lineage metadata (source, tools, date, verification status) — this is what makes agent output defensible to a client or a county.

## Phase 6 — Observability and evaluation (ongoing)

Log per task: tokens in/out, cost, tool-call sequence, verification outcomes, wall time. Then build the eval set — 20–30 real questions over your Sacramento data with known answers (counts, specific parcels, areas). Run on every prompt/tool-description change; track pass rate. This is the Building a Harness — Engineering Guide fitness-test discipline applied spatially, and it's also your sales demo: "92% verified-correct on county benchmark" is a sentence clients understand.

## Phase 7 — Deployment shapes

- **Local/interactive:** CLI entry point, you in the loop — the development default.
- **Scheduled:** the same harness invoked by cron/Hermes for the publication workflow; approvals fall back to "queue and notify" (Telegram, like primary-agent) instead of blocking.
- **Service:** FastAPI wrapper, per-client config (different DB, different jurisdiction polygon, same code) — the SaaS shape. Add per-tenant cost caps and an audit endpoint before any client touches it.

## Common build mistakes

Building tools before trying scope 1 (you'll build the wrong tools); putting safety in the prompt instead of the dispatcher; returning geometries by default; hardcoding the schema in the system prompt; verification as an afterthought ("it ran" ≠ "it's right"); 100-tool servers when 12 well-described tools outperform; skipping the eval set so every change is vibes.

---

Next: Configuring Hermes, Claude Code, and Codex for GIS — Guide · Templates: Template — GIS MCP Tool Description, Template — GIS Agent Skill (SKILL.md), Template — GIS Agent Project Runbook
