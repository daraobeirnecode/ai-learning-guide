---
title: "04 Loop Engineering"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# 04 Loop Engineering

One job: control repeated observe, act, validate, repair, and stop behavior.

## Inputs
- `capstone/loop-policy.json`
- Harness policy and validator result

## Process
1. Define observation, candidate action, validator, repair rule, and terminal states.
2. Prefer closed loops with deterministic evidence.
3. Bound attempts, runtime, tool/model calls, tokens, cost, repeated errors, and side effects.
4. Escalate rather than retry identical failures indefinitely.
5. Persist checkpoints needed for safe resume.

## Output
- Loop policy, attempt log, stop reason, and final status.

## Human check
Can an operator explain exactly why the loop stopped and what changed on each attempt?

## Limitation
A loop amplifies both useful and harmful behavior; without a gate and stop rule it is uncontrolled repetition.
