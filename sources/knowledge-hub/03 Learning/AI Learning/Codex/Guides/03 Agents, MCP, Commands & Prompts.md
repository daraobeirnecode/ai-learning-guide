---
title: "Master Codex Guide — Agents, MCP, Commands & Prompts"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 03 — Agents, MCP, Commands & Prompts

Codex's power systems. The honest framing up front: **Claude Code's specialization lives in subagent/skill *files*; Codex's lives in AGENTS.md + profiles + prompt templates.** Simpler machinery, same leverage — if you're deliberate.

---

## 1. "Agents" in Codex = AGENTS.md × profiles

Codex doesn't spawn named sub-personas from a folder the way Claude does. Its agent system is the **combination of standing orders (AGENTS.md) and operating mode (profile)** — you get specialist behavior by pairing them:

| "Agent" you want | How you get it |
|---|---|
| Repo scout | `--profile safe` + orient prompt (doc 04 #1) |
| Implementer | `--profile builder` + a work order + `--full-auto` |
| Reviewer | `--profile review` + the review prompt — read-only *enforces* reviewer behavior |
| Test engineer | `--profile builder` + "write tests only; do not modify source" |
| Lab rat | `--profile lab` on a throwaway branch |

**Project AGENTS.md is where the specialization deepens.** For the Inish Labs repos, each carries: purpose, the exact commands (`make up`, `pytest`, `pnpm build`), architecture map, rules (*don't commit .env; staging data only; never bind 0.0.0.0; confirm before anything touching a client box*), and definition of done. Write it once per repo — Tutorial 2.

**Shared repos with Claude:** Codex reads `CLAUDE.md` too. Division: general rules + commands → `AGENTS.md`; Claude-specific workflow → `CLAUDE.md`; critical commands duplicated in both. Don't create an AGENTS.md at all if the CLAUDE.md already steers Codex well — add it only when Codex needs *different* or *clearer* orders.

## 2. MCP — same servers, second client

Everything you wired for Claude plugs into Codex:

```bash
# CLI method
codex mcp add postgres -- npx -y @modelcontextprotocol/server-postgres "$DATABASE_URL"
codex mcp add esri -- npx -y esri-mcp        # env vars via config.toml block instead

# config.toml method (per-repo .codex/config.toml — the shareable way)
[mcp_servers.esri]
command = "npx"
args = ["-y", "esri-mcp"]
# env = { ARCGIS_API_KEY = "..." }  → keep keys OUT of committed files; use the global config
```

Your MCP roadmap (from the vault) applies here identically: postgres, esri-mcp, the FastMCP spatial servers, an Obsidian-search server. **Rule: wire per-repo, read the source of anything third-party, never hand a write-token to an unread server** — the same security posture as the Claude academy, because it's the same protocol and the same risk.

## 3. Commands & custom prompts

**CLI commands you actually use:** `codex` (interactive) · `codex exec "…"` · `codex exec --full-auto "…"` · `codex --profile <name>` · `codex -c key="value"` · `codex mcp add|list|remove` · `codex --version` / `--help`.

**In-session slash commands** ⚠️ exist and grow by version (`/model`, `/approvals` and friends in current builds) — run `/help` inside a session and trust that list.

**Custom prompts** ⚠️ — newer builds load markdown files from `~/.codex/prompts/` as reusable `/name` commands (Codex's analog of Claude custom commands). Because this surface moves, your durable system is the **prompt template library** (doc 04): versioned markdown in the vault/repo you paste or pipe in — works on every build, reviewable in git, shareable with a future employee. If your build supports `~/.codex/prompts/`, mirror the library there for `/`-invocation; the vault copies remain the source of truth.

**Skills** ⚠️ — Codex recognizes the `skills/<name>/SKILL.md` convention (invoke by asking: *"Use the api-change-review skill on this diff"*). Treat as a bonus surface: keep the same skill folders you built for Claude in shared repos, and let whichever agent is present use them.

## 4. The division of labor (the master pattern, made explicit)

Your vault's assignments, as a decision table:

| Task | Engine | Why |
|---|---|---|
| Architecture, multi-file planning, ambiguity | **Claude Code** (plan mode) | Deep reasoning, interactive refinement |
| First implementation of a designed system | **Claude Code** (Fable 5 for scaffolds) | Long-horizon builds |
| Bounded implementation from a clear work order | **Codex** (`builder`, `--full-auto`) | Fast, clean, sandboxed |
| Independent review of any AI-written diff | **The other engine** | Different model, different blind spots |
| Second version to compare approaches | **Codex** | Cheap way to buy a genuine alternative |
| n8n/business workflow design; skills/subagents/MCP-heavy work | **Claude Code** | Richer harness systems |
| Quick script, refactor, test backfill | **Codex** | Lowest ceremony |
| Exploratory debugging | **Claude Code** first | Better at hypothesis-driven digging |

**The handoff protocol (drilled in Tutorials 6–7):** all context moves through files — Claude ends a planning session by writing `WORK-ORDER.md` (task, constraints, definition of done, test command); Codex implements against it; the diff + test output travel back. No copy-pasting conversation fragments between agents: *git is the interface.*

**The weekly rhythm (yours, kept):** one 2-hour block — Claude plans → Codex implements → cross-review → tests → note to the vault.

---

*Next: [04 The 20 Starter Prompts & Skills](04%20The%2020%20Starter%20Prompts%20%26%20Skills.md) — the template library.*
