---
title: "Docker and Docker Compose"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Docker and Docker Compose

## Plain-English definition

**Docker** is software that runs applications inside *containers*. A container is a sealed box holding one application plus everything it needs to run — its code, libraries, and settings — isolated from the rest of the computer. Think of shipping containers: standardised boxes that can be moved between ships and trucks without anyone caring what's inside. Docker does the same for software: an app packaged as a container runs identically on a laptop, a Hetzner server, or anywhere else Docker exists.

**Docker Compose** is the companion tool that runs *several* containers together as one application stack, defined in a single YAML text file.

## How Docker actually works

- An **image** is a frozen template: a snapshot of an application and its dependencies, published by its developers (e.g., the official n8n image). Images are downloaded ("pulled") from registries like Docker Hub.
- A **container** is a running copy of an image. You can stop it, restart it, or delete it and start a fresh one from the same image — the app inside always starts from the same known-good state.
- A **volume** is persistent storage attached to a container. Containers themselves are disposable; anything that must survive (databases, workflow data) lives in volumes.
- Containers are isolated using Linux kernel features (namespaces and cgroups): each one gets its own view of the filesystem, network, and processes. Unlike a virtual machine, containers share the host's kernel, so they are lightweight — starting in seconds and using little overhead.
- Docker also creates a **private internal network** between containers. This is why n8n can call [LiteLLM](LiteLLM.md) at the address `http://litellm:4000` — Docker's internal DNS resolves the service name `litellm` to the right container, entirely inside the server.

## How Docker Compose works

Compose reads a file — here `stack/docker-compose.yml` — that declares the whole stack:

- which **images** to run (pinned to exact versions for reproducibility);
- what **environment variables** to inject (secrets come from the `.env` file rendered by SOPS and age);
- which **volumes** hold persistent data;
- which **ports** to publish, and on which IP (everything binds to the [Tailscale](Tailscale.md) IP only);
- **dependencies** (e.g., n8n waits for Postgres to be healthy);
- **restart policies** (containers come back automatically after a crash or reboot).

One command (`docker compose up -d`) brings the entire stack to the declared state. Because the file lives in the GitHub repo, the whole application layer is reproducible from source.

## The containers in the Inish Labs stack

| Container | Runs |
|---|---|
| `inish-labs-postgres-1` | [Postgres](Postgres.md) database |
| `inish-labs-n8n-1` | n8n workflow automation |
| `inish-labs-litellm-1` | [LiteLLM](LiteLLM.md) AI gateway |
| `inish-labs-langfuse-1` | [Langfuse](Langfuse.md) AI observability |
| `inish-labs-code-server-1` | code-server browser VS Code |
| `inish-labs-hermes-1` | Hermes Agent worker |

## Why containers instead of installing directly

- **Isolation**: a bug or compromise in one service doesn't automatically reach the others or the host OS.
- **Clean upgrades**: swap the image version in the Compose file, redeploy, done — no dependency hell on Ubuntu.
- **Reproducibility**: the server can be rebuilt from the repo in minutes.
- **Easy operations**: `docker compose ps` shows health, `docker compose logs` shows what happened, `docker compose restart n8n` fixes one service without touching the rest.

## Related

Ubuntu · SOPS and age · [Postgres](Postgres.md) · [Architecture Overview](Architecture%20Overview.md)
