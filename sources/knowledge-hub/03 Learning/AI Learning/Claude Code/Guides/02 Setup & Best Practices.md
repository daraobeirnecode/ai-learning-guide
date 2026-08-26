---
title: "Master Claude Guide — Setup & Best Practices"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 02 — Setup & Best Practices

Getting Claude Code installed, configured to *your* conventions, and the operating habits that separate a master from a user. Environment detail beyond this doc: `03 Learning/AI Learning/Claude/Lessons/Environment Configuration.md` (still current).

---

## 1. Install (July 2026 — native installer is now the recommended path)

```bash
# macOS / Linux / WSL2  (auto-updating native build — preferred over npm now)
curl -fsSL https://claude.ai/install.sh -o /tmp/claude-install.sh
less /tmp/claude-install.sh
bash /tmp/claude-install.sh

# Windows PowerShell (native)
Invoke-WebRequest https://claude.ai/install.ps1 -OutFile $env:TEMP\claude-install.ps1
Get-Content $env:TEMP\claude-install.ps1
& $env:TEMP\claude-install.ps1

# Alternatives: brew install --cask claude-code · winget install Anthropic.ClaudeCode
# npm install --global @anthropic-ai/claude-code@2.1.246 still works (needs Node 22+)

claude --version && claude doctor      # doctor = full health check (now a bundled skill)
```

**Your machines:** macOS workstation already runs it — just `claude update`. **[DEVICE REDACTED] (Windows): install into WSL2** with the curl line above (native Windows works too, but your stack docs assume WSL2). Vault gotcha to respect: OneDrive placeholder files break WSL2 reads — keep working repos outside OneDrive; the vault is read via the Windows side.

**Auth:** first run of `claude` opens browser OAuth — use your Claude subscription (covers usage; no per-token billing). `ANTHROPIC_API_KEY` is the alternative for headless/CI. Never both confusedly: subscription for interactive, key for automation.

## 2. Your configuration (the established canon)

Your global `~/.claude/CLAUDE.md` already exists (canonical copy: `03 Learning/AI Learning/Claude/Lessons/CLAUDE.md`). The load-bearing conventions it encodes — keep these stable across machines:

- **Python 3.12 + `uv`** (never pip/poetry directly) · **Node 22 + `pnpm`** (never npm)
- **Postgres 18 + PostGIS + pgvector + AGE** is the default data layer; *"Postgres is the default RAG/vector store, not Pinecone"*
- **MapLibre** for OSS/portfolio maps; ArcGIS JS API only in Esri-paid client work
- **n8n for predictable pipes, Hermes for judgment-heavy steps** (the hybrid rule)
- Cloudflare R2/Tunnel, Caddy, Hetzner — per the Inish Labs stack doc
- Style: frank, lead with the answer, conventional commits, ship small (>8 files → 3 commits)

**settings.json starting point** (`~/.claude/settings.json`):

```json
{
  "model": "claude-sonnet-5",
  "permissions": {
    "defaultMode": "acceptEdits",
    "allow": ["Bash(git status)", "Bash(git diff *)", "Bash(git log *)", "Read(**)"],
    "deny": ["Read(.env)", "Read(**/secrets*)", "Bash(rm -rf *)"]
  }
}
```

Model discipline (your rule, current names): **Sonnet 5 daily · Haiku 4.5 for batch/subagents · Opus 4.8 / Fable 5 as a deliberate splurge** (`claude --model claude-fable-5` for the big scaffolds, per the deploy guides). Watch spend with `/cost` and `/context`; treat ~$5/session as the default ceiling and decide consciously when a build justifies more.

**Per-project:** run `/init` in each repo to generate a project `CLAUDE.md`, then edit it to encode that repo's truths (commands, architecture, boundaries). The Inish Labs guardrails — *never bind 0.0.0.0, secrets only via SOPS, no CA-public-sector data, LLM never writes raw spatial SQL* — belong in the repo CLAUDE.md files, where every future session inherits them.

## 3. The session playbook (how masters run a session)

1. **One sentence of intent** before anything: *"Goal: workflow #7 deployed to DEMO and verified."* No goal, no session.
2. **Right mode for the risk:** plan mode (`Shift+Tab` twice or `/plan`) for anything architectural or destructive; acceptEdits for normal build flow; default when touching credentials/infra.
3. **Give the why, not just the what.** *"I'm prepping the DEMO server for Tuesday's sales call — seed it with…"* beats a bare command; Claude routes ambiguity better with intent.
4. **Let it verify.** End requests with the verification built in: *"…then run the smoke test and show me the output."* Never accept "should work."
5. **Checkpoint at milestones:** commit early and often; Claude's own git history is your undo.
6. **End with a landing:** commit + one-line note (or `/recap`). Sessions that end mid-air cost you the next session's first 20 minutes.

## 4. Best practices (the compounding habits)

| Habit | Why it compounds |
|---|---|
| **Plan before build** on anything >30 min | Misunderstandings die in plan mode for pennies |
| **CLAUDE.md over repetition** | Anything said twice goes in the file; the file teaches every future session |
| **Skills over CLAUDE.md bloat** | Keep CLAUDE.md <200 lines; overflow becomes lazily-loaded skills (doc 03) |
| **Subagents for context isolation** | Big explorations/reviews run in a fork; your main context stays lean |
| **Small tool surface** | Only wire the MCP servers a project needs — every idle server costs context |
| **Verify > trust** | Tests, smoke scripts, `curl` checks — make Claude prove it |
| **Fresh session per task** | Long meandering sessions degrade; `/compact` helps, a clean start helps more |
| **Dictate long specs** | Your best sessions start with a rich paragraph of intent — say more up front |
| **Review diffs like a lead** | You're the reviewer of record; `git diff` before every commit — always |
| **The three-times rule** | Third repetition of any instruction = write the skill that day |

## 5. Anti-patterns (observed in your own vault's lessons — avoid)

- **Plan-as-progress:** producing beautiful plans and no artifact. One build at a time, finished.
- **Context stuffing:** pasting whole files/URLs "for context" that a Grep would have found.
- **Permission fatigue → bypassPermissions on the host.** Never. If you need full-auto, do it in a container or throwaway VM.
- **Model maximalism:** Fable 5 for renaming variables. Match tier to task.
- **Secrets in prompts.** Claude reads `.env` only if allowed; keep the deny rules and use SOPS — a secret in chat history is a secret in history.
- **The 40-ideas trap:** Claude Code makes starting cheap; the discipline is *finishing* — that's a you-rule, not a tool-rule.

---

*Next: [03 Agents, MCP, Commands & Skills](03%20Agents%2C%20MCP%2C%20Commands%20%26%20Skills.md) — the four systems that turn a good session into an operation.*
