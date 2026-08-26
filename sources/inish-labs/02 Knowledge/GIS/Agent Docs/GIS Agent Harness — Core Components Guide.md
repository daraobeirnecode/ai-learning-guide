---
title: "GIS Agent Harness — Core Components Guide"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# GIS Agent Harness — Core Components Guide

> [!tldr]
> Part of the GIS + AI Agents — Knowledge Base MOC. This note is the *conceptual map*: every component you need to understand before wiring an agent harness (Hermes, Claude Code, Codex, or your own) to a GIS platform — open source or ESRI. It assumes Building a Harness — Engineering Guide (the ten generic harness components) and AI + GIS — Comprehensive Guide (the market/workflow view) and adds the GIS-specific layer on top. The build instructions live in [Building a GIS Agent Harness — Build Guide](Building%20a%20GIS%20Agent%20Harness%20%E2%80%94%20Build%20Guide.md); per-tool configuration lives in Configuring Hermes, Claude Code, and Codex for GIS — Guide.

---

## 1. The mental model

A GIS agent system is three stacked layers, and confusion almost always comes from mixing them up:

1. **The model** — Claude, GPT-5, Hermes 4, etc. Stateless. Knows general GIS concepts (projections, ST_DWithin, ArcPy syntax) but knows *nothing* about your data, your SRIDs, your portal, or your conventions.
2. **The harness** — the runtime loop around the model: context assembly, tool dispatch, permissions, memory, retries, cost caps. Claude Code, Codex CLI, and Hermes Agent are all general-purpose harnesses. See Harness Engineering — Practitioner Handbook.
3. **The GIS tool layer** — adapters that translate between "model-friendly JSON" and actual GIS systems: MCP servers (your esri-mcp, qgis-mcp, gdal-mcp, postgis-mcp), CLI tools the agent shells out to (ogr2ogr, gdalwarp), and Python libraries the agent writes code against (ArcPy, GeoPandas, Shapely).

The model never touches GIS directly. The harness never understands geometry. All spatial intelligence in the *system* comes from how well the tool layer describes itself and how well the context layer teaches the model your local conventions. This is why two people with identical models get wildly different results: the difference is layers 2 and 3.

## 2. The three integration patterns

Every GIS-agent integration on either platform reduces to one of three patterns. Know all three; pick deliberately.

### Pattern A — MCP tools (structured, safe, narrow)

The GIS system is wrapped in an MCP server exposing named tools with JSON schemas (`query_layer`, `geocode`, `clip_raster`). The agent calls tools; the server validates and executes. This is what esri-mcp does for ArcGIS REST, what [qgis-mcp](https://github.com/nkarasiak/qgis-mcp) does for QGIS Desktop (~102 tools), what [gdal-mcp](https://github.com/JordanGunn/gdal-mcp) does for raster/vector processing, and what [postgis-mcp](https://github.com/receptopalak/postgis-mcp) does for spatial SQL.

- **Strengths:** permission gating per tool, schema validation, works identically across Hermes/Claude Code/Codex, auditable.
- **Weaknesses:** every capability must be pre-built; long-tail requests hit a wall; tool sprawl bloats context (100+ tools = real token cost).
- **Use when:** non-developers will drive the agent, writes need gating, or the surface area is well-known (query/geocode/search).

### Pattern B — Code execution (flexible, powerful, riskier)

The agent writes and runs code: ArcPy in a Pro Python window or scheduled script, GeoPandas/Rasterio/Shapely in a venv, PyQGIS in the QGIS console, raw SQL against PostGIS, ogr2ogr/gdal CLI invocations. Claude Code and Codex are *built* for this pattern; Hermes does it via its terminal tool.

- **Strengths:** unlimited surface area — anything the library can do, the agent can do; the agent can debug its own errors; no adapter to maintain.
- **Weaknesses:** side-effects are only as safe as the sandbox; ArcPy errors are cryptic; a hallucinated `arcpy.management.Delete` is catastrophic without guardrails.
- **Use when:** you (a GIS professional) are in the loop reviewing, the task is novel analysis or one-off ETL, or you're building/maintaining the tool layer itself.

### Pattern C — Platform-native assistants (zero-build, vendor-bound)

The vendor embeds the assistant: ArcGIS Pro's AI assistants (NL → geoprocessing tools, ArcPy generation), AI assistants in ArcGIS Online/Survey123, QGIS plugins like QGPT Agent and GeoAgent. You configure, not build.

- **Strengths:** zero integration work, vendor-supported, UI-aware.
- **Weaknesses:** no custom tools, no cross-system orchestration, no harness control, telemetry/licensing constraints.
- **Use when:** quick wins inside one app; demos; users who will never leave Pro.

**The real answer for serious work is A + B together**: MCP tools for the safe, common, gateable operations; code execution for the long tail — inside one harness that has both.

## 3. The GIS-specific components

Building a Harness — Engineering Guide gives the ten generic components (model client, loop, tool dispatch, memory, permissions, observability, etc.). GIS adds eight concerns that generic harness writing never mentions:

### 3.1 Spatial context documents

The single highest-leverage artifact. A markdown file (CLAUDE.md / AGENTS.md / Hermes context — see Hermes Markdown Context Files Guide) that teaches the model your *local spatial truth*: which SRIDs your data uses (and that California State Plane Zone 2 is EPSG:2226, in US survey feet), which geocoder to trust, what an APN looks like in your county, which layers are authoritative versus derived, and units conventions. Models guess wrong on all of these by default, and they guess *confidently*. Template: Template — CLAUDE.md for GIS Repos.

### 3.2 Schema/metadata introspection

The agent must be able to *discover* data before querying it: PostGIS `information_schema` + `geometry_columns`, ArcGIS REST layer JSON (fields, geometryType, maxRecordCount), STAC for imagery, GDAL `info` for files. Rule: every query tool gets a sibling describe tool, and the system prompt tells the agent to describe before querying. Skipping this is the #1 cause of hallucinated field names.

### 3.3 CRS and unit discipline

The classic failure: model buffers by "500" in degrees because the layer is EPSG:4326, producing a 55 km buffer. The harness must make CRS explicit at every boundary — tools return CRS with every geometry payload, accept an explicit `crs` parameter, and refuse mixed-CRS operations rather than silently transforming. Put the rule in context *and* enforce it in the tool layer; context alone fails ~5% of the time, which is too often for parcels.

### 3.4 Geometry payload management

Geometries are huge. A county parcel layer as GeoJSON will blow any context window. The tool layer must default to: return counts and attributes, not geometries; return bounding boxes or centroids unless full geometry is requested; cap feature counts (esri-mcp's record-limit awareness); offer "write result to file/table and return the path" for anything big. An agent that pulls 50k vertices into context is burning money to get dumber.

### 3.5 The visual feedback loop

Unique to GIS: the agent can *look at the map*. A `screenshot_map` / render tool (qgis-mcp has render; MapLibre + headless browser works for web maps) turns a multimodal model into its own QA inspector — "render the result, check the buffer actually covers the school sites." This catches whole classes of silent spatial errors that attribute checks never would. Cheap to build, disproportionate payoff.

### 3.6 Spatial write gating

GIS writes are uniquely destructive: `applyEdits` on the authoritative parcel layer, an UPDATE without WHERE on a geometry column, overwriting a published service. The permission model needs GIS-aware tiers:

| Tier | Operations | Gate |
|---|---|---|
| Read | query, describe, geocode, render, export to scratch | none |
| Sandbox write | scratch schemas, temp file GDBs, local files | none or log-only |
| Production write | applyEdits, INSERT/UPDATE on authoritative tables, file overwrite | explicit approval per call |
| Publish/admin | publish services, delete layers, schema changes, share items | approval + dry-run diff |

esri-mcp's read-only-by-design + `ESRI_MCP_ALLOW_WRITES` env gate is the right v1 instinct; the table above is where it goes next.

### 3.7 Spatial verification

Generic harness verification is "did the code run." GIS verification is "is the answer *spatially* sane": feature counts within expected ranges, geometries valid (`ST_IsValid`), results within the jurisdiction bbox, areas/lengths plausible for the units, geocode confidence above threshold and inside the expected polygon. Build these as cheap checks the agent is instructed to run before reporting, plus hard assertions in write paths.

### 3.8 Long-running geoprocessing

Buffering a state's parcels or mosaicking imagery takes minutes-to-hours; tool calls can't block that long. Patterns: submit-and-poll (ArcGIS GP services are natively async — submit job, return job id, poll status tool), background process + status file for local GDAL/ArcPy jobs, or the harness's own scheduling (Hermes cron, see Agentic Ways to Use primary-agent - Long Running Work).

## 4. Platform component inventory

What you actually need to understand on each side. Depth on each lives in the two platform notes.

**Open source** (Agent Harnesses + Open Source GIS — Integration Guide): PostGIS (the spatial brain — NL→SQL is the killer workflow), GDAL/OGR (the universal converter — CLI for agents that shell out, gdal-mcp for structured access), QGIS Desktop + PyQGIS (qgis-mcp for desktop automation), GeoPandas/Shapely/Rasterio/PyProj (the code-execution stack), GeoServer/pg_tileserv (publishing), STAC + stac-mcp (imagery discovery), MapLibre (rendering/screenshots), Nominatim/Pelias (geocoding).

**ESRI** (Agent Harnesses + ESRI Platform — Integration Guide): the ArcGIS REST API (everything is REST underneath — this is why esri-mcp works), ArcGIS API for Python (`arcgis` package — the code-execution stack for AGOL/Enterprise), ArcPy (Pro-licensed geoprocessing — the deep automation layer), ArcGIS Pro AI assistants (Pattern C), Esri's announced ArcGIS MCP server (coming later in 2026 — watch this, it may obsolete parts of community servers), tokens/OAuth/IWA auth (the eternal ESRI integration tax), and licensing boundaries (what ArcPy needs Pro for vs. what the Python API does free).

## 5. How the harnesses differ for GIS work

| | Hermes Agent | Claude Code | Codex CLI |
|---|---|---|---|
| Nature | Persistent personal agent (profiles, SOUL.md, memory, cron, Telegram) | Repo-centric coding agent | Repo-centric coding agent |
| Context file | SOUL.md / MEMORY.md / HERMES.md / reads AGENTS.md+CLAUDE.md too | CLAUDE.md (global + project, concatenating) | AGENTS.md (global + per-dir, override chain) |
| MCP wiring | profile config / dashboard | `.mcp.json` / `claude mcp add` | `~/.codex/config.toml` `[mcp_servers.*]` |
| Skills | SKILL.md, self-authored via skill_manage | Skills + slash commands + plugins | Prompts/AGENTS.md guidance |
| Best GIS role | Scheduled spatial ops: nightly ETL, monitoring, briefings, publication workflow | Building the tool layer + interactive analysis | Second opinion / parallel builder, same MCP servers |
| Long-running | Native (cron, sessions) | Background tasks, but session-bound | Session-bound |

Key insight: **they share the tool layer**. One esri-mcp + one postgis-mcp + one gdal-mcp serves all three harnesses; the per-harness work is just config and context files. Build tools once, configure thrice. Full detail: Configuring Hermes, Claude Code, and Codex for GIS — Guide.

## 6. Failure modes to design against

- **Hallucinated field names** → introspection tools + "describe before query" rule (§3.2).
- **CRS/unit confusion** → explicit CRS at every boundary (§3.3).
- **Context flooding by geometry** → payload caps and file-handoff (§3.4).
- **Silent wrong geocodes** → jurisdiction biasing + confidence thresholds (see AI + GIS — Comprehensive Guide §2.2).
- **Destructive writes** → tiered gating (§3.6).
- **Plausible-but-wrong analysis** — the model produces a beautiful map of the wrong thing → spatial verification (§3.7) + render-and-look (§3.5).
- **Stale schema drift** — DB changes, context file doesn't → schedule a Hermes job to re-introspect weekly and diff against the context doc.

## 7. Reading order

1. This note (concepts)
2. Agent Harnesses + Open Source GIS — Integration Guide and Agent Harnesses + ESRI Platform — Integration Guide (platform specifics)
3. [Building a GIS Agent Harness — Build Guide](Building%20a%20GIS%20Agent%20Harness%20%E2%80%94%20Build%20Guide.md) (build it)
4. Configuring Hermes, Claude Code, and Codex for GIS — Guide (wire your three harnesses)
5. Templates in `GIS Agent Templates/` (copy-paste starting points)

---

**Sources:** [qgis-mcp (nkarasiak)](https://github.com/nkarasiak/qgis-mcp) · [gdal-mcp](https://github.com/JordanGunn/gdal-mcp) · [postgis-mcp](https://github.com/receptopalak/postgis-mcp) · [arcgis-location-services-mcp](https://github.com/lwsinclair/arcgis-location-services-mcp) · [ArcGIS Pro MCP Add-In (nicogis)](https://github.com/nicogis/MCP-Server-ArcGIS-Pro-AddIn) · [Esri: Understanding MCP and A2A for GIS Practitioners](https://mediaspace.esri.com/media/Understanding%20MCP%20and%20A2A:%20A%20Primer%20for%20GIS%20Practitioners/1_zi7zn935) · [Hermes Agent docs](https://hermes-agent.nousresearch.com/docs/) · [Codex config reference](https://developers.openai.com/codex/config-reference)
