---
title: "Master Claude Guide — Key Concepts & Definitions"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 01 — Key Concepts & Definitions (Plain English)

Everything Claude Code is built from, explained the way you'd explain it to a smart colleague who's never used it. Read once now; return whenever a term feels fuzzy.

---

## The big picture

**Claude Code** is an AI agent that lives in your terminal. You type what you want in plain English; it reads files, writes code, runs commands, and keeps going — step after step — until the job is done or it needs your decision. Think of it as **a very fast junior-to-senior engineer who works only inside the folders you allow, shows you every change, and asks permission for anything risky.**

**Agent** — a model in a loop. A chatbot answers once; an agent *acts*: it decides "I need to read that file," reads it, decides the next step, and repeats. The loop of decide → act → observe → decide is what makes it an agent.

**Harness** — the machinery around the model: the tools it can use, the permission system, the context management. Claude Code *is* a harness; the model (Fable 5, Sonnet 5…) is the brain inside it. Same brain, different harness = very different behavior — which is why Claude Code feels different from claude.ai.

**Session** — one continuous conversation in one working directory. Everything you and Claude say, plus every file it reads, accumulates in the session's context. `claude --continue` resumes the last one; `/rename` names it.

## Context, tokens, and cost

**Token** — the unit models read and bill in; roughly ¾ of a word. "Context" and "cost" are both measured in tokens.

**Context window** — the model's working memory: everything it can "see" right now (your messages, file contents, tool results). Current models hold ~1M tokens. It is finite — a master's core habit is *context hygiene*: don't read whole huge files when a section will do; don't paste what you can reference.

**Compaction** — when a long session nears the limit, Claude summarizes the older parts to free space (`/compact`, or automatic). Work continues; fine detail from early turns becomes summary.

**Model tiers (July 2026):** **Fable 5** (`claude-fable-5`) — the most capable; always-thinking; for scaffolding whole systems and long autonomous runs. **Opus 4.8** — top Opus tier, hard reasoning. **Sonnet 5** — the daily driver: near-Opus at a third of the price. **Haiku 4.5** — fast/cheap, for batch work and subagents. Your vault's discipline (updated to current names): *Sonnet daily, Haiku for batch, Opus/Fable as a deliberate splurge — $5/session default cap.*

**Effort** (`/effort low|medium|high|xhigh|max`) — how hard the model thinks per step. Higher = deeper reasoning, more tokens, slower. `xhigh` for gnarly builds; `low` for mechanical chores.

## Instructions and configuration

**CLAUDE.md** — the standing-orders file. Claude reads it automatically at session start; it's how you say things once instead of every session. It's a **hierarchy**: `~/.claude/CLAUDE.md` (you, everywhere) → `./CLAUDE.md` (this project, shared via git) → `./CLAUDE.local.md` (this project, just you, gitignored). Most specific wins. Keep each under ~200 lines (your rule); use `@path/file.md` imports for detail. **Rules** (`.claude/rules/*.md` with `paths:` frontmatter) scope instructions to matching files only.

**settings.json** — machine-readable config (permissions, hooks, env, model): `~/.claude/settings.json` (user) → `.claude/settings.json` (project, shared) → `.claude/settings.local.json` (project, private). Later overrides earlier.

**Permission modes** — the trust dial. **default** (asks for anything non-read), **acceptEdits** (file edits auto-approved), **plan** (read-only; proposes before touching anything — start risky work here), **auto** (nearly everything auto-approved with safety checks), **bypassPermissions** (no checks — containers/VMs only). Cycle with `Shift+Tab`; some paths (`.git/`, `.claude/`, dotfiles) are protected in every mode but bypass.

## The power systems (each gets full treatment in doc 03)

**Tool** — one concrete ability: Read, Write, Edit, Bash, Grep, WebSearch… Claude chooses tools; permissions gate them.

**Slash command** — a `/name` you type to trigger something: built-ins (`/model`, `/context`, `/compact`, `/mcp`, `/init`, `/doctor`) and custom ones — which, since v2.1.196, **are just skills**.

**Skill** — a reusable instruction package: a folder with a `SKILL.md` (frontmatter + markdown instructions, optionally scripts and references). Claude loads it when relevant or when you type `/skill-name`. *Plain English: a laminated recipe card you write once; Claude pulls it out whenever that dish is ordered.*

**Subagent** — a separate Claude with its own context window, tools, and (optionally) model, defined in `.claude/agents/name.md`. The main session delegates a chunk of work ("review this diff", "explore this repo") and gets back a summary — keeping the main context clean. *Plain English: a specialist employee you can clone at will.* Built-ins: `Explore` (read-only research), `Plan`, `general-purpose`.

**MCP (Model Context Protocol)** — the universal adapter that connects Claude to outside systems: Postgres, GitHub, ArcGIS, n8n, your own APIs. An **MCP server** exposes tools; Claude Code is the client. **Connectors** are the same idea managed through your claude.ai account (Gmail, Calendar, Drive). *Plain English: USB ports for your agent.*

**Hook** — a script that fires automatically at lifecycle moments (before a tool runs, after an edit, at session start). Deterministic guardrails and automation: auto-format after every edit, block commands touching prod, log everything. *Plain English: tripwires and conveyor belts around the agent.*

**Plugin** — a distributable bundle of skills/agents/hooks/MCP servers installed via `/plugin`. The official marketplace carries `anthropic-skills` (docx/pdf/pptx/xlsx…), `skill-creator`, and more.

## Working patterns

**Plan mode → execute** — for anything non-trivial: explore and agree on a plan in read-only plan mode, then let it execute. Cheap misunderstandings die in planning, not in your codebase.
**Worktree** — a parallel git checkout so an agent (or `/batch`) can work on an isolated copy without disturbing your working tree.
**Workflows / agent teams** — orchestrated fleets of subagents for big fan-out jobs (`/workflows` to watch). Master-level; Tutorial 8 touches it.
**Headless** (`claude -p "..."`) — run Claude non-interactively from scripts/CI — the bridge that lets n8n or cron *call* Claude Code.

---

*Next: [02 Setup & Best Practices](02%20Setup%20%26%20Best%20Practices.md) — install it, configure it your way, and the habits that compound.*
