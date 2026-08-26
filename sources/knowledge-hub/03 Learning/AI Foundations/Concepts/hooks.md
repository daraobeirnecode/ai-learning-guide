---
title: "Hooks as event handlers"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Hooks as event handlers

> Hooks run a shell command at specific points in the agent's lifecycle. They turn the agent from a conversational tool into a governed one.

## The events

Claude Code exposes hook events at several lifecycle points. The three most useful:

- **`PostToolUse`** — runs after every tool call (e.g., after every file edit). Use for: auto-formatting, auto-linting, triggering rebuilds.
- **`SessionStart`** — runs when a session begins. Use for: injecting current date, current git branch, environment status into context.
- **`Stop`** — runs when Claude finishes a task. Use for: running tests automatically, prompting yourself to write a session note.

(Codex CLI's hook story is less developed as of mid-2026; the concept transfers, but the implementation details are Claude Code-specific.)

## The minimal example

In `~/.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "ruff format \"$FILE_PATH\" || true" }
        ]
      }
    ]
  }
}
```

After Claude edits or writes any file, Ruff formats it. The `|| true` makes the hook a silent no-op for non-Python files. Result: every Python file Claude touches comes out formatted, without you ever asking for it.

## What makes hooks powerful

Two properties:

**1. They run automatically.** No prompt needed. The agent doesn't have to remember; you don't have to ask. The hook just happens.

**2. They can fail safely.** A hook that errors out doesn't break the session (with `|| true` or similar). It just doesn't do its thing. That means you can be aggressive with hooks without paying for it in broken sessions.

## What makes hooks dangerous

The same two properties, viewed differently:

**1. They run automatically.** A hook with a destructive command runs without confirmation. A bad PostToolUse hook can corrupt files. Test hooks in a throwaway directory before adding them to your main config.

**2. They can fail silently.** A hook that errors out silently is hard to debug. Watch for the symptom: "I thought my hook was running but the file isn't getting formatted." Add logging if you need to debug.

## Hook patterns worth knowing

**Auto-format after edits** (the canonical example):
```json
{
  "matcher": "Edit|Write",
  "hooks": [
    { "type": "command", "command": "ruff format \"$FILE_PATH\" || true" }
  ]
}
```

**Inject context at session start**:
```json
{
  "matcher": "*",
  "hooks": [
    { "type": "command", "command": "date && git branch --show-current" }
  ]
}
```
Output of this hook flows into Claude's session context. So Claude starts every session knowing the date and current branch.

**Run tests after Claude finishes a task** (Stop hook):
```json
{
  "matcher": "*",
  "hooks": [
    { "type": "command", "command": "pytest 2>&1 | tail -20 || true" }
  ]
}
```

**Remind yourself to log the session**:
```json
{
  "matcher": "*",
  "hooks": [
    { "type": "command", "command": "echo 'Reminder: /log-session if this was useful'" }
  ]
}
```

## The right number of hooks

For Week 4 of this curriculum: 1. Pick one. Make it work.

For long-term: maybe 3–5 active hooks. More than that is usually overkill — you've over-engineered your tooling.

The test for whether a hook should exist: would you do this thing manually if the hook didn't? If yes, the hook is just removing friction. If no, you're inventing work for the agent.

## Hooks vs slash commands

Slash commands run when *you* invoke them. Hooks run when an *event* fires.

- Slash commands: deliberate, user-driven, can have arbitrary complexity
- Hooks: automatic, event-driven, must be fast and safe

Don't put a slow operation in a hook — it'll grind your sessions to a halt. Don't put a destructive operation in a hook — it'll happen without confirmation.

## My active hooks

*Track what's running and why:*

- 

## Related

- [feedback-loops](feedback-loops.md) — hooks automate parts of the outer feedback loop
- [trust-and-sandboxing](trust-and-sandboxing.md) — hooks bypass approval, so trust analysis applies
- Project brief: `AI/Projects/05-session-to-lessons-pipeline.md`
