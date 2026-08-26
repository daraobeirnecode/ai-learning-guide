---
title: "Master Codex Guide — Ten Tutorials"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 05 — Ten Tutorials (Beginner → Master)

Ten hands-on tutorials, deliberately **complementary to the Claude academy's ten** — these play to Codex's strengths (bounded implementation, independent review, the pair pattern) and produce Inish Labs assets. Format: Goal · Time · Steps · Verify · Mastered. Template numbers (#) refer to [04 The 20 Starter Prompts & Skills](04%20The%2020%20Starter%20Prompts%20%26%20Skills.md).

---

## Tutorial 1 — Health check & first safe session
**Level 1 · 30 min · Asset: verified working Codex + your first orientation**

1. `codex --version` → `brew upgrade codex` if stale. Auth check, your canonical way: `cd "$(mktemp -d)" && git init -q && codex exec "Say hello and create no files."` — no API-key prompt = healthy.
2. `cd` into a real repo (the inish-stack or site repo). `codex --profile safe`, then in-session: `/help` — read what *this* build actually offers (the surface moves; this habit is the lesson).
3. Run template **#1 orient**. Compare its architecture summary to your own understanding — note one thing it saw that you'd have missed.

**Verify:** clean dry-run; an orientation summary you'd trust. **Mastered:** auth hygiene, profiles, read-only-first.

## Tutorial 2 — AGENTS.md: standing orders
**Level 1 · 1 hr · Asset: project AGENTS.md for the inish-stack repo**

1. Review the global file: *"Read ~/.codex/AGENTS.md and tell me, in a table, what it instructs you to do and not do."* (Making the agent recite its orders is the fastest audit.)
2. Write the project file — `codex --profile builder`: *"Create AGENTS.md for this repo: purpose (Inish Labs automation stack), commands (make up / make logs / make audit / pytest), architecture map from the compose file, rules — never commit .env or decrypted secrets; never bind 0.0.0.0; staging data only; never touch a client-* server without explicit confirmation — and definition of done (build passes, tests pass, diff reviewed)."*
3. Test it like Tutorial 2 of the Claude academy: fresh session, ask for a compose change, watch the rules hold. Then check the pair: does the repo's CLAUDE.md duplicate the critical commands? Align both per doc 03 §1.

**Verify:** fresh-session rule adherence. **Mastered:** the AGENTS.md/CLAUDE.md division; instruction auditing.

## Tutorial 3 — The bounded build (`--full-auto` done right)
**Level 2 · 1.5 hrs · Asset: a utility the business needs, built the disciplined way**

1. Branch: `git checkout -b ai/backup-verify-script`. Confirm clean: `git status --short`.
2. Template **#7**: *"Create scripts/verify_backup.py: … lists the newest backup files in b2:gis-ai-backups via rclone, checks age <26h and size >0, exits non-zero with a plain-English report otherwise. --dry-run mode. Run dry-run."* with `--full-auto`.
3. **You** review: `git diff` line by line. Then template **#2 diff-review** — watch it critique its own work.
4. Commit yourself. Note what `--full-auto` did *not* do (commit, push, wander) — the boundaries held because the prompt drew them.

**Verify:** dry-run output sane; diff reviewed twice (you + Codex). **Mastered:** the 7-step ritual end-to-end.

## Tutorial 4 — The reviewer: Codex judges Claude
**Level 2 · 1 hr · Asset: your first cross-review, on real code**

1. Take any diff Claude Code produced this week (Tutorial 3 or 9 of the Claude academy). On that branch: `codex --profile review`.
2. Template **#3 second-opinion** (point it at the work order / guide section Claude built from). Read the review with the right frame: *disagreement is the product* — you paid for a different brain.
3. Triage its findings into: real (fix), style (ignore), wrong (note why — this calibrates your trust). Send real ones back to Claude to fix, then have Codex re-review. One full cross-review cycle.

**Verify:** at least one finding triaged in each bucket (usually happens). **Mastered:** the second-opinion discipline; calibrated trust.

## Tutorial 5 — n8n Code nodes: the judgment steps
**Level 2 · 1.5 hrs · Asset: production Code nodes for catalog workflows**

1. Workflow #3 (Support Triage) needs its classification step. Template **#8 n8n-code-node**: *"…classify a support email into sales/support/billing/urgent from subject+body keywords before the LLM sees it (cheap pre-filter), return [{json: {category, confidence, reason}}]…"*
2. Paste into n8n on LAB, run the 3 test payloads Codex included, fix any drift by feeding the actual n8n error back to Codex verbatim.
3. Repeat for workflow #7's approval-threshold router. Two judgment steps, tested, in an afternoon — note this pattern is exactly what the $500/mo retainer's "one new workflow a month" costs you to deliver.

**Verify:** both nodes pass their own test payloads inside n8n. **Mastered:** the Code-node contract; feeding runtime errors back as prompts.

## Tutorial 6 — The pair pattern, full loop
**Level 3 · 2 hrs · Asset: WORK-ORDER.md protocol, proven**

The keystone tutorial. Pick a bounded feature (e.g., add `/api/layers/{id}/freshness` PATCH to the spatial-rag service).

1. **Claude Code** (plan mode): *"…design this endpoint and write WORK-ORDER.md: task, constraints (typed, tested, follows router pattern), files to touch, definition of done, test command. Don't implement."*
2. **Codex** (`builder`): template **#6 work-order**. It implements; tests go green.
3. **Claude Code**: `/code-review high` on Codex's diff. **Codex** (`review`): template #2 on its own diff after Claude's fixes land.
4. You arbitrate anything they disagree on; commit. Write 3 lines in the vault: what each engine caught.

**Verify:** endpoint works; both reviews happened; the work order file is reusable as a template. **Mastered:** the handoff protocol — git as the interface between agents.

## Tutorial 7 — The ArcPy migration drill (the $9,500 muscle)
**Level 3 · 2–3 hrs · Asset: a migrated script + paired test — your Sprint deliverable pattern**

1. Pick one real ArcPy script (from your old projects or a public sample). `codex --profile safe`: template **#5 test-gap** first — what behavior must be preserved?
2. `builder` + template **#14 arcpy-migrate**. Watch the paired-test discipline: same inputs → outputs within tolerance.
3. Have it flag the un-migratable parts honestly (that honesty is what the client pays $9,500 for). Then **Claude Code** reviews the migration for GIS correctness (its `gis-architect` subagent from the Claude academy).
4. Save the whole trail — orient, plan, migration, paired test, flags — as `samples/sprint-deliverable-example/`. This is a sales asset.

**Verify:** paired test green; flags honest; trail saved. **Mastered:** the Modernization Sprint's technical core, delivered by the pair.

## Tutorial 8 — MCP in Codex: same rails, second driver
**Level 3 · 1 hr · Asset: Codex wired to postgres + esri**

1. In the gis repo: add both servers to `.codex/config.toml` (doc 03 §2 — keys stay in the global config, not the committed file). New session; confirm the tools appear.
2. Template **#15 postgis-query**: *"…which entities within 1km of [point] have no CONTAINED_IN edge?"* — read-only, via the MCP.
3. Compare against Claude running the same question through *its* postgres MCP (Claude Tutorial 6). Same database, two agents, one wiring pattern — you now have redundancy: either agent can inspect production data safely.

**Verify:** both agents answer the same query consistently. **Mastered:** MCP portability; read-only data access from either engine.

## Tutorial 9 — Client prototype in an afternoon (discovery → demo)
**Level 4 · half a day · Asset: the sales-call prototype, Codex-built**

The give-first motion, on the second engine — proving you can produce it even while Claude is busy on a build.

1. Write a one-page `client-brief.md` for a fictional prospect (pick a niche from the automation catalog — say, the P&C brokerage).
2. Template **#17 client-discovery-proto** — outline, Code node, QA checklist, handoff SOP. Then template **#18 integrator-review** to harden it.
3. Wire the outline into n8n on DEMO yourself (or via Claude) — note where the prototype-to-demo seam is manual; that's your provisioning skill's job.
4. Template **#20 runbook** against the result. Total elapsed time is your quotable "prototype sprint" cost basis.

**Verify:** a demo you could screen-share tomorrow + its runbook. **Mastered:** Codex as an independent delivery lane.

## Tutorial 10 — The lab: bounded autonomy, safely
**Level 4 · 1 hr + ongoing · Asset: your experimentation protocol**

1. Create a genuinely disposable playground: `mkdir ~/lab/spike-$(date +%m%d) && cd $_ && git init`. Only here: `codex --profile lab`.
2. Give it something exploratory: *"Prototype three different approaches to scoring parcel road-access from OSM data; write a comparison table of the trade-offs; pick one and defend it."* No approvals — watch how it behaves unsupervised; this calibrates exactly how much you trust `never` mode (answer: this much, no more).
3. Harvest the lesson, not the code: the winning approach gets rebuilt properly in `builder` on the real repo (Tutorial 3 discipline).
4. `rm -rf` the lab dir. Codify your rule: **`lab` profile never sees a repo with secrets, client data, or a remote.**

**Verify:** lesson extracted, lab destroyed, real repo untouched. **Mastered:** the autonomy boundary — the final Codex skill.

---

## After the ten

You now run two engines with distinct jobs and one interface (git): Claude for architecture, first builds, and rich harness work; Codex for bounded implementation, independent review, and fast lanes. Between the two academies you've built the LAB server, the website, the first workflows, the Sprint deliverable pattern, the client drill, and the cross-review habit — the complete technical capability behind the Inish Labs price card. Keep the weekly 2-hour pair block, and let both template libraries grow by the three-times rule.
