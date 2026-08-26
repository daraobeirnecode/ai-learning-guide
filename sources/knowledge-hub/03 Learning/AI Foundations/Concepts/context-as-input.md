---
title: "Context as the unit of input"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Context as the unit of input

> What the model sees (files, instructions, history) is the actual input — your prompt is just one piece.

## The mistake

When Claude does something unexpected, the instinct is: "my prompt was bad, let me rewrite the prompt."

That's almost always the wrong diagnosis. The model didn't see "your prompt." It saw the *full context window*, which includes a lot more than what you typed.

## What's actually in the context

On any given turn in Claude Code, the input to the model is roughly:

```
[system prompt — Claude's built-in personality and rules]
   +
[user CLAUDE.md — your ~/.claude/CLAUDE.md]
   +
[project CLAUDE.md — the repo's CLAUDE.md]
   +
[conversation history — every message and tool result so far]
   +
[file contents — every file Claude has read this session, still in context]
   +
[YOUR CURRENT MESSAGE]
```

In Codex, the structure is similar; substitute `AGENTS.md` for `CLAUDE.md`.

The "prompt" is the small part at the end. The rest is the context, and the rest is doing most of the work.

## Why this matters

Three implications:

**1. Stale context is a real problem.** If you read a file early in a session, edited it outside Claude, and then asked Claude about it, Claude's still looking at the old version it has in context. `/clear` or re-read the file to fix.

**2. Long sessions degrade.** Each turn adds to context. After many turns, the context is crowded with old file contents, abandoned plans, and conversation that's no longer relevant. The signal-to-noise drops. Symptoms: Claude forgets recent instructions, repeats earlier suggestions, makes weirdly inconsistent decisions. Mitigation: `/compact` to summarize, or `/clear` to reset.

**3. CLAUDE.md is doing more work than you think.** Every instruction in your CLAUDE.md is in context for every turn. This is why bloated CLAUDE.md files are bad — they consume attention budget on every interaction. Keep it short and specific.

## The principle

The thing to optimize is not *the prompt you type*. It's *the entire context the model sees when it processes your prompt*. Your prompt is the steering input; context is the road, the weather, the car, and the speed limit.

## Practical implications

- **Be deliberate about what files you bring into context.** Use `@file` to add specifically; don't dump a whole repo.
- **Run `/clear` between unrelated tasks.** Don't try to do two different things in one session — they pollute each other's context.
- **Treat CLAUDE.md like real estate.** Every line costs context budget. Cut ruthlessly.
- **When something goes wrong, ask: what's in my context that pointed Claude this way?** Almost always more useful than rewording the prompt.

## What I noticed

*Fill this in during Project 1. Specifically: any moment where Claude did something unexpected and you traced it to context rather than prompt.*

- 

## Related

- [the-agent-loop](the-agent-loop.md)
- [instructions-as-constraints](instructions-as-constraints.md) — what to actually put in CLAUDE.md
