---
title: "Prompts as composable artifacts"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Prompts as composable artifacts

> Prompts are reusable code; they deserve version control, comments, and refactoring.

## The shift

People treat prompts as throwaway text. They type something, hit enter, see what comes out, type something different next time. The prompt is ephemeral; only the result matters.

This is wrong. Or rather: it's fine for one-off requests, and disastrous for anything you do more than twice.

A prompt you'll reuse is *code*. It has:

- An interface (what inputs it expects)
- A contract (what it promises to produce)
- Internal logic (the instructions inside)
- Bugs (cases where it produces bad output)
- A maintenance burden (the world changes, the prompt drifts)

Treating it like code unlocks the same practices that make code maintainable: version control, comments, refactoring, naming, testing.

## The two-layer pattern

The cleanest way to manage reusable prompts:

```
Knowledge Hub/
  AI/
    Prompts/
      review.md           ← the design (with notes, history, examples)

~/.claude/commands/
      review.md           ← the deployment (just the prompt text)
```

The vault note has the *why*. It documents:
- When to use the prompt
- Known failure modes
- Variations tried
- Date last updated
- Example of good output vs bad

The slash command file is just the prompt text. Claude Code reads it and expands it into your message. It's the executable form.

## Why duplicate?

Two reasons:

**1. Different audiences.** The slash command is for Claude — it should be tight, instruction-shaped. The vault note is for *you* — it can have explanations, history, surrounding context. Cramming all that into the slash command bloats Claude's context for no benefit.

**2. Different update cadences.** You'll refine the prompt logic many times. Each time, the vault note captures *why* you changed it. Six months later, when you wonder "why is this prompt phrased this weirdly," the vault note answers.

## Anatomy of a good prompt note

```markdown
---
type: prompt
slash-command: /review
tool: claude-code
last-updated: 2026-05-17
tags: [prompt, review]
---

# Review prompt

## When to use
After making changes but before committing. Catches obvious issues.
Use BEFORE commits, not after — once committed, Claude is reviewing
your decisions, not catching problems.

## Known failure modes
- Sometimes too gentle; if it says "ship as-is," trust ~80% but skim the diff yourself
- Doesn't catch logic errors as well as it catches style errors
- Bad at catching missing test coverage (separate prompt for that)

## Variations I tried
- Adding "be ruthless" made it worse — too many false positives
- Adding test-coverage check inside this prompt diluted the review focus

## The prompt

(content below mirrors ~/.claude/commands/review.md)

\`\`\`
Review the most recent uncommitted changes in this repository.

For each modified file:
1. Read the change.
2. Identify any obvious bugs, missing edge cases, or violations of the project's CLAUDE.md conventions.
3. Suggest improvements, but do not modify files unless I ask.

End with a one-paragraph summary: ship as-is, ship with minor edits, or rework.
\`\`\`
```

## Anti-patterns

**The kitchen-sink prompt.** "Review my code, suggest improvements, add tests, update docs, summarize." This kind of prompt gets each task done badly. Better: separate slash commands, each focused.

**The unversioned prompt.** You keep refining a slash command in place, never noting what you changed. Three months later you can't remember why it's worded the way it is. Vault note solves this.

**The prompt you used twice and forgot.** A slash command you wrote for one task and never reused is overhead. The point of slash commands is repetition. If you don't repeat, don't bother.

## When to promote a prompt

Don't write a slash command for every interesting prompt. Use this test:

- Used it 3+ times? → Make it a slash command.
- Used it once but suspect it'll be useful? → Keep in vault as a draft (in `AI/Prompts/drafts/`), promote when it earns it.

Trying to build a "library" before you have the use case is backwards. Let the library emerge from real use.

## What I've promoted

*Track which prompts have earned slash-command status:*

- 

## Related

- [instructions-as-constraints](instructions-as-constraints.md) — same principles apply inside the prompt itself
- [feedback-loops](feedback-loops.md) — session notes drive prompt refinement
