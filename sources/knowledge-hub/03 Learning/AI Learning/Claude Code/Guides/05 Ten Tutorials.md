---
title: "Master Claude Guide — Ten Tutorials"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 05 — Ten Tutorials (Beginner → Master)

Every tutorial produces a **real Inish Labs asset**. Format: Goal · Time · Steps (with the actual prompts to paste) · Verify · What you mastered. Do them in order; each builds on the last. Prompts are starting points — say more, not less.

---

## Tutorial 1 — First contact (install, doctor, and a vault conversation)
**Level 1 · 45 min · Asset: working Claude Code on [DEVICE REDACTED]/WSL2**

1. In WSL2: `curl -fsSL https://claude.ai/install.sh -o /tmp/claude-install.sh
less /tmp/claude-install.sh
bash /tmp/claude-install.sh` → `claude doctor` until all green. OAuth-login with your subscription.
2. `cd` to a scratch clone of a repo (NOT inside OneDrive — placeholder files break WSL2 reads) and run `claude`.
3. Learn the control surface hands-on — type each: `/model` (pick Sonnet 5), `/effort` (high), `/context`, `/cost`, `Shift+Tab` (watch the mode cycle), `/permissions`.
4. First real task: *"Read the folder `00 Inbox/Inish Labs/Business plan and strategy` (I'll give you the path). Summarize the 90-day plan as a checklist with dates starting Monday. Write it to TODO-90day.md."*
5. Interrupt it once (Esc) mid-task and redirect — learning to steer mid-flight is the skill.

**Verify:** TODO file exists and is right; `/cost` shows what the session cost. **Mastered:** install, auth, modes, steering, cost awareness.

## Tutorial 2 — CLAUDE.md: teach it once
**Level 1 · 1 hr · Asset: project CLAUDE.md for your infra repo**

1. In the (new or existing) `inish-stack` repo: `/init`. Read what it generates — then make it *yours*.
2. Add the Inish Labs guardrails: *"Edit CLAUDE.md: add a Rules section — never bind services to 0.0.0.0 (Tailscale IP only); secrets only via SOPS, never in files or output; conventional commits; Python via uv, Node via pnpm; snapshot before any risky infra change; no CA-public-sector data ever."*
3. Test the memory: open a **fresh session**, ask *"add a quick redis service to the compose file"* — it should bind to the Tailscale IP without being told. If not, tighten the wording.
4. Add `~/.claude/CLAUDE.md` user-level entries for cross-project prefs (answer style, uv/pnpm) — keep both files <200 lines.

**Verify:** the fresh-session test passes. **Mastered:** the memory hierarchy — the highest-leverage 30 minutes in this whole academy.

## Tutorial 3 — Ship workflow #1 (Lead Capture & CRM Enrichment)
**Level 2 · 2 hrs · Asset: the first catalog workflow, running**

1. On LAB (or local n8n): *"Read `05 AI Systems/n8n/SMB Use Cases/01 Lead Capture and CRM Enrichment.md`. Build this as n8n workflow JSON: webhook trigger → parse/enrich → dedupe against the Postgres crm table → insert → draft reply via LiteLLM (model claude-fast). Error branch → Telegram alert. Write to workflows/01-lead-capture.json."*
2. Have Claude import and test it: *"Import via the n8n CLI, fire a test payload with curl, show me the execution result and the CRM row."*
3. Iterate on one real detail (e.g., dedupe key) — notice how giving the *why* improves the fix.
4. Commit. This exact loop is your $1,500 product.

**Verify:** test lead → enriched CRM row + drafted reply. **Mastered:** the build-import-verify loop; n8n-as-code.

## Tutorial 4 — Your first two subagents
**Level 2 · 1.5 hrs · Asset: `code-reviewer` + `gis-architect` in `~/.claude/agents/`**

1. Write `code-reviewer.md` (tools: Read, Grep, Glob only — reviewers don't edit; model: sonnet): body = your review standards + "report every issue with confidence + severity; a downstream filter decides."
2. Write `gis-architect.md` (model: claude-opus-4-8, effort high, `memory-enabled: true`) — body from doc 03 §1.
3. Trigger delegation naturally: *"Use the code-reviewer subagent to review the diff from Tutorial 3."* Then watch background execution: `claude agents`.
4. Observe context isolation: `/context` in the main session stays small while the reviewer churns.

**Verify:** review comes back as a summary; main context stayed lean. **Mastered:** delegation, tool restriction, per-agent models, background agents.

## Tutorial 5 — Skills: brand-check + linkedin-post, stacked
**Level 2 · 2 hrs · Asset: your content engine**

1. `/plugin install anthropic-skills` then use skill-creator: *"Create a skill `brand-check` per the spec in `Master Claude Guide/04` — banned words list from `07 Website Content`, employer-reference scan, violations + rewrites."*
2. Build `linkedin-post` (args: artifact path + day-type; templates from `08 Marketing Material` §3).
3. Test the stack: `/linkedin-post "00 Inbox/Inish Labs/.../05 GIS + AI — 20 Sample Applications.md" fri` then `/brand-check` the output — or stacked: `/brand-check /linkedin-post <path> fri`.
4. Note the progressive disclosure: `/context` — the skills cost almost nothing until invoked.

**Verify:** a postable Friday artifact, zero banned words. **Mastered:** SKILL.md format, arguments, dynamic context, stacking — and your Friday post now takes 4 minutes.

## Tutorial 6 — MCP: talk to your database
**Level 3 · 2 hrs · Asset: natural-language PostGIS access**

1. In the gis repo, create `.mcp.json` with `postgres` (stdio, your LAB DATABASE_URL via Tailscale) and your `esri` server (per the GIS deploy guide §9). `/mcp` to verify both connect.
2. Ask through the wire: *"Using the postgres MCP: which tables exist in the gis database, and how many rows in entities? Then: the 5 nearest entities to [lon, lat] — remember, read-only."*
3. Esri side: *"Using the esri MCP, list feature services matching 'parcels' on the portal, and describe the first one's schema."*
4. Add the guardrail hook from doc 03 §5 blocking destructive Bash — belt and suspenders while MCP is wired.

**Verify:** both servers answer; `claude mcp list` clean. **Mastered:** transports, project-scoped wiring, the security posture.

## Tutorial 7 — The big one: build LAB with Fable 5
**Level 3 · 1–2 evenings · Asset: your production-grade automation server**

This is AI Automation Master Guide deploy executed as a Claude Code exercise.

1. `claude --model claude-fable-5`, `/effort xhigh`. Paste the guide's Phase-1 ⌘ prompt (provision CCX32). Approve each `hcloud` call *deliberately* — you're practicing supervised autonomy.
2. Phases 2–8, one ⌘ prompt each: hardening → Tailscale → Docker → repo/SOPS → core stack → on-box Claude+Codex → Hermes. Let Fable 5 run long turns; interrupt only to correct course.
3. When something fails (it will — a port, a healthcheck), resist fixing it yourself: *"The langfuse healthcheck is failing — diagnose and fix, show me the root cause."* Debugging-by-delegation is the master skill.
4. End: *"Run the full verification checklist from the guide §16 and give me a pass/fail table."* Commit everything.

**Verify:** the guide's checklist passes end-to-end. **Mastered:** long-horizon agentic work, infra-by-conversation, Fable 5's autonomy envelope.

## Tutorial 8 — Fleet work: the parallel vault audit
**Level 3 · 1.5 hrs · Asset: a vault hygiene report + the fan-out pattern**

1. *"Launch 4 Explore subagents in parallel: (1) find all docs still spelling 'Innish'; (2) find pricing numbers that contradict `03 Service Catalog & Pricing`; (3) find broken wikilinks in the Inish Labs + Master Guide folders; (4) list every doc referencing Sacramento in a commercial context. Consolidated report, one section each, file paths as links."*
2. Watch them run in background; keep working in the main thread meanwhile (that's the point).
3. Then try `/batch` on a mechanical fix across worktrees (e.g., the Innish→Inish rename in 00 Inbox only — review each diff).

**Verify:** report lands; you reviewed and applied fixes selectively. **Mastered:** parallelism, worktrees, when fan-out beats a single context.

## Tutorial 9 — Build inishlabs.com from doc 07
**Level 4 · 2–3 evenings · Asset: the live website**

1. New repo `inishlabs-site`. Plan mode first: *"Read `07 Website Content.md` and the Design Guide at `03 Learning/Web Design/01 Innish Labs - Editorial Consulting/Design Guide.md`. Propose the Astro architecture: 5 routes, MDX case studies, dark default, the drop-cap hero, zero client JS except the one scroll divider. Plan only."*
2. Approve → build with Fable 5. Then the QA gates as prompts: *"Grep the built site for the 8 banned words and 'Sacramento' — must be zero. Lighthouse it. Fix what's under 95."*
3. Deploy: *"Set up Cloudflare Pages deploy from the repo, walk me through the DNS step."* (Your first public artifact of the business.)
4. `/code-review high` on the final diff before the deploy commit.

**Verify:** live URL, grep-gates pass, Lighthouse ≥95. **Mastered:** plan-first builds, QA-as-prompts, end-to-end shipping.

## Tutorial 10 — The client drill (provision → deliver → teardown)
**Level 4 · half a day · Asset: proof you can onboard a client in <30 min**

The dress rehearsal for revenue. Fictional client: "Summit HVAC", starter tier.

1. Run your `provision-client` skill (Tutorial 5 pattern + doc 04 #1): snapshot-clone → fresh SOPS secrets → Tailscale → smoke test. **Time it.** Target <30 min.
2. Deploy their bundle: *"Deploy workflows 1, 2, 4, 5 from the catalog to summit-hvac's box, configured from this intake sheet: [paste]. Run each once with test data."*
3. Generate the deliverables: `/proposal` retroactively (practice), then *"produce the client runbook: what runs, where, how to pause it, who to call."*
4. **Teardown drill:** *"Snapshot summit-hvac, delete the server, prove you could restore it — show me the restore command and the snapshot ID."* Cost of the whole drill: pennies.

**Verify:** stopwatch <30 min to green smoke test; runbook exists; teardown clean. **Mastered:** the entire delivery pipeline — you are now dangerous.

---

## After the ten

You've built: a configured environment, the first catalog workflow, an agent roster, a content engine, MCP wiring, the LAB server, a fleet pattern, the public website, and a rehearsed client pipeline. That *is* the Inish Labs launch checklist. Keep the rhythm from doc 00, keep finishing one thing at a time, and let the three-times rule grow the skill library from here.
