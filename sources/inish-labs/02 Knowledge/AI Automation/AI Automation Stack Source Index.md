---
title: "AI Automation Stack — Source Index"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# AI Automation Stack — Source Index

A map of every vault document that references building an **AI Automation service on Hetzner + n8n + Claude Code**. Curated from a full-vault search (164 files reference the three technologies together; these are the ones that actually *teach* the build). The consolidated walkthrough that stitches them together is **[AI Automation Master Guide deploy](AI%20Automation%20Master%20Guide%20deploy.md)**.

> Verified 2026-07-09. Tiering reflects whether each doc contains genuine step-by-step, paste-ready Claude Code build instructions vs. a passing mention.

---

## ⭐ Tier 1 — Genuine step-by-step HOW-TO with Claude Code

Real, paste-ready Claude Code instructions where Hetzner + n8n + Claude Code are all load-bearing.

- How to Build an AI OS - The Novice Runbook — **most explicit.** 40 steps, each with a ready-to-paste Claude Code PROMPT block + verification CHECK (Windows/WSL2 novice framing).
- How to Build an AI OS - The Definitive Step-by-Step Guide — the master reference the Runbook pairs with; 40-step build + a map of every step to its Claude Code automation level.
- Claude Code to Hetzner — First Box Walkthrough — the definitive first-box doc: Claude Code writes the Terraform, runs plan/apply, drives SSH. Tightest Hetzner + Claude Code match.
- Hetzner Deploy - GIS + Hermes + n8n + Claude Code - Fable 5 Master Prompt — paste-ready Fable 5 prompt that scaffolds an Ansible provisioner for the exact stack; 5-sprint sequence + verify commands.
- AI OS Hetzner Deploy - Fable 5 Master Guide — most complete/advanced Fable 5 variant (Terraform + Ansible + SOPS, 6-sprint plan, client-provisioning path).
- Innish Labs Hetzner Hermes - Fable 5 Master Build Guide — business-specific version: scaffolds the `innish-ops` docker-compose repo (Postgres/PostGIS, n8n, LiteLLM, Hermes).
- Hetzner Deployment Plan — first-timer numbered plan; Claude Code installed as a first-class component **on** the box (Step 1.17) alongside n8n. (`05 AI Systems/Infrastructure/`)
- Hetzner + n8n — Automation, Backup, Strategy — full Hetzner+n8n build (Terraform/cloud-init/Compose/backups) + a dedicated "Claude + Hetzner" section on driving `hcloud` CLI. **Best snapshot/pause-resume reference.**
- IMPLEMENTATION GUIDE (`00 Inbox/Project Implementation Guides/01 GIS+AI Stack Template/claude-code/`) — 10 steps where Claude Code writes `deploy.sh`/`smoke-test.sh` for the Hetzner core stack.
- IMPLEMENTATION GUIDE (`00 Inbox/Project Implementation Guides/03 Personal AI OS as a Service/claude-code/`) — client install-to-retainer delivery runbook using Claude Code as the driver on CCX13/CCX23.
- GIS AI Operations Platform — Complete Claude Code Build Guide — 12-sprint build, copy-paste Claude Code prompts per sprint. *Caveat: n8n-light (GIS-specific).*

## Tier 2 — Real build guides, Claude Code one tool among several

- GIS + AI Stack — The Ultimate Build Guide — closest to the *full* triad with real setup steps, but Claude Code sits beside Hermes/Codex.
- Building AI Agents on a Virtual Server - GIS and Small Business Guide — heavy n8n/Docker build, Claude listed only as a model option.
- Build Your Own Agentic OS — Step-by-Step Guide — genuine build, but Hermes is the runtime; Claude Code a passing mention.
- AI Operating System — Tech Stack and Implementation Guide — architecture reference with a conceptual phased build.
- Repeatable AI OS — Multi-Vertical Build Spec — productization spec; points to the walkthrough for the actual build.
- Innish Labs — Hetzner Hermes Deployment Plan — the spec that the Fable 5 build guide above operationalizes.
- AI Automation Backend First Workflow Architecture Guide - Reddit r-AiAutomations - 2026-06-27 — Python/FastAPI-centric; Claude Code only a "build accelerator."
- 00 MASTER PLAYBOOK — Claude Code for Every Hermes Project — excellent generic Claude Code methodology; Hetzner/n8n mentioned in passing.

## Tier 3 — Strategy / business / reference (name the stack, no build steps)

- [From Nothing to Paying Customer — Hand-Holding Build Guide](AI%20Stack/From%20Nothing%20to%20Paying%20Customer%20%E2%80%94%20Hand-Holding%20Build%20Guide.md) — GTM plan; points to the Hetzner walkthrough for the build.
- AI accounting service Hermes n8n Claude Code Orgo Hetzner Stack Synthesis 2026-05-28 — roles/strategy for turning the stack into a service business.
- AI Automation Consulting — Tooling and Skills Guide — consultancy reference; stack named as the default picks.
- Personal AI OS as a Service — Productized Service Plan — productized-service plan (Hermes-based runtime).
- AI Agency Stack Addendum - Tools Hosting and Costs — hosting-and-cost reference addendum.

## Supporting references

- [n8n personal/00 README - n8n Personal Master Playbook](n8n%20personal/00%20README%20-%20n8n%20Personal%20Master%20Playbook.md) and [n8n smb/00 README - n8n SMB Master Playbook](n8n%20smb/00%20README%20-%20n8n%20SMB%20Master%20Playbook.md) — the n8n workflow libraries this box will run.
- Authenticated Gmail with n8n — Full Setup Guide — OAuth-into-n8n pattern.
- MASTER PLAN — the operator's Single Source of Truth — where this work sits in the wider plan.

---

*The remaining ~140 hits are mostly per-service `SETUP.md` / `CLAUDE.md` files under `00 Inbox/Fable 5/100 Hermes Business Services/` that name the stack in passing. Ask if you want that exhaustive list too.*
