---
title: "Postgres"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Postgres

## Plain-English definition

Postgres (formally PostgreSQL) is a free, open-source **relational database** — a program whose whole job is storing data safely and answering questions about it quickly. "Relational" means data is organised into tables of rows and columns, like rigorous spreadsheets, with enforced rules about what each column may contain and how tables relate to each other. Postgres has been in development since the 1980s and is widely considered the most capable open-source database in existence; huge amounts of the world's software runs on it.

## How it actually works

- **Tables and SQL.** Applications talk to Postgres using SQL (Structured Query Language) — commands like "insert this row", "find all workflows updated since yesterday". The application generates these queries automatically; you never write them yourself in this stack.
- **Transactions.** Postgres guarantees that groups of changes happen completely or not at all (the "ACID" guarantees). If the power dies mid-write, the database recovers to a consistent state rather than corrupting. This is why real applications use a database instead of writing to plain files.
- **A write-ahead log.** Every change is written to a journal before being applied, which is what makes crash recovery and reliable backups possible.
- **One server, many databases.** A single Postgres instance can host several independent databases. Here, one container serves both n8n's database and Langfuse's database.

## What it stores in the Inish Labs stack

| Client | What lives in Postgres |
|---|---|
| n8n | Workflow definitions, execution history, and **encrypted credentials** (encrypted with `N8N_ENCRYPTION_KEY` — see below). |
| [Langfuse](Langfuse.md) | Traces of AI calls: prompts, responses, costs, latency, errors, projects, and users. |

## Security and access model

- Postgres is **not exposed to any network** — not even the Tailscale one. It listens only on Docker's internal network, so the only things that can talk to it are the other containers on the same server ([Docker and Docker Compose](Docker%20and%20Docker%20Compose.md)).
- Its password lives in the encrypted secrets file.
- A critical subtlety: n8n encrypts credentials *before* storing them in Postgres, using `N8N_ENCRYPTION_KEY`. A database backup alone is not enough to recover n8n credentials — you also need that key (kept in Bitwarden). Losing the key makes the stored credentials permanently unreadable.

## Backups

The nightly [backup script](Backups%2C%20Cron%20and%20Snapshots.md) runs `pg_dump`, which asks Postgres to serialise every database into a plain SQL file (`pg-*.sql.gz`) that can rebuild it from scratch. A restore was tested into a disposable container and succeeded.

## Related

n8n · [Langfuse](Langfuse.md) · [Docker and Docker Compose](Docker%20and%20Docker%20Compose.md) · [Backups, Cron and Snapshots](Backups%2C%20Cron%20and%20Snapshots.md) · [Architecture Overview](Architecture%20Overview.md)
