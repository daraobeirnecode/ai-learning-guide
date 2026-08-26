---
title: "Master Codex Guide — Key Concepts & Definitions"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 01 — Key Concepts & Definitions (Plain English)

What Codex is made of, explained plainly. Where Codex and Claude Code share a concept (tokens, context, agents), doc 01 of the Claude academy covers it — this doc focuses on what's *Codex-shaped*.

---

## The big picture

**Codex** is OpenAI's coding agent. The piece you use is the **Codex CLI** (`codex` in your terminal): point it at a git repo, give it a task, and it reads, edits, and runs commands inside a **sandbox** whose strictness you choose. Same species as Claude Code — model in a loop with tools — but a different temperament: **Codex is repo-focused and execution-first**; it shines when the work order is already clear.

*Plain English: if Claude Code is your architect-engineer who thinks out loud, Codex is the fast contractor who works cleanly inside the fence you draw — and a second pair of eyes from a different brain.*

**Why run both?** Different models make different mistakes. A Claude-written diff reviewed by Codex (and vice versa) catches things neither catches alone — that's your established professional pattern, and it's also billable ("two independent AI reviews" is a real line in a deliverable).

## The control model — sandbox × approval

Codex's safety story is two dials, set independently. This is the single most important thing to understand:

**Sandbox mode — what Codex *can touch*:**
- `read-only` — look but don't touch. Orientation, review, learning a repo.
- `workspace-write` — edit files inside the workspace only. Normal building.
- (Broader/danger modes exist ⚠️ version-dependent — you don't use them; a disposable VM is the right tool instead.)

**Approval policy — when Codex *must ask*:**
- `on-request` — asks before consequential actions. Your default everywhere.
- `never` — no prompts. Only in your disposable `lab` profile, on throwaway branches.

*Plain English: sandbox = which rooms it may enter; approval = whether it knocks first.*

**Profile** — a named preset bundling both dials, defined in config.toml and selected at launch: `codex --profile safe|builder|review|lab`. Your four (already configured):

| Profile | Sandbox | Approval | Use |
|---|---|---|---|
| `safe` | read-only | on-request | Orientation, learning a repo |
| `builder` | workspace-write | on-request | Normal feature work |
| `review` | read-only | on-request | Diff/code review |
| `lab` | workspace-write | **never** | Disposable experiments only |

## Instructions and configuration

**AGENTS.md** — Codex's standing-orders file; the sibling of CLAUDE.md. Two tiers:
- **Global** `~/.codex/AGENTS.md` — durable personal preferences: working style (plan before large edits, git checkpoints), coding defaults (typed Python + ruff, FastAPI + Pydantic, modern TS), safety rules (no secrets, no destructive commands, no unapproved deps/network), and your **mandated response format** — every task ends with: *1) what changed, 2) files changed, 3) tests/validation run, 4) remaining risks, 5) suggested next step.* That last one is the habit that makes Codex output client-ready.
- **Project** `AGENTS.md` in the repo — purpose, commands (`dev/build/test`), architecture map, rules (don't commit `.env`, staging data only, confirm before deploy), definition of done.

Codex **also reads `CLAUDE.md`** and the README — so in shared repos: *general repo rules + commands → AGENTS.md; Claude-specific workflow → CLAUDE.md; duplicate the critical commands in both.* Never in the global file: API keys, one client's private data, issue numbers, temporary status.

**config.toml** — machine config: `~/.codex/config.toml` (global) and `.codex/config.toml` (per-repo). Holds the default model, sandbox/approval defaults, the profiles, and MCP servers. Full listing in doc 02.

**Model** — ⚠️ your config pins `gpt-5.1-codex`, a coding-tuned model. Names rotate; verify with the live CLI before pinning anything new.

## Execution modes

**Interactive** — `codex` opens a REPL-style session in the repo: converse, iterate, approve.
**One-shot** — `codex exec "prompt"`: run one task and exit. Your orientation pattern: *"Summarize this repo's architecture. Make no changes."*
**Bounded auto** — `codex exec --full-auto "task"`: freer rein to edit within the sandbox. The workhorse for well-specified implementation. The discipline around it (clean branch, bounded scope, no commit) *is* the skill — Tutorial 3.
**MCP** — Codex speaks MCP like Claude: `codex mcp add <name> -- <command>` or `[mcp_servers.*]` in config.toml. Same servers you built for Claude (postgres, esri) plug into Codex.
**Custom prompts** — ⚠️ reusable prompt files that surface as slash-commands in newer builds (`~/.codex/prompts/`); your vault treats "prompt templates you paste" as the durable version — doc 04 is built that way, so it works on every build.
**Skills** — Codex supports the same `skills/<name>/SKILL.md` folder convention; support is newer and thinner than Claude's ⚠️ — treat AGENTS.md + prompt templates as the primary system, skills as a bonus.
**Cloud/delegated tasks** — Codex has a cloud/web surface for delegating async tasks ⚠️ (not documented in your vault, not part of this curriculum; the CLI is your tool).

## The pair pattern (the reason this academy exists)

```
Claude Code (plan + first build)  →  git diff  →  Codex (review / second version / refactor)
        ↑                                                        │
        └──────────── tests + your judgment ◄────────────────────┘
```

Handoffs travel through **git and files, never through vibes**: Claude writes `PLAN.md`/a work order; Codex implements against it; both review each other's diffs; tests arbitrate. Tutorials 6–8 drill this loop.

---

*Next: [02 Setup & Best Practices](02%20Setup%20%26%20Best%20Practices.md).*
