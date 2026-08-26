---
title: "Docker and Kubernetes — Practical Beginner Guide"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Docker and Kubernetes — Practical Beginner Guide

> [!summary] The benefit in one sentence
> **Docker packages an application so it runs consistently; Kubernetes operates many containerized applications across machines and keeps them near the desired state.**

Source carousel: [Cloud DevOps Engineer on TikTok](https://www.tiktok.com/t/ZP8nxkGRF/)

This write-up expands and corrects the four-page cheat sheet. The screenshots preserve the creator's overview; the explanations below add practical context, limitations, and a small exercise you can actually run.

## The simplest mental model

Think of a restaurant chain:

- **Docker image:** the documented kitchen design and recipe book.
- **Container:** one operating kitchen created from that design.
- **Container registry:** the warehouse where approved kitchen designs are stored.
- **Kubernetes:** the operations manager deciding which locations run which kitchens, replacing failed kitchens, scaling capacity, and routing customers.

Docker answers: **“How do I package and run this application consistently?”**

Kubernetes answers: **“How do I operate many copies reliably across a cluster?”**

---

# Part I — Docker

## Screenshot 1 — Docker overview

> Screenshot omitted from the public export; the surrounding explanation is complete without it.

## 1. What Docker is

Docker is a platform and toolchain for building, distributing, and running applications in **containers**.

A container is not a miniature virtual machine. It is a set of operating-system processes isolated with kernel features such as namespaces and resource controls. Containers normally:

- Start faster than full virtual machines.
- Share the host kernel.
- Package application code and runtime dependencies together.
- Produce repeatable environments when the image and configuration are pinned.

> [!warning] Important limitation
> “Build once, run anywhere” means *compatible infrastructure*. An image built only for ARM64 will not automatically run natively on an x86-64 host, and a Linux container still needs a Linux kernel—directly or through a lightweight VM such as Docker Desktop's Linux VM on macOS.

## 2. The three core Docker objects

### Dockerfile

A text file containing instructions used to build an image.

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
```

### Image

An immutable, layered application package produced from a Dockerfile or pulled from a registry.

An image usually contains:

- Application files.
- Runtime libraries.
- Default command or entrypoint.
- Metadata and environment defaults.

### Container

A running—or stopped—instance of an image with a writable runtime layer, process state, network interfaces, and optional persistent volumes.

Many containers can be created from one image.

## 3. Basic flow

```text
Write Dockerfile
      ↓
Build immutable image
      ↓
Store or pull image from registry
      ↓
Create and run container
      ↓
Observe logs, health, ports and resource use
      ↓
Replace container with a new image version when updating
```

## 4. Essential Docker commands

```bash
# Build an image from the Dockerfile in the current directory
docker build -t myapp:local .

# Run it in the background and publish a port
docker run --detach --name myapp -p 8080:80 myapp:local

# Show running containers
docker ps

# Show running and stopped containers
docker ps --all

# Follow logs
docker logs --follow myapp

# Inspect configuration and runtime state
docker inspect myapp

# Stop, then remove the container
docker stop myapp
docker rm myapp

# List local images
docker image ls
```

Useful operating habit: **containers should be disposable; important data should not live only in their writable layers.**

## Screenshot 2 — Docker architecture, volumes and networking

> Screenshot omitted from the public export; the surrounding explanation is complete without it.

## 5. Docker architecture

Docker normally follows a client/server model:

```text
Docker CLI or API client
          ↓
Docker daemon / engine
   ├── manages images
   ├── creates containers
   ├── manages networks
   └── manages volumes
          ↕
Container registry
```

The CLI sends commands to the engine through an API. The engine pulls and pushes images from registries such as Docker Hub or a private registry.

Security implication: access to the Docker daemon is highly privileged. Do not expose its socket or unauthenticated API to untrusted users or containers.

## 6. Persistent storage

The container writable layer is normally temporary. Use a **volume** or controlled bind mount for data that must survive replacement.

### Named volume

```bash
docker volume create app-data

docker run --detach \
  --name app \
  --mount type=volume,source=app-data,target=/var/lib/app \
  myapp:local
```

### Bind mount for local development

```bash
docker run --rm \
  --mount type=bind,source="$PWD",target=/workspace \
  -w /workspace \
  python:3.12-slim python app.py
```

Use bind mounts carefully: they expose a host directory directly to the container. Prefer read-only mounts where writes are unnecessary:

```bash
--mount type=bind,source="$PWD/config",target=/config,readonly
```

## 7. Networking

A user-defined bridge network lets containers find each other by container or service name.

```bash
docker network create app-network

docker run --detach --name database --network app-network postgres:17

docker run --detach --name api --network app-network -p 8000:8000 my-api:local
```

Inside `api`, the database hostname would normally be `database`, not `localhost`.

Common network modes include:

- **bridge:** normal single-host container networking.
- **host:** container uses the host network namespace; behavior differs on Docker Desktop.
- **none:** no external container networking.
- **overlay:** multi-host networking, commonly with Docker Swarm.
- **macvlan:** gives containers addresses visible on the physical network; requires careful network design.

## 8. Better Docker practices

- Pin base-image versions instead of relying only on `latest`.
- Use `.dockerignore` to exclude Git history, local caches, credentials, and unnecessary files.
- Use multi-stage builds to keep production images small.
- Run as a non-root user when the application permits it.
- Do not bake credentials into images or Dockerfiles.
- Add health checks and structured logs.
- Scan images and dependencies before release.
- Rebuild and replace containers instead of manually patching running containers.
- Use one main responsibility per container, while allowing intentional helper/sidecar processes when justified.

---

# Part II — Kubernetes

## Screenshot 3 — Kubernetes overview and architecture

> Screenshot omitted from the public export; the surrounding explanation is complete without it.

## 9. What Kubernetes is

Kubernetes is an open-source orchestration system for deploying and operating containerized workloads across a cluster.

You declare the **desired state**—for example, three healthy copies of an API—and Kubernetes continuously reconciles actual state toward it.

Kubernetes can provide:

- Scheduling across worker nodes.
- Restart and replacement of failed workloads.
- Horizontal scaling.
- Rolling updates and rollback support.
- Stable service discovery.
- Configuration and secret injection.
- Resource requests and limits.
- Extensible storage and networking.

It does not automatically make an application well designed, secure, observable, or highly available. Those properties still require application and infrastructure work.

## 10. Kubernetes architecture

### Control plane

The control plane makes cluster-level decisions and stores desired state.

- **API server:** the authenticated front door for cluster operations.
- **Scheduler:** chooses a suitable node for unscheduled Pods.
- **Controller manager:** runs reconciliation controllers.
- **etcd:** strongly consistent key-value store containing cluster state.

“Control plane” is the current term; older material may call it the “master.”

### Worker node

A worker node runs application workloads.

- **kubelet:** ensures assigned Pods and containers run on the node.
- **container runtime:** runs containers, commonly containerd or CRI-O.
- **kube-proxy or another dataplane implementation:** supports Service networking.
- **Pods:** the scheduled workload units.

### Simplified request flow

```text
User or CI system
      ↓
kubectl / API client
      ↓
API server validates and stores desired state
      ↓
Controllers reconcile resources
      ↓
Scheduler assigns pending Pods
      ↓
kubelet starts containers on selected worker nodes
      ↓
Status flows back through the API server
```

## 11. Core Kubernetes resources

### Pod

The smallest deployable Kubernetes unit. A Pod contains one or more tightly coupled containers sharing the same network namespace. Containers share storage only through volumes explicitly attached to the Pod.

Pods are ephemeral. Manage application Pods through a controller rather than treating an individual Pod as a permanent server.

### Deployment

Manages stateless application replicas through ReplicaSets. It supports declarative scaling, rolling updates, and rollout history.

### Service

Provides stable service discovery and a virtual address for selected Pods.

Common Service types:

- **ClusterIP:** internal cluster access; default.
- **NodePort:** exposes a port on each node.
- **LoadBalancer:** requests an external load balancer when the environment supports one.
- **ExternalName:** returns a DNS alias to an external name.

### ConfigMap

Stores non-secret configuration.

### Secret

Stores sensitive values as a Kubernetes object. Secret data is usually base64 encoded—not encrypted merely because it is a Secret. Protect Secrets with RBAC, encryption at rest, workload identity, and an external secret manager where appropriate.

### Namespace

Groups and scopes namespaced resources. A Namespace is not, by itself, a complete security boundary. Use RBAC, NetworkPolicies, admission controls, and resource quotas for meaningful separation.

## 12. Essential kubectl commands

```bash
# Confirm the active cluster and user context
kubectl config current-context
kubectl config get-contexts

# List resources
kubectl get nodes
kubectl get pods --all-namespaces
kubectl get services
kubectl get deployments

# Inspect a resource
kubectl describe pod <pod-name>
kubectl get deployment <name> -o yaml

# Apply declarative configuration
kubectl apply -f app.yaml

# View application logs
kubectl logs deployment/myapp --follow

# Inspect recent cluster events
kubectl get events --sort-by=.metadata.creationTimestamp

# Show rollout status and history
kubectl rollout status deployment/myapp
kubectl rollout history deployment/myapp

# Undo the most recent Deployment rollout
kubectl rollout undo deployment/myapp

# Delete resources defined by a manifest
kubectl delete -f app.yaml
```

> [!warning] Context check
> Always run `kubectl config current-context` before an apply, delete, scale, or rollout command. A correct command against the wrong cluster is still a serious failure.

## Screenshot 4 — Pods, Services, Deployments and interview topics

> Screenshot omitted from the public export; the surrounding explanation is complete without it.

## 13. How the major resources fit together

```text
Deployment
   ↓ manages
ReplicaSet
   ↓ maintains
Pods
   ↑ selected by labels
Service
   ↑ reached by
Client or Ingress/Gateway
```

A typical update works like this:

1. Change the image tag or Pod template in the Deployment.
2. Kubernetes creates a new ReplicaSet.
3. New Pods become ready according to readiness probes.
4. The Service routes traffic only to ready selected Pods.
5. Old Pods are terminated gradually according to rollout strategy.
6. Roll back if health or application checks fail.

## 14. Minimal Deployment and Service example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-web
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-web
  template:
    metadata:
      labels:
        app: hello-web
    spec:
      containers:
        - name: web
          image: nginx:1.27-alpine
          ports:
            - containerPort: 80
          readinessProbe:
            httpGet:
              path: /
              port: 80
          resources:
            requests:
              cpu: 50m
              memory: 32Mi
            limits:
              cpu: 250m
              memory: 128Mi
---
apiVersion: v1
kind: Service
metadata:
  name: hello-web
spec:
  selector:
    app: hello-web
  ports:
    - port: 80
      targetPort: 80
  type: ClusterIP
```

Apply and test it on a disposable local cluster:

```bash
kubectl config current-context
kubectl apply -f hello-web.yaml
kubectl rollout status deployment/hello-web
kubectl get pods -l app=hello-web
kubectl port-forward service/hello-web 8080:80
```

Then visit `http://127.0.0.1:8080`.

Cleanup:

```bash
kubectl delete -f hello-web.yaml
```

---

# Part III — A safe 30-minute hands-on exercise

## Exercise A — Run an existing Docker image

Prerequisite: Docker Desktop, Colima, or another compatible Docker engine must already be running.

```bash
docker version
docker run --detach --name hello-nginx -p 8080:80 nginx:1.27-alpine
docker ps
docker logs hello-nginx
```

Open `http://127.0.0.1:8080` and confirm the nginx page appears.

Inspect and clean up:

```bash
docker inspect hello-nginx
docker stop hello-nginx
docker rm hello-nginx
```

## Exercise B — Build your own tiny site image

Create `index.html`:

```html
<!doctype html>
<html lang="en">
  <head><meta charset="utf-8"><title>Container Demo</title></head>
  <body><h1>Hello from a Docker container</h1></body>
</html>
```

Create `Dockerfile`:

```dockerfile
FROM nginx:1.27-alpine
COPY index.html /usr/share/nginx/html/index.html
```

Build and run:

```bash
docker build -t hello-site:local .
docker run --rm -p 8080:80 hello-site:local
```

Definition of completion:

- The image builds without error.
- `docker image ls hello-site` lists it.
- `http://127.0.0.1:8080` shows your custom page.
- No credential or private file was copied into the build context.
- The container can be deleted and recreated with the same result.

---

# Part IV — Interview-question quick answers

## Docker

**Image versus container:** an image is the immutable package; a container is a runtime instance created from it.

**How is an image built?** Docker processes Dockerfile instructions into cached filesystem layers plus metadata.

**How is data persisted?** Use named volumes, bind mounts, databases, or external storage—not only the container writable layer.

**CMD versus ENTRYPOINT:** `ENTRYPOINT` defines the executable; `CMD` supplies defaults that can be replaced more easily. Their exact interaction depends on shell versus exec form.

## Kubernetes

**Pod versus container:** a Pod is the Kubernetes scheduling unit and may contain multiple cooperating containers.

**Deployment versus ReplicaSet:** the ReplicaSet maintains a number of Pods; a Deployment manages ReplicaSets and rollout history.

**How does a Pod receive an IP?** The cluster's CNI networking plugin configures Pod networking according to the environment.

**What happens when a node fails?** The control plane detects the loss; controllers create replacement Pods elsewhere when scheduling constraints, capacity, and storage allow it.

**How does scheduling work?** The scheduler filters and scores nodes using resource requirements, affinity, taints/tolerations, topology, volumes, policies, and plugins.

**How should Secrets be handled?** Avoid committing them to Git. Restrict access, enable encryption at rest, prefer workload identity, and synchronize from an approved secret manager.

**How do you troubleshoot a failing application?** Check context, desired state, Pod status, events, container logs, probes, resources, Services/selectors, endpoints, DNS/network policy, mounted configuration, and recent rollouts—in that order.

---

# What the original cheat sheet simplifies

| Cheat-sheet idea | More precise interpretation |
|---|---|
| Docker provides “security” | Containers provide useful isolation, but usually share the host kernel and are not automatically equivalent to VM security. |
| One container equals one service | Good default for a main responsibility, not a rigid rule; sidecars and tightly coupled helper processes are legitimate. |
| Volumes provide better performance | Performance depends on storage driver, host OS, filesystem, mount type, and workload. The reliable claim is persistence and controlled data sharing. |
| Kubernetes provides load balancing | Services provide stable discovery and traffic distribution; an external load balancer depends on the cluster environment and configuration. |
| Pods share storage | Containers share a Pod network; storage is shared only when an attached volume is mounted by those containers. |
| Namespace provides isolation | It provides naming and organizational scope. Security isolation requires RBAC, NetworkPolicies, policies, and quotas. |
| Secret stores data securely | It creates a separate sensitive-data object, but values are commonly only base64 encoded unless encryption and access controls are configured. |
| Kubernetes self-heals everything | Controllers replace failed workloads when the workload design, capacity, dependencies, storage, probes, and policies allow it. |

---

# Recommended learning order

1. Run and inspect one Docker container.
2. Build one image from a Dockerfile.
3. Learn ports, logs, environment variables, volumes, and networks.
4. Use Docker Compose for a small multi-container application.
5. Learn Kubernetes Pods, Deployments, Services, ConfigMaps, and Secrets.
6. Operate a disposable local cluster with `kind`, `k3d`, minikube, or Docker Desktop Kubernetes.
7. Add probes, resource requests/limits, rollout verification, and observability.
8. Only then move toward production networking, storage, security, autoscaling, and GitOps.

## Practical relevance for the operator's systems

- **Echo:** Docker/Compose can package its application, Postgres, and supporting workers consistently.
- **n8n:** containers simplify repeatable local and server deployment, but workflow data and database storage must be persistent and backed up.
- **GIS APIs:** FastAPI/PostGIS workers can be containerized; large GIS files and databases should use controlled storage rather than image layers.
- **Hermes infrastructure:** Kubernetes would become useful only when independent services, replicas, failure recovery, and multi-node scheduling justify its complexity. Docker/Compose remains the simpler choice for many single-Mac services.

---

# Source and capture notes

- Original source: [TikTok carousel](https://www.tiktok.com/t/ZP8nxkGRF/)
- Creator shown in the post: **Cloud DevOps Engineer** (`@clouddevopsengineer`)
- Format: four-image public carousel.
- Screenshots were captured from TikTok's official embedded player on 2026-08-08 for private study and commentary.
- This note expands the creator's cheat sheet and adds independent technical corrections; it is not an official Docker or Kubernetes document.

For production decisions, confirm current behavior with the official [Docker documentation](https://docs.docker.com/) and [Kubernetes documentation](https://kubernetes.io/docs/).
