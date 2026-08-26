---
title: "Docker - Complete Practical Guide"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Docker — Complete Practical Guide

> [!summary]
> Docker packages an application and its runtime dependencies into an **image**. Docker starts that image as an isolated **container**. A `Dockerfile` describes how to build one image; a Compose file describes how several containers, networks, volumes, ports, and settings work together.
>
> The most important operational rule is: **containers are replaceable; important data must live outside the container writable layer.**

## What this guide covers

- Docker’s mental model and architecture
- Images, containers, registries, networks, volumes, bind mounts, build cache and contexts
- Docker Engine versus Docker Desktop
- How Docker differs on macOS, Windows and Linux
- Dockerfiles, Compose and everyday development workflows
- Multi-platform builds and Apple Silicon considerations
- Storage, networking, security, secrets and production practices
- Backups, recovery and upgrades
- A systematic troubleshooting workflow
- Command cheat sheets and common failure patterns

---

# 1. The mental model

## Containers are not small virtual machines

A virtual machine emulates or virtualizes hardware and normally boots a complete guest operating system. A container usually runs one application process while sharing the host kernel.

| Property | Container | Virtual machine |
|---|---|---|
| Unit | Process plus filesystem/runtime isolation | Complete guest OS |
| Startup | Usually seconds or less | Usually slower |
| Image size | Often MB to low GB | Often many GB |
| Kernel | Shares the Docker host’s kernel | Has its own guest kernel |
| Isolation | Process/container isolation | Stronger hardware/VM boundary |
| Best use | Portable services, builds, tests, repeatable app stacks | Different kernels, stronger isolation, full desktops/servers |

A Linux container needs a Linux kernel. This matters because:

- On **Linux**, Docker Engine can run Linux containers directly on the host kernel.
- On **macOS**, Docker runs Linux containers inside a lightweight Linux VM because macOS does not have a Linux kernel.
- On **Windows**, Docker Desktop normally runs Linux containers using WSL 2 or Hyper-V. Native Windows containers use the Windows kernel and are a separate mode.

## The six objects to understand

1. **Dockerfile** — source instructions for building an image.
2. **Image** — immutable, layered application template.
3. **Container** — a running or stopped instance of an image.
4. **Registry** — image storage and distribution service, such as Docker Hub or GHCR.
5. **Volume/bind mount** — storage outside the replaceable container layer.
6. **Network** — controlled connectivity and DNS between containers and the outside world.

## Image versus container

Think of an image as a class or installation artifact and a container as one runtime instance.

```text
Dockerfile + build context
        ↓ docker build
      image
        ↓ docker run
    container
```

You can run many containers from one image. Removing a container does not remove its image. Rebuilding an image does not automatically replace already-running containers.

## Immutable infrastructure in practice

Do not patch a running container and expect the change to survive. Instead:

1. Change source code, dependency files or the Dockerfile.
2. Build a new image.
3. Test it.
4. Replace the old container.
5. Keep persistent data in a named volume or external service.

`docker exec` is useful for inspection and temporary diagnosis, not as a deployment mechanism.

---

# 2. Docker architecture

Docker uses a client-server model:

```text
Docker CLI / Compose / Desktop UI
              ↓ Docker API
       Docker daemon (dockerd)
              ↓
 images · containers · networks · volumes · builds
```

- `docker` is the CLI client.
- `dockerd` is the daemon that manages Docker objects.
- `containerd` and a low-level runtime manage container lifecycle beneath the daemon.
- BuildKit performs modern Docker builds.
- Compose is a client that translates a multi-service YAML model into Docker API operations.

The CLI and daemon may be on the same machine or different machines. Always verify which daemon you are targeting:

```bash
docker context show
docker context ls
docker info
```

> [!danger]
> The Docker daemon is highly privileged. Access to its socket is effectively administrative/root-level access on the Docker host. Never expose an unauthenticated Docker TCP socket, and never mount the Docker socket into untrusted containers.

---

# 3. Docker Engine, Docker Desktop and alternatives

## Docker Engine

Docker Engine is the core daemon, API and CLI. On a Linux server it usually runs as a system service:

```bash
sudo systemctl status docker
sudo systemctl start docker
sudo systemctl restart docker
```

Use Engine directly when:

- You run Linux servers or CI runners.
- You do not need a desktop GUI.
- You want native Linux performance and control.
- You manage Docker using system packages and systemd.

## Docker Desktop

Docker Desktop is a managed development bundle for macOS, Windows and Linux. It includes Docker Engine, the Docker CLI, Compose, BuildKit/buildx, a GUI, credential integration and optional features.

The Desktop dashboard can:

- Start, stop, inspect and delete containers
- View container logs and resource use
- Browse images, volumes and builds
- Configure CPU, memory, disk, proxies and file sharing
- Change Docker Engine settings
- Enable optional Kubernetes
- Run diagnostics, restart Desktop, clean data or factory-reset

Use Desktop when:

- You want the easiest supported installation on macOS or Windows.
- You want GUI inspection and integrated updates.
- You want WSL 2 integration on Windows.
- You want built-in Compose, credential storage and diagnostics.

### Docker Desktop licensing

Docker Desktop is free for personal use, education, non-commercial open-source projects, and qualifying small businesses. Docker’s current terms require a paid subscription for professional use in larger organizations and government entities. Verify the current [Docker Desktop license page](https://docs.docker.com/subscription/desktop-license/) for exact eligibility before organizational deployment.

Docker Engine itself is open source, but obtaining/using it as part of Docker Desktop is subject to the Desktop agreement.

## macOS alternatives: Colima and OrbStack

Docker Desktop is not the only way to provide a Linux Docker daemon on macOS.

- **Colima** uses a lightweight Linux VM and can provide Docker/containerd runtimes from the CLI.
- **OrbStack** is another commercial desktop runtime with a different VM and filesystem implementation.

The Docker CLI can talk to any of them through contexts/sockets. Do not run multiple local runtimes casually: they can create context confusion, duplicate image stores and host-port conflicts.

For the operator’s macOS workstation, Colima has been used for local stacks. Before acting, verify rather than assume:

```bash
docker context ls
docker context show
docker info --format '{{.Name}}'
colima status 2>/dev/null || true
```

> [!warning]
> Docker Desktop, Colima and OrbStack have separate VM disks, containers, images and sometimes contexts. An image visible in one runtime is not automatically visible in another.

---

# 4. How Docker runs on each operating system

## macOS

### Architecture

Docker Desktop or Colima runs a Linux VM. The Docker CLI is a native macOS program, but Linux containers run in the VM.

```text
macOS terminal → Docker CLI → Unix socket/context → Linux VM → containers
```

Consequences:

- Linux container paths and permissions still follow Linux rules.
- Host file sharing crosses the macOS-to-VM boundary.
- Named volumes live inside the runtime’s Linux VM disk.
- A container cannot use macOS kernel APIs as though it were a native macOS process.
- `host.docker.internal` is the normal Desktop hostname for reaching the Mac host from a container.

### Apple Silicon versus Intel

Apple Silicon is `arm64`; many cloud/server images are `amd64`.

Check image architecture:

```bash
docker image inspect IMAGE --format '{{.Architecture}}/{{.Os}}'
docker buildx imagetools inspect IMAGE:TAG
```

Run an Intel image under emulation only when necessary:

```bash
docker run --platform linux/amd64 IMAGE
```

Emulation is slower, uses more resources and can expose architecture-specific bugs. Prefer native ARM64 or multi-architecture images.

Build both common Linux architectures:

```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t registry.example.com/app:VERSION \
  --push .
```

A local Docker image store normally cannot load a multi-platform manifest directly; multi-platform builds are commonly pushed to a registry. For a single local platform, use `--load`.

### macOS filesystem considerations

- macOS is usually case-insensitive but case-preserving; Linux is case-sensitive.
- `Foo.ts` and `foo.ts` may behave differently after deployment.
- Large bind-mounted dependency trees can be slower than named volumes.
- Native modules must be built for the container OS/architecture, not copied from macOS.
- Do not bind-mount host `node_modules` into a Linux container.

Useful pattern:

```yaml
services:
  app:
    volumes:
      - .:/workspace
      - node_modules:/workspace/node_modules
volumes:
  node_modules:
```

### Mac resource tuning

Docker Desktop lets you configure VM CPU, memory, disk and file sharing. Increase resources only after measuring. Common symptoms of insufficient resources include builds terminated with exit code `137`, databases becoming unhealthy, and the VM becoming unresponsive.

## Windows

### Linux containers with WSL 2

This is the normal development path. Docker Desktop runs its engine in a managed WSL environment and integrates the CLI into selected WSL distributions.

```text
PowerShell or WSL shell → Docker CLI → Docker Desktop/WSL 2 engine → Linux containers
```

Check WSL:

```powershell
wsl --status
wsl --version
wsl -l -v
```

Docker currently recommends a recent WSL release; verify [WSL requirements](https://docs.docker.com/desktop/features/wsl/) before troubleshooting obscure failures.

### Where to keep source code

For Linux-container development, keep active source inside the WSL Linux filesystem, for example:

```text
/home/yourname/projects/my-app
```

Avoid performance-sensitive bind mounts from `/mnt/c/...` where possible. Linux filesystem mounts provide better performance and more reliable file-change events than mounting Windows NTFS paths into Linux containers.

Access WSL files from Windows through:

```text
\\wsl$\DISTRO\home\USER\projects
```

### WSL resource tuning

WSL 2 dynamically uses memory. Resource ceilings can be configured through Windows/WSL settings. If Docker becomes memory-heavy, distinguish active container use, build cache, WSL page cache and an actual leak before imposing very low limits.

A clean WSL restart is:

```powershell
wsl --shutdown
```

This stops all WSL distributions, so save work and stop important services first.

### Hyper-V backend

Hyper-V is an alternative backend. It may be preferable where a separate VM boundary is desired or WSL integration is unnecessary. Availability depends on Windows edition and installation mode.

### Native Windows containers

Windows containers are not the same as Linux containers. They use Windows base images and Windows kernel compatibility rules.

- The Desktop menu can switch between Linux and Windows container engines where supported.
- The two modes have different image stores and settings.
- Windows container support generally requires supported Professional/Enterprise editions and the appropriate Desktop installation mode.
- A Linux image cannot run in Windows-container mode, and vice versa.

Check current mode:

```powershell
docker info --format '{{.OSType}}'
```

Expected output is `linux` or `windows`.

### Windows-specific pitfalls

- CRLF line endings can break Linux shell entrypoints with `bad interpreter` errors.
- NTFS permissions do not map perfectly to Linux UID/GID/mode semantics.
- Antivirus/EDR can slow large build contexts and bind mounts.
- VPN, proxy and DNS settings can affect both Windows and the WSL VM.
- Drive-letter paths need correct quoting in PowerShell and Compose.
- Windows and Linux container settings are retained separately when switching modes.

## Linux

### Native Docker Engine

Linux is the most direct environment for Linux containers:

```text
Linux CLI → /var/run/docker.sock → dockerd → Linux namespaces/cgroups → containers
```

Advantages:

- No mandatory Desktop VM layer
- Native filesystem and networking performance
- Systemd integration and predictable server automation
- Closest match to most Linux production hosts

### Permissions

The default Docker socket is commonly owned by `root:docker`. Adding a user to the `docker` group avoids `sudo`, but grants root-equivalent control of the host.

```bash
getent group docker
ls -l /var/run/docker.sock
```

Use **rootless Docker** where its limitations are acceptable. Rootless mode runs both daemon and containers without host root privileges and reduces daemon-level risk.

### Docker Desktop on Linux

Docker Desktop for Linux runs its own VM and uses a `desktop-linux` context. It can coexist with native Engine, but the stores are separate and both can compete for ports.

```bash
docker context ls
docker context use default        # commonly native Engine
docker context use desktop-linux  # Docker Desktop VM
```

Do not assume a missing container was deleted until checking the active context.

### Linux-specific pitfalls

- SELinux labeling may require `:z` or `:Z` for bind mounts; use these carefully.
- AppArmor/SELinux policies may block container actions even when Unix permissions appear correct.
- UID/GID mismatch commonly causes bind-mount permission errors.
- Docker network subnets can overlap VPN or corporate routes.
- `iptables`/`nftables` interactions can affect published ports.
- Disk usage may grow under `/var/lib/docker` or the configured data root.

---

# 5. Installation and initial verification

Always use Docker’s current platform-specific installation documentation rather than a random install script:

- [Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Docker Engine install](https://docs.docker.com/engine/install/)
- [Docker Desktop for Linux](https://docs.docker.com/desktop/setup/install/linux/)

After installation:

```bash
docker version
docker info
docker compose version
docker buildx version
docker context ls
docker run --rm hello-world
```

`docker version` shows both client and server. If the client works but the server section fails, the CLI is installed but cannot reach the daemon.

> [!tip]
> Use Compose v2 syntax: `docker compose`, not the legacy `docker-compose` Python command, unless maintaining an older environment deliberately.

---

# 6. Everyday container lifecycle

## Run a container

```bash
docker run --name web -d -p 127.0.0.1:8080:80 nginx:alpine
```

Meaning:

- `--name web` assigns a stable name.
- `-d` detaches.
- `-p 127.0.0.1:8080:80` maps host loopback port 8080 to container port 80.
- `nginx:alpine` is the image reference.

Inspect it:

```bash
docker ps
docker logs web
docker inspect web
docker stats web
docker port web
```

Enter it temporarily:

```bash
docker exec -it web sh
```

Stop and remove it:

```bash
docker stop web
docker rm web
```

Run an ephemeral command and delete the container automatically:

```bash
docker run --rm alpine:3.22 echo hello
```

## Container states

```bash
docker ps                 # running
docker ps -a              # all
docker inspect CONTAINER  # full state
docker wait CONTAINER     # wait for exit
docker start CONTAINER
docker restart CONTAINER
docker stop CONTAINER
docker kill CONTAINER     # immediate signal; not normal shutdown
```

Prefer graceful `stop` before `kill`.

## Exit codes worth recognizing

| Exit | Typical meaning |
|---:|---|
| 0 | Success |
| 1 | Generic application error |
| 126 | Command exists but is not executable |
| 127 | Command not found |
| 130 | Interrupted with Ctrl+C/SIGINT |
| 137 | Killed, commonly SIGKILL or out-of-memory |
| 143 | Stopped with SIGTERM |

Always confirm the real reason using `docker inspect` and logs rather than relying only on the number.

---

# 7. Images and registries

## Image naming

```text
REGISTRY/NAMESPACE/REPOSITORY:TAG
```

Examples:

```text
nginx:1.27-alpine
ghcr.io/org/app:1.4.2
registry.example.com/team/api:git-abc123
```

Tags are mutable labels. Digests identify immutable content:

```text
image@sha256:...
```

Use tags for human release names and digests when exact reproducibility matters.

## Image commands

```bash
docker image ls
docker pull IMAGE:TAG
docker image inspect IMAGE:TAG
docker history IMAGE:TAG
docker image rm IMAGE:TAG
docker image prune
```

Inspect supported remote platforms without pulling every layer:

```bash
docker buildx imagetools inspect IMAGE:TAG
```

## Registry authentication

```bash
docker login REGISTRY
```

Use a scoped access token rather than an account password. Let Docker’s credential helper store it. Never commit Docker config credentials or paste them into a Dockerfile.

## Do not use `latest` as a release strategy

`latest` has no special immutability or recency guarantee. Use explicit version or commit-derived tags. A practical release may publish all of:

```text
app:1.4.2
app:1.4
app:git-abc123
```

Production should record the resolved digest.

---

# 8. Writing a good Dockerfile

## A production-oriented Node example

```dockerfile
# syntax=docker/dockerfile:1

FROM node:22-bookworm-slim AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

FROM deps AS build
COPY . .
RUN npm test && npm run build

FROM node:22-bookworm-slim AS production
ENV NODE_ENV=production
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --omit=dev && npm cache clean --force
COPY --from=build /app/dist ./dist

USER node
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

Why this is better:

- Lockfile-based installs are reproducible.
- Tests/build tools stay outside the final stage.
- The final dependency tree excludes development dependencies.
- The process runs as a non-root user.
- Exec-form `CMD` gives correct signal handling.

## Dockerfile instruction meanings

| Instruction | Purpose |
|---|---|
| `FROM` | Select base image or begin a build stage |
| `WORKDIR` | Set a stable working directory |
| `COPY` | Copy files from build context or another stage |
| `RUN` | Execute a build-time command and create a layer |
| `ENV` | Set image/runtime environment defaults |
| `ARG` | Define build-time input; not suitable for secrets |
| `USER` | Set runtime user |
| `EXPOSE` | Document expected container port; does not publish it |
| `ENTRYPOINT` | Define primary executable |
| `CMD` | Define default command/arguments |
| `HEALTHCHECK` | Define container-level health probe |

## Build context

The final `.` in this command is the build context:

```bash
docker build -t myapp:dev .
```

Only files in the context can be copied. Keep context small with `.dockerignore`:

```gitignore
.git
.env
.env.*
node_modules
coverage
dist
*.log
Docker.raw
```

Do not exclude files required by the build.

## Layer/cache ordering

Copy stable dependency manifests before frequently changing source:

```dockerfile
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
```

If source is copied first, every source edit invalidates the dependency-install cache.

## Build secrets

Do not put credentials in `ARG`, `ENV`, copied files or shell history. Use BuildKit secret mounts:

```dockerfile
RUN --mount=type=secret,id=npmrc,target=/root/.npmrc npm ci
```

```bash
docker build --secret id=npmrc,src="$HOME/.npmrc" -t myapp .
```

The build step can read the secret without baking it into a normal image layer.

## Reproducibility limits

A lockfile alone does not make the entire image reproducible. Also consider:

- Base-image tags can move; pin digests where warranted.
- OS package repositories change.
- `curl | sh` and remote install scripts can change.
- Unpinned `pip install`, `npm install` or Git branches can change.
- Architecture-specific wheels/packages may differ.
- Build time, locale and network availability can affect outputs.

CI must build the **final runtime image**, not merely an early dependency stage.

---

# 9. Docker Compose

Compose defines a multi-container application declaratively in `compose.yaml`.

## Example

```yaml
name: example-stack

services:
  app:
    build:
      context: .
      target: production
    environment:
      DATABASE_URL: postgres://app:${POSTGRES_PASSWORD}@db:5432/app
    ports:
      - "127.0.0.1:${APP_PORT:-3000}:3000"
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    networks:
      - frontend
      - backend

  db:
    image: postgres:17
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?set POSTGRES_PASSWORD}
    volumes:
      - db-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app -d app"]
      interval: 5s
      timeout: 3s
      retries: 20
    restart: unless-stopped
    networks:
      - backend

volumes:
  db-data:

networks:
  frontend:
  backend:
    internal: true
```

## Core Compose workflow

```bash
docker compose config                 # render and validate
docker compose build
docker compose up -d
docker compose ps
docker compose logs -f --tail=200
docker compose exec app sh
docker compose run --rm app COMMAND   # one-off task
docker compose restart app
docker compose stop
docker compose down
```

Rebuild and replace after source/image changes:

```bash
docker compose up -d --build
```

Force recreation without rebuilding:

```bash
docker compose up -d --force-recreate
```

## `stop`, `down` and volume deletion

- `docker compose stop` stops containers but keeps them.
- `docker compose down` removes Compose containers and its default networks.
- `docker compose down -v` also removes declared named volumes and can destroy databases.

> [!danger]
> Treat `docker compose down -v`, `docker volume rm`, `docker system prune --volumes`, factory reset and Docker Desktop “Clean/Purge data” as destructive data operations.

## Project names

Compose prefixes objects with the project name. Set it explicitly to prevent surprises:

```yaml
name: myproject
```

Or:

```bash
docker compose -p myproject up -d
```

Different project names create different containers, networks and usually different volumes even from the same YAML file.

## Environment-variable model

Do not confuse:

1. Variables used to interpolate the Compose YAML.
2. Variables injected into a container.
3. Build arguments used only during image build.
4. Secrets mounted at build or runtime.

Render the effective model before launch:

```bash
docker compose config
```

Be careful: rendered output can contain sensitive values. Do not paste it publicly or into logs without redaction.

Useful commands:

```bash
docker compose config --services
docker compose config --images
docker compose config --volumes
```

## Override files and profiles

A practical layout is:

```text
compose.yaml
compose.override.yaml       # automatic local development overrides
compose.production.yaml     # explicit production overrides
```

Production invocation:

```bash
docker compose -f compose.yaml -f compose.production.yaml config
docker compose -f compose.yaml -f compose.production.yaml up -d
```

Profiles allow optional services such as observability or admin tools:

```yaml
services:
  adminer:
    image: adminer
    profiles: [tools]
```

```bash
docker compose --profile tools up -d
```

---

# 10. Storage and persistence

## The writable container layer is disposable

Files written inside a container disappear when that container is removed unless they are mounted to persistent storage.

## Storage choices

| Type | Managed by | Persists | Best for | Main warning |
|---|---|---:|---|---|
| Container layer | Container | Until container removal | Temporary runtime files | Not durable |
| Named volume | Docker | Yes | Databases, durable app data | Must be backed up separately |
| Bind mount | Host/user | Yes | Source code, config, host-shared files | Container can modify host files |
| `tmpfs` | Memory | No | Temporary/sensitive/cache data | Lost on stop/reboot |

## Named volumes

```bash
docker volume create app-data
docker volume ls
docker volume inspect app-data
```

Mount it:

```bash
docker run --rm -v app-data:/data IMAGE
```

Prefer volumes for databases and high-I/O state. Do not edit a volume’s internal storage path directly.

## Bind mounts

Long syntax is clearer and fails if the source is missing:

```bash
docker run --rm \
  --mount type=bind,src="$PWD/config",dst=/app/config,readonly \
  IMAGE
```

Use read-only mounts when the container does not need to write.

> [!warning]
> Bind mounts are host-coupled and writable by default. A container with a broad bind mount can change or delete host files. Never mount `/`, your home directory, credential directories or the Docker socket into an untrusted image.

## UID/GID and permission problems

Linux permissions are numeric. A container process running as UID 1001 may not be able to write files owned by host UID 501 or 1000.

Inspect:

```bash
docker compose exec app id
ls -ln HOST_PATH
docker compose exec app ls -ln /container/path
```

Possible fixes:

- Run the container with an intended UID/GID.
- Build a matching non-root user into the image.
- Change ownership of the specific data directory.
- Use a named volume instead of a cross-OS bind mount.
- Avoid `chmod -R 777`; it hides the design problem and weakens security.

## Backups

Your Compose file recreates infrastructure configuration, not database contents.

For databases, prefer database-native tools:

```bash
# PostgreSQL example — output path is illustrative
docker compose exec -T db pg_dump -U app -d app > backup.sql
```

For a quiesced generic volume, a tar archive can be useful:

```bash
docker run --rm \
  -v myproject_db-data:/data:ro \
  -v "$PWD/backups":/backup \
  alpine:3.22 \
  tar czf /backup/db-data.tar.gz -C /data .
```

Before relying on a backup:

1. Quiesce writes or use an application/database-consistent snapshot method.
2. Store the backup outside Docker’s VM disk.
3. Encrypt sensitive backups.
4. Test restoration into a separate volume/environment.
5. Record the image/database version needed for restoration.

Docker Desktop VM-disk backups can help with disaster recovery, but they are not a substitute for service-aware data backups. See [Desktop backup and restore](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/).

---

# 11. Networking

## Container-to-container communication

In a user-defined network or Compose project, use service names, not container IPs:

```text
postgres://app@db:5432/app
```

Docker provides internal DNS for service/container names. Container IPs are ephemeral.

## Ports: container, host and published

If an app listens on port 3000 inside a container:

```yaml
ports:
  - "127.0.0.1:8080:3000"
```

- Container listens on `0.0.0.0:3000` inside its own namespace.
- Host accepts connections on `127.0.0.1:8080`.
- Docker forwards those connections to container port 3000.

`EXPOSE 3000` documents intent but does not publish the port.

## Bind to loopback by default

```yaml
ports:
  - "127.0.0.1:3000:3000"
```

versus:

```yaml
ports:
  - "3000:3000"
```

The second commonly binds all host interfaces. Use it only when LAN/external exposure is intentional and firewall/authentication are ready.

For the operator’s macOS workstation services, prefer loopback plus an explicitly configured Tailscale Serve/reverse-proxy path rather than accidental `0.0.0.0` exposure.

## Reaching the host from a container

On Docker Desktop, use:

```text
host.docker.internal
```

On native Linux Engine, this hostname may require explicit configuration:

```bash
docker run --add-host=host.docker.internal:host-gateway IMAGE
```

Avoid hard-coding the host’s current LAN IP.

## User-defined networks

```bash
docker network create mynet
docker run --network mynet --name api IMAGE
docker network inspect mynet
```

Compose creates project networks automatically. Use an `internal: true` backend network where services do not require external connectivity.

## Common networking mistakes

- Application listens on `127.0.0.1` inside the container instead of `0.0.0.0`.
- Host port is already occupied.
- One service tries to reach another at `localhost`; inside a container, `localhost` means that same container.
- VPN routes overlap Docker’s private subnets.
- Proxy variables are missing from build or runtime.
- DNS behavior differs between host, VM and container.
- Firewall rules target the wrong backend process on Desktop.

Diagnose:

```bash
docker compose ps
docker compose port app 3000
docker network ls
docker network inspect NETWORK
docker compose exec app getent hosts db
docker compose exec app sh -lc 'wget -S -O- http://db:PORT/ || true'
```

Use the smallest available diagnostic tool in the image; production images may intentionally omit `curl`, `ping` or a shell.

---

# 12. Security fundamentals

## Treat containers as isolation, not invulnerability

A container shares a kernel with its Docker host/VM. Security depends on the host, daemon, runtime configuration, image contents, capabilities, mounts and application behavior.

## Practical hardening checklist

- Use trusted, maintained base images.
- Pin versions and consider digest pinning for production.
- Rebuild regularly for patched dependencies.
- Run as a non-root user.
- Use read-only root filesystems where practical.
- Drop unnecessary Linux capabilities.
- Add only the precise capability needed.
- Use `no-new-privileges`.
- Avoid `--privileged`.
- Never expose the daemon unauthenticated.
- Do not mount the Docker socket into untrusted containers.
- Limit CPU, memory, PIDs and disk/log growth.
- Put only required ports on the host, preferably loopback.
- Keep secrets out of images, build arguments, Git and logs.
- Scan final images and record an SBOM/provenance where useful.
- Back up volumes and test restore procedures.

Example runtime restrictions:

```bash
docker run --rm \
  --read-only \
  --tmpfs /tmp:rw,noexec,nosuid,size=64m \
  --cap-drop ALL \
  --security-opt no-new-privileges:true \
  --memory 512m \
  --cpus 1.0 \
  --pids-limit 200 \
  IMAGE
```

Add back only what the application demonstrably needs.

## Secrets

Bad patterns:

```dockerfile
ENV API_KEY=...
ARG API_KEY
COPY .env /app/.env
```

Secrets can leak through layers, metadata, caches, process environments, crash reports or `docker inspect`.

Better options:

- BuildKit secret mounts for build-time credentials.
- Runtime secret files supplied by an orchestrator or protected host mount.
- A secret manager with short-lived credentials.
- Compose `secrets` where the deployment/runtime supports the required semantics.

`.env` helps configuration but is not automatically secure secret storage. Keep it out of Git and restrict permissions.

## Image scanning and supply chain

At minimum:

```bash
docker scout cves IMAGE:TAG
```

Or use another scanner such as Trivy/Grype. Scan the **final image**, not only package manifests or an intermediate stage.

For release builds, consider:

```bash
docker buildx build \
  --provenance=true \
  --sbom=true \
  -t REGISTRY/APP:TAG \
  --push .
```

A scanner finding is evidence to assess, not automatic proof of exploitability or safety. Record accepted residual risks.

---

# 13. Development, CI and production workflows

## Recommended development loop

1. Validate configuration:
   ```bash
   docker compose config -q
   ```
2. Build:
   ```bash
   docker compose build
   ```
3. Start:
   ```bash
   docker compose up -d
   ```
4. Check status and health:
   ```bash
   docker compose ps
   ```
5. Follow relevant logs:
   ```bash
   docker compose logs -f --tail=200 app
   ```
6. Run tests in the intended environment:
   ```bash
   docker compose run --rm app npm test
   ```
7. Rebuild/recreate after dependency or Dockerfile changes.
8. Stop without deleting data:
   ```bash
   docker compose stop
   ```

## Development versus production images

Development images may contain:

- Compilers, debuggers and test tools
- Bind-mounted source
- Hot reload
- Development dependencies

Production images should contain:

- Only runtime artifacts and dependencies
- A non-root runtime user
- A defined entrypoint/command
- Health checks or externally monitored readiness
- Minimal packages and no unnecessary shells/debuggers
- No bind-mounted source tree

Use multi-stage builds rather than deploying the development container.

## CI gate

A useful CI pipeline should:

1. Validate Dockerfile/Compose syntax.
2. Install from lockfiles.
3. Run lint, typecheck and tests.
4. Build the **final** image.
5. Start it and exercise a real smoke/health check.
6. Scan the final image.
7. Test the target architectures or build multi-platform.
8. Verify the image does not contain development-only dependencies or secrets.
9. Push only after all required checks pass.
10. Tag with an immutable commit/release identifier.

## Production with Compose

Compose is reasonable for a small, single-host service when you also provide:

- Version-pinned images
- External backups and restore tests
- Restart policies
- Health monitoring and alerting
- Resource ceilings
- Log rotation/collection
- Host patching and firewalling
- A controlled secrets mechanism
- Rollback instructions
- A staging or pre-production smoke test

Compose does not by itself provide multi-host scheduling, automatic failover, sophisticated rollout control or a complete backup system.

## Safe deployment pattern

1. Build once in CI.
2. Push an immutable image.
3. Pull that exact tag/digest on the target.
4. Back up durable data if a migration is involved.
5. Apply migrations with explicit rollback/recovery planning.
6. Replace containers.
7. Verify health and key user flows.
8. Keep the previous known-good image reference for rollback.

---

# 14. Docker Desktop in practical use

## What the GUI is good for

- Quick visibility into running/stopped containers
- Tail logs without remembering commands
- Inspect ports, mounts, environment and resource use
- Browse images and volumes
- Restart the Desktop backend
- Configure resource limits and file sharing
- Gather diagnostics

The CLI remains better for repeatable workflows because commands can be documented, scripted and reproduced.

## Settings to understand

### Resources

CPU, memory, swap and disk settings affect the Linux VM. Do not reduce the virtual disk or purge data without backups.

### File sharing

Bind-mounted host paths must be available to Desktop’s VM. A “mount denied” error may mean the path is outside shared locations or blocked by host permissions.

### WSL integration

Enable only the Windows WSL distributions that need Docker CLI integration. Store Linux projects in the WSL filesystem for performance.

### Proxies

Desktop and containers/builds may require separate proxy configuration. Check host system proxy, Desktop proxy settings, build arguments and runtime `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` as applicable.

### Kubernetes

Docker Desktop’s Kubernetes is optional and consumes resources. Do not enable it merely to learn Docker. Docker and Kubernetes are related but distinct layers.

### Extensions

Extensions are third-party software with access to Docker APIs and sometimes host capabilities. Install only trusted extensions and remove those no longer required.

### Reset and purge actions

Escalation order:

1. Restart a container/service.
2. Recreate the affected service.
3. Restart Docker Desktop.
4. Gather diagnostics and inspect logs.
5. Back up data.
6. Use Clean/Purge or factory reset only when scope and data loss are understood.

Factory reset is not a routine troubleshooting command.

## Desktop CLI

Recent Desktop versions provide commands such as:

```bash
docker desktop status
docker desktop logs
docker desktop diagnose
docker desktop restart
```

Availability varies by Desktop version. Use `docker desktop --help` to confirm locally.

---

# 15. Systematic troubleshooting workflow

> [!important]
> Do not repeatedly rerun `docker compose up` without learning which layer failed. Classify the failure, inspect the smallest relevant evidence, fix one layer, then retest that layer.

## Layer 1 — Are client and daemon connected?

```bash
docker version
docker context show
docker context ls
docker info
```

Symptoms:

- `Cannot connect to the Docker daemon`
- Wrong containers/images appear
- A command works in one terminal but not another

Checks:

- Is Desktop/Colima/Engine running?
- Is the active context correct?
- Are `DOCKER_HOST` or `DOCKER_CONTEXT` overriding the selected context?
- Does the user have socket permission on Linux?

```bash
env | grep '^DOCKER_' || true
```

## Layer 2 — Does Compose parse to what you expect?

```bash
docker compose config -q
docker compose config --services
docker compose config --images
```

Look for:

- Missing variables
- Wrong project/override file
- Invalid paths
- Unexpected image tags
- Host-port collisions

## Layer 3 — Does the image build?

```bash
docker compose build --progress=plain SERVICE
```

For a clean diagnostic build:

```bash
docker build --pull --no-cache --progress=plain -t app:debug .
```

Use no-cache diagnostically, not as a permanent substitute for understanding cache invalidation.

Look for:

- Wrong build context
- Files excluded by `.dockerignore`
- Dependency or lockfile mismatch
- Network/proxy failure
- Architecture mismatch
- Build-time database/network access that should not occur
- Missing native build headers/tools
- Secrets incorrectly expected in the build

## Layer 4 — Did the container start and stay running?

```bash
docker compose ps -a
docker compose logs --tail=200 SERVICE
docker inspect CONTAINER --format '{{json .State}}'
```

If it exits immediately, inspect command, entrypoint, environment, permissions and exit code.

## Layer 5 — Is it healthy?

A running process is not necessarily ready.

```bash
docker inspect CONTAINER --format '{{json .State.Health}}'
docker compose ps
```

Run the health command manually inside the container when possible.

Common health-check errors:

- Tool such as `curl` is absent in the minimal image.
- Check targets `localhost` but app listens elsewhere.
- Startup period is too short.
- Database dependency is not ready.
- Health endpoint itself depends on an unavailable external service.

## Layer 6 — Is networking correct?

```bash
docker compose port SERVICE CONTAINER_PORT
docker network inspect NETWORK
lsof -nP -iTCP:HOST_PORT -sTCP:LISTEN      # macOS/Linux
```

On Windows:

```powershell
Get-NetTCPConnection -LocalPort PORT -ErrorAction SilentlyContinue
```

Verify:

- App binds `0.0.0.0` in the container.
- Services call each other by service name.
- Host access uses the published host port.
- Host access from a container uses the appropriate host gateway.
- VPN/firewall/proxy does not intercept the route.

## Layer 7 — Are mounts and permissions correct?

```bash
docker inspect CONTAINER --format '{{json .Mounts}}'
docker compose exec SERVICE id
docker compose exec SERVICE ls -la /EXPECTED/PATH
```

Check:

- Source path exists.
- You mounted a file as a file and directory as a directory.
- A mount has not hidden files shipped in the image.
- Host path is shared with Desktop.
- UID/GID and read/write mode are correct.
- WSL project is not unnecessarily mounted from `/mnt/c`.

## Layer 8 — Are resources exhausted?

```bash
docker stats
docker system df
docker buildx du
```

Inspect host disk/memory too. Typical signs:

- Exit 137
- `no space left on device`
- BuildKit cache consumes large disk space
- Database corruption/recovery after abrupt kill
- Desktop VM disk at capacity

Clean only identified, unused objects.

## Layer 9 — Is architecture/OS correct?

```bash
uname -m
docker info --format '{{.OSType}}/{{.Architecture}}'
docker image inspect IMAGE --format '{{.Os}}/{{.Architecture}}'
docker buildx imagetools inspect IMAGE
```

Look for:

- ARM64 host with AMD64-only image
- Windows container mode with Linux image
- Native dependency copied from host into different container platform
- Final image never tested for the claimed platform

---

# 16. Common errors and practical responses

| Symptom | Likely causes | First checks |
|---|---|---|
| Cannot connect to daemon | Runtime stopped, wrong context/socket, permissions | `docker version`, `docker context ls`, runtime status |
| Port already allocated | Host process or another container owns port | `docker ps`, `lsof`/`Get-NetTCPConnection` |
| Container exits immediately | Main process failed/finished, bad command, missing env | `docker compose ps -a`, logs, inspect state |
| `exec format error` | Wrong CPU architecture or malformed entrypoint | image platform, line endings, shebang |
| `bad interpreter: ^M` | Windows CRLF in Linux script | line-ending settings and Git attributes |
| Mount denied | Desktop file sharing or host permissions | inspect mount path, Desktop Resources/File Sharing |
| Permission denied in mount | UID/GID/SELinux/read-only mismatch | `id`, numeric ownership, SELinux context |
| Service cannot reach DB | Used `localhost`, DNS/network mismatch, DB not ready | service name, network inspect, health |
| Build ignores source change | Wrong context, cache, `.dockerignore` | plain-progress build, context, Dockerfile order |
| `no space left on device` | Images, layers, logs, volumes or VM disk full | `docker system df -v`, host disk, build cache |
| Exit 137 | OOM or forced SIGKILL | inspect `OOMKilled`, `docker stats`, host memory |
| Works on Mac but not Linux | Case sensitivity, architecture, bind-mount assumptions | final image test on Linux target architecture |
| Works locally but not CI | hidden local files/cache, uncommitted config, architecture | clean checkout and no-cache final build |
| Missing files in container | `.dockerignore`, wrong `COPY`, bind mount obscures path | image inspection, mounts, build context |
| DNS/proxy failures | VPN, corporate DNS, missing proxy config | host/VM/container DNS and proxy layers |
| “Container unhealthy” | health command/tool/timeout wrong | inspect health log, run probe manually |

---

# 17. Logs, disk and cleanup

## Application logs

```bash
docker logs --tail=200 CONTAINER
docker logs -f --since=10m CONTAINER
docker compose logs -f --tail=200 SERVICE
```

Applications should normally log to stdout/stderr. Configure log rotation on long-running hosts to prevent unbounded JSON log growth.

## Docker daemon/Desktop logs

- Linux Engine: `journalctl -u docker.service` or `journalctl -xu docker.service`
- Docker Desktop: Troubleshoot menu, `docker desktop logs`, or platform-specific log locations
- macOS Console can filter for Docker processes
- Desktop internal logs may exist under `~/.docker/desktop/log/`

See [Docker daemon logs](https://docs.docker.com/engine/daemon/logs/) and [Desktop troubleshooting](https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/).

## Disk accounting

```bash
docker system df
docker system df -v
docker image ls
docker volume ls
docker builder prune --filter 'until=168h'
```

Review before deleting:

```bash
docker container prune
docker image prune
docker network prune
docker builder prune
docker system prune
```

`docker system prune` can remove stopped containers, unused networks, dangling images and build cache. Adding `-a` broadens image deletion. Adding `--volumes` can delete persistent data. Do not use broad pruning as a first response.

---

# 18. Upgrades, backup and recovery

## Before a Desktop/Engine upgrade

1. Record versions and context:
   ```bash
   docker version
   docker compose version
   docker context ls
   ```
2. Save Compose/Dockerfiles in version control.
3. Back up databases and important volumes.
4. Record critical image tags/digests.
5. Stop applications cleanly when the upgrade requires it.
6. Verify free disk space.
7. Read release notes for breaking changes.

## After upgrade

```bash
docker version
docker info
docker compose version
docker context ls
docker compose config -q
docker compose up -d
docker compose ps
docker compose logs --tail=100
```

Run a real smoke test rather than trusting “running” status.

## Recovery hierarchy

1. Recreate a single container from its image and configuration.
2. Rebuild the image from a clean checkout.
3. Restore a named volume/database into a separate recovery environment.
4. Restart the Docker runtime.
5. Repair/reinstall Desktop or Engine with backups preserved.
6. Factory reset only after verified external backups and explicit acceptance of local Docker-data loss.

---

# 19. Contexts and remote Docker hosts

Contexts let one CLI control different daemons:

```bash
docker context ls
docker context inspect CONTEXT
docker context use CONTEXT
docker --context CONTEXT ps
```

Use an SSH-backed context for a remote Linux host:

```bash
docker context create staging --docker host=ssh://user@staging-host
docker --context staging ps
```

> [!danger]
> Before destructive commands, verify context and target host. `docker compose down` against the wrong context can stop a remote application.

Safe preflight:

```bash
docker context show
docker info --format 'name={{.Name}} os={{.OperatingSystem}}'
docker compose ls
```

Do not expose `tcp://HOST:2375` without strong TLS/authentication and network controls. SSH or a properly secured daemon endpoint is preferable.

---

# 20. Practical workflow for the operator’s environments

## macOS workstation local service

1. Determine whether Colima or Docker Desktop owns the active context.
2. Validate Compose.
3. Check intended loopback ports for conflicts.
4. Start only the target stack.
5. Verify container health and an actual HTTP/database smoke test.
6. Keep admin interfaces on `127.0.0.1` unless a separate, approved Tailscale/reverse-proxy exposure exists.
7. Back up named volumes independently of the VM disk.

```bash
docker context show
docker compose config -q
docker compose up -d
docker compose ps
docker compose logs --tail=100
```

## Windows development workstation

1. Use Docker Desktop with WSL 2 for Linux containers.
2. Keep source under the Linux distribution’s home directory.
3. Enable Docker integration only for the intended WSL distribution.
4. Run Git/build tooling inside WSL for Linux-targeted projects.
5. Keep Dockerfiles and Compose paths Linux-compatible.
6. Test final images in CI on the production architecture.

## Linux server

1. Use native Engine unless Desktop-specific features are required.
2. Restrict Docker socket access.
3. Bind public services deliberately and firewall them.
4. Use explicit image versions/digests.
5. Run non-root containers with resource and log limits.
6. Back up volumes/databases off-host.
7. Monitor health, disk, restart loops and daemon logs.
8. Test rollback before risky upgrades.

---

# 21. Command cheat sheet

## Inspect current target

```bash
docker context show
docker context ls
docker version
docker info
```

## Containers

```bash
docker ps
docker ps -a
docker logs -f --tail=200 NAME
docker inspect NAME
docker stats
docker exec -it NAME sh
docker stop NAME
docker rm NAME
```

## Images/builds

```bash
docker image ls
docker pull IMAGE:TAG
docker build -t IMAGE:TAG .
docker build --pull --no-cache --progress=plain -t IMAGE:TAG .
docker history IMAGE:TAG
docker image inspect IMAGE:TAG
docker buildx imagetools inspect IMAGE:TAG
```

## Compose

```bash
docker compose config -q
docker compose build
docker compose up -d
docker compose ps
docker compose logs -f --tail=200
docker compose exec SERVICE sh
docker compose run --rm SERVICE COMMAND
docker compose restart SERVICE
docker compose stop
docker compose down
```

## Networks

```bash
docker network ls
docker network inspect NETWORK
docker port CONTAINER
```

## Volumes and disk

```bash
docker volume ls
docker volume inspect VOLUME
docker system df -v
docker buildx du
```

## Desktop

```bash
docker desktop status
docker desktop logs
docker desktop diagnose
docker desktop restart
```

Confirm Desktop CLI availability with `docker desktop --help`.

---

# 22. Rules of thumb

1. **Build images; replace containers. Do not hand-edit production containers.**
2. **Keep persistent data outside the container layer.**
3. **Back up volumes and test restores.**
4. **Use Compose v2: `docker compose`.**
5. **Validate with `docker compose config` before launch.**
6. **Use service DNS names between containers, never dynamic container IPs.**
7. **Bind host ports to `127.0.0.1` unless broader exposure is intentional.**
8. **Use lockfiles, multi-stage builds and a small non-root final image.**
9. **Build and smoke-test the final image in CI.**
10. **Test every claimed CPU architecture.**
11. **Never bake secrets into images or build arguments.**
12. **Treat Docker socket access as host-admin access.**
13. **Avoid `--privileged`, broad host mounts and unnecessary capabilities.**
14. **Check the Docker context before destructive actions.**
15. **Do not solve unknown problems with broad prune/reset commands.**
16. **On Windows/WSL, keep Linux-container source in the Linux filesystem.**
17. **On Apple Silicon, prefer native ARM64 or multi-architecture images over emulation.**
18. **A green container status is not proof that the application works—run a smoke test.**

---

# 23. Further reading

Primary official references used for this guide:

- [Docker overview and architecture](https://docs.docker.com/get-started/docker-overview/)
- [Docker Desktop](https://docs.docker.com/desktop/)
- [Docker Desktop networking](https://docs.docker.com/desktop/features/networking/)
- [Install Docker Desktop on Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Docker Desktop for Linux](https://docs.docker.com/desktop/setup/install/linux/)
- [Docker Desktop licensing](https://docs.docker.com/subscription/desktop-license/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Compose file reference](https://docs.docker.com/reference/compose-file/)
- [Environment variables in Compose](https://docs.docker.com/compose/how-tos/environment-variables/)
- [Dockerfile reference](https://docs.docker.com/reference/dockerfile/)
- [Build best practices](https://docs.docker.com/build/building/best-practices/)
- [Docker storage](https://docs.docker.com/engine/storage/)
- [Volumes](https://docs.docker.com/engine/storage/volumes/)
- [Bind mounts](https://docs.docker.com/engine/storage/bind-mounts/)
- [Networking overview](https://docs.docker.com/engine/network/)
- [Docker contexts](https://docs.docker.com/engine/manage-resources/contexts/)
- [Docker Engine security](https://docs.docker.com/engine/security/)
- [Rootless mode](https://docs.docker.com/engine/security/rootless/)
- [WSL 2 best practices](https://docs.docker.com/desktop/features/wsl/best-practices/)
- [Docker Desktop troubleshooting](https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/)
- [Docker daemon logs](https://docs.docker.com/engine/daemon/logs/)
- [Docker Desktop backup and restore](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/)

> [!note]
> Docker changes quickly. Treat platform requirements, Desktop licensing, supported operating-system versions and experimental Desktop features as time-sensitive; verify the linked official documentation before a major installation or organizational rollout.
