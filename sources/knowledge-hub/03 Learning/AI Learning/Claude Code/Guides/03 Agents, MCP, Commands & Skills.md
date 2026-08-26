---
title: "Master Claude Guide — Agents, MCP, Commands & Skills"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 03 — Agents, MCP, Commands & Skills

The four power systems (plus hooks). Concepts in plain English are in doc 01; this is the *how*, current to v2.1.205 (July 2026).

---

## 1. Subagents — your cloneable specialists

A subagent is a markdown file. That's the whole trick: `.claude/agents/<name>.md` (project) or `~/.claude/agents/<name>.md` (everywhere).

```markdown
---
name: gis-architect
description: Designs PostGIS schemas, spatial ops, and pipeline architecture.
  Use for any spatial data-modeling or GIS architecture decision.
tools: Read, Glob, Grep, WebSearch
model: claude-opus-4-8
effort: high
memory-enabled: true
---
You are a senior GIS architect. You favor PostGIS-native solutions, typed
operations over ad-hoc SQL, and EPSG:4326 at rest. You never propose Esri-paid
components unless the client already owns them. Always end with: schema DDL,
index plan, and the one risk you'd watch.
```

**What matters:**
- `description` is the routing signal — Claude delegates automatically when a task matches it. Write it like a job ad: *when* to use, not just what it is.
- `tools:` restricts capability (read-only reviewers can't edit); `model:` lets a Haiku subagent do cheap batch work inside a Sonnet session.
- `memory-enabled: true` gives the agent persistent notes across sessions (v2.1.195+).
- Subagents run **in the background by default** now (v2.1.198+) — the main session keeps working; results return as summaries. Check on them with `claude agents` / the notification stream.
- **Built-ins you get free:** `Explore` (read-only fan-out search), `Plan` (architecture), `general-purpose` (everything). Reach for `Explore` whenever the answer means sweeping many files.

**Your starting roster** (from your library + the GIS Ops guide): `code-reviewer`, `researcher`, `gis-architect`, `n8n-builder`, `layer-cataloger`, `spatial-op-writer`, `intent-planner-tester`, `report-composer`, `audit-reviewer`, `test-engineer`, `devops-deployer`, `copywriter` (brand-voice guard). Tutorial 4 builds two of them.

**When to delegate:** exploration that would flood your context; reviews needing fresh eyes; parallelizable batches; anything where a different model tier fits. **When not to:** single-file reads, sequential edits — direct work is faster.

## 2. MCP & connectors — plugging in the outside world

**Add servers:**

```bash
# HTTP (remote, OAuth) — the modern default
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
# stdio (local process) — note the `--` separator
claude mcp add --transport stdio postgres -- npx -y @modelcontextprotocol/server-postgres "$DATABASE_URL"
claude mcp list · claude mcp remove <name> · /mcp   # manage + authenticate in-session
```

**Project scope = `.mcp.json`** at repo root (shared via git; teammates and future-you get the same wiring). Env expansion supported: `${VAR}` / `${VAR:-default}`. Your GIS repo's canonical four: `esri`, `postgres`, `composio`, `gisops` — already specified in GIS + AI Server on Hetzner — Fable 5 Deploy Guide §9.

**Scopes & precedence:** local (just you, this repo) > project (`.mcp.json`) > user (all projects) > plugin > **claude.ai connectors** (Gmail, Calendar, Drive — managed in your claude.ai account, auto-synced; that's what "connectors" means).

**Your minimum-viable set** (per Claude Lessons, still right): `filesystem`(built-in now), `github`, `postgres`, your `esri-mcp`, plus FastMCP for building your own — and the three connectors: Gmail, Calendar, GitHub. **Wire per-project, not globally** — idle servers cost context every session.

**Security (non-negotiable):** an MCP server runs with your permissions. Pin versions, read the source of community servers (<500 lines is a 20-min audit), run third-party servers stdio-local not hosted, and never hand a write-capable token to a server you haven't read. Your `AI Security — Comprehensive Guide` covers the full treatment.

## 3. Slash commands — the control panel

**Daily drivers:** `/model` (switch model) · `/effort` (thinking depth) · `/context` (what's eating the window) · `/cost` · `/compact` · `/mcp` · `/permissions` · `/memory` (browse CLAUDE.md + auto-memory) · `/init` · `/config key=value` · `/cd` (move working dir) · `/rename` · `/recap` · `/doctor`.
**Bundled skill-commands:** `/code-review` (diff review at chosen effort) · `/batch` (parallel agents across worktrees) · `/loop` (recurring runs) · `/run`, `/verify` (launch and prove the app works) · `/plan`.

**Custom commands are skills now** (v2.1.196 unification): a file at `.claude/skills/deploy/SKILL.md` *is* the `/deploy` command. Legacy `.claude/commands/*.md` still work, but write new ones as skills — they get frontmatter control, arguments, and dynamic context. You can **stack** them: `/brand-check /linkedin-post draft.md` runs both in sequence (v2.1.199+).

## 4. Skills — packaged expertise (the deepest system)

A skill = folder + `SKILL.md`. Locations: `~/.claude/skills/<name>/` (personal) · `.claude/skills/<name>/` (project) · nested dirs in monorepos get auto-qualified names (`apps/web:deploy`).

```markdown
---
name: provision-client
description: Provision a new Inish Labs client server on Hetzner — snapshot
  clone, fresh secrets, smoke test. Use when onboarding a signed client.
argument-hint: "[client-slug] [tier: starter|pro]"
allowed-tools: Bash(hcloud *), Bash(ssh *), Read, Write
context: fork
model: claude-fable-5
---
## Example server inventory

Run only against an account you own, after confirming the active account and project:

```bash
hcloud server list -o columns=name,status,type
```

# Steps
1. Confirm $0 is a new slug (check the list above); tier $1 → ccx13|ccx23 ...
2. ...snapshot clone → Tailscale join → SOPS re-key → docker compose up → smoke test.
Never reuse another client's secrets. Never bind 0.0.0.0.
```

**The mechanics that make skills powerful:**
- **Progressive disclosure:** only the `description` sits in context by default; the body loads when triggered. You can have 50 skills for the price of 50 sentences.
- **Dynamic context:** `` !`command` `` lines execute locally *before* Claude reads the skill. Treat them as code: inspect first, keep them read-only, scope credentials narrowly, and avoid secret-bearing output.
- **Substitutions:** `$ARGUMENTS`/`$0`/`$1`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`.
- **Control:** `allowed-tools` pre-approves exactly what the skill needs; `context: fork` + `agent:` runs it as an isolated subagent; `model:`/`effort:` override per-skill; `disable-model-invocation: true` = manual-only (for dangerous ops); `paths:` loads only when matching files are touched.
- **Triggering:** type `/provision-client acme starter`, or just describe the task — the description auto-matches.

**Install the official packs** (your Claude Lessons one-liner, still correct): `/plugin install anthropic-skills` (docx, pdf, pptx, xlsx, schedule, skill-creator) — then build your own with `skill-creator`. The 20 Inish Labs skills are next in [04 The 20 Starter Skills](04%20The%2020%20Starter%20Skills.md).

## 5. Hooks — deterministic guardrails (the 10% that needs no AI)

Configured in `settings.json` (or a skill/agent's frontmatter). The events you'll actually use: `PreToolUse` (validate/block before a tool runs), `PostToolUse` (auto-format, log), `SessionStart` (load env), `PreCompact` (re-inject critical context).

```json
{ "hooks": { "PostToolUse": [ { "matcher": "Edit|Write",
  "hooks": [{ "type": "command",
    "command": "jq -r '.tool_input.file_path' | xargs -I{} sh -c 'case {} in *.py) uv run ruff format {};; esac'" }] } ],
  "PreToolUse": [ { "matcher": "Bash",
  "hooks": [{ "type": "command",
    "command": "jq -r '.tool_input.command' | grep -qE 'hcloud server delete|rm -rf /' && echo 'Blocked: destructive' >&2 && exit 2 || exit 0" }] } ] } }
```

Exit code `2` blocks the action and feeds stderr back to Claude as guidance. Rule of thumb: **policy that must *always* hold → hook; judgment that usually holds → CLAUDE.md.**

---

*Next: [04 The 20 Starter Skills](04%20The%2020%20Starter%20Skills.md) — the Inish Labs skill library, ready to install.*
