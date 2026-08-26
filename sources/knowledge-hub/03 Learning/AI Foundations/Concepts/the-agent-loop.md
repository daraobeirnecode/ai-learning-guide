---
title: "The agent loop"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# The agent loop

> An agent doesn't answer once; it plans, acts, observes, and iterates until done.

## The shape

Every modern AI coding tool — Claude Code, Codex CLI, Cursor's agent mode, Aider — works the same way at the core:

```
USER GOAL
   ↓
  ┌────────────────────────────────────┐
  │  PLAN: what should I do next?      │
  └────────────────────────────────────┘
                 ↓
  ┌────────────────────────────────────┐
  │  ACT: call a tool (read, write,    │
  │       run command, edit, search)   │
  └────────────────────────────────────┘
                 ↓
  ┌────────────────────────────────────┐
  │  OBSERVE: what came back?          │
  │  (file contents, output, error)    │
  └────────────────────────────────────┘
                 ↓
       Is the goal done?
        /              \
      Yes              No
       ↓                ↓
     Stop          Back to PLAN
```

This loop is the entire mechanism. There is no other magic. Every impressive thing an "AI agent" does is some combination of: a smart plan, a useful tool call, and a good interpretation of the result.

## Why this matters for prompting

If you think you're talking to a chat assistant, you'll write chat prompts: "Could you also..." "What do you think about..." "Maybe try..."

If you think you're directing an agent loop, you'll write goal prompts: "The goal is X. The constraints are Y. The success criterion is Z."

Goal prompts are dramatically better because they give the agent something to plan *toward*. Chat prompts give the agent something to *talk about*.

## Where it goes wrong

Three common failure modes:

1. **Bad plan, executed competently.** The agent decides to refactor when you wanted a bug fix. The execution is fine, the diff is clean, but you got the wrong thing. Mitigation: plan-then-execute pattern (see [planning-vs-execution](planning-vs-execution.md)).

2. **Good plan, bad observation.** The agent acts, the result is ambiguous, and the agent infers the wrong thing. Example: a test fails for an unrelated reason and the agent assumes its change caused it. Mitigation: tighter test feedback, or asking the agent to interpret results before acting on them.

3. **Loop won't terminate.** The agent has a goal that's slightly underspecified, so it keeps "improving." Mitigation: explicit success criteria up front.

## How to use this concept

When something goes wrong in a Claude Code or Codex session, ask: which step of the loop broke?

- Did Claude plan badly? → tighter goal prompt next time
- Did Claude act badly given a good plan? → instructions probably need a constraint
- Did Claude misread the result? → the feedback signal in your project (test output, error messages) is too noisy

This decomposition is more useful than "Claude is dumb today."

## What I noticed

*Fill this in after Project 1. Specifically: in your first session, what did the plan-act-observe cycle look like? Where did you see each step?*

- 

## Related

- [context-as-input](context-as-input.md) — what the agent sees during the loop
- [planning-vs-execution](planning-vs-execution.md) — the highest-leverage intervention on the loop
- [tool-use-and-mcp](tool-use-and-mcp.md) — what "acting" actually means at the protocol level
