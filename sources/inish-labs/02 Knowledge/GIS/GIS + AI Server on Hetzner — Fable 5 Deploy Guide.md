---
title: "GIS + AI Server on Hetzner — Fable 5 Deploy Guide"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# GIS + AI Server on Hetzner — Fable 5 Deploy Guide

**The single, end-to-end walkthrough** for deploying a full **AI + GIS server** on one Hetzner box, driven by **Claude Code (Fable 5)** from your macOS workstation. It runs **n8n, Hermes, Claude Code, Codex, PostGIS, and Spatial RAG** as one integrated spatial-intelligence platform.

> **Relationship to the base guide.** This is the GIS-specialised sibling of [AI Automation Master Guide deploy](../AI%20Automation/AI%20Automation%20Master%20Guide%20deploy.md). That guide covers the *generic* mechanics in depth — Hetzner account/SSH keys, Tailscale, OS hardening, Cloudflare Tunnel, backups, snapshots/cloning, the Claude-Code-from-Mac-mini workflow. **This guide assumes those and focuses on the GIS + Spatial-RAG layer**, but repeats the load-bearing steps so you can follow it start-to-finish. Where it says "as in the base guide," open that doc for the detail.

> **A reconciliation up front.** Your vault contains two build lineages: (A) a **Docker Compose** stack (the *Ultimate Build Guide* + *GIS+AI Stack Template*, which hold the verbatim, paste-ready config) and (B) a **native-install / systemd + Ansible provisioner** (the *Hetzner Deploy Fable 5 Master Prompt* + *GIS AI Ops Platform* guide). **This guide standardises on lineage A (Docker Compose)** — it's reproducible in one file, matches the base guide, and has the real config. The Ansible/systemd path is noted at the end as an alternative; the two don't co-deploy — pick one.

Sources distilled here: GIS + AI Stack — The Ultimate Build Guide (verbatim compose/init.sql/LiteLLM), Spatial RAG with Claude Code — Complete Build Guide + Spatial Graph RAG — Implementation Plan (Open Source) (Spatial RAG), GIS-AI Hybrid App - Esri MCP + Spatial RAG + Live Feature Services - Fable 5 Build + the Civic Spatial Intelligence Console docs (Esri MCP), GIS AI Operations Platform — Complete Claude Code Build Guide + Hetzner Deploy - GIS + Hermes + n8n + Claude Code - Fable 5 Master Prompt (Fable 5 orchestration).

---

## Contents

1. What you're building (architecture)
2. The stack at a glance
3. Prerequisites & the Fable 5 build philosophy
4. Phase 1 — Provision the box (CCX23) + secure it
5. Phase 2 — Repo & secrets (SOPS + age)
6. Phase 3 — The data core: PostGIS 18 + pgvector + Apache AGE
7. Phase 4 — The service stack (LiteLLM, n8n, Langfuse, pg_tileserv, Hermes)
8. Phase 5 — Claude Code + Codex on the box
9. Phase 6 — The MCP layer (esri, postgres, composio, gisops)
10. Phase 7 — Spatial RAG (the GIS brain)
11. Phase 8 — Esri MCP + live feature services
12. Phase 9 — Tile serving + the geospatial Python env
13. Phase 10 — Ingress (Cloudflare Tunnel) & when you need DNS
14. Phase 11 — Backups & snapshots
15. The Fable 5 build orchestration (paste-ready prompts + sprint sequence)
16. Verification checklist
17. Security
18. Cost
19. Alternative lineage & related

---

## 1. What you're building

One Hetzner **CCX23** (dedicated vCPU) running a Docker Compose stack where **one Postgres/PostGIS instance is the spine** — it holds spatial data, vector embeddings (pgvector), and a property graph (Apache AGE) in a single database. Everything else orbits it. Claude Code (Fable 5) on the macOS workstation builds and operates it over Tailscale.

```
              macOS workstation (you)                              Hetzner CCX23  (example-gis-server)
  ┌──────────────────────────────┐        Tailscale       ┌───────────────────────────────────────────┐
  │ Claude Code (Fable 5) ────────┼──── SSH / Remote-SSH ──┼─► Docker Compose:                          │
  │ Codex CLI                     │       (no public 22)   │    ┌─────────────────────────────────────┐ │
  │ hcloud CLI                    │                        │    │ postgres  (PostGIS 18 + pgvector +   │ │
  │ .mcp.json → esri/gisops/…     │                        │    │           Apache AGE) — THE SPINE     │ │
  └──────────────────────────────┘                        │    └─────────────────────────────────────┘ │
                                                           │      • litellm    (model router + caps)    │
  Public inbound (only when needed):                       │      • n8n         (spatial workflows)     │
  Cloudflare Tunnel ─► n8n webhooks / Spatial-RAG API      │      • hermes      (agent runtime)         │
                                                           │      • spatial-rag (FastAPI + FastMCP)     │
                                                           │      • langfuse    (LLM traces)            │
                                                           │      • pg_tileserv (vector tiles)          │
                                                           │      • code-server (browser VS Code)       │
                                                           │      • cloudflared (outbound tunnel)       │
                                                           │    + Claude Code & Codex installed on box  │
                                                           │    + MCP servers: esri, postgres,          │
                                                           │      composio, gisops (spatial ops)        │
                                                           └───────────────────────────────────────────┘
```

**The core principle (from the Spatial RAG guides):** *there is no separate vector store, no separate graph store, no separate spatial store — everything sits inside one Postgres instance.* PostGIS reasons over geometry, pgvector does semantic recall, Apache AGE does multi-hop graph traversal, and the Spatial-RAG service fuses all three. **Esri MCP connects; Spatial RAG reasons.**

---

## 2. The stack at a glance

| Service | Image / tool | Port (Tailscale-only) | Role |
|---|---|---|---|
| **postgres** | `postgis/postgis:18-3.5` | `127.0.0.1:5432` | PostGIS + pgvector + Apache AGE — spatial + vector + graph in one DB |
| **litellm** | `ghcr.io/berriai/litellm:main-stable` | `127.0.0.1:4000` | Model router, prompt cache, per-key budget caps |
| **n8n** | `n8nio/n8n:1.95.0` | `127.0.0.1:5678` | Spatial workflows, scheduled data refresh, webhooks |
| **hermes** | `nousresearch/hermes-agent:latest` | `127.0.0.1:8000` | Agent runtime (profiles), routed through LiteLLM |
| **spatial-rag** | built locally (FastAPI + FastMCP) | `127.0.0.1:8001` | Hybrid spatial-graph-vector retrieval + `/mcp` |
| **langfuse** | `langfuse/langfuse:2` | `127.0.0.1:3000` | LLM/agent observability |
| **pg_tileserv** | `pramsey/pg_tileserv:latest` | `127.0.0.1:7800` | Dynamic vector tiles from PostGIS |
| **redis** | `redis:7-alpine` | `127.0.0.1:6379` | LiteLLM cache + Celery/queue (fills a gap in the source config) |
| **code-server** | `lscr.io/linuxserver/code-server:latest` | `127.0.0.1:8443` | Browser VS Code + on-box Claude Code terminal |
| **cloudflared** | `cloudflare/cloudflared:2026.5.0` | (dials out) | Public ingress for the few things that must be public |

Plus, **installed on the host** (not containers): Claude Code, Codex, the geospatial Python env (GDAL/GeoPandas), and the MCP servers (`esri`, `postgres`, `composio`, `gisops`).

> **Model IDs:** the source docs were written against older tags (sonnet-4-6/opus-4-6/4-7). This guide uses current IDs: **`claude-fable-5`** (build), **`claude-opus-4-8`** (hard planning), **`claude-sonnet-5`** (daily driver / synthesis), **`claude-haiku-4-5`** (subagents/batch). Embeddings: **Voyage `voyage-3-large` (1024-dim)** to match the `VECTOR(1024)` schema.

---

## 3. Prerequisites & the Fable 5 build philosophy

**Accounts:** Hetzner Cloud, Anthropic (API key), OpenAI (Codex + optional GPT routing), **Voyage AI** (embeddings), **Esri Developer** (ArcGIS API key) or ArcGIS Online org, GitHub, Cloudflare (+ a domain on Cloudflare NS when you go public), **Composio** (per-tenant ArcGIS/Gmail brokerage — optional but the vault's production auth path), Bitwarden, Backblaze B2/Hetzner Storage Box.

**On the macOS workstation** (as in the base guide, §4): `brew install hcloud sops age tailscale git node`, `npm install --global @anthropic-ai/claude-code@2.1.246 @openai/codex@0.150.0`, generate the SSH keypair.

**The Fable-5-first doctrine** (from both GIS build guides): drive the build with the most capable model, dropping to cheaper models per task —

```bash
claude --model claude-fable-5     # multi-file scaffolds, the whole build
# per-task: opus-4-8 = hard planning/prompt design · sonnet-5 = daily code · haiku-4-5 = subagents/batch
```

Fable 5 is always-on-thinking and excels at long-horizon, multi-file scaffolding — exactly this job. Each phase below has a paste-ready **⌘ Fable 5 prompt**; §15 has the two big master prompts and the full sprint sequence.

---

## 4. Phase 1 — Provision the box (CCX23) + secure it

**Why CCX23 (not CX32):** GIS + embeddings + AGE graph + Hermes is compute-heavy; **dedicated** vCPU (CCX line) avoids the noisy-neighbour stalls of shared CX during spatial joins and embedding batches. CCX23 = 4 dedicated vCPU / 16 GB / 160 GB (~€30/mo). Scale to CCX33 (8 vCPU/32 GB) when parcel counts or tenants grow. Attach a Hetzner Volume for `pgdata` if the DB outgrows the boot disk.

```bash
hcloud context create gis-ai                    # paste your Read&Write API token
hcloud server create \
  --name example-gis-server --type ccx23 --image ubuntu-24.04 --location nbg1 \
  --ssh-key example-admin-ed25519 --label env=prod --label project=gis-ai
hcloud server ip example-gis-server
```

Then **harden + Tailscale exactly as the base guide §6–§7**: create the `adminuser` sudo user, disable root/password SSH, install Tailscale (`sudo tailscale up --ssh`), bind SSH to the Tailscale IP, and set the Hetzner firewall to `ufw default deny incoming` + allow only `tailscale0` (plus 41641/udp for Tailscale; 80/443 stay closed — Cloudflare Tunnel dials out). Note the box's Tailscale IP — every service binds to it.

**⌘ Fable 5 prompt — provision + harden**
```
Using the hcloud CLI (context gis-ai), create a Hetzner CCX23 named example-gis-server,
ubuntu-24.04, nbg1, ssh-key example-admin-ed25519, labels env=prod project=gis-ai
(no paid backup add-on). Then SSH in and harden it exactly per the AI Automation
Master Guide §6–§7: sudo user `adminuser`, disable root+password SSH after I confirm the
adminuser login works, install Tailscale with --ssh, bind sshd to the Tailscale IP, and
set ufw to deny-incoming with only tailscale0 allowed. Pause for my confirmation
before disabling root. Report the Tailscale IP.
```

**Stop point:** hardened, Tailscale-only CCX23; you have its Tailscale IP.

---

## 5. Phase 2 — Repo & secrets (SOPS + age)

On the macOS workstation, create the repo (config in git; server is disposable — same discipline as the base guide §9):

```bash
mkdir -p ~/code/gis-ai-stack && cd ~/code/gis-ai-stack
git init -b main
printf '%s\n' '*.tfstate*' '.env' '!.env.example' '*.key' '*.pem' > .gitignore
age-keygen -o ~/.config/sops/age/keys.txt        # note the public key; back the PRIVATE key up in Bitwarden
cat > .sops.yaml <<'EOF'
creation_rules:
  - path_regex: \.enc\.(env|json|yaml)$
    age: age1<YOUR_PUBLIC_KEY>
EOF
```

Generate and encrypt the secret set (note the GIS-specific keys — Voyage, ArcGIS, Composio):

```bash
cat > secrets.env <<EOF
PG_USER=gis
PG_PASSWORD=$(openssl rand -base64 32)
LITELLM_MASTER_KEY=sk-$(openssl rand -hex 24)
ANTHROPIC_API_KEY=<paste>
OPENAI_API_KEY=<paste>
VOYAGE_API_KEY=<paste>
ARCGIS_API_KEY=<paste>
ARCGIS_PORTAL_URL=https://www.arcgis.com
COMPOSIO_API_KEY=<paste>
N8N_ENCRYPTION_KEY=$(openssl rand -hex 32)
N8N_JWT_SECRET=$(openssl rand -hex 32)
LANGFUSE_NEXTAUTH_SECRET=$(openssl rand -hex 32)
LANGFUSE_SALT=$(openssl rand -hex 16)
CLOUDFLARED_TOKEN=<paste later, §13>
EOF
sops -e secrets.env > stack/secrets.enc.env && rm secrets.env
```

> **Two secrets you can never lose:** the **age private key** (decrypts everything) and **`N8N_ENCRYPTION_KEY`** (decrypts every n8n credential). Both into Bitwarden the moment they exist.

---

## 6. Phase 3 — The data core: PostGIS 18 + pgvector + Apache AGE

This one database is the whole point. `stack/postgres/init.sql` (verbatim from the Ultimate Build Guide, trimmed to what this server needs):

```sql
-- Spatial
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;
CREATE EXTENSION IF NOT EXISTS postgis_raster;
-- Vector (pgvector)
CREATE EXTENSION IF NOT EXISTS vector;
-- Graph (Apache AGE) — requires the LOAD + search_path dance
CREATE EXTENSION IF NOT EXISTS age;
LOAD 'age';
SET search_path = ag_catalog, "$user", public;
-- Utility
CREATE EXTENSION IF NOT EXISTS pg_trgm;          -- fuzzy match / conflation
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS hstore;
CREATE EXTENSION IF NOT EXISTS btree_gist;

-- Per-service databases (one cluster, isolated DBs)
CREATE DATABASE litellm;
CREATE DATABASE n8n;
CREATE DATABASE langfuse;
CREATE DATABASE hermes;
CREATE DATABASE gis;                              -- spatial + RAG + graph live here
```

> **Version pins if you want them harder** (from the Innish Labs guide): PostGIS 3.5, **pgvector 0.8+**, **Apache AGE 1.5+**. Verify after boot: `SELECT PostGIS_Version();` and `\dx | grep -E "postgis|vector|age"`. **Not included** (add net-new only if you need them): `pgrouting` (network routing), `h3` (hex indexing).

The Spatial-RAG schema (created by the RAG service's migration, §10) uses `VECTOR(1024)` + a GIST geometry index + an AGE graph — covered in Phase 7.

---

## 7. Phase 4 — The service stack

`stack/docker-compose.yml` — every port bound to the **Tailscale IP** (`${TS_IP}`), every tag pinned:

```yaml
name: gis-ai

services:
  postgres:
    image: postgis/postgis:18-3.5
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${PG_USER}
      POSTGRES_PASSWORD: ${PG_PASSWORD}
      POSTGRES_DB: gis
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./postgres/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${PG_USER}"]
      interval: 10s

  redis:
    image: redis:7-alpine
    restart: unless-stopped
    ports: ["${TS_IP}:6379:6379"]

  litellm:
    image: ghcr.io/berriai/litellm:main-stable
    restart: unless-stopped
    depends_on: { postgres: { condition: service_healthy } }
    environment:
      LITELLM_MASTER_KEY: ${LITELLM_MASTER_KEY}
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY}
      OPENAI_API_KEY: ${OPENAI_API_KEY}
      DATABASE_URL: postgresql://${PG_USER}:${PG_PASSWORD}@postgres:5432/litellm
    volumes: [./litellm/config.yaml:/app/config.yaml:ro]
    command: ["--config", "/app/config.yaml"]
    ports: ["${TS_IP}:4000:4000"]

  n8n:
    image: n8nio/n8n:1.95.0
    restart: unless-stopped
    depends_on: { postgres: { condition: service_healthy } }
    environment:
      DB_TYPE: postgresdb
      DB_POSTGRESDB_HOST: postgres
      DB_POSTGRESDB_DATABASE: n8n
      DB_POSTGRESDB_USER: ${PG_USER}
      DB_POSTGRESDB_PASSWORD: ${PG_PASSWORD}
      N8N_ENCRYPTION_KEY: ${N8N_ENCRYPTION_KEY}
      N8N_USER_MANAGEMENT_JWT_SECRET: ${N8N_JWT_SECRET}
      N8N_HOST: example-gis-server
      N8N_PROTOCOL: http
      GENERIC_TIMEZONE: America/Los_Angeles
    volumes: [n8n_data:/home/node/.n8n]
    ports: ["${TS_IP}:5678:5678"]

  hermes:
    image: nousresearch/hermes-agent:latest
    restart: unless-stopped
    depends_on: { litellm: { condition: service_started } }
    environment:
      LITELLM_BASE_URL: http://litellm:4000
      LITELLM_API_KEY: ${LITELLM_MASTER_KEY}
      HERMES_PROFILE: mercator
      DATABASE_URL: postgresql://${PG_USER}:${PG_PASSWORD}@postgres:5432/hermes
    volumes:
      - ./hermes/skills:/app/skills
      - ./hermes/data:/app/data
    ports: ["${TS_IP}:8000:8000"]

  langfuse:
    image: langfuse/langfuse:2
    restart: unless-stopped
    depends_on: { postgres: { condition: service_healthy } }
    environment:
      DATABASE_URL: postgresql://${PG_USER}:${PG_PASSWORD}@postgres:5432/langfuse
      NEXTAUTH_SECRET: ${LANGFUSE_NEXTAUTH_SECRET}
      SALT: ${LANGFUSE_SALT}
    ports: ["${TS_IP}:3000:3000"]

  pg_tileserv:
    image: pramsey/pg_tileserv:latest
    restart: unless-stopped
    depends_on: { postgres: { condition: service_healthy } }
    environment:
      DATABASE_URL: postgresql://${PG_USER}:${PG_PASSWORD}@postgres:5432/gis
    ports: ["${TS_IP}:7800:7800"]

  spatial-rag:
    build: ./spatial-rag           # FastAPI + FastMCP service, Phase 7
    restart: unless-stopped
    depends_on: { postgres: { condition: service_healthy } }
    environment:
      DATABASE_URL: postgresql://${PG_USER}:${PG_PASSWORD}@postgres:5432/gis
      VOYAGE_API_KEY: ${VOYAGE_API_KEY}
      LITELLM_BASE_URL: http://litellm:4000
      LITELLM_API_KEY: ${LITELLM_MASTER_KEY}
    ports: ["${TS_IP}:8001:8001"]

  code-server:
    image: lscr.io/linuxserver/code-server:latest
    restart: unless-stopped
    environment: { PUID: 1000, PGID: 1000, TZ: America/Los_Angeles }
    volumes: [code_data:/config, /home/yourname/gis-ai:/config/workspace/gis-ai]
    ports: ["${TS_IP}:8443:8443"]

volumes: { postgres_data: {}, n8n_data: {}, langfuse_data: {}, code_data: {} }
```

`stack/litellm/config.yaml` (current model tags + Redis cache the source config referenced but didn't define):

```yaml
model_list:
  - model_name: claude-fable
    litellm_params: { model: anthropic/claude-fable-5, api_key: os.environ/ANTHROPIC_API_KEY }
  - model_name: claude
    litellm_params: { model: anthropic/claude-opus-4-8, api_key: os.environ/ANTHROPIC_API_KEY }
  - model_name: claude-mid
    litellm_params: { model: anthropic/claude-sonnet-5, api_key: os.environ/ANTHROPIC_API_KEY }
  - model_name: claude-fast
    litellm_params: { model: anthropic/claude-haiku-4-5, api_key: os.environ/ANTHROPIC_API_KEY }
  - model_name: gpt
    litellm_params: { model: openai/gpt-5.4, api_key: os.environ/OPENAI_API_KEY }
litellm_settings:
  drop_params: true
  cache: true
  cache_params: { type: redis, host: redis, port: 6379 }
general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  database_url: os.environ/DATABASE_URL
  max_budget: 100          # USD/month hard cap — raise deliberately
  budget_duration: 30d
```

Bring it up:

```bash
# On the box, in ~/gis-ai/stack, with the repo synced:
sops -d secrets.enc.env > .env && echo "TS_IP=$(tailscale ip -4)" >> .env
docker compose up -d && docker compose ps
```

**⌘ Fable 5 prompt — write & launch the stack**
```
In my gis-ai-stack repo, write stack/docker-compose.yml, stack/postgres/init.sql,
and stack/litellm/config.yaml exactly per the GIS + AI Server Fable 5 Deploy Guide
(PostGIS 18 + pgvector + Apache AGE; litellm, redis, n8n, hermes, langfuse,
pg_tileserv, spatial-rag, code-server; every port bound to ${TS_IP}; secrets from a
SOPS-decrypted .env). Commit. Then SSH to example-gis-server, sync, decrypt secrets,
append TS_IP, `docker compose up -d`, wait for healthchecks, and verify: postgres
answers `SELECT PostGIS_Version()`, `\dx` shows postgis+vector+age, and each
service responds on its Tailscale port. Never bind to 0.0.0.0. Report the status table.
```

**Stop point:** the full stack running, PostGIS + pgvector + AGE confirmed, Tailscale-only.

---

## 8. Phase 5 — Claude Code + Codex on the box

You drive mostly from the macOS workstation, but installing both on the box gives you a browser agent surface (via code-server) and lets n8n/Hermes call them locally.

```bash
# On the box (as adminuser), via SSH or the code-server terminal:
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh -o /tmp/nvm-install.sh
less /tmp/nvm-install.sh
bash /tmp/nvm-install.sh
source ~/.bashrc && nvm install --lts && nvm use --lts
npm install --global @anthropic-ai/claude-code@2.1.246 && claude --version && claude   # OAuth login
npm install --global @openai/codex@0.150.0 && codex --version                          # verify pkg name (see base guide §4)
```

Add a repo-root `CLAUDE.md` capturing the **non-negotiable GIS design rules** (straight from the GIS Ops guide's `CLAUDE.md` — these are what keep a spatial AI honest):

- **Never let the LLM write raw spatial SQL** — it picks from a typed op catalog (`OP_REGISTRY`); ops are typed Python functions.
- **Every op carries provenance + confidence**; every LLM call / op / agent step is logged to audit tables.
- **Evidence citations resolve to a real feature/layer id.** Never invent layer or field names.
- Tenant-scoped schemas (`client_<slug>`); client ArcGIS creds via Composio, never raw env tokens.
- Tailscale-only; never bind `0.0.0.0`; secrets only via SOPS; deploy via the Makefile.

**Stop point:** Claude Code + Codex on the box; GIS guardrails encoded in `CLAUDE.md`.

---

## 9. Phase 6 — The MCP layer

Four MCP servers give Claude Code (and Hermes) typed access to ArcGIS, Postgres, connectors, and your custom spatial ops. `mcp/.mcp.json` at the repo root (verbatim from the GIS-AI Hybrid + GIS Ops guides):

```json
{
  "mcpServers": {
    "esri": {
      "command": "npx",
      "args": ["-y", "esri-mcp"],
      "env": { "ARCGIS_API_KEY": "$ARCGIS_API_KEY", "ARCGIS_PORTAL_URL": "$ARCGIS_PORTAL_URL" }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "$DATABASE_URL"]
    },
    "composio": {
      "command": "npx",
      "args": ["-y", "composio-mcp"],
      "env": { "COMPOSIO_API_KEY": "$COMPOSIO_API_KEY" }
    },
    "gisops": {
      "command": "python",
      "args": ["-m", "gisops.mcp_server.server"],
      "env": { "DATABASE_URL": "$DATABASE_URL" }
    }
  }
}
```

- **esri** — ArcGIS discovery/query (`search_items`/`esri_list_items`, `describe_layer`, `query_features`, optional geocode). The "hands for ArcGIS."
- **postgres** — direct read access to the spatial DB for Claude Code.
- **composio** — per-tenant ArcGIS/Gmail/Drive brokerage (production auth path; env keys in dev).
- **gisops** (custom, *"the moat"*) — exposes your typed `OP_REGISTRY` as `spatial_<op>` tools so both Claude Code sessions and the platform UI call the **same audited ops**. Cache ops prefixed `spatial_`, live ops `esri_`.

**Verify** from a Claude Code session in the repo: *"list items in the ArcGIS Portal for keyword 'zoning'"* should invoke the **esri** MCP; *"call spatial_hotspots on sac_311"* should route through **gisops**.

---

## 10. Phase 7 — Spatial RAG (the GIS brain)

This is what makes it a *spatial-intelligence* server, not just a database. The design (from your two Spatial RAG guides): **the retrieval unit is an entity — a geometry + attributes — not a text chunk.** One Postgres holds geometry (PostGIS/GIST), embeddings (pgvector), and a property graph (AGE); the FastAPI/FastMCP service fuses them.

### 10a. Schema

The `spatial-rag` service's migration creates, in the `gis` database:

```sql
-- Entities: geometry + attributes + embedding, all in one row
CREATE TABLE entities (
  id BIGSERIAL PRIMARY KEY,               -- integer PKs: pgvector indexes prefer them over UUIDs
  entity_type TEXT NOT NULL,
  name TEXT,
  attributes JSONB,
  geom GEOMETRY(Geometry, 4326) NOT NULL,
  embedding VECTOR(1024),                 -- voyage-3-large; dimensions are STICKY — never mix
  source_dataset TEXT, source_id TEXT,
  ingested_at TIMESTAMPTZ DEFAULT now()
);
CREATE INDEX ON entities USING GIST (geom);
CREATE INDEX ON entities USING HNSW (embedding vector_cosine_ops);   -- IVFFlat also fine to start
CREATE INDEX ON entities USING GIN (attributes);

-- Edges: relationships with provenance + confidence (non-optional for defensible answers)
CREATE TABLE edges (
  id BIGSERIAL PRIMARY KEY,
  src_id BIGINT REFERENCES entities(id),
  dst_id BIGINT REFERENCES entities(id),
  relationship TEXT NOT NULL,             -- 'CONTAINED_IN','ACCESSED_VIA','ADJACENT_TO', ...
  confidence REAL,
  provenance TEXT,                        -- 'spatial_join','knn_join','llm_inferred'
  attributes JSONB,                       -- overlap_pct, distance_m, shared_length_m
  created_at TIMESTAMPTZ DEFAULT now()
);
```

Optionally promote edges into a real **Apache AGE** property graph for multi-hop OpenCypher (add when narratives need 2+ hop reasoning):

```sql
LOAD 'age'; SET search_path = ag_catalog, "$user", public;
SELECT create_graph('spatial_graph');
SELECT create_vlabel('spatial_graph', 'Parcel');     -- Fire, Road, Address, ...
SELECT create_elabel('spatial_graph', 'ADJACENT_TO'); -- NEAREST_FIRE_5KM, CONTAINS, ...
```

### 10b. Edge generation — PostGIS predicates, not LLM guesses

Edges are derived deterministically with spatial SQL (verbatim pattern from the Spatial RAG guide):

```sql
-- CONTAINED_IN: parcels inside boundaries, confidence = overlap fraction
INSERT INTO edges (src_id, dst_id, relationship, confidence, provenance, attributes)
SELECT p.id, b.id, 'CONTAINED_IN',
       ST_Area(ST_Intersection(b.geom, p.geom)) / ST_Area(p.geom),
       'spatial_join',
       jsonb_build_object('overlap_pct', ST_Area(ST_Intersection(b.geom,p.geom))/ST_Area(p.geom))
FROM entities p JOIN entities b
  ON b.entity_type='boundary' AND p.entity_type='parcel'
  AND ST_Contains(b.geom, p.geom);
-- ACCESSED_VIA (nearest road): CROSS JOIN LATERAL + ST_DWithin(...,20) + ORDER BY p.geom <-> r.geom LIMIT 1
-- ADJACENT_TO: ST_Touches ; NEAREST_FIRE_5KM: ST_DWithin(...,5000) ; LIKELY_SAME_AS: pg_trgm similarity + distance
```

### 10c. Ingestion + embeddings

Python loaders (GeoPandas/GDAL/Fiona) stage → QA → promote each dataset idempotently. Each entity gets a **normalized text descriptor** embedded via Voyage, batched:

```
descriptor = "{entity_type}: {name}. Attributes: {key: value pairs}."   # cap ~400 chars, batch 128
embedding  = voyage.embed(descriptor, model="voyage-3-large")           # → VECTOR(1024)
```

Cost is trivial — a full county backfill (~80k parcels) is well under $1.

### 10d. Hybrid retrieval (the actual query)

The 5-step pipeline the service exposes (`spatial_graph_search`):

1. **Embed** the query (Voyage, 1024-dim).
2. **Vector recall** top-50, **pre-filtered by `ST_DWithin`** to a radius if the query has a location: `... ORDER BY embedding <=> :q LIMIT 50`.
3. **Graph expand** each candidate 1–2 hops (recursive CTE over `edges`, or AGE `MATCH (p)-[r*1..2]-(n)`).
4. **Re-rank**: `0.6·vector_similarity + 0.2·graph_density + 0.2·recency`.
5. **Return** top-k structured `RetrievalResult(entity, subgraph, score, factors)`.

An LLM (Sonnet 5, cached system prompt) then synthesizes a cited answer — `{score, paragraph, citations}` — where every citation resolves to a real feature id.

```python
def spatial_graph_search(query: str, lat: float|None=None, lon: float|None=None, k: int=10) -> list[RetrievalResult]: ...
```

### 10e. Expose it over MCP

A ~40-line **FastMCP** server wraps `spatial_graph_search` (and convenience tools like `risk_for_address(addr)`) and runs on `:8001`:

```python
mcp.run(transport="streamable-http", host="0.0.0.0", port=8001)
```

Claude Code adds the server (local `python -m spatial_rag.mcp_server` or the tunnel URL) and calls it with a natural-language spatial question; the tool does geocode → search → synthesize and returns structured JSON Claude reads.

**⌘ Fable 5 prompt — build the Spatial RAG service**
```
Scaffold a `spatial-rag/` FastAPI + FastMCP service in my gis-ai-stack repo per
the GIS + AI Server Fable 5 Deploy Guide, Phase 7: Alembic migration creating the
entities (VECTOR(1024) + GIST + HNSW) and edges tables in the `gis` DB; GeoPandas
loaders that stage→QA→promote and generate voyage-3-large embeddings from a
normalized descriptor; PostGIS edge-generation SQL (CONTAINED_IN, ACCESSED_VIA,
ADJACENT_TO, NEAREST_FIRE_5KM, LIKELY_SAME_AS); a spatial_graph_search() doing the
5-step embed→ST_DWithin-filtered vector recall→graph expand→re-rank→synthesize
pipeline; and a FastMCP server on :8001 exposing spatial_graph_search and
risk_for_address. Never construct spatial SQL from LLM output at runtime — ops come
from a typed OP_REGISTRY with provenance. Add a Dockerfile. Then bring it up and run
one end-to-end query, showing the {score, paragraph, citations} result.
```

**Stop point:** natural-language spatial questions return cited answers over MCP.

---

## 11. Phase 8 — Esri MCP + live feature services

The **esri** MCP (registered in Phase 6) is your live connection to ArcGIS. It queries Feature Services at:

```
https://services{n}.arcgis.com/{org_id}/arcgis/rest/services/{service}/FeatureServer/{layer_index}
```

Key ingest rules the MCP enforces (from `ESRI_MCP.md`): page with `resultOffset` (watch `exceededTransferLimit`, ~1–2k `maxRecordCount`); dates are **epoch milliseconds** (`datetime.fromtimestamp(v/1000, tz=utc)`); reproject Web gis-agent (3857) → **EPSG:4326** on ingest; `f=geojson` for ingestion; `returnGeometry=false` for attribute-only; start wide-extent queries (e.g. FEMA NFHL) on a small bbox then page.

**Auth (three modes):** public layers (no token), Esri Developer **API key** (`x-api-key`/`token`), or Enterprise **OAuth/token** (the `arcgis` Python lib refreshes). In production, per-tenant creds come from **Composio** (`auth_ref` = a Composio entity); in dev, from `ARCGIS_API_KEY`. Store credentials server-side only — never in the repo, logs, or client.

**Live-vs-cache (the hybrid pattern):** register each layer with a **FreshnessPolicy** (`cache_ttl_seconds`, `live_preferred`, `live_source_config` JSONB). A planner decides per query: *"now/today" + live_preferred → live; history → cache; spans both → hybrid.* A deterministic **ResultMerger** dedupes by `(layer_id, source_id)`, prefers live on overlap, and stamps every result with `source: "live"|"cache"`, `fetched_at`, and the FeatureServer URL as provenance. Seed layers as examples: `sac_311` (live, TTL 900s), `sac_parcels` (cache, TTL 30d), `fema_nfhl` (live, TTL 3600s). Feature Server URLs come from env, never hardcoded in git.

**⌘ Fable 5 prompt — wire live feature services**
```
Add a LiveFetchAdapter to the spatial-rag service that spawns the esri MCP as a
persistent stdio subprocess at FastAPI startup (npm-linked ~/code/esri-mcp) and
multiplexes requests via an asyncio.Queue. Add a FreshnessPolicy per layer
(cache_ttl_seconds, live_preferred, live_source_config JSONB), a HybridPlanner that
tags each step source: cache|live|hybrid, and a deterministic ResultMerger that
dedupes by (layer_id, source_id) and stamps provenance + as_of timestamps. Seed
sac_311 (live, 900s), sac_parcels (cache, 30d), fema_nfhl (live, 3600s) with
FeatureServer URLs from env. Run /api/query and show `.plan.steps[].source` and
`.as_of`.
```

**Stop point:** Claude Code and the Spatial-RAG service can pull live ArcGIS data, merged with the cache, with full provenance.

---

## 12. Phase 9 — Tile serving + the geospatial Python env

**Tiles:** `pg_tileserv` (already in compose, `:7800`) serves dynamic vector tiles straight from PostGIS — no extra config beyond `DATABASE_URL`. Point MapLibre/ArcGIS SDK at it for maps. Alternatives if you outgrow it (discussed but not wired in your vault): **Martin** (Rust, faster), **TiTiler/rio-tiler** (raster tiles from COGs), **PMTiles + MapLibre** (static, serverless).

**Host geospatial Python env** (for the loaders and ad-hoc analysis) — GDAL is the engine:

```bash
mamba create -n geo python=3.12 \
  geopandas shapely pyproj rasterio fiona gdal pyogrio \
  pandas numpy pyarrow duckdb contextily folium psycopg2-binary sqlalchemy \
  rio-tiler titiler pystac pystac-client stackstac \
  -c conda-forge
```

(`pyogrio` replaces Fiona for speed; `duckdb` for GeoParquet; `rio-tiler`/`titiler` for COG raster tiles.)

**Optional analytics tier — the "Spatial Insight Engine":** if you want autonomous pattern-finding beyond RAG, add the typed PySAL/esda primitives catalog (`hotspot_detect` = Getis-Ord Gi*, `local_morans_i`, `emerging_hotspots`, `dbscan_spatial`, `scan_statistics`) plus a Celery/cron "pattern hunter" writing to `findings`/`hypotheses` tables. This is the differentiator layer, not needed for a first build — see GIS - AI/Spatial Insight Engine — Beyond Spatial RAG.

---

## 13. Phase 10 — Ingress (Cloudflare Tunnel) & when you need DNS

**Same rule as the base guide (§9/§13): you need DNS only when something must be reachable from the public internet by name.** Until then, Tailscale-only = no DNS, no open ports. For a GIS+AI server the public surface is usually:

- **n8n webhooks** (client systems, scheduled data feeds, Telegram/Stripe).
- **The Spatial-RAG API** (`:8001`), if a client-facing web map / console (e.g. a Vercel frontend using the ArcGIS Maps SDK) needs to call it.

Add `cloudflared` (image already pinned) with the tunnel token in SOPS, and map only what must be public:

```yaml
# ~/.cloudflared/config.yml (verbatim shape from the Ultimate Build Guide)
ingress:
  - hostname: n8n.yourbrand.com
    service: http://localhost:5678
  - hostname: gis-api.yourbrand.com     # spatial-rag, only if a public frontend needs it
    service: http://localhost:8001
  - service: http_status:404
```

Everything else (Langfuse, pg_tileserv, code-server, Postgres) stays Tailscale-only. Set n8n's `WEBHOOK_URL=https://n8n.yourbrand.com/` and `N8N_PROTOCOL=https` once the tunnel is live. If you build a Vercel frontend, restrict the ArcGIS Maps API key to the Vercel domain + localhost and set FastAPI CORS to allow only that origin.

---

## 14. Phase 11 — Backups & snapshots

**Backups (three layers, as base guide §14 — but mind PostGIS):**

```bash
# Nightly, off-site to B2. Use pg_dump --format=custom for the spatial DB (handles PostGIS types cleanly).
docker compose exec -T postgres pg_dump -U "$PG_USER" --format=custom --compress=9 gis > "$D/gis-$TS.dump"
docker compose exec -T postgres pg_dumpall -U "$PG_USER" --roles-only > "$D/roles-$TS.sql"
docker run --rm -v gis-ai_n8n_data:/d:ro -v "$D":/b alpine tar czf "/b/n8n-$TS.tgz" -C /d .
rclone copy "$D" b2:gis-ai-backups --include "*-$TS.*"
```

Also export n8n workflows to git (`n8n export:workflow`), and **test a restore** of the `gis` dump into a throwaway PostGIS container once — confirm `SELECT PostGIS_Version()` and a `SELECT count(*) FROM entities` after restore.

**Snapshots / cloning (dev-test-prod):** exactly the base guide §15 — `hcloud server create-image --type snapshot` to clone a dev twin or pause cheaply (snapshot → delete → recreate). For a GIS box, **quiesce first** (`docker compose down`) so Postgres is consistent, and regenerate secrets on the clone so dev/prod don't share an encryption key or DB password. Snapshot **before any risky ingest or schema change**.

**⌘ Fable 5 prompt — backups**
```
Write ~/gis-ai/backup.sh per Phase 11 (pg_dump --format=custom of the gis DB +
roles + n8n volume tar + rclone to b2:gis-ai-backups, 14-day local retention),
make it executable, add a 3am cron entry, run it once, and then verify by restoring
the gis dump into a throwaway postgis/postgis:18-3.5 container and confirming
PostGIS_Version() and a row count from entities. Report success.
```

---

## 15. The Fable 5 build orchestration

You can build phase-by-phase with the prompts above, **or** hand Fable 5 the two master prompts and let it scaffold in sprints. Both are in your vault verbatim; here they are adapted to this Docker-Compose lineage.

### Launch

```bash
mkdir -p ~/code/gis-ai-stack && cd ~/code/gis-ai-stack
git init && git branch -m main
gh repo create your-github-account/gis-ai-stack --private --source=. --remote=origin
mkdir -p ~/.secrets   # write ~/.secrets/gis-ai.env, chmod 600 (or use the SOPS repo from Phase 2)
claude --model claude-fable-5
```

### Master prompt — scaffold the whole stack (Sprint 0)

> Read CLAUDE.md at the repo root (which I've placed there). Scaffold the GIS + AI server monorepo per the "GIS + AI Server Fable 5 Deploy Guide":
> - `stack/` — docker-compose.yml (postgres[postgis 18 + pgvector + age], redis, litellm, n8n, hermes, langfuse, pg_tileserv, spatial-rag, code-server; every port bound to `${TS_IP}`), `postgres/init.sql`, `litellm/config.yaml`
> - `spatial-rag/` — Python 3.12 + Poetry + FastAPI + FastMCP; Alembic; the entities/edges schema; GeoPandas loaders; `spatial_graph_search`; Dockerfile
> - `mcp/.mcp.json` — esri, postgres, composio, gisops
> - `hermes/` — skills + profile stubs
> - `docs/` — DEPLOY.md, RUNBOOK.md, ARCHITECTURE.md stubs; `.env.example` documenting every variable
> - `.github/workflows/ci.yml` — pytest + typecheck + lint
>
> Design principles: idempotent, auditable, reproducible; secrets never in the repo (SOPS-encrypted, decrypted to `.env` at deploy); never let the LLM write raw spatial SQL; every op typed with provenance. Do NOT implement module logic yet — just the shape. **Stop when I can run `docker compose up` and see all services boot healthy, `curl` the spatial-rag `/health`, and `\dx` shows postgis + vector + age.**

### Sprint sequence (adapted to this stack)

| Sprint | Model | Goal | Verify |
|---|---|---|---|
| 0 | **Fable 5** | Repo + compose scaffold (above) | `docker compose up` healthy; `\dx` shows postgis/vector/age |
| 1 | Sonnet 5 | Alembic models: entities, edges, layers, audit_* + `create_tenant(slug)` | `alembic upgrade head`; `pytest tests/models` |
| 2 | **Fable 5** | Ingestion: GeoPandas loaders, stage→QA→promote, Typer CLI `gisops ingest` | load a real dataset; rows in `entities` |
| 3 | Sonnet 5 | Catalog + Voyage embeddings + `@layer-cataloger` subagent | embeddings populated; HNSW index built |
| 4 | **Fable 5** scaffold | Typed spatial ops (`near, within, intersects, summarize_by_boundary, trend, nearest, compare_periods, hotspots`) + `OP_REGISTRY` + `@spatial-op-writer` | `pytest tests/ops` green |
| 5 | Sonnet 5 | Spatial RAG retriever (`spatial_graph_search`) | end-to-end query returns ranked entities |
| 6 | **Opus 4.8** (prompt) | Intent planner + executor + synthesizer + `@intent-planner-tester` | cited answer; planner refuses on missing layer; cost <$0.10/query |
| 7 | Sonnet 5 | Agent workflows + Celery (bounded DAGs, daily ingest refresh, qa_geometry) | scheduled refresh runs |
| 8 | **Fable 5** | gisops MCP server (`spatial_<op>` tools) + Esri live adapter | Claude Code calls `spatial_near` → `OpResult` |
| 9 | **Fable 5** | Docs + smoke tests + first snapshot; commit/push | `scripts/smoke-test.sh` green |

### Subagents to define (`.claude/agents/`)

`layer-cataloger` (registers layers, embeds), `spatial-op-writer` (writes typed ops), `intent-planner-tester` (adversarially tests the planner — ambiguous/injection/impossible), `report-composer` (PDF briefings with mandatory caveats), `agent-workflow-designer` (bounded DAGs), `audit-reviewer` (nightly anomaly scan). Plus the global library: `gis-architect, arcgis-web-dev, n8n-builder, planner, code-reviewer, debugger, test-engineer, devops-deployer`.

### The planner's non-negotiable contract (pin this)

> - Only use ops that exist in `OP_REGISTRY`. Never invent op names.
> - Only reference layers in the LAYER catalog provided. Never invent layer or field names.
> - `input_params` must match the op's `input_schema` exactly. **Never write SQL.**
> - Output either `{"steps":[{op_name, input_params, why}]}` or `{"refusal":{reason, suggested_rephrase}}`. Aim for ≤5 steps.

---

## 16. Verification checklist

```bash
# Data core
docker compose exec postgres psql -U $PG_USER -d gis -c "SELECT PostGIS_Version();"     # 3.5.x
docker compose exec postgres psql -U $PG_USER -d gis -c "\dx" | grep -E "postgis|vector|age"
# Services (all on the Tailscale IP)
docker compose ps                                    # every service Up/healthy
curl -sf http://$(tailscale ip -4):8001/health       # spatial-rag
curl -sf http://$(tailscale ip -4):5678/healthz       # n8n
curl -sf http://$(tailscale ip -4):3000/api/public/health   # langfuse
# Agents on the box
claude --version && claude doctor && codex --version
# MCP (from a claude session in the repo): "list ArcGIS items for 'zoning'" -> esri MCP;
#   "call spatial_near ..." -> gisops MCP
# End-to-end spatial answer
gisops query "which parcels are within 500m of a school in tenant 'demo'"   # cited answer, cost <$0.10
```

---

## 17. Security

Inherit the full checklist from [AI Automation Master Guide deploy](../AI%20Automation/AI%20Automation%20Master%20Guide%20deploy.md) §16 (root SSH disabled, Tailscale-bound SSH, never-`0.0.0.0`, SOPS secrets, 2FA everywhere, pinned tags, verified restores, MCP supply-chain caution). **GIS-specific additions:**

- **ArcGIS credentials server-side only** — never in the repo, logs, or any client bundle; per-tenant via Composio, scoped API keys, short-lived Enterprise tokens.
- **The LLM never writes spatial SQL** — it selects from the typed `OP_REGISTRY`; this is a security control (prevents injection through natural-language queries), not just a design nicety.
- **Every op/answer carries provenance + citations** resolving to real feature ids — audit tables log every op, LLM call, and agent step.
- **Restrict a public ArcGIS Maps API key** to your frontend domain; set FastAPI CORS to that origin only.

---

## 18. Cost

| Item | Monthly |
|---|---|
| Hetzner **CCX23** (4 dedicated vCPU / 16 GB) | ~€30 |
| Snapshot storage + B2 off-site backups | ~€1 |
| Cloudflare + Tailscale + GitHub free tiers | €0 |
| Domain | ~$1 |
| **Infra subtotal** | **~€32** |
| Voyage embeddings | pennies (county backfill < $1) |
| Anthropic + OpenAI usage | Variable — capped via LiteLLM `max_budget` + per-key console limits |

Dev twin (CCX13, when running) adds ~€15. Paused (snapshot + delete): ~€1/mo. As always, the real variable is model spend — LiteLLM budget caps + Langfuse cost logging keep it honest.

---

## 19. Alternative lineage & related

**The native/systemd path (lineage B).** If you'd rather run without Docker — the standing preference in Hetzner Deploy - GIS + Hermes + n8n + Claude Code - Fable 5 Master Prompt and GIS AI Operations Platform — Complete Claude Code Build Guide — build an **Ansible `hetzner-provisioner`** instead: playbooks `00-base` → `10-tailscale` → `20-postgres` (PG+PostGIS+pgvector) → `30-redis` → `40-node` → `50-python` → `60-n8n` (native systemd) → `70-claude-code` (+Hermes workspace) → `80-mcp-servers` (esri/composio/postgres/spatial-ops as systemd `--user` services) → `90-caddy` → `91-backup` (restic) → `99-verify`. Same components, different delivery; **don't mix it with the compose stack above** — pick one.

**Related:**
- [AI Automation Master Guide deploy](../AI%20Automation/AI%20Automation%20Master%20Guide%20deploy.md) — the base: Hetzner account, SSH, Tailscale, hardening, Cloudflare Tunnel, backups, snapshots, the Mac-mini workflow.
- AI Automation Stack — Source Index — the tiered map of every source doc.
- GIS + AI Stack — The Ultimate Build Guide — verbatim compose/init.sql/LiteLLM this guide is built on.
- Spatial RAG with Claude Code — Complete Build Guide / Spatial Graph RAG — Implementation Plan (Open Source) — the Spatial RAG deep dives (example risk-scoring product PoC has copy-paste phases 0–12).
- GIS-AI Hybrid App - Esri MCP + Spatial RAG + Live Feature Services - Fable 5 Build — the live-feature-service hybrid architecture.
- GIS AI Operations Platform — Complete Claude Code Build Guide — the 12-sprint platform build + subagents/skills.
- Spatial Insight Engine — Beyond Spatial RAG — the autonomous analytics tier (PySAL primitives, pattern hunter).
