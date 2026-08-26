---
title: "Trust boundaries and sandboxing"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Trust boundaries and sandboxing

> Agents need permission systems; the question isn't "can I trust this agent" but "what can it touch."

## The wrong question

When people first use AI agents on their machine, the framing is:

> "Can I trust Claude / Codex enough to let it run commands?"

This question doesn't have a useful answer. The agent is going to be right most of the time and wrong some of the time. The question is too binary.

## The better question

> "If the agent does the worst thing it could plausibly do right now, what happens, and is that bounded?"

This question always has an answer. If the answer is "it nukes my git history" or "it leaks an API key" or "it makes a charge on my credit card" — that's an unbounded blast radius. Don't grant permission for those actions.

If the answer is "it makes a syntactically valid but wrong change to a file in this project, which I can revert with git" — that's bounded. Grant permission freely.

This framing is *sandboxing*: defining the cage the agent can operate in, such that worst-case behavior is acceptable.

## Codex's clean model

Codex separates this into two independent dials:

**Sandbox mode** — what the agent *can* do, technically:
- `read-only`: can read but not write or execute
- `workspace-write`: can write inside cwd; no network access by default
- `danger-full-access`: no sandbox

**Approval policy** — when the agent must *ask*:
- `untrusted`: ask for almost everything
- `on-request`: ask only when the agent itself flags a need
- `never`: never ask

The sandbox sets the cage. The approval policy sets the leash inside the cage. They're orthogonal: you can have a tight cage with no leash (small space, full autonomy inside) or a wide cage with a short leash (large space, ask before each step).

## Claude Code's model

Claude Code uses a single permissions concept (Ask, Allowlist, Skip) that mixes both ideas. Functionally similar, less clean conceptually. The mental separation from Codex is worth applying mentally even when working in Claude Code:

- What CAN this session do? (sandbox)
- When should it ask me? (approval)

## Practical defaults

For most work:

```bash
# Codex
codex --sandbox workspace-write --ask-for-approval on-request

# Claude Code
# default permissions (Ask mode) — let it ask, build intuition
```

For risky work (unfamiliar repo, important code, automated runs):

```bash
# Codex
codex --sandbox read-only --ask-for-approval untrusted

# Claude Code
# permissions: strict — approve every write
```

For trusted automation (sandboxed throwaway environment):

```bash
# Codex
codex --sandbox workspace-write --ask-for-approval never

# Claude Code
# only in containers/VMs you don't care about
```

## The generalization

This concept generalizes far beyond AI agents. Any tool you give power to needs the same analysis:

- API keys: scope to the minimum, rotate often, never grant `admin`
- Production access: read-only by default, write only behind explicit approval
- CI/CD agents: same model applies
- Future autonomous systems: same

The skill you're building this week isn't really about Codex. It's about how to think about delegation under uncertainty. That skill will pay off in every tool you use for the next decade.

## What I've configured

*Track your actual sandbox/permission defaults across tools:*

- Codex default profile: 
- Claude Code default: 
- Hermes equivalent: 

## Related

- [the-agent-loop](the-agent-loop.md) — sandboxing constrains the "act" step of the loop
- [tool-use-and-mcp](tool-use-and-mcp.md) — MCP tools each need their own trust analysis
