---
title: "Agent Engineering Methods Lab"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Agent Engineering Methods Lab

A runnable learning workspace showing prompt, context, harness, loop, graph, assurance, and agent organization engineering as cumulative layers.

The “other future method” is interpreted as **agent organization engineering**, matching the existing guide `Assurance Engineering and Agent Organization Engineering — GIS Implementation Guide.md`.

## Quick start

```bash
python3 scripts/validate_workspace.py   # static structure + REQUIRED_FILES coverage map
python3 scripts/run_demo.py             # producer run (graph-routed, budget-enforced)
python3 scripts/verify_demo.py          # independent verifier (separate process, authors the verdict)
python3 scripts/validate_demo.py        # final validation gate (run_id + digest binding)
python3 scripts/check_method_01.py      # standalone Method 01 fixture check
```

The capstone recommends an implementation lane for a fixture GIS web-application request. The producer executes the graph from `capstone/graph.json`, enforces harness/loop/delegation budgets, and writes an artifact, run report, and attestation — all bound to a fresh `run_id`. A separate verifier process recomputes digests, sections, the decision, and trace legality, then writes the only verdict, the evidence bundle, and the typed handoff to the registered human reviewer. Outputs land in `capstone/output/` (see `capstone/README.md` for the full list).

## Folder map

```text
methods/01_prompt_engineering ... 07_agent_organization_engineering
_shared/       stable principles, local authorization boundary, integrity limits
_templates/    reusable task, evidence, verdict, delegation, and handoff forms
capstone/      one integrated fixture, JSON schemas, enforcement map, coverage profile
scripts/       producer, verifier, final validator, workspace and method checks
```

## Important distinction

This lab is an executable local demonstration, not proof of production readiness. Enforcement status for every policy field is declared honestly in `capstone/enforcement-map.json`, and `_shared/assurance-integrity-limits.md` documents what these workspace-editable validators cannot prove. A production system still needs real identity, sandboxing, network controls, policy enforcement, durable state, artifact storage, CI/CD, monitoring, incident response, and target-specific tests.
