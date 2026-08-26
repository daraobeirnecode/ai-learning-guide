---
title: "n8n SMB Master Playbook — Claude Code deploy pattern"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# n8n SMB Master Playbook

This folder contains 20 production-ready n8n workflows small businesses actually need. Each workflow has its own file with the exact Claude Code deploy prompt, node structure, LLM agent integration, error handling, and required credentials.

Read this playbook once. Then work through the individual workflow files whenever you (or a client) need one live.

## The shared deployment pattern

Every workflow in this folder follows the same six-step deployment:

1. **Set up credentials in n8n** (Settings → Credentials) — each workflow lists which credentials it needs and the exact scopes.
2. **Launch Claude Code inside your n8n project directory.** For self-hosted n8n, that's typically `~/code/n8n-workflows/` where you keep exported JSON versioned in git.
3. **Paste the workflow's Claude Code deploy prompt.** Fable 5 for a new workflow scaffold; Sonnet 4.6 to iterate.
4. **Claude Code produces the workflow JSON** at `workflows/<slug>.json` and gives you the `n8n import:workflow --input=workflows/<slug>.json` command.
5. **Test with the workflow's test procedure** — every file has a "Testing" section.
6. **Activate the workflow** (top-right toggle in n8n) and monitor the first 24 hours through the executions log.

If you're on n8n Cloud instead of self-hosted, replace step 4 with "paste the produced JSON into the n8n editor via Menu → Import from Clipboard."

## Required Claude Code + n8n setup (do once)

**Local project structure:**

```bash
mkdir -p ~/code/n8n-workflows/{workflows,credentials-schemas,tests,docs}
cd ~/code/n8n-workflows
git init && git branch -m main

# CLAUDE.md at repo root
cat > CLAUDE.md <<'EOF'
# n8n workflows for small business

## Purpose
Versioned, git-tracked n8n workflows deployed to our self-hosted (or Cloud) n8n instance.

## Conventions
- Workflow JSON in workflows/<slug>.json
- Slug is kebab-case, e.g. lead-capture-crm
- Every workflow has an Error Trigger node routing to a shared "notify-error" workflow
- Every workflow has a Sticky Note documenting: purpose, trigger, owner, last-modified
- Every LLM call is a Function node calling Claude via HTTP Request (not the built-in AI nodes — we want explicit prompt control)
- Timeout defaults: 30s for Haiku, 60s for Sonnet
- Credentials use the exact names from the workflow's Credentials section — never rename

## Never
- Never commit workflow JSON exports that contain credential values (n8n exports strip them, but double-check)
- Never activate a new workflow in production before the test suite passes
- Never bypass the Error Trigger routing to notify-error
EOF

# .gitignore
cat > .gitignore <<'EOF'
.env
.env.local
*.credentials.json
credentials-cache/
EOF
```

**Global n8n MCP wiring for Claude Code** (`~/.claude/config.json`):

```json
{
  "mcpServers": {
    "n8n": {
      "command": "npx",
      "args": ["-y", "n8n-mcp"],
      "env": {
        "N8N_API_URL": "$N8N_API_URL",
        "N8N_API_KEY": "$N8N_API_KEY"
      }
    }
  }
}
```

Restart Claude Code. Now `claude` sessions can list, import, activate, and log-check workflows via the n8n MCP.

## Shared error handling: the notify-error workflow

Every workflow in this folder routes failures to a single `notify-error` workflow. Deploy this ONCE before any others.

**Claude Code prompt for `notify-error`:**

```
Create an n8n workflow at workflows/notify-error.json that:
- Trigger: Manual + Webhook (n8n-webhook-id: notify-error)
- Node 1: Set node — normalizes the incoming error payload with fields
  {source_workflow, execution_id, error_message, error_stack, at}
- Node 2: Function node — categorizes the error via Anthropic Haiku 4.5
  ("transient" / "config" / "credential" / "external-api" / "bug") using
  the HTTP Request node calling api.anthropic.com/v1/messages with the
  ANTHROPIC_API_KEY credential
- Node 3: Switch — routes by category
  - "credential" → immediate Telegram to admin chat + Slack #ops-urgent
  - "external-api" → Slack #ops-alerts with retry hint
  - "transient" → log to Google Sheet "n8n error log", no notify
  - "config" / "bug" → Slack #ops-alerts + GitHub Issue in your workflows repo
- Node 4: Google Sheets — appends to "n8n error log" tab with the normalized payload
- Node 5: Set node — returns a structured response for the calling workflow

Credentials: Anthropic API, Slack (bot with #ops-alerts + #ops-urgent access),
Telegram (bot token + admin chat ID), Google Sheets (service account with
edit access to the "n8n error log" sheet), GitHub (PAT with issues write).
```

Every subsequent workflow references this by webhook URL. Change nothing in this workflow without regression-testing every downstream workflow.

## Shared credentials required across the SMB catalog

Set these up in n8n BEFORE deploying any workflow. Every workflow references credentials by these exact names.

| Credential name | Type | Purpose | Scopes needed |
|---|---|---|---|
| `Anthropic API` | HTTP Header Auth | LLM calls (Claude Sonnet/Haiku) | header: `x-anthropic-key`, value from console.anthropic.com |
| `OpenAI API` | HTTP Header Auth | Optional; some workflows use GPT-4o mini | Bearer token |
| `Google Sheets` | Service Account | Read/write ops logs, error log, financial digests | https://www.googleapis.com/auth/spreadsheets |
| `Google Calendar` | OAuth2 | Appointment workflows | https://www.googleapis.com/auth/calendar |
| `Gmail` | OAuth2 (per operator seat) | Send + read email | https://mail.google.com/ |
| `Slack Bot` | Slack API | Notifications | chat:write, files:write, users:read |
| `Telegram Bot` | Telegram API | Admin alerts | full bot API |
| `Stripe API` | HTTP Header Auth | Revenue workflows | restricted key, at minimum read invoices/customers |
| `HubSpot` | OAuth2 | CRM workflows | crm.objects.contacts.write, crm.objects.deals.write |
| `Airtable` | API Key | Backup CRM if not HubSpot | full access to relevant base |
| `Twilio` | HTTP Basic Auth | SMS workflows | Account SID + auth token |
| `Composio` | API Key | Client credential brokerage (when serving external clients) | full |
| `GitHub` | Personal Access Token | Repo automations | repo, issues, workflows |
| `Notion` | Internal Integration Token | Knowledge base updates | insert content, read content |
| `QuickBooks Online` | OAuth2 | Accounting workflows | Accounting scope |
| `Xero` | OAuth2 | Alternative accounting | accounting.transactions, accounting.contacts |
| `AWS S3` | Access Key + Secret | File storage workflows | s3:PutObject on the target bucket |
| `Resend` | HTTP Header Auth | Transactional email | domain-restricted API key |

Not every workflow uses every credential. Each workflow file names which subset it needs.

## Universal error handling pattern in every workflow

Every workflow file in this folder implements this pattern. It's cheap and catches 95% of production issues:

- **Error Trigger node** at the top of every workflow → sends payload to `notify-error` webhook
- **HTTP Request nodes** have `Retry on Fail` enabled with 3 attempts + exponential backoff (base 1s, max 30s)
- **Function nodes** that call LLMs wrap the API call in try/catch and emit a structured `error` field the downstream Switch node routes on
- **Rate-limited API calls** (like Stripe, Slack) use n8n's built-in rate-limit handling — do not bypass
- **Credential rotation** — every 90 days, run `~/code/n8n-workflows/scripts/rotate-credentials.sh` (Claude Code produces this in each workflow's deploy prompt) which rotates the corresponding stored value and re-imports the workflow

## Model choice per workflow

To keep costs sane, workflows use the cheapest model that reliably does the job. The pattern:

- **Haiku 4.5** — classification, extraction from short text, deterministic labeling. ~90% of workflow LLM calls.
- **Sonnet 4.6** — drafting emails/messages that a human will send, summarizing multi-source content, decision-making with context. ~9%.
- **Opus 4.6** — only where reasoning quality is the product (e.g. contract redlining, complex analytical narratives). ~1%.
- **Fable 5** — never used inside n8n workflows themselves; Fable is for Claude Code sessions building the workflows.

Each workflow file names which model each node uses.

## Cost envelope

Rough monthly cost of running all 20 SMB workflows against a typical small business (say a 15-person services firm processing ~500 leads/month, ~200 invoices/month, ~800 customer emails/month):

- n8n Cloud Pro tier: $50/mo (or self-hosted on a $6 Hetzner box)
- Anthropic API (all workflows combined): $15-40/mo
- OpenAI API (optional): $0-15/mo
- Twilio SMS: $2-10/mo
- Third-party service subscriptions (Slack, HubSpot, etc.) — separate from n8n cost, business-normal
- **Total incremental cost of the AI-orchestration layer: $70-115/month**

Contrast with hiring even a 20-hour/month VA at $25/hr = $500/mo, and the ROI is stark.

## Deployment order

If you're standing up all 20 for the first time, deploy in this order — later workflows depend on earlier ones:

1. `notify-error` (per this playbook) — before anything else
2. `01 Lead Capture and CRM Enrichment`
3. `02 Website Contact Form Router`
4. `03 Customer Support Triage`
5. `04 Appointment Reminders`
6. `05 Review Request Automation`
7. `06 Invoice Categorization`
8. `07 Vendor Invoice OCR Approval`
9. `08 Weekly Financial Digest`
10. `09 Client Onboarding Flow`
11. `10 Contract Expiration Reminder`
12. `11 Support Ticket SLA Monitor`
13. `12 Google Reviews Monitor`
14. `13 Newsletter Subscriber Management`
15. `14 Meeting Notes to CRM`
16. `15 Refund Request Handler`
17. `16 Employee Time-Off Router`
18. `17 Social Media Cross-Poster`
19. `18 Inventory Low-Stock Alert`
20. `19 Employee Onboarding Kickoff`
21. `20 Weekly Executive Briefing`

## What each workflow file contains

Every file in this folder has the same eight sections:

1. **Purpose + business value** — one paragraph
2. **Trigger + cadence** — when it fires
3. **Credentials required** — subset of the table above
4. **Node structure** — the exact n8n node list in order
5. **Agent (LLM) nodes** — with the prompt text ready to paste
6. **Error handling specifics** — beyond the shared pattern
7. **The Claude Code deploy prompt** — paste-ready, produces the workflow JSON
8. **Testing** — the exact test procedure before activation

Read all eight before deploying.

## Employer boundary (for the operator specifically)

None of these workflows can touch a municipal government data or City-owned systems. If a client engagement uses these for their business, provision them on a per-client tenant's n8n instance (Hetzner box or their n8n Cloud account), never on your dev box. File the outside-employment disclosure before charging for any client's workflow build.

## The one-line summary

Deploy `notify-error` first. Then walk down the numbered list. Every file has a paste-ready Claude Code prompt. Total build time for all 20 with a first-time operator: about 2 weekend evenings. Cost per month: ~$100 all-in.
