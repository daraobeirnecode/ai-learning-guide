---
title: "LiteLLM"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# LiteLLM

## Plain-English definition

LiteLLM is an **AI model gateway** — a piece of middleware that sits between your tools and the AI companies. Your tools make all their AI requests to one local address, and LiteLLM forwards each request to the right provider (Anthropic, OpenAI, or others), returns the answer, and keeps track of what happened.

The plain-English pitch: instead of wiring Anthropic keys into n8n, OpenAI keys into Hermes, and different code for each provider's API format everywhere, every tool talks to **one endpoint, one key, one format** — and LiteLLM handles the messy differences behind the scenes.

## How it actually works

1. **It speaks "OpenAI-compatible".** OpenAI's chat API format became the de facto standard, so most tools already know how to talk to it. LiteLLM presents exactly that format at `http://[IP ADDRESS REDACTED]:4000` (or `http://litellm:4000` from inside Docker). Any tool that can call OpenAI can call LiteLLM.
2. **It translates.** When a request arrives for an Anthropic model, LiteLLM converts the OpenAI-style request into Anthropic's actual API format, attaches the real Anthropic API key (stored server-side in the encrypted env), sends it, and converts the response back. The calling tool never knows or cares which provider was used.
3. **Model aliases.** The config file (`stack/litellm-config.yaml`) defines friendly names that map to real upstream models:

   | Alias | Routes to |
   |---|---|
   | `claude` | Anthropic Claude Opus 4.8 |
   | `claude-fast` | Anthropic Claude Haiku 4.5 |
   | `gpt` | An OpenAI GPT model |

   This means workflows say "use `claude-fast`" and the actual model version can be upgraded in one place later without touching any workflow.
4. **One master key.** Callers authenticate to LiteLLM with a single `LITELLM_MASTER_KEY`. The real provider keys never leave the server config. Rotating providers or keys happens in one file.
5. **Extras when needed.** LiteLLM can also enforce per-model budgets, rate limits, and automatic failover to another provider when one fails — planned future steps for this stack.

## What it's used for in the Inish Labs stack

LiteLLM is the **single doorway to all AI models**. n8n workflows, the Hermes Agent worker, and any future tool on the box all call it instead of calling providers directly. Benefits:

- **One integration** instead of one per provider per tool.
- **Central key management** — provider keys live in one encrypted place.
- **Swappable models** — change an alias's target and every consumer upgrades at once.
- **Central observability** — one choke point where [Langfuse](Langfuse.md) tracing and cost tracking can see everything.

A typical call from an n8n HTTP Request node:

```text
POST http://litellm:4000/v1/chat/completions
Authorization: Bearer <LITELLM_MASTER_KEY>   (stored as an n8n credential, never in the workflow body)
Body: { "model": "claude-fast", "messages": [ ... ] }
```

## Access

- From Tailscale devices: `http://[IP ADDRESS REDACTED]:4000`
- From other containers: `http://litellm:4000`
- List available models: `GET /v1/models` with the master key as a Bearer token.

## Related

n8n · Hermes Agent · [Langfuse](Langfuse.md) · SOPS and age · [Architecture Overview](Architecture%20Overview.md)
