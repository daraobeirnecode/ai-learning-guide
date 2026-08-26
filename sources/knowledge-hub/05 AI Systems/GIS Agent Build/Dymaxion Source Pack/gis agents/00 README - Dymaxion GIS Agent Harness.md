---
title: "Dymaxion — GIS Agent Harness"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Dymaxion — GIS Agent Harness

Dymaxion is a long-running agent that conducts advanced ESRI and Open Source GIS work on your behalf. Configurable across any LLM you set up. Persistent memory. Ships with a real skill library of 40+ GIS skills. Can author new skills when it encounters problems it doesn't already have a skill for (with your approval). Can design web + mobile mapping applications. Reaches you through Telegram, Microsoft Teams, email, Slack, and CLI. Wraps your Esri MCP, cli-anything-qgis, and CLI-Anything-Arcgis-Pro as first-class tools.

Named for Buckminster Fuller's Dymaxion Map — the 1943 projection that unwraps the globe onto an icosahedron so every landmass reads as a single connected island with minimal distortion. Fuller solved the projection problem cartographers actually had. The tool exists to solve the projection problems you actually have.

## What this package is

Ten files. Read them in the order below. Then paste the Fable 5 Prompt into a fresh Fable 5 workspace and let it build.

1. **`00 README - Dymaxion GIS Agent Harness.md`** (this file) — orientation, top-level architecture, decision context
2. **`Design Guide.md`** — philosophy, capabilities, boundaries, non-negotiables
3. **`Full Product Spec.md`** — every component, every schema, every module — the technical architecture
4. **`Skills Library.md`** — the initial 40+ skill catalog (ESRI + OSS GIS + web/mobile + architecture + meta)
5. **`Knowledge Base.md`** — reference material to preload so the agent knows the GIS landscape from day one
6. **`Gateways Integration.md`** — Telegram, Teams, Email, Slack integration specs
7. **`Windows Worker.md`** — Windows-side installer + ArcGIS Pro CLI + arcpy integration (Sprint 1)
8. **`Framework Decision.md`** — Mastra + Vercel AI SDK + openid-client selection reasoning
9. **`CLAUDE.md`** — repo conventions for iteration after Fable 5's scaffold
10. **`Fable 5 Prompt.md`** — the paste-ready master prompt

## The core design decisions

**1. Multi-LLM by design.** Every LLM call routes through LiteLLM. You configure the provider set in one YAML file. Add Anthropic, OpenAI, Google, Ollama-local, or anything else LiteLLM supports. Change primary and fallback per skill.

**2. Persistent memory in Postgres + pgvector.** Long-running conversations, past skill invocations, per-project context, learned preferences — all persist. Nothing is re-explained.

**3. Real skills, not just prompts.** Skills are folders with a `SKILL.md`, a `manifest.yaml` (dependencies, timeouts, cost caps), and executable scripts. Skills invoke real tools (arcpy, GDAL, QGIS CLI, ArcGIS REST API, PostGIS) not just LLM calls.

**4. The agent can author its own skills.** When it hits a problem no existing skill covers, it can draft a new one. Drafts land in `skills/proposed/` for your review. Approved drafts move to `skills/active/` and become part of the library.

**5. Wraps your Esri MCP + CLI tools as first-class.** `github.com/your-github-account/esri-mcp` is configured as an MCP server the agent uses. `github.com/opengeos/cli-anything-qgis` and `github.com/Jasper0122/CLI-Anything-Arcgis-Pro` are installed as CLI tools with pre-built skill wrappers.

**6. ArcGIS Pro is first-class in Sprint 1.** Three install topologies: **(A) Windows-only** — one Windows machine runs everything, WSL2 Docker for the main runtime + native Windows Worker for arcpy + ArcGIS Pro CLI. **(B) Split** — macOS workstation runs the main runtime, Windows laptop runs the Windows Worker, communicate over Tailscale. **(C) Linux/Mac + optional Windows** — main runtime on Linux/Mac, ArcGIS Pro skills disabled unless you connect an optional Windows Worker. See `Windows Worker.md` for the install.ps1 script + REST API. For 10 of 14 ESRI skills (`arcgis` Python API-based), the Windows Worker isn't needed at all.

**7. Multi-gateway.** Same agent, multiple channels. Telegram for personal use. Microsoft Teams for organizational use. Email for structured deliverables. Slack for team notifications. CLI for direct developer control. Web UI for the browser-preferring.

**8. Employer boundary baked in.** No a municipal government data or systems. Ever. Enforced structurally (allow-list of data sources, block-list of hostnames).

**9. Cost caps everywhere.** Per-skill LiteLLM virtual key with monthly USD cap. Runaway workflow never costs more than the cap.

**10. Audit trail.** Every LLM call, every tool invocation, every file touched — logged in Postgres + LangFuse. Debuggable a month later. Defensible to a client.

## The top-level architecture (200-foot view)

```
                            YOU
                             │
      ┌──────┬──────┬────────┼────────┬──────┬──────┐
      │      │      │        │        │      │      │
      ▼      ▼      ▼        ▼        ▼      ▼      ▼
   Telegram Teams  Email    CLI    Web UI  Slack  ArcGIS
                                                   Portal
      │      │      │        │        │      │      │
      └──────┴──────┴────────┼────────┴──────┴──────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   DYMAXION      │
                    │   Agent Runtime │
                    └────────┬────────┘
                             │
     ┌────────────┬──────────┼──────────┬────────────┐
     ▼            ▼          ▼          ▼            ▼
  LiteLLM     Postgres    Skills      MCP         CLI Tools
  Gateway     +pgvector   Registry    Servers     (subprocess)
     │        (memory)       │           │            │
     ▼                       ▼           ▼            ▼
  Any LLM              40+ ESRI/OSS   Esri MCP    QGIS CLI
  (Anthropic,          GIS +          Postgres     ArcGIS Pro
   OpenAI,             web/mobile     MCP          CLI (via
   Google,             + architecture Filesystem   Windows
   Ollama,             skills, plus   MCP          Worker)
   ...)                self-authored                GDAL
                                                    ogr2ogr
```

## The stack

**Agent framework: Mastra (TypeScript).** TypeScript-native agent framework with built-in agents, workflows, memory, and evals. Uses Vercel AI SDK under the hood for LLM provider abstraction (30+ providers). Runs on Node.js 20+ on any Mac or Linux host. See `Framework Decision.md` for the reasoning against LangGraph, CrewAI, and building from scratch.

- **Runtime**: TypeScript / Node.js 20+ daemon built on Mastra
- **LLM providers**: Vercel AI SDK abstraction — Anthropic (API key), OpenAI (OAuth), Google Gemini (OAuth), Azure OpenAI (OAuth), Cohere (OAuth), Ollama (no auth), plus any Vercel-AI-SDK-supported provider
- **OAuth middleware**: `openid-client` npm package handles OAuth 2.0 with PKCE for every non-Anthropic provider. Tokens encrypted at rest in Postgres. Auto-refresh on expiry.
- **Cost tracking + budget caps**: custom middleware wrapping every LLM call. Per-skill virtual budgets stored in Postgres; enforced pre-call.
- **Memory**: Postgres 18 with pgvector, AGE (graph), pg_trgm — via Mastra's memory abstraction with a custom Postgres adapter
- **Embeddings**: Voyage `voyage-3-large` (1024-dim) by default; configurable per skill
- **MCP client**: `@modelcontextprotocol/sdk` (official TypeScript SDK). Spawns MCP servers as subprocesses; Mastra tool integration.
- **Skill executor**: Mastra's tool/agent registry with a filesystem loader. Docker sandbox for proposed (unapproved) skills; direct subprocess for approved skills.
- **Gateway adapters**: One per channel (telegram, teams, email, slack, cli, web). Common interface implemented per adapter.
- **Observability**: LangFuse (self-hosted); Postgres audit log
- **Deploy target**: Docker Compose on macOS workstation (primary), Linux Hetzner AI OS (secondary), or any Docker-capable host
- **Cross-platform**: multi-arch images (amd64 + arm64) — Apple Silicon works natively, Linux x86_64 works natively
- **Windows Worker (optional, Sprint 2+)**: Node.js service on Windows laptop for ArcGIS Pro CLI + arcpy; communicates over Tailscale

## Install (Sprint 1)

Choose per platform:

**macOS or Linux** (single command):
```bash
curl -fsSL https://raw.githubusercontent.com/your-github-account/dymaxion/main/install.sh -o /tmp/dymaxion-install.sh
less /tmp/dymaxion-install.sh
bash /tmp/dymaxion-install.sh
```

**Windows** (PowerShell as Administrator):
```powershell
Invoke-WebRequest https://raw.githubusercontent.com/your-github-account/dymaxion/main/install.ps1 -OutFile $env:TEMP\dymaxion-install.ps1
Get-Content $env:TEMP\dymaxion-install.ps1
& $env:TEMP\dymaxion-install.ps1
```
On Windows the installer sets up WSL2 Ubuntu (if not already present) + Docker Desktop for the main runtime, THEN registers the Windows Worker as a native Windows Service so ArcGIS Pro CLI + arcpy skills work from day one.

**Git clone** (any platform, inspect first):
```bash
git clone https://github.com/your-github-account/dymaxion ~/dymaxion
cd ~/dymaxion && ./setup.sh   # or .\setup.ps1 on Windows
```

Both flows:
1. Check prerequisites (Docker, Node 20+, git, curl) — install missing ones on macOS via Homebrew if approved
2. Prompt for essential env vars (Anthropic key, Telegram bot token, Voyage key)
3. Generate `.env` with strong defaults for everything else
4. Run `docker compose up -d`
5. Apply Postgres migrations
6. Register initial skill catalog
7. Load knowledge base
8. Verify healthchecks
9. Print Telegram + admin dashboard URLs

Typical time: 10 minutes on a warm machine, 25 minutes on a cold one (image pulls).

## What you'll have after Fable 5's Sprint 1

A working Dymaxion installation on your macOS workstation that:

- Accepts messages via Telegram (default gateway)
- Default routing points at your configured `workhorse-tier` model — Claude Sonnet 4.6 in the shipped defaults, but freely swappable to OpenAI GPT-4o, Google Gemini 2.5 Pro, or any Ollama model based on which providers you connected
- Has all 40+ initial skills registered
- Can invoke your Esri MCP + QGIS CLI + arcpy
-
