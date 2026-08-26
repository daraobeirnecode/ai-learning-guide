---
title: "Master Codex Guide — START HERE"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Master Codex Guide — Codex Mastery Path

**START HERE.** This folder is a complete training academy for **OpenAI Codex** — the terminal coding agent that is your *second* AI engineer. It's grounded in your actual setup (Homebrew install on the macOS workstation, `codex-cli 0.125.0`, `~/.codex/config.toml` profiles, the `~/.codex/AGENTS.md` conventions) and in the role your own vault assigns Codex: **the fast, sandboxed implementation-and-review engine that pairs with Claude Code.**

> **The doctrine (from your Codex Master Guide, kept):** *Claude Code reasons through architecture and creates the first implementation. Codex reviews, refactors, or builds a second version. `git diff` and tests are the source of truth.* This academy teaches Codex as that second engine — not as a Claude replacement. The pair is the product.

> **Version caveat (your own guides insist on this):** Codex's CLI surface, model names, and config keys move fast. Facts here match your vault (verified 2026-05-22, codex-cli 0.125.0) plus stable patterns; **trust the live `codex --help` over any written tutorial, including this one.** Anything version-volatile is flagged ⚠️.

## The documents

| # | Document | What you'll learn |
|---|---|---|
| 00 | This file | The learning path |
| 01 | [01 Key Concepts & Definitions](01%20Key%20Concepts%20%26%20Definitions.md) | Codex's mental model in plain English — sandbox, approvals, profiles, AGENTS.md |
| 02 | [02 Setup & Best Practices](02%20Setup%20%26%20Best%20Practices.md) | Install, auth, config.toml, the four profiles, and the 7-step session ritual |
| 03 | [03 Agents, MCP, Commands & Prompts](03%20Agents%2C%20MCP%2C%20Commands%20%26%20Prompts.md) | AGENTS.md as the agent system, MCP wiring, custom prompts/commands, and the Claude+Codex division of labor |
| 04 | [04 The 20 Starter Prompts & Skills](04%20The%2020%20Starter%20Prompts%20%26%20Skills.md) | Twenty reusable prompt templates/skills for Inish Labs work |
| 05 | [05 Ten Tutorials](05%20Ten%20Tutorials.md) | Ten hands-on tutorials — all playing to Codex's strengths, all producing Inish Labs assets |

## The mastery path (four levels)

**Level 1 — Operator (week 1).** Docs 01–02, Tutorials 1–2. You can: run safe read-only sessions, understand sandbox/approval modes, keep auth healthy.
**Level 2 — Implementer (week 2).** Doc 03, Tutorials 3–5. You can: run bounded `--full-auto` builds, drive work through AGENTS.md, review diffs properly.
**Level 3 — Pair operator (weeks 3–4).** Tutorials 6–8. You can: run the Claude→Codex→tests loop, wire MCP, use profiles deliberately.
**Level 4 — Master (ongoing).** Tutorials 9–10 + the 20 prompts installed. You can: use Codex as the independent second opinion on client deliverables and the fast lane for bounded implementation.

## The prime rules (your vault's, verbatim in spirit)

1. **Always in a git repo; `git status` before and after.** Codex without git is a chainsaw without a chain brake.
2. **Read-only orient first** (`codex exec "..."`), *then* bounded implementation (`--full-auto`), *then* review.
3. **`--full-auto` only for bounded tasks** — right repo, understood status, no prod creds in reach.
4. **You commit; Codex never pushes or deploys.**
5. **Never let Codex handle raw secrets.**

*Companion academy: [../Master Claude Guide/00 START HERE — Claude Code Mastery Path](../../Claude%20Code/Guides/00%20START%20HERE%20%E2%80%94%20Claude%20Code%20Mastery%20Path.md) — do that one first if you're choosing; Codex mastery assumes Claude fluency.*
