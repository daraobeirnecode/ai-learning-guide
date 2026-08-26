---
title: "AI Automation Master Guide deploy"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# AI Automation Master Guide — Deploy

**The single, end-to-end walkthrough** for standing up the foundational stack of an AI automation business on one Hetzner server: **n8n + Hermes agent + Claude Code + Codex + LiteLLM + Postgres**, driven as much as possible by **Claude Code (Fable 5) running from your macOS workstation**, and locked down as a **highly secure environment**.

> **How to read this.** This is a reference you work through phase by phase, not a Saturday sprint. Each phase has a clear stop point. Commands you run literally are in `code blocks`. Things you replace are in `<ANGLE_BRACKETS>`. The **⌘ Claude Code prompt** callouts are the paste-ready blocks that let Claude Code do the work for you.
>
> Companion docs (deeper on individual pieces): Hetzner + n8n — Automation, Backup, Strategy (snapshots, backups, Terraform), Hetzner Deployment Plan (numbered hardening steps), Claude Code to Hetzner — First Box Walkthrough (infra-as-code first box), and the full map in AI Automation Stack — Source Index.

---

## Contents

1. What you're building (architecture + decisions)
2. The Claude-Code-first philosophy (how much Claude can do)
3. Prerequisites & accounts
4. Phase 0 — macOS workstation setup + SSH key
5. Phase 1 — Hetzner account, project, first server
6. Phase 2 — First connection & OS hardening
7. Phase 3 — Tailscale (secure access, zero public ports)
8. Phase 4 — Docker
9. Phase 5 — Project repo & secrets (SOPS + age)
10. Phase 6 — The core stack (Postgres, n8n, LiteLLM, Langfuse)
11. Phase 7 — Claude Code on the server + Codex
12. Phase 8 — Hermes agent
13. Phase 9 — DNS & Cloudflare Tunnel (when you actually need DNS)
14. Phase 10 — Backups (three layers)
15. **Snapshots & cloning — dev / test / prod** (your snapshot question, answered)
16. Security hardening checklist
17. The single Claude-Code-from-Mac-mini workflow
18. Come-back-later cheat sheet
19. Cost reality

---

## 1. What you're building

One Hetzner Cloud VPS running a Docker Compose stack. Everything that matters lives in a git repo or can be regenerated from it — the server is **cattle, not a pet**.

```
                 macOS workstation (you)                          Hetzner VPS  (example-ai-server)
   ┌─────────────────────────────┐         Tailscale     ┌──────────────────────────────────────┐
   │ Claude Code (Fable 5)  ──────┼──── SSH / Remote-SSH ─┼──► Docker Compose stack:             │
   │ Codex CLI                    │      (no public 22)   │      • postgres   (n8n + app DBs)     │
   │ hcloud CLI                   │                       │      • n8n         (workflows)        │
   │ Terraform / OpenTofu (opt.)  │                       │      • litellm     (model router)     │
   └─────────────────────────────┘                       │      • hermes      (agent runtime)    │
                                                          │      • langfuse    (LLM traces)       │
   Public inbound (only when needed):                     │      • code-server (browser VS Code)  │
   Cloudflare Tunnel ──► n8n webhooks / public URLs       │      • cloudflared (outbound tunnel)  │
                                                          │    + Claude Code & Codex installed    │
                                                          └──────────────────────────────────────┘
```

**Decisions baked in (and why):**

| Decision      | Choice                                                              | Why                                                                                                                          |
| ------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Server        | Hetzner **CX32** (4 vCPU / 8 GB / 80 GB) to start                   | 2× headroom over the stack's ~2.5–4 GB footprint; room for a local Ollama router later. Resize in-place in ~5 min if needed. |
| OS            | Ubuntu 24.04 LTS                                                    | Long support, best Docker story.                                                                                             |
| Runtime       | Docker Compose                                                      | Rebuild-ability is the whole game for a one-person op.                                                                       |
| n8n DB        | Postgres (not SQLite)                                               | Corruption risk under concurrent webhook writes; migration later is painful.                                                 |
| Access        | **Tailscale only**, zero public ports in Phase 1                    | Eliminates ~90% of attack surface. Public ingress added deliberately, per-service, via Cloudflare Tunnel.                    |
| Secrets       | **SOPS + age** committed encrypted to git; private key in Bitwarden | File-level encryption you can commit, no daemon, disaster-recoverable.                                                       |
| Model routing | **LiteLLM** in front of Anthropic/OpenAI/local                      | One endpoint, cost caps, per-key budgets, provider-swappable.                                                                |
| Ingress       | **Cloudflare Tunnel**                                               | Server dials out — no inbound ports, and a resumed server's new IP is a non-event.                                           |
| Environments  | One box now; **snapshot/Terraform to clone** dev/test/prod later    | Don't pay for separation you don't need yet — but build it clone-ready from day one (§15).                                   |

---

## 2. The Claude-Code-first philosophy — how much can Claude do?

You run Claude Code **from the macOS workstation** and point it at the server over SSH/Remote-SSH. Claude Code does the writing, running, and verifying; you approve and watch. Use **Fable 5** — the most capable model — for the build:

```bash
claude --model claude-fable-5      # alias: claude --model fable-5
```

> **Fable 5 notes (from the Claude API reference):** thinking is always-on (don't pass a `thinking` flag); control depth with effort, not a token budget; turns on hard tasks can run several minutes — let it work. It's excellent at long-horizon, multi-step agentic execution, which is exactly this job.

**What Claude Code can own end-to-end (FULL):**

- Write every file: `docker-compose.yml`, `.env.example`, `.sops.yaml`, `Makefile`, `cloud-init.yaml`, Terraform, backup scripts, the Cloudflared config, per-service `CLAUDE.md`.
- Drive the `hcloud` CLI: list/create/snapshot/resize servers, manage firewalls, SSH keys, images.
- Run remote commands over SSH: install Docker, bring the stack up, tail logs, run `pg_dump`, verify health.
- Author and iterate n8n workflows as JSON, commit them, and import via the n8n CLI.
- Write and register its own subagents and MCP servers, and a repo-root `CLAUDE.md` that encodes your conventions.

**What stays HUMAN (never automate):**

- First Hetzner signup + ID verification, adding a payment method, 2FA enrolment.
- Generating the SSH keypair passphrase and storing it (you hold the private key).
- Approving any destructive `hcloud`/`docker`/`git` operation.
- Pasting the Anthropic/OpenAI/Cloudflare tokens into your secret store the first time.

**The loop for every phase below:** open the phase, read it, then either run the commands yourself *or* paste the **⌘ Claude Code prompt** and let Claude do it — reviewing each diff/command before you approve.

---

## 3. Prerequisites & accounts

Create these first (each is a HUMAN step):

- **Hetzner Cloud** account — console.hetzner.cloud (ID verification can take 1–24 h).
- **Anthropic Console** — console.anthropic.com — an API key for LiteLLM/n8n/Hermes to call (separate from your Claude Code login, which uses its own OAuth).
- **OpenAI** — platform.openai.com — API key for Codex and any GPT routing.
- **GitHub** — an org (e.g. `yourname`) + a private `infra` repo.
- **Cloudflare** — free account + a domain whose nameservers point at Cloudflare (needed only when you go public, §9/§13).
- **Bitwarden** (or 1Password) — the vault of record for the age private key, SSH passphrases, and all API keys.
- **Backblaze B2** (or Hetzner Storage Box) — off-site backup target (~$0.10/mo at this volume).

Naming convention (pick once): server `example-ai-server`; users first-name lowercase (`adminuser`); containers `<service>` (`n8n`, `postgres`); env files `.env` (SOPS-encrypted, never a bare plaintext `.env` in git); Bitwarden items `<Service> - <purpose> (yourname)`.

---

## 4. Phase 0 — macOS workstation setup + SSH key

Everything you drive from lives here. On the macOS workstation (zsh + Homebrew):

```bash
# Core tooling
brew install hcloud sops age tailscale git node
brew install opentofu            # optional: Terraform-compatible IaC
npm install --global @anthropic-ai/claude-code@2.1.246   # Claude Code CLI
npm install --global @openai/codex@0.150.0               # Codex CLI (verify current package name below)

claude --version && claude doctor          # confirm Claude Code is healthy
claude                                     # first run → browser OAuth login
```

> **Codex package:** the OpenAI Codex CLI package name has moved before — if `@openai/codex` errors, ask Claude Code to find and install the current package (`⌘` prompt below), or check platform.openai.com. This is the one line in this guide worth verifying live.

**Generate a dedicated SSH keypair** (keep it separate from any personal key so you can revoke cleanly):

```bash
ssh-keygen -t ed25519 -C "adminuser@yourname-macmini" -f ~/.ssh/hetzner_yourname
# SET A PASSPHRASE when prompted. Store it in Bitwarden: "SSH passphrase - yourname macmini".

# You now have:
#   ~/.ssh/hetzner_yourname       (PRIVATE — never leaves this Mac, never git)
#   ~/.ssh/hetzner_yourname.pub   (PUBLIC — goes on servers / into Hetzner)

pbcopy < ~/.ssh/hetzner_yourname.pub   # public key now on clipboard
```

**⌘ Claude Code prompt — bootstrap the workstation**
```
You are helping me set up a macOS workstation to deploy and manage a Hetzner-based AI
automation stack. Verify that hcloud, sops, age, tailscale, git, node, claude,
and the OpenAI Codex CLI are installed and on PATH; install anything missing via
Homebrew or npm. Find the current OpenAI Codex CLI package name and install it.
Confirm `claude --version` and `codex --version` work. Do not touch my SSH keys.
Report a checklist of what's installed and any versions.
```

**Stop point:** tooling installed, SSH keypair generated, public key on clipboard.

---

## 5. Phase 1 — Hetzner account, project, first server

1. **Project.** Hetzner console → new project `yourname`. (Optionally make a throwaway `practice` project first and destroy a CX22 in it once — cheap muscle memory; see Hetzner Deployment Plan Phase 0.)
2. **Add your SSH key.** Console → Security → SSH Keys → paste `~/.ssh/hetzner_yourname.pub` → name it `example-admin-ed25519`. (Keys are project-scoped.)
3. **API token.** Console → Security → API Tokens → **Read & Write** token → store in Bitwarden as `Hetzner - API token (yourname)`. On the macOS workstation:
   ```bash
   hcloud context create yourname      # paste the token when prompted
   hcloud server-type list              # sanity check the CLI works
   ```
4. **Create the server** (via CLI so it's reproducible — or let Claude Code do it):
   ```bash
   hcloud server create \
     --name example-ai-server \
     --type cx32 \
     --image ubuntu-24.04 \
     --location nbg1 \
     --ssh-key example-admin-ed25519 \
     --label env=prod --label project=yourname
   # Do NOT enable Hetzner's paid backup add-on — we run our own (see §10).
   hcloud server ip example-ai-server   # note the IPv4
   ```

**⌘ Claude Code prompt — provision the box**
```
Using the hcloud CLI with my `yourname` context, create a Hetzner Cloud server:
name example-ai-server, type cx32, image ubuntu-24.04, location nbg1, ssh-key
example-admin-ed25519, labels env=prod and project=yourname. Do not enable the
paid backup add-on. After it boots, print the IPv4, confirm it responds to ping,
and give me the exact `ssh` command to connect as root the first time. Do not run
anything destructive without asking.
```

**Stop point:** server exists, you have its IPv4.

---

## 6. Phase 2 — First connection & OS hardening

```bash
ssh -i ~/.ssh/hetzner_yourname root@<IPV4>     # answer "yes" to the host prompt
```

Then, as root, create your non-root user and lock the box down:

```bash
adduser adminuser                          # set a sudo password; store in Bitwarden
usermod -aG sudo adminuser
mkdir -p /home/yourname/.ssh
cp /root/.ssh/authorized_keys /home/yourname/.ssh/authorized_keys
chown -R adminuser:adminuser /home/yourname/.ssh
chmod 700 /home/yourname/.ssh && chmod 600 /home/yourname/.ssh/authorized_keys

apt update && apt upgrade -y          # patch; reboot if it asks
```

**Test the `adminuser` login in a second terminal before you disable root** (a locked-out box needs Hetzner Rescue mode to recover — practise that once in the `practice` project):

```bash
ssh -i ~/.ssh/hetzner_yourname adminuser@<IPV4>
sudo whoami                           # should print: root
```

Then disable root + password auth:

```bash
sudo sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sudo sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl reload ssh
```

**⌘ Claude Code prompt — harden the OS** (Claude drives it over SSH; you approve each step)
```
SSH into example-ai-server at <IPV4> as root using ~/.ssh/hetzner_yourname.
Create a sudo user `adminuser`, copy root's authorized_keys to it with correct 700/600
perms, run apt update && upgrade. Then — only after confirming I can log in as
`adminuser` and run sudo — disable PermitRootLogin and PasswordAuthentication in
sshd_config and reload ssh. Pause and ask me to verify the `adminuser` login in a
separate terminal before you disable root. Report each change as a diff.
```

**Stop point:** hardened non-root access; root login disabled.

---

## 7. Phase 3 — Tailscale (secure access, zero public ports)

This is the security backbone: SSH and every service UI become reachable **only** over your private Tailnet; nothing listens on the public IP.

On the server (as `adminuser`):

```bash
curl -fsSL https://tailscale.com/install.sh -o /tmp/tailscale-install.sh
less /tmp/tailscale-install.sh
sh /tmp/tailscale-install.sh
sudo tailscale up --ssh                 # opens a URL → approve the device in your Tailnet
tailscale ip -4                         # note the 100.x.y.z address — you'll bind services to it
```

Lock SSH to the Tailscale interface, then close public 22 at the Hetzner firewall:

```bash
TS_IP=$(tailscale ip -4)
echo "ListenAddress $TS_IP" | sudo tee -a /etc/ssh/sshd_config
sudo systemctl reload ssh
```

```bash
# From the macOS workstation — firewall: allow ICMP, drop public SSH (Tailscale handles it)
hcloud firewall create --name yourname-fw
hcloud firewall add-rule yourname-fw --direction in --protocol icmp --source-ips 0.0.0.0/0 --source-ips ::/0
hcloud firewall apply-to-resource yourname-fw --type server --server example-ai-server
# (No inbound TCP rules. Cloudflare Tunnel dials OUT, so it needs none either.)
```

Verify: `ssh adminuser@example-ai-server` works with Tailscale up; times out with Tailscale off.

> **2FA the Tailscale account** — it's now your single door to the box. Keep the key-based SSH path working as a fallback (don't gut `sshd_config`, just bind it to the Tailscale IP).

**Stop point:** access is Tailscale-only; public attack surface is effectively zero.

---

## 8. Phase 4 — Docker

```bash
sudo apt install -y ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker adminuser            # log out/in for it to take effect
docker run hello-world                  # verify
```

**⌘ Claude Code prompt — install Docker**
```
Over SSH to example-ai-server as adminuser, install Docker CE + the compose plugin the
official way (apt repo + GPG key), add adminuser to the docker group, and verify with
`docker run hello-world`. Show me the commands before running and report the
installed versions.
```

**Stop point:** Docker + Compose working.

---

## 9. Phase 5 — Project repo & secrets (SOPS + age)

On the macOS workstation, create the repo that provisions everything. **Config in git; the server is disposable.**

```bash
mkdir -p ~/code/yourname-stack/stack && cd ~/code/yourname-stack
git init -b main
cat > .gitignore <<'EOF'
*.tfstate*
.env
!.env.example
*.key
*.pem
~/.config/sops/age/keys.txt
EOF

# One-time age key (the ONLY secret you don't commit — back it up in Bitwarden)
age-keygen -o ~/.config/sops/age/keys.txt        # prints "Public key: age1..."
cat > .sops.yaml <<'EOF'
creation_rules:
  - path_regex: \.enc\.(env|json|yaml)$
    age: age1<YOUR_PUBLIC_KEY>
EOF
```

Generate strong secrets and encrypt them:

```bash
cat > secrets.env <<EOF
PG_USER=n8n
PG_PASSWORD=$(openssl rand -base64 32)
N8N_ENCRYPTION_KEY=$(openssl rand -hex 32)
N8N_JWT_SECRET=$(openssl rand -hex 32)
ANTHROPIC_API_KEY=<paste>
OPENAI_API_KEY=<paste>
LITELLM_MASTER_KEY=sk-$(openssl rand -hex 24)
LANGFUSE_SALT=$(openssl rand -hex 16)
LANGFUSE_NEXTAUTH_SECRET=$(openssl rand -hex 32)
CLOUDFLARED_TOKEN=<paste later, §9-DNS>
EOF
sops -e secrets.env > stack/secrets.enc.env && rm secrets.env
```

> **The `N8N_ENCRYPTION_KEY` is the one secret you can never lose** — it decrypts every credential saved in n8n. It's in the encrypted file *and* must go into Bitwarden the moment you generate it. Same for the age private key: lose it and every encrypted secret is scrap.

**Stop point:** repo initialised, secrets encrypted, private age key + `N8N_ENCRYPTION_KEY` in Bitwarden.

---

## 10. Phase 6 — The core stack (Postgres, n8n, LiteLLM, Langfuse)

`stack/docker-compose.yml` — pin every image tag; bind every port to the **Tailscale IP** so nothing is public:

```yaml
name: yourname

services:
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${PG_USER}
      POSTGRES_PASSWORD: ${PG_PASSWORD}
      POSTGRES_DB: n8n
    volumes: [pgdata:/var/lib/postgresql/data]
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${PG_USER}"]
      interval: 10s

  n8n:
    image: n8nio/n8n:1.95.0
    restart: unless-stopped
    depends_on: { postgres: { condition: service_healthy } }
    environment:
      DB_TYPE: postgresdb
      DB_POSTGRESDB_HOST: postgres
      DB_POSTGRESDB_USER: ${PG_USER}
      DB_POSTGRESDB_PASSWORD: ${PG_PASSWORD}
      N8N_ENCRYPTION_KEY: ${N8N_ENCRYPTION_KEY}
      N8N_USER_MANAGEMENT_JWT_SECRET: ${N8N_JWT_SECRET}
      N8N_HOST: example-ai-server
      N8N_PROTOCOL: http
      GENERIC_TIMEZONE: Europe/Dublin
    volumes: [n8n_data:/home/node/.n8n, ./backups:/backups]
    ports: ["${TS_IP}:5678:5678"]        # Tailscale-only

  litellm:
    image: ghcr.io/berriai/litellm:main-stable
    restart: unless-stopped
    environment:
      LITELLM_MASTER_KEY: ${LITELLM_MASTER_KEY}
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY}
      OPENAI_API_KEY: ${OPENAI_API_KEY}
    volumes: [./litellm-config.yaml:/app/config.yaml:ro]
    command: ["--config", "/app/config.yaml"]
    ports: ["${TS_IP}:4000:4000"]        # Tailscale-only

  langfuse:
    image: langfuse/langfuse:2
    restart: unless-stopped
    depends_on: { postgres: { condition: service_healthy } }
    environment:
      DATABASE_URL: postgresql://${PG_USER}:${PG_PASSWORD}@postgres:5432/langfuse
      NEXTAUTH_SECRET: ${LANGFUSE_NEXTAUTH_SECRET}
      SALT: ${LANGFUSE_SALT}
    ports: ["${TS_IP}:3000:3000"]        # Tailscale-only

  code-server:
    image: lscr.io/linuxserver/code-server:latest
    restart: unless-stopped
    environment: { PUID: 1000, PGID: 1000, TZ: Europe/Dublin }
    volumes: [code_data:/config, /home/yourname/yourname:/config/workspace/yourname]
    ports: ["${TS_IP}:8443:8443"]        # Tailscale-only

volumes: { pgdata: {}, n8n_data: {}, code_data: {} }
```

`litellm-config.yaml` (the model router — one endpoint, cost caps, provider-swap):

```yaml
model_list:
  - model_name: claude
    litellm_params: { model: anthropic/claude-opus-4-8, api_key: os.environ/ANTHROPIC_API_KEY }
  - model_name: claude-fast
    litellm_params: { model: anthropic/claude-haiku-4-5, api_key: os.environ/ANTHROPIC_API_KEY }
  - model_name: gpt
    litellm_params: { model: openai/gpt-5.4, api_key: os.environ/OPENAI_API_KEY }
litellm_settings:
  drop_params: true
  max_budget: 100        # USD/month hard cap — raise deliberately
```

Bring it up (Claude Code drives, or you do):

```bash
# On the server, in ~/yourname/stack, with a decrypted .env in place:
sops -d secrets.enc.env > .env && echo "TS_IP=$(tailscale ip -4)" >> .env
docker compose up -d && docker compose ps
curl http://$(tailscale ip -4):5678      # n8n responds over Tailscale only
```

Create your n8n owner account at `http://example-ai-server:5678` (Tailscale up). Then load your workflow library from [n8n personal/00 README - n8n Personal Master Playbook](n8n%20personal/00%20README%20-%20n8n%20Personal%20Master%20Playbook.md) and [n8n smb/00 README - n8n SMB Master Playbook](n8n%20smb/00%20README%20-%20n8n%20SMB%20Master%20Playbook.md).

**⌘ Claude Code prompt — write & launch the stack**
```
In my yourname-stack repo, write stack/docker-compose.yml and litellm-config.yaml
exactly per the AI Automation Master Guide (Postgres 16, n8n pinned, LiteLLM router,
Langfuse, code-server; every port bound to the server's Tailscale IP; secrets from a
SOPS-decrypted .env; TS_IP appended at deploy time). Commit them. Then SSH to
example-ai-server, sync the repo, decrypt secrets.enc.env to .env, append
TS_IP=$(tailscale ip -4), run `docker compose up -d`, wait for healthchecks, and
verify each service answers on its Tailscale port. Report the status table. Never
bind a service to 0.0.0.0.
```

**Stop point:** n8n + Postgres + LiteLLM + Langfuse + code-server all running, Tailscale-only.

---

## 11. Phase 7 — Claude Code on the server + Codex

You'll mostly drive Claude Code *from the macOS workstation*, but installing it **on the box** too gives you a browser-based agent surface (via code-server) and lets scheduled/agent workflows call it locally.

```bash
# On the server (as adminuser), via code-server's terminal or SSH:
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh -o /tmp/nvm-install.sh
less /tmp/nvm-install.sh
bash /tmp/nvm-install.sh
source ~/.bashrc && nvm install --lts && nvm use --lts

npm install --global @anthropic-ai/claude-code@2.1.246
claude --version && claude          # first run → OAuth (Claude Code's own login is fine on a server)

npm install --global @openai/codex@0.150.0        # Codex CLI (verify package name as in §4)
codex --version                     # authenticate with your OpenAI key when prompted
```

> Claude Code's OAuth is Anthropic's own product login and is unaffected by third-party OAuth restrictions. The `ANTHROPIC_API_KEY` in your `.env` is for LiteLLM/n8n/Hermes to call the API — a separate concern from Claude Code's interactive login.

Add a repo-root `CLAUDE.md` so both your Mac-mini and on-box Claude sessions share conventions (naming, "never bind to 0.0.0.0", "secrets only via SOPS", deploy = `make up`). Let Claude write it:

**⌘ Claude Code prompt — install on-box agents + conventions**
```
SSH to example-ai-server as adminuser. Install Node LTS via nvm, then Claude Code
(@anthropic-ai/claude-code) and the OpenAI Codex CLI globally. Verify both
`--version` commands. Then, in my yourname repo, write a root CLAUDE.md capturing
the project conventions from the AI Automation Master Guide: naming (yourname-*,
first-name users, <service> containers), the Tailscale-only + never-bind-0.0.0.0
rule, SOPS-for-all-secrets, and that deploys run via the Makefile. Commit it.
```

**Stop point:** Claude Code + Codex installed on the box; conventions captured.

---

## 12. Phase 8 — Hermes agent

Hermes runs as **another container** in the same compose stack — Tailscale-only port, named volume for state, env from the decrypted `.env`, pinned image tag (not `latest`). Point Hermes at **LiteLLM** (`http://litellm:4000`) rather than a provider directly, so all model traffic is routed, budgeted, and traced through one place.

Hermes packaging varies by release and deployment target. Consult current first-party documentation, inspect the installation safely, and then have the coding agent propose a container configuration for review:

**⌘ Claude Code prompt — deploy Hermes**
```
Review the current first-party Hermes deployment documentation and the example project. Add a `hermes` service to
stack/docker-compose.yml: pinned image or a Dockerfile if it isn't containerised
yet, its port bound to the Tailscale IP only, state in a named volume, config from
the SOPS-decrypted .env, and its model calls pointed at http://litellm:4000 using
LITELLM_MASTER_KEY. Do not use `latest`. Bring it up over SSH, tail its logs, and
confirm it can reach LiteLLM and complete one test task. Report what you changed.
```

**Stop point:** Hermes running as a container, routed through LiteLLM.

---

## 13. Phase 9 — DNS & Cloudflare Tunnel — *when you actually need DNS*

**You need DNS at exactly one moment: when something must be reachable from the public internet by name.** Until then, Tailscale-only means **no DNS, no public ports, no certificates.** Concretely, add DNS when:

- **Inbound webhooks** must reach n8n — Stripe, Telegram, GitHub, a client's system calling your automation. These can't traverse Tailscale.
- You want a **public URL** for a client-facing n8n form, a status page, or a demo.
- A service needs a **stable public hostname + TLS** (custom domain on the n8n UI, etc.).

**The pattern: Cloudflare Tunnel, not open ports.** The `cloudflared` container dials *out* to Cloudflare, so you never open inbound 80/443, and — crucially — a resumed/cloned server's new IP doesn't matter (the tunnel name is the stable identity). You need a domain whose nameservers are on Cloudflare (that's the "DNS" part).

Setup:

1. Cloudflare dashboard → add your domain → point its nameservers at Cloudflare (one-time, at your registrar).
2. Zero Trust → Networks → Tunnels → **Create tunnel** → copy the **tunnel token** into your SOPS `secrets.enc.env` as `CLOUDFLARED_TOKEN`.
3. Add the `cloudflared` service and a public hostname mapping (e.g. `n8n.yourdomain.com` → `http://n8n:5678`):
   ```yaml
   cloudflared:
     image: cloudflare/cloudflared:2026.5.0
     restart: unless-stopped
     command: tunnel --no-autoupdate run
     environment: { TUNNEL_TOKEN: ${CLOUDFLARED_TOKEN} }
   ```
4. In the tunnel's **Public Hostname** config, map only what must be public (usually just the n8n webhook host). Everything else stays Tailscale-only.
5. Set n8n's `WEBHOOK_URL=https://n8n.yourdomain.com/` and `N8N_PROTOCOL=https`, then `docker compose up -d n8n`.

**⌘ Claude Code prompt — wire Cloudflare Tunnel**
```
Add a cloudflared service to the compose stack (image pinned, TUNNEL_TOKEN from the
SOPS-decrypted .env). Update the n8n service to WEBHOOK_URL=https://n8n.<DOMAIN>/ and
N8N_PROTOCOL=https. Do NOT open any inbound Hetzner firewall ports — the tunnel dials
out. Bring the stack up, and give me the exact steps to finish the Public Hostname
mapping (n8n.<DOMAIN> -> http://n8n:5678) in the Cloudflare Zero Trust UI. Only the
n8n webhook host should be public; everything else stays Tailscale-only.
```

**Stop point:** public webhooks live via tunnel; internal UIs still private.

---

## 14. Phase 10 — Backups (three layers)

1. **Postgres dump + volume tar, nightly, to Backblaze B2** (off-site — survives the whole VPS vanishing):
   ```bash
   # ~/yourname/backup.sh (Claude Code can write this)
   set -euo pipefail
   TS=$(date -u +%FT%TZ); D=~/yourname/backups; cd ~/yourname/stack
   docker compose exec -T postgres pg_dumpall -U "$PG_USER" | gzip > "$D/pg-$TS.sql.gz"
   docker run --rm -v yourname_n8n_data:/d:ro -v "$D":/b alpine tar czf "/b/n8n-$TS.tgz" -C /d .
   rclone copy "$D" b2:yourname-backups --include "*-$TS.*"
   find "$D" -type f -mtime +14 -delete
   ```
   `crontab -e` → `0 3 * * * /home/yourname/yourname/backup.sh >> ~/yourname/backups/backup.log 2>&1`
2. **n8n workflows + credentials to a private git repo** (see Hetzner + n8n — Automation, Backup, Strategy §4 for the `n8n export:workflow` + SOPS pattern). Workflows are code; keep them versioned.
3. **Test a restore once, now, while it's empty** — restore `pg-*.sql.gz` into a throwaway Postgres container and confirm the tables exist. Untested backups aren't backups.

**Stop point:** nightly off-site backups + a verified restore.

---

## 15. Snapshots & cloning — dev / test / prod

**Your question: does Hetzner let you snapshot/image the server to copy the setup or spin up a dev/test/prod twin? Yes — two complementary mechanisms.**

### A. Hetzner Snapshots (a full disk image of the running box)

- **What it is:** `hcloud server create-image --type snapshot` captures the entire disk — OS, Docker, images, volumes, your whole stack — as a reusable image. Priced at ~€0.0119/GB/month (a CX32 stack snapshots to roughly 5–15 GB → cents to ~€1/month).
- **Clone a server from it** — this is your dev/test/prod duplication:
  ```bash
  # Snapshot prod (quiesce first so Postgres is consistent)
  ssh adminuser@example-ai-server 'cd ~/yourname/stack && docker compose down'
  hcloud server create-image --type snapshot --description "prod-$(date -u +%F)" example-ai-server
  ssh adminuser@example-ai-server 'cd ~/yourname/stack && docker compose up -d'
  hcloud image list --type snapshot            # note the snapshot ID

  # Spin up an identical dev twin from that image
  hcloud server create --image <SNAPSHOT_ID> --type cx22 --location nbg1 \
    --ssh-key example-admin-ed25519 --name [DEVICE REDACTED] --label env=dev
  ```
  The dev box boots with the exact same stack. **Before using it:** join it to Tailscale, and rotate its secrets so dev and prod don't share an `N8N_ENCRYPTION_KEY`/DB password (regenerate `.env`, re-run `docker compose up -d`).
- **Constraint:** a snapshot is locked to the same architecture/image family — CX (x86) → CX is fine; CX → CAX (ARM) is not.
- **Also use snapshots to pause cheaply:** snapshot → `hcloud server delete` → billing on compute stops; recreate from the snapshot when you return (storage cost is cents/month). A powered-off server still bills full price, so *delete*, don't power off. Cloudflare Tunnel makes the new IP on resume a non-event.

### B. Terraform / OpenTofu + tfvars (parameterised, clone-at-apply)

Snapshots duplicate a *point-in-time disk*. For clean, drift-free environments, describe the box in Terraform once and apply it per-environment — the recommended long-term pattern from Hetzner + n8n — Automation, Backup, Strategy (§2–3):

```
infra/envs/
├── dev.tfvars      # cx22, name=[DEVICE REDACTED]
├── staging.tfvars  # cx32, name=yourname-staging-01
└── prod.tfvars     # cx32, name=example-ai-server
```
```bash
tofu apply -var-file=envs/dev.tfvars     # dev twin
tofu apply -var-file=envs/prod.tfvars    # prod
```
Duplication happens at **apply time** with different variables and *different secrets*, not by copying live boxes. Config lives in git; each environment is reproducible from a single commit.

**Recommendation:** use **snapshots** for fast "give me a copy of exactly this, now" and for cheap pause/resume; use **Terraform** as the durable source of truth once you have more than one environment. Take a snapshot **before any risky change**, keep weekly snapshots, prune monthly. Snapshots are *not* off-site backup (they live in Hetzner) — keep the §14 B2 backups too.

**⌘ Claude Code prompt — clone to a dev environment**
```
Quiesce the stack on example-ai-server (docker compose down), take a Hetzner
snapshot named prod-<date>, bring prod back up, then create [DEVICE REDACTED] (cx22)
from that snapshot. Join the dev box to Tailscale, regenerate its .env with fresh
secrets via SOPS so it shares no encryption key or DB password with prod, and bring
its stack up. Confirm dev's n8n answers on its own Tailscale IP. Report both boxes'
IDs, snapshot ID, and monthly cost delta.
```

---

## 16. Security hardening checklist

This is meant to be a **highly secure environment**. Confirm every line:

- [ ] Root SSH login **disabled**; password auth **disabled**; per-person keys with passphrases.
- [ ] SSH bound to the **Tailscale interface**; public port 22 **closed** at the Hetzner firewall.
- [ ] **Every** container port bound to the Tailscale IP — audit with `sudo ss -tlnp | grep -v 127.0.0.1 | grep -v '100\.'` (should be empty). **Never `0.0.0.0`.**
- [ ] Public ingress only via **Cloudflare Tunnel** (outbound), only for the specific hosts that need it.
- [ ] All secrets **SOPS-encrypted** in git; age private key + `N8N_ENCRYPTION_KEY` in Bitwarden; nothing plaintext in the repo (run `git status` before every commit).
- [ ] LiteLLM `max_budget` set; per-key budgets in Anthropic/OpenAI consoles; API cost logged (Langfuse).
- [ ] 2FA on Hetzner, Cloudflare, GitHub, Anthropic, OpenAI, Tailscale, Bitwarden.
- [ ] Image tags **pinned** (no `latest` in prod); updates are a deliberate event, not a reflex.
- [ ] Nightly **off-site** backups to B2 + a **verified restore**; snapshot before risky changes.
- [ ] `fail2ban` or at least a weekly `auth.log` review; `docker system prune -a` monthly to keep the disk healthy.
- [ ] MCP servers: run locally (stdio), pin versions, read the source before installing (supply-chain risk — see AI Security — Comprehensive Guide).
- [ ] Rotate SSH keys and API tokens on a schedule (calendar reminder); rotate immediately on any suspected exposure.

---

## 17. The single Claude-Code-from-Mac-mini workflow

Once the repo exists, this is the day-to-day loop — everything runs through Claude Code (Fable 5) on the macOS workstation:

```bash
cd ~/code/yourname-stack
claude --model claude-fable-5
```

Then work in natural language; Claude does the rest via the `hcloud` CLI, SSH, git, and Docker:

- *"Show me every Hetzner server and what each costs; flag anything not tagged `project=yourname`."*
- *"Add a new n8n workflow that <does X>; write it as JSON, commit it, and import it on prod. Then run it once and show me the result."*
- *"Bump n8n to the next patch release on **dev** first, run the smoke test, and only if it passes, do the same on prod."*
- *"Take a pre-change snapshot, then apply <change>. If the smoke test fails, tell me the rollback command."*
- *"Audit the box: confirm no port is on 0.0.0.0, backups ran last night, and the disk is under 70%."*

Encode the guardrails once in the repo-root `CLAUDE.md` (Tailscale-only, never-bind-0.0.0.0, SOPS-for-secrets, deploy-via-Makefile, snapshot-before-risky-changes) and every session inherits them. Give Claude a `Makefile` so "deploy" is one verb:

```make
up:       ; ssh adminuser@example-ai-server 'cd ~/yourname/stack && sops -d secrets.enc.env > .env && echo TS_IP=$$(tailscale ip -4) >> .env && docker compose up -d'
logs:     ; ssh adminuser@example-ai-server 'cd ~/yourname/stack && docker compose logs -f --tail=200'
backup:   ; ssh adminuser@example-ai-server '~/yourname/backup.sh'
snapshot: ; hcloud server create-image --type snapshot --description "manual-$(shell date -u +%FT%TZ)" example-ai-server
audit:    ; ssh adminuser@example-ai-server "sudo ss -tlnp | grep -v 127.0.0.1 | grep -v '100\\.'"
```

---

## 18. Come-back-later cheat sheet

```bash
# Connect (Tailscale must be up on the macOS workstation)
ssh adminuser@example-ai-server

# What's running?
cd ~/yourname/stack && docker compose ps

# Logs for one service
docker compose logs -f n8n

# Restart one service
docker compose restart n8n

# Run a backup now
~/yourname/backup.sh

# Snapshot before a risky change
hcloud server create-image --type snapshot --description "pre-change" example-ai-server

# What ports are exposed publicly? (should be empty)
sudo ss -tlnp | grep -v 127.0.0.1 | grep -v '100\.'

# Rotate an API key: edit Bitwarden -> update secrets.enc.env (sops) -> make up -> revoke old key

# Pause the project cheaply: snapshot, then `hcloud server delete example-ai-server`
#   (recreate from the snapshot when you return; Cloudflare Tunnel handles the new IP)
```

---

## 19. Cost reality

| Item | Monthly |
|---|---|
| Hetzner CX32 (prod) | ~€7.55 |
| Hetzner CX22 (dev twin, when running) | ~€4.50 |
| Snapshot storage (a few images) | ~€0.50–1 |
| Backblaze B2 off-site backups | ~$0.10 |
| Cloudflare + Tailscale + GitHub free tiers | €0 |
| Domain | ~$1 (amortised) |
| **Infra subtotal** | **~€10 (prod only) / ~€15 (prod + dev)** |
| Anthropic + OpenAI API usage | Variable — cap via LiteLLM `max_budget` + console limits |

Paused (snapshot + deleted server): **~€0.50–1/month.** The financial risk here is API spend, not infrastructure — the LiteLLM budget cap and Langfuse cost logging are how you keep it honest.

---

### Related
- AI Automation Stack — Source Index — every source doc, tiered.
- Hetzner + n8n — Automation, Backup, Strategy — deep dive on snapshots, backups, Terraform, pause/resume.
- Hetzner Deployment Plan — numbered OS-hardening + credential-management detail.
- Claude Code to Hetzner — First Box Walkthrough — the infra-as-code (Terraform + cloud-init) first-box path.
- How to Build an AI OS - The Novice Runbook — paint-by-numbers, prompt-per-step companion.
- AI Security — Comprehensive Guide — MCP supply chain, secrets discipline.
