---
title: "Langfuse"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Langfuse

## Plain-English definition

Langfuse is an **AI observability platform** — a flight recorder for your AI calls. Every time a workflow or agent sends a prompt to a model, Langfuse can record what was sent, what came back, how long it took, what it cost, and whether it failed. You then browse this history in a web dashboard to understand and improve how your AI systems behave.

Without observability, AI automations are a black box: you know a workflow "used AI" but not what it actually asked, what the model said, or why last Tuesday's output was weird. Langfuse makes all of that inspectable.

## How it actually works

1. **Instrumentation.** Your tools (workflows, agents, or [LiteLLM](LiteLLM.md) itself) are configured with a Langfuse project's public/secret key pair. After each AI call, they send Langfuse a record of the event.
2. **Traces and spans.** Langfuse organises records into **traces** — the full story of one operation, end to end. A trace contains **spans** (steps) and **generations** (individual model calls). A single "generate weekly brief" workflow run might be one trace containing three model calls, and you can drill into each.
3. **Storage and dashboard.** Records are stored in [Postgres](Postgres.md), and the web UI at `http://[IP ADDRESS REDACTED]:3000` lets you search, filter, and inspect them: which prompts ran, which model handled them, token counts, computed costs, latency, and errors.
4. **Beyond logging.** Langfuse also supports prompt versioning (store and compare iterations of an important prompt), scoring/evaluations (rate outputs against a rubric), and datasets (collect good/bad examples for testing) — all future steps for this stack.

Because it is self-hosted here (a [Docker container](Docker%20and%20Docker%20Compose.md)), all of this potentially sensitive data — prompts and responses may contain business or client information — stays on the private server rather than a third-party cloud.

## What it's used for in the Inish Labs stack

Langfuse answers operational and business questions:

- **Which prompts are running**, and what did the model actually reply?
- **What is each workflow costing?** Model usage is metered by token; Langfuse turns that into per-workflow, per-model cost visibility so you can spot expensive automations.
- **Where are the failures?** Repeated model errors or timeouts show up here first.
- **Did quality drift?** Comparing outputs over time reveals when a prompt or model change made results better or worse.
- **Which model is best for a job?** e.g., comparing `claude-fast` versus `gpt` outputs on the same prompt.

Since every AI call in the stack flows through [LiteLLM](LiteLLM.md), LiteLLM is the natural single point to hook Langfuse tracing into — one integration covers n8n, Hermes Agent, and everything else.

## Access and setup

- URL (Tailscale-only): `http://[IP ADDRESS REDACTED]:3000`
- First-time setup: open the URL, create the admin account and a project in the UI, generate the project's public/secret keys, add them to the tool configs that should report traces. Store logins and keys in Bitwarden — never in notes or chat.

## Related

[LiteLLM](LiteLLM.md) · n8n · [Postgres](Postgres.md) · [Architecture Overview](Architecture%20Overview.md)
