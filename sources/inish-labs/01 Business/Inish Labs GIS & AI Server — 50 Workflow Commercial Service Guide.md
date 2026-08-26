---
title: "Inish Labs GIS & AI Server — 50 Workflow Commercial Service Guide"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Inish Labs GIS & AI Server — 50 Workflow Commercial Service Guide

> [!important] Current-state boundary — verified 2026-08-26
> `example-gis-server` is live private compute, but the GIS application stack is **not deployed**: Docker is installed, zero containers exist, and no GIS application ports are listening. The 50 workflows below are designs and commercial hypotheses backed by vault runbooks and category evidence—not working products, compliance claims, or validated Inish demand.

## Executive decision

Do **not** sell “access to a GIS AI server.” Sell a narrow operational result with a buyer, trigger, accepted artifact, reviewer and metric. Host it as a **single-tenant managed workflow environment** only after the required stack, backup/restore, identity, monitoring and support controls have been exercised.

The best initial front doors are:

1. **GIS Workflow Reliability Sprint** — one ETL/QA/release workflow.
2. **Field-to-Verified-Deliverable Sprint** — one inspection type, correction queue and approved report.
3. **Cited Site Evidence Dossier** — one site decision, reproducible constraints and qualified review.
4. **ArcGIS Governance and Cost Audit** — read-only diagnostic that can convert to remediation.

The best first transaction is a paid diagnostic/pilot through an established AEC, environmental or GIS consultancy—not a broad autonomous-agent platform. The commercial baseline remains **no verified paying customer or repeatable offer**; all prices are hypotheses.

## What “use all components” means

A trustworthy architecture uses the **smallest necessary subset per workflow**. Forcing every service into every job increases failure modes and support cost. Across the catalog, all planned components have a defined role; each card states when a component is active and when it is deliberately unnecessary.

## Planned platform role map

| Component | Correct role | Must not become |
|---|---|---|
| Hetzner Ubuntu + Docker Compose | Per-client compute, service packaging and recoverable lifecycle | A shared unisolated multi-client production box |
| PostgreSQL + PostGIS | Authoritative relational/spatial truth, GIS calculations, status and audit-support data | A free-form agent playground |
| pgvector + Apache AGE | Permissioned semantic recall and explicit relationship traversal alongside spatial truth | Replacements for PostGIS or professional reasoning |
| Spatial RAG / FastAPI / FastMCP | Evidence retrieval and typed spatial-operation interface | Free-form SQL or autonomous spatial decision-maker |
| n8n | Schedules, webhooks, retries, integrations and human-routing states | Geometry engine, transaction authority or secret broker to prompts |
| Redis/worker queue | Cache and bounded long-running job queue | Durable system of record |
| pg_tileserv / optional QGIS Server | Vector tiles and, only when needed, advanced authored map/OGC delivery | Public exposure by default |
| LiteLLM | Approved model routing, budgets and per-key policy | Workflow engine or approval system |
| Langfuse | Model-call trace, latency/cost/evaluation evidence | GIS/system-of-record audit ledger |
| Hermes | Bounded project worker under a dedicated client profile | primary-agent clone, production admin or autonomous operator |
| Esri/Postgres/Composio/Spatial Ops MCPs | Typed, least-privilege connection and operation surfaces | Generic credential-bearing tool access |
| code-server | Private development workspace | Browser root shell or customer application |
| Claude Code / Codex | Isolated implementation, test and review work | Secret reader, production deployer or unsupervised maintainer |
| Tailscale / SSH | Private identity-aware administration and service mesh | Public dashboard/Funnel by convenience |
| Object storage + database backups/snapshots | Immutable raw/evidence artifacts and recoverability | “Backup” without tested restore evidence |

## Live readiness gate

Before calling any recurring server workflow “available,” complete and verify:

1. pinned Compose stack and health checks;
2. per-client isolation, roles and secret handling;
3. PostGIS extensions/schema migrations and restore rehearsal;
4. private-only ingress unless a separately approved public endpoint is essential;
5. typed Spatial Ops APIs and no unrestricted SQL/tool execution;
6. n8n retry/idempotency and approval-state tests;
7. LiteLLM budget/data policy plus Langfuse redaction/evaluation;
8. object-storage/database backup and off-server restore proof;
9. business-output monitoring, support hours, revoke/offboarding and exit package;
10. one synthetic proof followed by one paid client pilot with UAT.

## Market evidence and niche selection

Current research supports purchase categories, not Inish Labs close probability. Vendor case studies are positive-selection evidence; public programs show category activity; neither proves the operator has a reachable buyer.

| Niche                          | Evidenced problem / budget signal                                                       | What to sell                                             | What not to sell                                |
| ------------------------------ | --------------------------------------------------------------------------------------- | -------------------------------------------------------- | ----------------------------------------------- |
| AEC/environmental consulting   | AECO cost, talent and execution pressure [R1][R2]; field-report labor [R3]              | One field-to-report or data-reliability workflow         | Generic “AI transformation”                     |
| Construction/digital delivery  | Repeated CAD→GIS changes and standards failures; quantified case [R4]                   | Controlled design-data pipeline and decision portal      | Map-only portal                                 |
| Utilities/asset operations     | Cross-system location discrepancies and field search time [R5]; infrastructure gap [R9] | Asset identity/field/maintenance reliability sprint      | Autonomous work-order or safety decisions       |
| Environmental/site diligence   | Brownfields assessment/cleanup activity [R6]                                            | Cited preliminary screen with professional gate          | ESA, permit or legal conclusion by AI           |
| Telecom/broadband              | FCC location/file specifications and active BEAD deployment [R7][R8]                    | BSL matching, serviceability QA and route support        | Unlicensed Fabric redistribution or OSP signoff |
| Energy/infrastructure siting   | Transmission constraints and planning need [R10]                                        | Reproducible constraints/scenario package                | “Optimal site” claim without review             |
| Terrain/imagery/change         | Public elevation and imagery have documented value [R11][R12]                           | Narrow change, terrain or delivery pipeline              | Undifferentiated imagery dashboard              |
| Property/climate/insurance     | Large 2025 catastrophe losses [R13]                                                     | Portfolio evidence tied to capex/inspection/underwriting | Generic hazard map or underwriting automation   |
| Agriculture/forestry           | Precision-tech adoption motivated by labor/input/soil outcomes [R14]                    | Reviewed monitoring for larger operators/partners        | Broad small-farm SaaS before validation         |
| GIS AI / knowledge work        | Governance standards are current [R15], but agent demand alone is weak                  | Permissioned cited assistant attached to a paid workflow | Generic autonomous GIS agent                    |
| Platform monitoring/permitting | Strong incumbents already exist [R16][R17]                                              | Integration and operating assurance around client tools  | Clone ArcGIS Monitor or PermitFlow              |

## Commercial model — managed private GIS operations

Sell four layers, not raw infrastructure:

1. **Paid discovery / workflow reliability diagnostic:** typically $1.5k–$6k; baseline, data/access audit, workflow contract, risk register and fixed pilot proposal.
2. **Implementation sprint:** normally $6k–$25k for one bounded workflow; higher only where integration, imagery or specialist participation is explicit.
3. **Managed operations:** normally $1k–$6k/month after acceptance; monitored runs, exception triage, updates, model routing, backup/restore, source/schema drift, quarterly value review and transferable runbook.
4. **Pass-through costs:** client licenses, imagery/data, model/API use, travel, object storage and specialist review stay visible.

### Isolation and ownership

- Default: one client environment/database/bucket/identity boundary; do not host unrelated clients in one shared production data plane.
- Prefer client-owned accounts for production. If Inish hosts, contract for data processing, retention, subprocessors, support, incident notice, export and deletion.
- Inish operates the workflow; the client owns business decisions and professional approvals.
- No 24/7 SLA without a named backup operator and funded coverage.

## The 50 workflows

### 1. Field inspection and audit workflow modernization

- **Niche / buyer:** field operations, quality, environmental, utility-services, telecom, civil, or asset-maintenance manager.
- **Paid trigger / problem:** paper/Excel inspection data, detached photographs, duplicate entry, missing fields, slow correction, or delayed client/regulatory report.
- **Outcome:** one inspection type moves from field capture to deterministic validation, correction, review, and one approved report/dashboard.
- **Delivered artifact:** workflow map; data contract; mobile form; test dataset; validation/exception queue; map/dashboard; approved report export; audit history; training; operations and rollback runbook.
- **Action enabled:** staff can identify incomplete/invalid submissions, correct them, review evidence, and release an approved deliverable faster.
- **Major processing chain:** Qualify one inspection transaction → Observe the current workflow → Write the workflow and data contract → Create acceptance fixtures → Choose and provision staging → Build the mobile form and map → Implement deterministic validation → Build the correction/review queue → Generate the controlled deliverable → Test devices and failure paths → Run client UAT and measure the pilot → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Esri/client-ArcGIS lane
- Survey123 Connect for conditional forms, calculations, repeats, attachments, and validation.
- Field Maps when the task starts from an existing mapped asset and needs offline areas or map-centric editing.
- ArcGIS Online or Enterprise hosted feature layers and related tables.
- ArcGIS Dashboards or Experience Builder for office review and status.
- ArcGIS API for Python/REST webhooks or n8n for approved validation and routing.
- Survey123 report templates or a controlled document-generation service.
- ArcGIS Pro/ArcPy only when genuinely required, running on client Windows/ArcGIS Pro or an approved licensed Windows worker—not natively on macOS.
#### Open-source/vendor-neutral lane
- QField/QFieldCloud, ODK Central/KoboToolbox, SurveyCTO, or another client-approved field platform.
- PostgreSQL/PostGIS or GeoPackage for a bounded offline pilot.
- FastAPI/Pydantic for typed validation and workflow endpoints.
- Python, GeoPandas, Shapely, pyproj, and GDAL for deterministic spatial/data checks.
- n8n or a bounded worker for event routing, correction notifications, and approved report generation.
- Metabase/Superset or a lightweight MapLibre application for office review.
#### AI lane, only if justified AI may draft narrative from validated fields and selected photographs/documents, classify bounded notes, or summarize the exception queue. It must return record/source IDs and `unknown` when evidence is missing. It must not determine compliance, safety, engineering condition, environmental impact, or final acceptance.

- **Human approval / exclusions:** field staffing, device procurement, legal/regulatory determinations, engineering/environmental judgments, emergency dispatch, unrestricted production edits, and external submission without named approval.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 4–6 weeks.
- **Commercial hypothesis:** $8k–$20k pilot; $20k–$60k rollout; $1.5k–$4k/mo support. Buyer-value hypothesis: $25k–$150k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Monitor failed submissions, validation exceptions, webhook/job failures, queue age, report errors, storage/attachment growth, service/API changes, and credential expiry. Review schema, domain, asset-layer, mobile OS/app, template, and business-rule changes before deployment.
- **Evidence:** references [12][13][14] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 2. Spatial ETL and CAD/BIM/GIS automation

- **Niche / buyer:** AEC delivery manager, GIS manager, BIM/VDC lead, utility data manager, or environmental consultancy operations lead.
- **Paid trigger / problem:** a recurring conversion/update requires manual renaming, projection, joins, QA, publishing, or repair and creates delay/rework.
- **Outcome:** one defined source package becomes one deterministic, validated target dataset or release package with an exception log.
- **Delivered artifact:** source/target contract; automated pipeline; configuration; test fixtures; exception outputs; run manifest; controlled publish/release step; runbook; training; rollback package.
- **Action enabled:** a trained operator can run the conversion repeatedly, understand failures, approve the release, and reproduce prior outputs.
- **Major processing chain:** Select one recurring transaction → Capture representative evidence → Write source and target contracts → Create a mapping and exception policy → Build immutable fixtures and a gold output → Provision isolated staging → Implement ingestion and normalization → Implement deterministic transformation → Implement QA and exception outputs → Build the controlled release step → Exercise operational failures and UAT → Handoff and measure.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Vendor-neutral lane
- GDAL/OGR for format conversion and inspection.
- Python with GeoPandas, Shapely, pyproj, Fiona/pyogrio, Pandera/Pydantic, and DuckDB Spatial where useful.
- ezdxf for bounded DXF semantics; IfcOpenShell for approved IFC extraction; source-authoring application export is preferred when proprietary semantics are needed.
- PostgreSQL/PostGIS for recurring multiuser targets, geometry constraints, indexes, and transactional release.
- GeoPackage/GeoParquet for bounded file delivery.
- Docker/uv or equivalent reproducible environment, pytest, and golden fixtures.
- n8n/scheduler/queue only when recurrence and approval routing justify it.
#### Esri/FME lane
- FME Form for authored workspaces and FME Flow for scheduled, monitored, client-owned execution.
- ArcGIS Data Interoperability where already licensed and supportable.
- ArcGIS Pro geoprocessing/ArcPy on a licensed Windows environment for geodatabase-specific behavior, annotation, topology, Utility Network, or publishing that open tools cannot faithfully reproduce.
- ArcGIS API for Python/REST for staging item/service publication and validation.
#### BIM/cloud lane
- Autodesk-authorized exports or Autodesk Platform Services only when the client owns access and API use is contractually approved.
- IFC as an interchange format when it preserves required geometry/properties; validate model view, units, georeferencing, and property-set mapping. AI is generally unnecessary. It may help classify free-text exceptions or draft a run summary from verified metrics, but it must not infer coordinate systems, field mappings, engineering meaning, or whether a record is fit for release.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 3–6 weeks.
- **Commercial hypothesis:** $10k–$25k pilot; $25k–$75k implementation; $2k–$6k/mo. Buyer-value hypothesis: $60k–$300k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Monitor job success, queue age, runtime, volume, exception rate/type, schema/version changes, target capacity, and variable license/cloud cost. Review source application/export and target schema changes before upgrading.
- **Evidence:** references [10][11] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 3. GIS data QA, schema remediation and provenance

- **Niche / buyer:** GIS/data manager, utility asset owner, engineering/environmental delivery manager, migration lead, or application owner.
- **Paid trigger / problem:** geometry, attributes, duplicates, freshness, lineage, ownership, or schema defects block migration, reporting, publishing, analysis, or trustworthy decisions.
- **Outcome:** measure one data domain, agree deterministic rules, prioritize defects, repair only approved classes, and deliver a reproducible quality/provenance package.
- **Delivered artifact:** source inventory; quality contract; baseline profile; defect layers/tables; severity and ownership queue; approved repair process; before/after evidence; provenance ledger; tests; runbook.
- **Action enabled:** the client can decide what is usable, repairable, quarantined, or owner-resolved and can repeat the checks before release.
- **Major processing chain:** Define the decision and domain → Preserve and inventory sources → Write the quality contract → Profile without mutation → Build deterministic defect rules → Create a defect and uncertainty queue → Agree remediation classes → Repair only in staging → Re-run full QA and downstream tests → Produce the release package → Obtain acceptance and release → Handoff repeatable governance.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

- **Inspection/profile:** QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj, DuckDB Spatial, SQL.
- **Contracts/tests:** Pydantic, Pandera, pytest, SQL constraints, Great Expectations/Soda where appropriate.
- **Database:** PostgreSQL/PostGIS constraints, indexes, views, functions, transaction, and audit approach.
- **Esri:** ArcGIS Data Reviewer if owned; ArcGIS Pro validation/topology/geodatabase tools and ArcPy on licensed Windows; ArcGIS API for Python/REST for service metadata/content checks.
- **Metadata/provenance:** ISO/DCAT/client catalog fields, dataset/run/source IDs, source-vintage/license/owner/transform records, and checksums where allowed.
- **Reporting:** controlled summary plus defect GeoPackage/feature layer/CSV and acceptance evidence. AI is not required. It may cluster free-text defect descriptions or draft explanations from verified metrics, but it must not decide which duplicate is authoritative, infer missing attributes, or approve repairs.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 2–5 weeks.
- **Commercial hypothesis:** $6k–$18k assessment; $15k–$50k remediation. Buyer-value hypothesis: $20k–$150k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Run the agreed checks at intake, before publish/migration, or on schedule. Track defect counts/rates by rule/severity/owner, recurrence, time-to-resolution, freshness, schema drift, and unresolved critical items.
- **Evidence:** references [10][11][16] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 4. AEC/environmental site constraints dossier

- **Niche / buyer:** environmental consultancy project manager, civil/site engineer, developer/acquisition lead, or infrastructure planning manager.
- **Paid trigger / problem:** an early site/route decision requires fragmented parcel, environmental, hazard, infrastructure, terrain, and regulatory evidence before commissioning deeper studies.
- **Outcome:** a cited, review-ready evidence package for one defined site and decision, with deterministic constraint relationships, source dates, uncertainty, and next-investigation questions.
- **Delivered artifact:** AOI definition; decision/constraint matrix; source and license register; immutable source snapshots or retrieval evidence; normalized GIS package; constraint map series; conflict/uncertainty table; cited memo; qualified-review record; handoff archive.
- **Action enabled:** the buyer can decide whether to investigate, reject, redesign, or escalate the site—with evidence and limitations visible.
- **Major processing chain:** Define the paid decision → Fix the AOI and boundary uncertainty → Write a jurisdiction-specific constraint matrix → Build the source and license register → Acquire and preserve evidence → Normalize data deterministically → Run explicit spatial tests → Create the evidence/uncertainty table → Produce map and cited draft → Run technical QA → Obtain qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

- **GIS:** QGIS; GDAL/OGR; GeoPandas/Shapely/pyproj; PostGIS or GeoPackage; Rasterio/xarray for terrain/hazard rasters; PDAL for client-supplied LiDAR when needed.
- **Esri option:** client ArcGIS Online/Enterprise layers, Living Atlas, ArcGIS Pro on licensed Windows, and controlled web-map/StoryMap/Experience Builder deliverable if the client already owns the environment.
- **Data acquisition:** official APIs/downloads, client subscriptions, parcel/jurisdiction sources, environmental/regulatory portals, imagery/elevation, and documented retrieval scripts.
- **Evidence:** source URL/agency/title, dataset/version, retrieval time, geography, license, vintage, coverage, field definitions, snapshot/artifact ID, and limitations.
- **Documents:** text/OCR extraction for discovery; page-level citations; controlled Word/PDF generation. AI may summarize only from registered evidence and must preserve citations/unknowns. Do not use AI to create constraint geometry, infer absence, choose authoritative sources, or make environmental/engineering/legal conclusions.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 1–3 weeks.
- **Commercial hypothesis:** $3.5k–$7.5k/site; $12k–$25k portfolio batch. Buyer-value hypothesis: $10k–$100k per decision. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** For portfolio or refreshed dossiers, monitor source availability, schema, vintage, licensing, retrieval failures, and jurisdiction/rule changes. Version AOIs, assumptions, sources, rules, results, reviewer decisions, and releases.
- **Evidence:** references [5][6][20][40] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 5. ArcGIS platform health, governance and cost roadmap

- **Niche / buyer:** GIS manager, CIO/IT manager, digital-delivery leader, or business-unit owner paying for ArcGIS.
- **Paid trigger / problem:** content sprawl, unclear ownership, broken dependencies, broad sharing, fragile publishers, credit/storage/licensing concern, or an upcoming migration/reorganization.
- **Outcome:** read-only inventory and risk/cost roadmap for one ArcGIS Online organization or defined Enterprise portal, followed by a separately approved remediation backlog.
- **Delivered artifact:** organization/content/user/group/license inventory; dependency and ownership analysis; sharing/security findings; credit/storage/usage review where available; risk register; governance model; prioritized 30/60/90-day roadmap; item-level remediation candidates; operating checklist.
- **Action enabled:** leadership can decide what to preserve, fix, transfer, archive, restrict, standardize, or budget—without allowing an auditor to mutate production during discovery.
- **Major processing chain:** Define the audit decision → Establish access and safety → Interview owners and capture policy → Collect a versioned inventory → Validate collection coverage → Build ownership and dependency maps → Apply transparent governance rules → Analyze cost and licensing evidence → Risk-rank with owners → Produce governance and roadmap → If approved, remediate a bounded batch → Handoff and establish cadence.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

- ArcGIS REST API and ArcGIS API for Python for inventories of users, roles, groups, items, types, ownership, sharing, dependencies, usage, service definitions, and organization settings available to the account.
- ArcGIS Online/Enterprise administrative reports and client billing/licensing exports.
- Python, pandas/DuckDB, NetworkX or equivalent for dependency/ownership graphs, rules, and evidence tables.
- ArcGIS Assistant or supported export/backup methods only when client-approved and appropriate; do not assume every hosted item has a complete one-click restore.
- ArcGIS Monitor/Enterprise logs and infrastructure tools only if they are in scope and client IT provides access. A content audit is not an infrastructure performance/security audit.
- Playwright/browser smoke tests for representative critical user workflows if remediation is included. AI is unnecessary for authoritative findings. It may draft a management summary from verified inventory/risk records but must not classify an item as safe to delete or infer ownership without human confirmation.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 2–4 weeks.
- **Commercial hypothesis:** $6k–$15k assessment; $2k–$5k/mo governance support. Buyer-value hypothesis: $15k–$120k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Run read-only inventories monthly or quarterly based on organization change rate. Track orphan/single-owner critical content, broad/public sharing, stale/archive candidates, broken dependencies, service accounts, expiring users, storage/credits, high-cost workflows, and policy exceptions.
- **Evidence:** references [8][9][31] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 6. Asset inventory and maintenance workflow

- **Niche / buyer:** Water/wastewater; energy; facilities; private infrastructure.
- **Paid trigger / problem:** Asset records differ across ERP, GIS, CRM and field systems.
- **Outcome:** Reconciled asset schema; mobile capture; maintenance queue; operational dashboard.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- Survey123 and Field Maps with ArcGIS Online/Enterprise, or QField/ODK/Kobo/SurveyCTO.
- PostgreSQL/PostGIS or client-owned feature services.
- Python, Pydantic/Pandera, GeoPandas/Shapely/pyproj/GDAL.
- n8n or a bounded worker for validation, routing and approved reports.
- Dashboards/Experience Builder or a small MapLibre review interface.
#### Offering-specific additions
- CMMS/EAM API or approved import/export.
- barcode/QR only if client asset policy supports it. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 4–8 weeks.
- **Commercial hypothesis:** $12k–$30k pilot; $30k–$90k rollout; $2k–$6k/mo. Buyer-value hypothesis: $40k–$300k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [11][13][16] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 7. Underground utility conflict and SUE pre-screening

- **Niche / buyer:** Civil engineering; subsurface utility engineering; contractors.
- **Paid trigger / problem:** Unknown utilities drive field time, clashes, redesign and change orders.
- **Outcome:** Records aggregation; confidence model; conflict matrix; focused field-investigation plan.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj and PostGIS/GeoPackage.
- Rasterio/xarray and PDAL when terrain, hazard or point-cloud evidence is required.
- official/client-approved APIs and downloads with a source/version/license register.
- controlled Word/PDF/HTML map-report generation with claim-to-source IDs.
- ArcGIS Pro on licensed Windows or client ArcGIS services only when the client requires that lane.
#### Offering-specific additions
- 3D/Z-aware checks only when source quality supports them.
- document/plan extraction with human verification. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Partner-led; expected bounded pilot 2–4 weeks.
- **Commercial hypothesis:** $8k–$25k/project; $2k–$5k/mo portfolio support. Buyer-value hypothesis: $25k–$250k/project. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [10][36] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 8. Environmental permitting and constraints screening

- **Niche / buyer:** Environmental firms; developers; infrastructure owners.
- **Paid trigger / problem:** Permit schedules slip when wetlands, species, contamination or jurisdictional constraints surface late.
- **Outcome:** Jurisdiction-specific constraint register; map; cited evidence; review-ready screening memo.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj and PostGIS/GeoPackage.
- Rasterio/xarray and PDAL when terrain, hazard or point-cloud evidence is required.
- official/client-approved APIs and downloads with a source/version/license register.
- controlled Word/PDF/HTML map-report generation with claim-to-source IDs.
- ArcGIS Pro on licensed Windows or client ArcGIS services only when the client requires that lane.
#### Offering-specific additions
- official agency portals/APIs.
- document citation ledger and page-level extraction. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 2–4 weeks.
- **Commercial hypothesis:** $5k–$15k/site; $20k–$50k program. Buyer-value hypothesis: $15k–$200k/project. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [5][20][40] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 9. Construction GIS coordination and project portal

- **Niche / buyer:** General contractors; program managers; engineering JV teams.
- **Paid trigger / problem:** Design, survey, environmental and progress data sit in incompatible systems.
- **Outcome:** Controlled project map; CAD/BIM/GIS sync; issue layers; stakeholder views; audit trail.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- ArcGIS Dashboards/Experience Builder/Maps SDK when client ArcGIS is authoritative.
- or MapLibre GL JS, a typed web framework and FastAPI/PostGIS.
- Playwright for critical flows and axe-core plus manual accessibility testing.
- Sentry/OpenTelemetry or client monitoring with structured application/API logs.
- PMTiles/COG/TiTiler/deck.gl/Cesium only when the data and user task justify them.
#### Offering-specific additions
- Autodesk-approved exports/APIs.
- issue-tracker/document-management integration only through client staging. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 4–8 weeks.
- **Commercial hypothesis:** $15k–$40k setup; $3k–$8k/mo during construction. Buyer-value hypothesis: $75k–$500k/project. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [9][10][36] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 10. Remote-sensing change monitoring managed service

- **Niche / buyer:** Environmental; construction; forestry; land portfolios; utilities.
- **Paid trigger / problem:** Site visits are expensive and changes are noticed late.
- **Outcome:** Baseline; scheduled imagery analysis; reviewed alerts; evidence snapshots; monthly digest.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- STAC, COG/GeoParquet and object storage where appropriate.
- GDAL, Rasterio/rioxarray/xarray, GeoPandas/Shapely and PostGIS.
- PDAL for point clouds and TiTiler/MapLibre/ArcGIS for reviewed evidence.
- deterministic change rules first; model inference only with labeled evaluation data.
- scheduler/queue, run manifests, structured logs and client-approved notifications.
#### Offering-specific additions
- Sentinel/Landsat/commercial imagery as approved.
- STAC search.
- optional segmentation/classification model only after baseline. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 4–6 weeks.
- **Commercial hypothesis:** $5k–$15k setup; $1.5k–$6k/mo plus imagery. Buyer-value hypothesis: $25k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [18][26] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 11. PostGIS/spatial database modernization

- **Niche / buyer:** AEC; environmental tech; location-data teams.
- **Paid trigger / problem:** File geodatabases and spreadsheets do not scale or support controlled APIs.
- **Outcome:** Data model; migration; spatial indexing; backup; roles; performance tests; runbook.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PostgreSQL/PostGIS, SQL, EXPLAIN/ANALYZE and spatial indexes.
- GDAL/OGR, GeoPandas, DuckDB Spatial and database-native loaders.
- Pydantic/Pandera/SQL constraints/pytest for contracts and fixtures.
- Alembic or client-approved migration tooling plus backup/restore tools.
- FastAPI, BI or ArcGIS integration only for the agreed consumers.
#### Offering-specific additions
- pg_dump/pg_restore or client-approved migration tools.
- connection pooling and read replicas only if justified. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 3–6 weeks.
- **Commercial hypothesis:** $12k–$35k implementation; $1.5k–$5k/mo support. Buyer-value hypothesis: $30k–$200k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [10][11][35] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 12. Fiber field survey and route-planning workflow

- **Niche / buyer:** Fiber engineering firms; broadband contractors.
- **Paid trigger / problem:** Slow surveys and inaccurate records increase design and construction costs.
- **Outcome:** Mobile survey; QA; route/design handoff; exception map; progress dashboard.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- Survey123 and Field Maps with ArcGIS Online/Enterprise, or QField/ODK/Kobo/SurveyCTO.
- PostgreSQL/PostGIS or client-owned feature services.
- Python, Pydantic/Pandera, GeoPandas/Shapely/pyproj/GDAL.
- n8n or a bounded worker for validation, routing and approved reports.
- Dashboards/Experience Builder or a small MapLibre review interface.
#### Offering-specific additions
- GNSS/device capture as client-approved.
- fiber design platform import/export.
- barcode/photo handling. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 4–8 weeks.
- **Commercial hypothesis:** $12k–$30k pilot; $30k–$80k rollout. Buyer-value hypothesis: $50k–$500k/project. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [14][21] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 13. Flood and stormwater screening/prioritization

- **Niche / buyer:** Developers; engineering firms; campuses; property portfolios.
- **Paid trigger / problem:** Flood exposure and drainage conflicts affect siting, design and insurance.
- **Outcome:** Cited flood/drainage screen; terrain analysis; scenario maps; priority list.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj and PostGIS/GeoPackage.
- Rasterio/xarray and PDAL when terrain, hazard or point-cloud evidence is required.
- official/client-approved APIs and downloads with a source/version/license register.
- controlled Word/PDF/HTML map-report generation with claim-to-source IDs.
- ArcGIS Pro on licensed Windows or client ArcGIS services only when the client requires that lane.
#### Offering-specific additions
- DEM/3DEP/LiDAR, flow-direction/accumulation tools and scenario rasters as appropriate.
- WhiteboxTools, TauDEM, GRASS or SAGA may provide reproducible terrain/hydrology operations; select one validated lane rather than mixing outputs without reconciliation. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 2–4 weeks.
- **Commercial hypothesis:** $5k–$18k/site or portfolio batch; $1k–$4k/mo monitoring. Buyer-value hypothesis: $20k–$250k/project. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [17][19][24][25] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 14. Utility vegetation risk prioritization

- **Niche / buyer:** Electric cooperatives; campus utilities; rail/pipeline operators.
- **Paid trigger / problem:** Vegetation causes outages, overtime, complaints and safety exposure.
- **Outcome:** Risk model; inspection queue; crew map; change monitoring; outcome dashboard.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- STAC, COG/GeoParquet and object storage where appropriate.
- GDAL, Rasterio/rioxarray/xarray, GeoPandas/Shapely and PostGIS.
- PDAL for point clouds and TiTiler/MapLibre/ArcGIS for reviewed evidence.
- deterministic change rules first; model inference only with labeled evaluation data.
- scheduler/queue, run manifests, structured logs and client-approved notifications.
#### Offering-specific additions
- vegetation indices/change/height evidence.
- EAM/work-management integration only with utility approval. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Partner-led; expected bounded pilot 6–10 weeks.
- **Commercial hypothesis:** $15k–$40k pilot; $3k–$10k/mo. Buyer-value hypothesis: $100k–$1m+/yr for a utility. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [15][37] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 15. GIS regression testing and release QA

- **Niche / buyer:** GIS software teams; AEC digital teams; ArcGIS administrators.
- **Paid trigger / problem:** Map/app changes silently break layers, queries, symbology and workflows.
- **Outcome:** Test inventory; automated smoke/regression suite; release gate; evidence report.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- pytest and typed schema/data validators.
- GeoPandas/Shapely/pyproj/GDAL/PostGIS checks for spatial correctness.
- Playwright for browser flows and API contract tests.
- visual/map evidence with explicit tolerances rather than brittle pixel equality alone.
- ArcGIS API/REST and licensed Windows ArcGIS Pro/ArcPy only where the tested stack requires it.
#### Offering-specific additions
- Playwright, pytest, API contract checks and optional visual map assertions with tolerance. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 2–5 weeks.
- **Commercial hypothesis:** $6k–$18k setup; $1.5k–$5k/mo. Buyer-value hypothesis: $20k–$150k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [10][16][27] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 16. AI document/plan extraction to GIS review queue

- **Niche / buyer:** Environmental; AEC; utilities; property due diligence.
- **Paid trigger / problem:** Coordinates, parcel IDs, assets and constraints are trapped in PDFs, plans and reports.
- **Outcome:** Extraction pipeline; confidence scores; human review queue; GIS export; provenance.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** permission-filtered document, graph and spatial retrieval with source/chunk/feature IDs and refusal when evidence is missing; no invented geometry or conclusions.
- **LiteLLM + Langfuse:** approved model routing, budgets and data policy; traces for retrieval, tool calls, latency, cost and evaluation. AI remains non-authoritative.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- OCR/parser appropriate to the source, structured extraction with Pydantic/JSON Schema.
- PostgreSQL/PostGIS for authoritative data; vector/hybrid search only for approved text retrieval.
- model gateway with source IDs, confidence/unknown states, allowlisted tools and budgets.
- retrieval/evaluation metrics plus adversarial, ambiguous and refusal fixtures.
- human review application/queue; AI can be disabled without losing authoritative GIS results.
#### Offering-specific additions
- OCR/layout parser, coordinate/parcel/entity resolver and review UI. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 4–6 weeks.
- **Commercial hypothesis:** $10k–$25k pilot; $2k–$6k/mo. Buyer-value hypothesis: $30k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [8][9][28][29][38] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 17. LiDAR and terrain site analysis

- **Niche / buyer:** Civil/site engineering; renewables; drainage; forestry.
- **Paid trigger / problem:** Terrain, access, cut/fill and visibility decisions need high-quality elevation analysis.
- **Outcome:** DEM/point-cloud QA; slope/drainage/visibility outputs; review-ready map pack.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PDAL, COPC/Entwine, GDAL/Rasterio and QGIS.
- CesiumJS/3D Tiles, deck.gl or ArcGIS Scene layers depending client platform.
- STAC/object storage for catalog and versioning.
- IfcOpenShell/Autodesk-approved exports when BIM is involved.
- ArcGIS Pro/ArcPy only on licensed Windows where required.
#### Offering-specific additions
- WhiteboxTools/GRASS/SAGA or client ArcGIS Spatial/3D Analyst where licensed.
- CloudCompare for point-cloud inspection/comparison and Potree for a bounded web review viewer when needed. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 2–4 weeks.
- **Commercial hypothesis:** $6k–$20k/site; $20k–$60k portfolio. Buyer-value hypothesis: $20k–$200k/project. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [17][36] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 18. ArcGIS dashboard/Experience Builder client portal

- **Niche / buyer:** AEC/environmental project teams; utilities; private program owners.
- **Paid trigger / problem:** Stakeholders lack a controlled, current view of status, evidence and issues.
- **Outcome:** Role-based web portal; dashboards; forms; print/export; accessibility and handoff.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- ArcGIS Dashboards/Experience Builder/Maps SDK when client ArcGIS is authoritative.
- or MapLibre GL JS, a typed web framework and FastAPI/PostGIS.
- Playwright for critical flows and axe-core plus manual accessibility testing.
- Sentry/OpenTelemetry or client monitoring with structured application/API logs.
- PMTiles/COG/TiTiler/deck.gl/Cesium only when the data and user task justify them.
#### Offering-specific additions
- ArcGIS Dashboards/Experience Builder/Instant Apps or custom ArcGIS Maps SDK. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 3–6 weeks.
- **Commercial hypothesis:** $10k–$30k build; $1k–$4k/mo support. Buyer-value hypothesis: $25k–$150k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [12][14][31] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 19. Address, geocoding and entity-resolution QA

- **Niche / buyer:** Utilities; logistics; property; telecom; insurers.
- **Paid trigger / problem:** Bad addresses and duplicate locations corrupt serviceability, routing and portfolio analytics.
- **Outcome:** Match-rate baseline; normalization; exception queue; confidence output; repeatable QA.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PostgreSQL/PostGIS, SQL, EXPLAIN/ANALYZE and spatial indexes.
- GDAL/OGR, GeoPandas, DuckDB Spatial and database-native loaders.
- Pydantic/Pandera/SQL constraints/pytest for contracts and fixtures.
- Alembic or client-approved migration tooling plus backup/restore tools.
- FastAPI, BI or ArcGIS integration only for the agreed consumers.
#### Offering-specific additions
- libpostal where appropriate.
- client geocoder/ArcGIS/Google/etc. under approved terms.
- probabilistic linkage only with thresholds. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 2–4 weeks.
- **Commercial hypothesis:** $6k–$18k project; $1k–$4k/mo refresh. Buyer-value hypothesis: $20k–$150k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [11][14][21] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 20. Geospatial web accessibility audit and remediation

- **Niche / buyer:** AEC/public-facing project portals; vendors serving government; utilities.
- **Paid trigger / problem:** Maps, widgets and reports frequently fail keyboard, contrast and screen-reader needs.
- **Outcome:** WCAG/Section 508 audit; issue evidence; remediation; retest; accessibility statement.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- ArcGIS Dashboards/Experience Builder/Maps SDK when client ArcGIS is authoritative.
- or MapLibre GL JS, a typed web framework and FastAPI/PostGIS.
- Playwright for critical flows and axe-core plus manual accessibility testing.
- Sentry/OpenTelemetry or client monitoring with structured application/API logs.
- PMTiles/COG/TiTiler/deck.gl/Cesium only when the data and user task justify them.
#### Offering-specific additions
- axe-core, Lighthouse as secondary evidence, Playwright and real screen-reader/manual testing. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 2–5 weeks.
- **Commercial hypothesis:** $5k–$15k audit; $8k–$30k remediation. Buyer-value hypothesis: $15k–$150k risk and rework value. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [31][39] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 21. GIS automation managed-support retainer

- **Niche / buyer:** Small/mid-sized AEC and environmental firms.
- **Paid trigger / problem:** Useful automations decay when schemas, APIs, licenses and staff change.
- **Outcome:** Monitoring; exception handling; small enhancements; monthly value report; runbook ownership.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- pytest and typed schema/data validators.
- GeoPandas/Shapely/pyproj/GDAL/PostGIS checks for spatial correctness.
- Playwright for browser flows and API contract tests.
- visual/map evidence with explicit tolerances rather than brittle pixel equality alone.
- ArcGIS API/REST and licensed Windows ArcGIS Pro/ArcPy only where the tested stack requires it.
#### Offering-specific additions
- scheduler/queue logs, Sentry/OpenTelemetry or client monitoring.
- repository/CI and issue queue. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot Recurring after 2–4 week onboarding.
- **Commercial hypothesis:** $2k–$7k/mo. Buyer-value hypothesis: $30k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [10][11][12] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 22. ArcGIS Online content lifecycle and governance cleanup

- **Niche / buyer:** ArcGIS Online organizations with many publishers.
- **Paid trigger / problem:** Orphaned items, duplicated layers, broken dependencies and uncontrolled sharing create cost and risk.
- **Outcome:** Read-only dependency inventory; ownership cleanup plan; archive candidates; sharing/credit controls.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- structured interviews, process mapping and spreadsheet/BI analysis.
- read-only platform reports/APIs where approved.
- QGIS/Python notebooks or workflow prototypes for evidence.
- NIST AI RMF and client governance controls for AI-related audits.
- controlled decision memo, backlog and measurement plan.
#### Offering-specific additions
- ArcGIS REST/API for Python and administrative exports.
- dependency graph analysis. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 2–4 weeks.
- **Commercial hypothesis:** $5k–$15k assessment; $10k–$35k remediation. Buyer-value hypothesis: $15k–$100k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [16][31] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 23. Geospatial metadata, lineage and data-catalog implementation

- **Niche / buyer:** AEC/environmental data teams; asset owners.
- **Paid trigger / problem:** Teams cannot tell which spatial data is current, authoritative, licensed or decision-ready.
- **Outcome:** Catalog; owner/freshness fields; lineage; data contracts; source and license controls.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PostgreSQL/PostGIS, SQL, EXPLAIN/ANALYZE and spatial indexes.
- GDAL/OGR, GeoPandas, DuckDB Spatial and database-native loaders.
- Pydantic/Pandera/SQL constraints/pytest for contracts and fixtures.
- Alembic or client-approved migration tooling plus backup/restore tools.
- FastAPI, BI or ArcGIS integration only for the agreed consumers.
#### Offering-specific additions
- DataHub/OpenMetadata/CKAN/client catalog as appropriate.
- dbt-style contracts where nonspatial stack exists. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 3–6 weeks.
- **Commercial hypothesis:** $10k–$30k implementation; $1.5k–$4k/mo. Buyer-value hypothesis: $30k–$180k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [10][11][27] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 24. AI-assisted evidence-based GIS report generation

- **Niche / buyer:** Environmental/AEC analysts; insurers; property research teams.
- **Paid trigger / problem:** Analysts repeatedly assemble maps, citations and narrative while preserving reviewability.
- **Outcome:** Template pipeline; map exports; cited draft; reviewer checklist; source snapshots.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** permission-filtered document, graph and spatial retrieval with source/chunk/feature IDs and refusal when evidence is missing; no invented geometry or conclusions.
- **LiteLLM + Langfuse:** approved model routing, budgets and data policy; traces for retrieval, tool calls, latency, cost and evaluation. AI remains non-authoritative.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- OCR/parser appropriate to the source, structured extraction with Pydantic/JSON Schema.
- PostgreSQL/PostGIS for authoritative data; vector/hybrid search only for approved text retrieval.
- model gateway with source IDs, confidence/unknown states, allowlisted tools and budgets.
- retrieval/evaluation metrics plus adversarial, ambiguous and refusal fixtures.
- human review application/queue; AI can be disabled without losing authoritative GIS results.
#### Offering-specific additions
- document template engine.
- model structured output.
- page/data source IDs.
- diff/review interface. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 3–5 weeks.
- **Commercial hypothesis:** $8k–$20k pilot; $1.5k–$5k/mo. Buyer-value hypothesis: $25k–$180k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [28][29][38] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 25. GIS/AI workflow discovery and ROI audit

- **Niche / buyer:** AEC/environmental leadership; GIS managers.
- **Paid trigger / problem:** Leaders face AI pressure but lack prioritized, measurable, safe use cases.
- **Outcome:** Workflow inventory; cost baseline; risk review; ranked pilots; business case and 90-day plan.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- structured interviews, process mapping and spreadsheet/BI analysis.
- read-only platform reports/APIs where approved.
- QGIS/Python notebooks or workflow prototypes for evidence.
- NIST AI RMF and client governance controls for AI-related audits.
- controlled decision memo, backlog and measurement plan.
#### Offering-specific additions
- process mapping, spreadsheet/BI scoring and small synthetic demonstrations only. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 2–3 weeks.
- **Commercial hypothesis:** $5k–$12k workshop/audit. Buyer-value hypothesis: $20k–$150k decision value. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [8][9][28][29] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 26. Renewable-energy siting constraints screening

- **Niche / buyer:** Solar/storage/wind developers; engineering advisors.
- **Paid trigger / problem:** Interconnection, land, environmental and community constraints can kill sites early.
- **Outcome:** Ranked parcel screen; exclusion/sensitivity layers; cited data; shortlist and assumptions.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj and PostGIS/GeoPackage.
- Rasterio/xarray and PDAL when terrain, hazard or point-cloud evidence is required.
- official/client-approved APIs and downloads with a source/version/license register.
- controlled Word/PDF/HTML map-report generation with claim-to-source IDs.
- ArcGIS Pro on licensed Windows or client ArcGIS services only when the client requires that lane.
#### Offering-specific additions
- weighted overlay/MCDA implemented transparently.
- scenario sensitivity rather than opaque AI score. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 3–5 weeks.
- **Commercial hypothesis:** $8k–$25k/market or portfolio. Buyer-value hypothesis: $50k–$500k per avoided bad site. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [23][24] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 27. Property/asset-portfolio climate screening

- **Niche / buyer:** Property managers; lenders; corporate real estate; brokers.
- **Paid trigger / problem:** Flood, fire, heat and wind increasingly affect acquisition, insurance and capex.
- **Outcome:** Portfolio exposure screen; data limitations; priorities; property-level evidence pack.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj and PostGIS/GeoPackage.
- Rasterio/xarray and PDAL when terrain, hazard or point-cloud evidence is required.
- official/client-approved APIs and downloads with a source/version/license register.
- controlled Word/PDF/HTML map-report generation with claim-to-source IDs.
- ArcGIS Pro on licensed Windows or client ArcGIS services only when the client requires that lane.
#### Offering-specific additions
- batch geocoding, hazard raster/vector services and BI/map pack.
- no generic black-box score without documentation. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 3–5 weeks.
- **Commercial hypothesis:** $7k–$20k portfolio; $1k–$4k/mo refresh. Buyer-value hypothesis: $25k–$500k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [24][25] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 28. Spatial knowledge assistant/RAG pilot

- **Niche / buyer:** AEC/environmental firms with maps, reports and standards.
- **Paid trigger / problem:** Staff spend time finding project precedents and authoritative answers across documents and spatial records.
- **Outcome:** Scoped corpus; retrieval; map/document citations; permission model; evaluation set.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + pgvector + Apache AGE:** spatial truth in PostGIS, approved semantic recall in pgvector and explicit relationship traversal in AGE; none replaces deterministic GIS.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** permission-filtered document, graph and spatial retrieval with source/chunk/feature IDs and refusal when evidence is missing; no invented geometry or conclusions.
- **LiteLLM + Langfuse:** approved model routing, budgets and data policy; traces for retrieval, tool calls, latency, cost and evaluation. AI remains non-authoritative.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- OCR/parser appropriate to the source, structured extraction with Pydantic/JSON Schema.
- PostgreSQL/PostGIS for authoritative data; vector/hybrid search only for approved text retrieval.
- model gateway with source IDs, confidence/unknown states, allowlisted tools and budgets.
- retrieval/evaluation metrics plus adversarial, ambiguous and refusal fixtures.
- human review application/queue; AI can be disabled without losing authoritative GIS results.
#### Offering-specific additions
- hybrid lexical/vector retrieval, permission filters, source viewer and optional spatial prefilter.
- PostgreSQL/pgvector, OpenSearch/Elasticsearch, Qdrant or Weaviate are alternative retrieval stores; choose one compatible with client operations.
- LlamaIndex or LangChain may provide retrieval plumbing, but neither is the permission, evaluation or security boundary. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 4–8 weeks.
- **Commercial hypothesis:** $12k–$30k pilot; $2k–$6k/mo. Buyer-value hypothesis: $30k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [27][28][29][38] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 29. Governed geospatial agent pilot

- **Niche / buyer:** GIS teams with repetitive, reviewable analysis.
- **Paid trigger / problem:** Multi-step GIS requests consume analyst time but autonomous execution creates safety and trust risks.
- **Outcome:** One bounded workflow; approval gates; evidence bundle; regression tests; kill switch.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + pgvector + Apache AGE:** spatial truth in PostGIS, approved semantic recall in pgvector and explicit relationship traversal in AGE; none replaces deterministic GIS.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** permission-filtered document, graph and spatial retrieval with source/chunk/feature IDs and refusal when evidence is missing; no invented geometry or conclusions.
- **LiteLLM + Langfuse:** approved model routing, budgets and data policy; traces for retrieval, tool calls, latency, cost and evaluation. AI remains non-authoritative.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- OCR/parser appropriate to the source, structured extraction with Pydantic/JSON Schema.
- PostgreSQL/PostGIS for authoritative data; vector/hybrid search only for approved text retrieval.
- model gateway with source IDs, confidence/unknown states, allowlisted tools and budgets.
- retrieval/evaluation metrics plus adversarial, ambiguous and refusal fixtures.
- human review application/queue; AI can be disabled without losing authoritative GIS results.
#### Offering-specific additions
- state/checkpoint engine, typed GIS APIs, policy layer, evaluation harness and kill switch. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 6–10 weeks.
- **Commercial hypothesis:** $15k–$35k pilot; $2k–$7k/mo. Buyer-value hypothesis: $40k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [27][28][29] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 30. GIS automation and AI upskilling

- **Niche / buyer:** AEC/environmental GIS teams; technical leaders.
- **Paid trigger / problem:** Hiring is difficult and existing staff need practical automation and AI governance skills.
- **Outcome:** Role-based workshop; organization examples; sandbox exercises; 30-day office hours.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- structured interviews, process mapping and spreadsheet/BI analysis.
- read-only platform reports/APIs where approved.
- QGIS/Python notebooks or workflow prototypes for evidence.
- NIST AI RMF and client governance controls for AI-related audits.
- controlled decision memo, backlog and measurement plan.
#### Offering-specific additions
- QGIS/Python/ArcGIS sandbox, notebooks and AI evaluation exercises without production credentials. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 1–4 weeks including preparation.
- **Commercial hypothesis:** $3k–$8k/workshop; $12k–$25k cohort. Buyer-value hypothesis: $10k–$100k workforce value. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [2][4][8][30] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 31. Parcel, zoning and entitlement pre-screening

- **Niche / buyer:** Developers; brokers; site-selection consultants.
- **Paid trigger / problem:** Zoning, parcel and jurisdictional constraints delay preliminary feasibility.
- **Outcome:** Cited parcel/zoning dossier; conflicts; missing-data list; planning questions.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj and PostGIS/GeoPackage.
- Rasterio/xarray and PDAL when terrain, hazard or point-cloud evidence is required.
- official/client-approved APIs and downloads with a source/version/license register.
- controlled Word/PDF/HTML map-report generation with claim-to-source IDs.
- ArcGIS Pro on licensed Windows or client ArcGIS services only when the client requires that lane.
#### Offering-specific additions
- official zoning maps/codes and page-level document citations.
- parcel geocoding/entity resolution. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 2–3 weeks.
- **Commercial hypothesis:** $2.5k–$7.5k/site; $10k–$30k portfolio. Buyer-value hypothesis: $10k–$150k/decision. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [20][25] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 32. Custom web-mapping MVP

- **Niche / buyer:** Startups; consultancies; data publishers.
- **Paid trigger / problem:** Teams need branded spatial UX beyond desktop GIS but generic map builders are cheap.
- **Outcome:** User-tested MapLibre/Mapbox/CARTO MVP; analytics; deployment; handoff.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- ArcGIS Dashboards/Experience Builder/Maps SDK when client ArcGIS is authoritative.
- or MapLibre GL JS, a typed web framework and FastAPI/PostGIS.
- Playwright for critical flows and axe-core plus manual accessibility testing.
- Sentry/OpenTelemetry or client monitoring with structured application/API logs.
- PMTiles/COG/TiTiler/deck.gl/Cesium only when the data and user task justify them.
#### Offering-specific additions
- MapLibre or ArcGIS Maps SDK.
- PMTiles/PostGIS/FastAPI based on update needs.
- privacy-safe analytics. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 4–8 weeks.
- **Commercial hypothesis:** $15k–$45k MVP; $1k–$5k/mo. Buyer-value hypothesis: $25k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [33][34][35] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 33. Imagery/STAC/COG/TiTiler delivery pipeline

- **Niche / buyer:** Remote-sensing teams; drone programs; environmental platforms.
- **Paid trigger / problem:** Large imagery collections are hard to catalog, serve and update efficiently.
- **Outcome:** Cloud-optimized assets; STAC catalog; tile API; lifecycle and cost tests.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- STAC, COG/GeoParquet and object storage where appropriate.
- GDAL, Rasterio/rioxarray/xarray, GeoPandas/Shapely and PostGIS.
- PDAL for point clouds and TiTiler/MapLibre/ArcGIS for reviewed evidence.
- deterministic change rules first; model inference only with labeled evaluation data.
- scheduler/queue, run manifests, structured logs and client-approved notifications.
#### Offering-specific additions
- rio-cogeo, stac-fastapi/PySTAC, TiTiler, object storage/CDN and optional PMTiles/COPC. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 4–8 weeks.
- **Commercial hypothesis:** $15k–$45k implementation; $2k–$6k/mo. Buyer-value hypothesis: $40k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [17][18][26] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 34. Emergency/event operational dashboard

- **Niche / buyer:** Utilities; campuses; private infrastructure; response contractors.
- **Paid trigger / problem:** Incidents require rapid field status, common operating picture and resource prioritization.
- **Outcome:** Prebuilt data model; field forms; incident dashboard; offline workflow; drill.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- ArcGIS Field Maps/Survey123/Dashboards/Experience Builder or client emergency platform.
- PostGIS/MapLibre only when client operations can support it.
- offline packages, controlled status model and resilient exports.
- monitoring, audit logs and exercise evidence.
- communications integrations only with explicit approval and operational owner.
#### Offering-specific additions
- client incident-management integration only in sandbox/approved staging. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Partner-led; expected bounded pilot 6–10 weeks.
- **Commercial hypothesis:** $12k–$35k setup; $2k–$6k/mo readiness. Buyer-value hypothesis: $50k–$500k/event risk value. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [19][24] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 35. Routing, dispatch and service-territory optimization

- **Niche / buyer:** Field services; waste; delivery; utilities.
- **Paid trigger / problem:** Miles, travel time and poor territory design drive recurring labor and fuel cost.
- **Outcome:** Baseline; constraint model; route/territory scenarios; operational export; KPI tracking.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PostGIS/pgRouting, NetworkX or OR-Tools as appropriate.
- GeoPandas/Shapely/pyproj and geocoding/address QA.
- QGIS/ArcGIS Network Analyst on licensed Windows where client requires it.
- FastAPI/BI/web map for scenario review; operational export rather than direct dispatch by default.
- optimization solver with explicit objective, constraints, seeds and reproducibility.
#### Offering-specific additions
- traffic/travel-time provider if licensed.
- solver configuration and seed/version.
- OSRM, Valhalla or OpenRouteService can supply routable networks/travel matrices when their coverage, restrictions, licenses and operating burden fit the client; use the client-approved source of travel truth. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 3–6 weeks.
- **Commercial hypothesis:** $10k–$30k study; $2k–$6k/mo. Buyer-value hypothesis: $40k–$300k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [7][33] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 36. Brownfield/Phase I ESA research-support map pack

- **Niche / buyer:** Environmental consultants; lenders; developers.
- **Paid trigger / problem:** Historical and regulatory sources are fragmented; research is repetitive.
- **Outcome:** Preliminary source pack; mapped records; citations; data gaps; qualified-professional review.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** permission-filtered document, graph and spatial retrieval with source/chunk/feature IDs and refusal when evidence is missing; no invented geometry or conclusions.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj and PostGIS/GeoPackage.
- Rasterio/xarray and PDAL when terrain, hazard or point-cloud evidence is required.
- official/client-approved APIs and downloads with a source/version/license register.
- controlled Word/PDF/HTML map-report generation with claim-to-source IDs.
- ArcGIS Pro on licensed Windows or client ArcGIS services only when the client requires that lane.
#### Offering-specific additions
- OCR/page citation and geocoding/entity resolution with human verification. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 1–2 weeks.
- **Commercial hypothesis:** $2.5k–$6k/site; $8k–$20k portfolio. Buyer-value hypothesis: $5k–$75k/decision. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [5][20][40] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 37. GIS-to-BI semantic layer and dashboard integration

- **Niche / buyer:** Asset owners; environmental/AEC program teams.
- **Paid trigger / problem:** Spatial measures and business KPIs use inconsistent definitions across GIS and BI.
- **Outcome:** Metric definitions; governed model; GIS/BI integration; tests; executive dashboard.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PostgreSQL/PostGIS, SQL, EXPLAIN/ANALYZE and spatial indexes.
- GDAL/OGR, GeoPandas, DuckDB Spatial and database-native loaders.
- Pydantic/Pandera/SQL constraints/pytest for contracts and fixtures.
- Alembic or client-approved migration tooling plus backup/restore tools.
- FastAPI, BI or ArcGIS integration only for the agreed consumers.
#### Offering-specific additions
- dbt/semantic layer where client uses it.
- Power BI/Tableau/Metabase/Looker integration. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 4–8 weeks.
- **Commercial hypothesis:** $12k–$35k implementation; $1.5k–$5k/mo. Buyer-value hypothesis: $30k–$200k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [11][35] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 38. Drone/LiDAR data management portal

- **Niche / buyer:** Survey/drone programs; engineering firms; asset owners.
- **Paid trigger / problem:** Missions, point clouds and deliverables become hard to find, govern and reuse.
- **Outcome:** Mission catalog; QA metadata; 2D/3D viewing; permissions; retention and handoff.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PDAL, COPC/Entwine, GDAL/Rasterio and QGIS.
- CesiumJS/3D Tiles, deck.gl or ArcGIS Scene layers depending client platform.
- STAC/object storage for catalog and versioning.
- IfcOpenShell/Autodesk-approved exports when BIM is involved.
- ArcGIS Pro/ArcPy only on licensed Windows where required.
#### Offering-specific additions
- drone platform exports, STAC/COPC/3D Tiles and client CDE links.
- Potree or CesiumJS for bounded point-cloud/3D review; MinIO/S3-compatible object storage only where the client can operate lifecycle, permissions and egress controls. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 4–8 weeks.
- **Commercial hypothesis:** $15k–$45k build; $2k–$6k/mo. Buyer-value hypothesis: $40k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [17][37] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 39. Precision-agriculture/forestry monitoring

- **Niche / buyer:** Large farms; agronomy groups; forestry managers.
- **Paid trigger / problem:** Field scouting and intervention prioritization are costly at scale.
- **Outcome:** Seasonal indicators; reviewed alerts; management-zone maps; field-check queue.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- STAC, COG/GeoParquet and object storage where appropriate.
- GDAL, Rasterio/rioxarray/xarray, GeoPandas/Shapely and PostGIS.
- PDAL for point clouds and TiTiler/MapLibre/ArcGIS for reviewed evidence.
- deterministic change rules first; model inference only with labeled evaluation data.
- scheduler/queue, run manifests, structured logs and client-approved notifications.
#### Offering-specific additions
- vegetation indices/time-series, zonal statistics and optional model with field labels. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Partner-led; expected bounded pilot 6–12 weeks.
- **Commercial hypothesis:** $8k–$25k setup; $1.5k–$7k/mo plus imagery. Buyer-value hypothesis: $30k–$300k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [22][26] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 40. Insurance exposure and accumulation reporting

- **Niche / buyer:** MGAs; brokers; property insurers; risk consultants.
- **Paid trigger / problem:** Carriers need current hazard/exposure aggregation and explainable portfolio views.
- **Outcome:** Geocoded exposure QA; hazard overlays; accumulation maps; limitations and refresh workflow.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- secure source-specific connectors, GDAL/GeoPandas/PostGIS and encrypted object storage.
- typed exposure/peril schemas, deterministic geocoding and spatial aggregation.
- schema/data contracts, run manifests, catalog/metadata and versioned release notes.
- client identity/authorization, audit logs and controlled BI/report delivery.
- AI only for bounded explanation with human review and source IDs; not for actuarial calculations or decisions.
#### Offering-specific additions
- insurance data schemas and BI.
- secure geocoding.
- model outputs only under client licenses.
- H3/S2 grids may support controlled accumulation summaries; dbt and Great Expectations/Pandera may implement governed transformations and data-quality tests when they match the client stack. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Partner-led; expected bounded pilot 8–12 weeks.
- **Commercial hypothesis:** $15k–$50k pilot; $3k–$12k/mo. Buyer-value hypothesis: $100k–$1m+/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [24][25] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 41. Telecom serviceability and network expansion analytics

- **Niche / buyer:** ISPs; fiber engineering; infrastructure investors.
- **Paid trigger / problem:** Build economics depend on accurate premises, route, cost and coverage data.
- **Outcome:** Serviceability model; demand/route scenarios; field exceptions; investment map.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PostGIS/pgRouting, NetworkX or OR-Tools as appropriate.
- GeoPandas/Shapely/pyproj and geocoding/address QA.
- QGIS/ArcGIS Network Analyst on licensed Windows where client requires it.
- FastAPI/BI/web map for scenario review; operational export rather than direct dispatch by default.
- optimization solver with explicit objective, constraints, seeds and reproducibility.
#### Offering-specific additions
- fiber/telecom planning platform exports and network graph/cost model.
- OpenStreetMap or Overture may provide non-authoritative contextual networks/places where licensed and fit; H3 may support scenario aggregation. Client network records remain authoritative. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 5–8 weeks.
- **Commercial hypothesis:** $15k–$45k study; $2k–$7k/mo. Buyer-value hypothesis: $75k–$750k/project. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [14][21] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 42. 3D/BIM-GIS integration and digital-twin foundation

- **Niche / buyer:** AEC programs; campuses; utilities.
- **Paid trigger / problem:** Asset, design, survey and operational data do not align across 2D/3D systems.
- **Outcome:** Common identifiers; coordinate QA; integration pipeline; 2D/3D portal; governance.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PDAL, COPC/Entwine, GDAL/Rasterio and QGIS.
- CesiumJS/3D Tiles, deck.gl or ArcGIS Scene layers depending client platform.
- STAC/object storage for catalog and versioning.
- IfcOpenShell/Autodesk-approved exports when BIM is involved.
- ArcGIS Pro/ArcPy only on licensed Windows where required.
#### Offering-specific additions
- IFC/Autodesk-approved APIs, 3D Tiles/Cesium or ArcGIS Indoors/Scene as client-owned.
- IfcOpenShell and Speckle may support bounded, client-approved model exchange; ArcGIS GeoBIM is an Esri alternative where already licensed and governed. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Partner-led; expected bounded pilot 8–12 weeks.
- **Commercial hypothesis:** $25k–$75k pilot; $5k–$15k/mo. Buyer-value hypothesis: $100k–$1m+/program. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [10][17][37] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 43. OGC API and geospatial interoperability modernization

- **Niche / buyer:** Data publishers; platform teams; multi-vendor asset owners.
- **Paid trigger / problem:** Proprietary interfaces and duplicated exports inhibit reuse and partner integration.
- **Outcome:** Standards assessment; OGC API prototype; conformance tests; migration plan.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PostGIS and FastAPI or a standards-capable geospatial server.
- OGC API Features/Tiles/Maps/Processes as required, with official conformance tooling.
- MapLibre/ArcGIS client compatibility tests.
- k6/Locust, EXPLAIN/ANALYZE, CDN/cache and tile/PMTiles/COG options.
- OpenTelemetry/Sentry/client cloud metrics and cost exports.
#### Offering-specific additions
- pygeoapi/GeoServer/deegree or client platform.
- official OGC conformance tests. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 3–6 weeks.
- **Commercial hypothesis:** $12k–$35k project; $1k–$4k/mo. Buyer-value hypothesis: $30k–$200k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [10][11][35] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 44. Geospatial API performance and cloud-cost optimization

- **Niche / buyer:** Web-map/data-product teams.
- **Paid trigger / problem:** Tile, query, egress and credit costs rise unpredictably with usage.
- **Outcome:** Telemetry baseline; load test; caching/tiling/index plan; verified cost model.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PostGIS and FastAPI or a standards-capable geospatial server.
- OGC API Features/Tiles/Maps/Processes as required, with official conformance tooling.
- MapLibre/ArcGIS client compatibility tests.
- k6/Locust, EXPLAIN/ANALYZE, CDN/cache and tile/PMTiles/COG options.
- OpenTelemetry/Sentry/client cloud metrics and cost exports.
#### Offering-specific additions
- CDN/cache, PMTiles/COG/tiles, PostGIS tuning and load tools based on bottleneck. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 2–5 weeks.
- **Commercial hypothesis:** $8k–$25k assessment; $2k–$6k/mo. Buyer-value hypothesis: $25k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [31][32][33][35] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 45. Retail/logistics location-intelligence study

- **Niche / buyer:** Regional retailers; logistics operators; service networks.
- **Paid trigger / problem:** Expansion and territory choices combine demographics, access, competition and cost.
- **Outcome:** Decision model; ranked sites/territories; assumptions; scenario map; executive memo.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n:** optional for handoffs and approvals; use a simpler reproducible Python/SQL job when orchestration adds no buyer value.
- **FastAPI/Spatial Ops MCP:** typed allowlisted endpoints only when integration is required; tile/map servers are unnecessary for file/report-only delivery.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** not a runtime dependency; internal research/QA only inside the approved project corpus.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- QGIS, GDAL/OGR, GeoPandas, Shapely, pyproj and PostGIS/GeoPackage.
- Rasterio/xarray and PDAL when terrain, hazard or point-cloud evidence is required.
- official/client-approved APIs and downloads with a source/version/license register.
- controlled Word/PDF/HTML map-report generation with claim-to-source IDs.
- ArcGIS Pro on licensed Windows or client ArcGIS services only when the client requires that lane.
#### Offering-specific additions
- travel-time/isochrone and demographic sources.
- weighted/optimization model with scenario controls.
- OSM/Overture and Census/ACS may provide approved contextual inputs; H3 may support transparent aggregation and scenario comparison. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Deliverable now as a bounded local/client-system service**, but not from the empty GIS host. Recurring server delivery requires the readiness gate.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 3–5 weeks.
- **Commercial hypothesis:** $10k–$30k study. Buyer-value hypothesis: $50k–$500k/decision. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [7][33][35] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 46. Natural-language spatial analysis interface

- **Niche / buyer:** Non-GIS users in asset/property/environmental teams.
- **Paid trigger / problem:** Decision makers want answers without desktop GIS, but semantic ambiguity is dangerous.
- **Outcome:** Bounded question set; audited query translation; map/table answer; evidence and refusal rules.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + pgvector + Apache AGE:** spatial truth in PostGIS, approved semantic recall in pgvector and explicit relationship traversal in AGE; none replaces deterministic GIS.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** permission-filtered document, graph and spatial retrieval with source/chunk/feature IDs and refusal when evidence is missing; no invented geometry or conclusions.
- **LiteLLM + Langfuse:** approved model routing, budgets and data policy; traces for retrieval, tool calls, latency, cost and evaluation. AI remains non-authoritative.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- OCR/parser appropriate to the source, structured extraction with Pydantic/JSON Schema.
- PostgreSQL/PostGIS for authoritative data; vector/hybrid search only for approved text retrieval.
- model gateway with source IDs, confidence/unknown states, allowlisted tools and budgets.
- retrieval/evaluation metrics plus adversarial, ambiguous and refusal fixtures.
- human review application/queue; AI can be disabled without losing authoritative GIS results.
#### Offering-specific additions
- semantic parser constrained to query DSL.
- PostGIS/ArcGIS read API.
- answer evidence viewer. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 6–10 weeks.
- **Commercial hypothesis:** $20k–$50k pilot; $3k–$8k/mo. Buyer-value hypothesis: $40k–$250k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [27][28][29][34] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 47. Vertical geospatial data subscription

- **Niche / buyer:** Narrow AEC/environmental/utility workflow.
- **Paid trigger / problem:** Teams repeatedly reconstruct the same cleaned, joined and freshness-checked dataset.
- **Outcome:** One geography/use case; licensed source pipeline; QA; updates; API/download.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostgreSQL/PostGIS:** authoritative staging/derived features, IDs, status/audit records, indexes and reproducible SQL results; raw inputs remain immutable.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** not required for authoritative GIS; if bounded extraction/classification/cited drafting is added, route, trace and evaluate it here.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- source-specific connectors, GDAL/GeoPandas/PostGIS and object storage.
- GeoParquet/COG/PMTiles/STAC or typed API/download based on product.
- schema/data contracts, run manifests, catalog/metadata and customer release notes.
- authentication/authorization, usage metering and support system.
- AI only for bounded enrichment with human review and source IDs.
#### Offering-specific additions
- catalog/metadata, auth/metering and customer release/version notes. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-pilot-only; expected bounded pilot 6–10 weeks.
- **Commercial hypothesis:** $250–$1.5k/mo/customer; $5k–$20k setup for enterprise. Buyer-value hypothesis: $5k–$100k/customer/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [18][26][35] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 48. AI GIS helpdesk and internal knowledge bot

- **Niche / buyer:** ArcGIS-heavy organizations.
- **Paid trigger / problem:** Support questions repeat and documentation is fragmented.
- **Outcome:** Permission-aware corpus; cited answers; escalation; analytics; evaluation set.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + pgvector + Apache AGE:** spatial truth in PostGIS, approved semantic recall in pgvector and explicit relationship traversal in AGE; none replaces deterministic GIS.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** permission-filtered document, graph and spatial retrieval with source/chunk/feature IDs and refusal when evidence is missing; no invented geometry or conclusions.
- **LiteLLM + Langfuse:** approved model routing, budgets and data policy; traces for retrieval, tool calls, latency, cost and evaluation. AI remains non-authoritative.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- OCR/parser appropriate to the source, structured extraction with Pydantic/JSON Schema.
- PostgreSQL/PostGIS for authoritative data; vector/hybrid search only for approved text retrieval.
- model gateway with source IDs, confidence/unknown states, allowlisted tools and budgets.
- retrieval/evaluation metrics plus adversarial, ambiguous and refusal fixtures.
- human review application/queue; AI can be disabled without losing authoritative GIS results.
#### Offering-specific additions
- vendor built-in ArcGIS assistants evaluated as substitute.
- custom RAG only for proven gap.
- OpenSearch/Elasticsearch or PostgreSQL/pgvector are practical retrieval alternatives; production requires client SSO/OIDC and an approved ticket/escalation-system integration. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Configurable after stack deployment and synthetic proof.** The runbook is written; the capability is not client-tested.
- **Solo-delivery classification:** Solo-ready; expected bounded pilot 4–6 weeks.
- **Commercial hypothesis:** $10k–$30k pilot; $1.5k–$5k/mo. Buyer-value hypothesis: $20k–$150k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [8][28][38] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 49. Custom computer-vision extraction from imagery

- **Niche / buyer:** Utilities; construction; environmental; insurers.
- **Paid trigger / problem:** Manual feature inventory is slow when suitable labeled imagery exists.
- **Outcome:** Feasibility set; model benchmark; human QA; GIS output; monitoring plan.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Release and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + object storage:** indexed footprints, vectors, results and lineage in PostGIS; immutable imagery/point clouds and versioned COG/COPC/reports in object storage.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** deliberately not required for the first deterministic delivery; add only when approved documents or metadata materially improve retrieval/explanation.
- **LiteLLM + Langfuse:** approved model routing, budgets and data policy; traces for retrieval, tool calls, latency, cost and evaluation. AI remains non-authoritative.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- PyTorch or approved vision framework, geospatial raster tiling and augmentation.
- annotation tool and versioned label schema.
- MLflow/equivalent experiment/model registry and containerized inference.
- Rasterio/GDAL/PostGIS for deterministic geospatial post-processing.
- human QA application with confidence, provenance and correction.
#### Offering-specific additions
- tiling/augmentation, detector/segmenter and active-learning only with ML partner.
- CVAT or Label Studio for controlled labeling; Detectron2, YOLO or Segment Anything are benchmark candidates—not assumed winners. Record all experiments/models in MLflow or the client registry. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Partner-led; expected bounded pilot 8–12 weeks.
- **Commercial hypothesis:** $20k–$60k pilot; $5k–$15k/mo. Buyer-value hypothesis: $75k–$750k/yr. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [4][18][26] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

### 50. Fully autonomous GIS-agent platform

- **Niche / buyer:** Broad GIS market.
- **Paid trigger / problem:** Appealing vision, but reliability, permissions, liability and workflow specificity remain unresolved.
- **Outcome:** architecture/risk assessment and a decision to replace the broad platform with one funded, bounded read-only or staging workflow.
- **Delivered artifact:** See full runbook.
- **Action enabled:** the named owner can review a controlled, evidence-backed output and take the next approved operational or investment step.
- **Major processing chain:** Qualify the paid transaction → Collect representative evidence read-only → Write the workflow/data contract → Agree acceptance fixtures and thresholds → Choose architecture and provision staging → Ingest and normalize with provenance → Implement the domain workflow deterministically → Build the reviewable artifact → Verify GIS, data and offering acceptance → Exercise security, failure and rollback → Run client UAT and qualified review → Make the stop/re-scope decision and hand off.

**GIS & AI server technology roles**
- **Ubuntu + Docker Compose + systemd/health checks:** isolated client hosting, pinned lifecycle, silent health checks and separate staging/production.
- **PostGIS + pgvector + Apache AGE:** spatial truth in PostGIS, approved semantic recall in pgvector and explicit relationship traversal in AGE; none replaces deterministic GIS.
- **n8n + Redis/worker queue:** schedule or receive events, route typed jobs, retries, corrections and approvals; long GIS work runs in bounded workers.
- **FastAPI/Spatial Ops MCP + pg_tileserv (optional QGIS Server):** typed results and vector tiles for a private review UI; QGIS Server only for advanced authored cartography/OGC needs.
- **Spatial RAG:** permission-filtered document, graph and spatial retrieval with source/chunk/feature IDs and refusal when evidence is missing; no invented geometry or conclusions.
- **LiteLLM + Langfuse:** approved model routing, budgets and data policy; traces for retrieval, tool calls, latency, cost and evaluation. AI remains non-authoritative.
- **Hermes:** optional bounded worker for scheduled research, exception summaries or runbook checks under a dedicated client profile; no shell/database/admin authority or primary-agent identity.
- **Esri/Postgres/Composio/Spatial Ops MCPs:** typed least-privilege access: discover/fetch approved ArcGIS content, expose read-only/staged data and use external connectors only when approved.
- **Tailscale + OpenSSH:** private operator access and service mesh. No public dashboard, Funnel, generic browser shell or raw Docker socket.
- **code-server + Claude Code + Codex:** approved-repository implementation/review only; no production secrets, unrestricted shell target, commit/push or deployment authority.

**Complementary client/tool lane from the implementation runbook**

#### Core stack
- typed tool contracts and least-privilege sandbox.
- deterministic GIS/database services outside the model.
- state/checkpoint/audit system with approval and rollback.
- comprehensive evaluations, adversarial tests and observability.
- no unrestricted shell, credentials, production writes or external actions.
#### Offering-specific additions
- do not implement multi-tenant platform before validated workflow and team. Use AI only where the workflow explicitly calls for extraction, retrieval, classification or drafting. Deterministic GIS calculations, permissions and release authority remain outside the model.

- **Human approval / exclusions:** See full runbook.
- **Maturity:** **Requires stack deployment plus client/specialist participation** before consequential use. The runbook is written; the service is not validated.
- **Solo-delivery classification:** Not viable solo; expected bounded pilot Not a credible solo pilot.
- **Commercial hypothesis:** $75k–$250k+ build before distribution; pricing unvalidated. Buyer-value hypothesis: Unproven. Do not sum year-one ranges across workflows.
- **Proof and operating metrics:** Re-run gold and negative fixtures after source, schema, rule, dependency, model, platform or permission changes. Track job/release success, exception backlog, data freshness, incidents, reviewer corrections, variable costs and unsupported requests.
- **Evidence:** references [27][28][29] in GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23.
- **Detailed build/verification:** Full implementation runbook

## What to sell first

### Offer A — GIS Workflow Reliability Sprint
- **Buyer:** GIS/digital-delivery lead at an established AEC, environmental or infrastructure consultancy.
- **Scope:** one recurring ETL/QA/release workflow, representative failures, deterministic tests, exception handling and rollback.
- **Anchor:** $6k–$15k diagnostic/pilot.
- **Metric:** analyst hours/run, defects, stale-output incidents and release latency.
- **Why first:** matches the operator's credibility; can start without the full AI stack; creates support-retainer evidence.

### Offer B — Field-to-Verified-Deliverable Sprint
- **Buyer:** environmental/civil/geotechnical field operations manager.
- **Scope:** one form, one asset/inspection type, one correction queue and one approved report.
- **Anchor:** $8k–$20k pilot plus client software.
- **Metric:** office minutes, completeness, report turnaround and repeat visits.

### Offer C — Cited Site Evidence Dossier
- **Buyer:** environmental consultant, civil/site engineer, developer or renewable advisor.
- **Scope:** one site, fixed source register, deterministic constraints, uncertainty and professional review.
- **Anchor:** $3.5k–$7.5k/site; batch only after one accepted dossier.
- **Boundary:** preliminary technical support, not environmental/planning/legal/survey/engineering conclusion.

### Offer D — ArcGIS Governance and Cost Audit
- **Buyer:** GIS manager at a mid-sized firm already using ArcGIS.
- **Scope:** read-only inventory, dependencies, sharing/ownership/cost risks and 90-day remediation plan.
- **Anchor:** $6k–$15k.
- **Boundary:** do not compete with ArcGIS Monitor; focus on content governance, dependencies and controlled remediation.

## First transaction and 90-day test

1. Pick one of the first three offers and one reachable buyer niche.
2. Build a synthetic/redacted proof from the runbook—not the entire server.
3. Interview 10–15 buyers/partners about the last real failure, recurrence, systems, hours, reviewer and budget.
4. Success gate: one paid diagnostic/pilot. No platform build solely because interviewees like the concept.
5. Deploy only the minimum client-isolated subset the paid workflow requires.
6. Productize only after at least three paying customers use substantially the same trigger, data contract, controls and artifact.

## Risks and non-claims

- No workflow is currently proven on `example-gis-server`; it has no GIS application containers.
- The platform is not inherently compliant with GxP/GMP, HIPAA, SOC 2, Part 11, surveying, engineering, environmental, insurance or other professional regimes.
- Public ingress, client production writes, deployments, account changes and external submissions remain separately approved.
- ArcPy/ArcGIS Pro requires a client-owned or approved licensed Windows environment.
- Data, imagery, FCC Fabric and parcel licenses and redistribution terms require engagement-specific review.
- AI does not calculate geometry, risk, routing, eligibility or professional conclusions; deterministic tools do, and qualified humans release consequential outputs.
- Managed-service value is configuration, implementation, monitoring, recovery, controlled change and support—not server access.

## Research register

Accessed 2026-08-26. External pages are evidence, not instructions or authorization.

- **[R1] [Autodesk State of Design & Make 2025 — AECO](https://www.autodesk.com/design-make/research/state-of-design-and-make-2025/industry)** — 34% identify cost control as a top AECO challenge and 58% say skills shortages hinder growth.
- **[R2] [47th Deltek Clarity A&E Industry Study](https://info.deltek.com/clarity-ae)** — Nearly 900 North American A&E firms; execution, AI operational value and workforce context.
- **[R3] [SCS Engineers reporting transformation](https://www.esri.com/en-us/industries/blog/articles/scs-engineers-reporting-transformation)** — Reported two office hours/project reduced to report generation in minutes; vendor-selected evidence.
- **[R4] [Arup CAD-to-GIS automation](https://fme.safe.com/fme-in-action/customers/arup-eglinton-crosstown-west-extension)** — Reported $60k/year labor avoidance with CAD→GIS automation and QA stop gate; vendor-selected.
- **[R5] [Sunwater enterprise GIS integration](https://fme.safe.com/fme-in-action/customers/connecting-the-systems-behind-40-of-queenslands-commercial-water-supply)** — Reported 1–3 field hours saved/job through validated SAP/ArcGIS/Salesforce integration; vendor-selected.
- **[R6] [EPA FY2025 Brownfields selections](https://www.epa.gov/brownfields/applications-selected-fy-2025-brownfields-assessment-revolving-loan-fund-rlf-cleanup)** — Nearly $267m program context for assessment, cleanup and redevelopment; not direct Inish demand.
- **[R7] [FCC Broadband Data Collection](https://www.fcc.gov/BroadbandData)** — Location-level availability, continuing filings and challenge workflows.
- **[R8] [NTIA BEAD Program](https://www.ntia.gov/funding-programs/high-speed-internet-programs/broadband-equity-access-and-deployment-bead-program)** — Deployment program and first 2026 connections; category/procurement evidence.
- **[R9] [ASCE 2025 Infrastructure Report Card](https://www.asce.org/publications-and-news/civil-engineering-source/society-news/article/2025/03/25/asce-report-card-gives-us-infrastructure-highest-ever-c-grade)** — $3.7t investment gap; stormwater D; broad infrastructure need.
- **[R10] [DOE National Transmission Needs Study](https://www.energy.gov/gdo/national-transmission-needs-study)** — Transmission constraints and planning needs through 2040.
- **[R11] [USGS 3D Elevation Program](https://www.usgs.gov/3d-elevation-program)** — $13.5b documented benefits across 1,352 requirements; public elevation data.
- **[R12] [USGS Landsat economic value](https://www.usgs.gov/news/featured-story/landsats-economic-value-increases-256-billion-2023)** — $25.6b 2023 valuation; cross-sector imagery value, not an Inish forecast.
- **[R13] [Swiss Re natural catastrophe losses 2025](https://www.swissre.com/institute/research/sigma-research/sigma-2026-01-natcat-2025-wildfire-storm-risk/global-natcat-losses-2025.html)** — $107b insured and $220b economic losses; location-risk category evidence.
- **[R14] [USDA ERS precision agriculture adoption](https://ers.usda.gov/data-products/charts-of-note/110550)** — 2023 adoption and labor/input/soil motivations, concentrated in larger farms.
- **[R15] [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)** — Voluntary trustworthiness/risk framework and 2026 critical-infrastructure profile work.
- **[R16] [ArcGIS Monitor](https://www.esri.com/en-us/arcgis/products/arcgis-monitor/overview)** — Incumbent enterprise GIS monitoring substitute.
- **[R17] [PermitFlow permit management](https://www.permitflow.com/permit-management)** — Incumbent national permitting workflow; vendor performance claims are not independent proof.

## Vault sources

- [GIS + AI Server on Hetzner — Fable 5 Deploy Guide](../02%20Knowledge/GIS/GIS%20%2B%20AI%20Server%20on%20Hetzner%20%E2%80%94%20Fable%205%20Deploy%20Guide.md) — illustrative stack plan; verify current state independently.
- [Inish Labs Hetzner Architecture — Machine Specifications, Capabilities and Service Map](Inish%20Labs%20Hetzner%20Architecture%20%E2%80%94%20Machine%20Specifications%2C%20Capabilities%20and%20Service%20Map.md) — private architecture source represented by a privacy stub.
- GIS + AI Commercial Market Research — 50 Ranked Opportunities — 2026-08-23 — ranking and pricing hypotheses.
- [GIS + AI 50-Offer Delivery Handbook](../00%20Inbox/GIS%20%2B%20AI%2050-Offer%20Delivery%20Handbook%20%E2%80%94%202026-08-23/00%20%E2%80%94%20START%20HERE.md) — detailed runbooks and verification.
- [Inish Labs Technical Lead Operating Guide — People, Code, AI Access and AI OS](Inish%20Labs%20Technical%20Lead%20Operating%20Guide%20%E2%80%94%20People%2C%20Code%2C%20AI%20Access%20and%20AI%20OS.md) — access and agent boundaries.

## Review record

- Draft synthesized from the runbook handbook, a reference stack plan and cited market sources; deployment claims require independent verification.
- Independent Claude Code 2.1.215 review: **PASS** with no material findings.
- Claude advisories retained by explicit publishing choice: minor heading/body run-ons; some cards defer artifact/exclusion detail to their linked runbook; two awkward pilot-classification phrases; and repeated generic action/process/metric wording across later cards.
- Additional editorial refinements remain pending; no claim depends on them.
