---
title: "Instructions as constraints"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Instructions as constraints

> Good agent instructions are constraints and "don'ts," not aspirations and "tries."

## The problem with aspirations

The first instinct when writing a `CLAUDE.md` or `AGENTS.md` is to write things like:

- "Be thorough"
- "Write clean code"
- "Think step by step"
- "Be careful with edge cases"
- "Use best practices"

These all *sound* like instructions. They're not. They're wishes. The model has been trained on so many of these phrases that they have nearly zero behavioral weight. "Be thorough" is the AI-instruction equivalent of "have a nice day" — universally said, rarely meaningful.

A test: would Claude do something *different* if this line weren't in your CLAUDE.md? If you can't name what would change, the line is decoration.

## What works: specific constraints

Compare to:

- "Don't add new dependencies without asking"
- "Always type-hint public functions"
- "If a test exists for code you change, run it and report the result"
- "Don't write more than 50 lines without proposing a plan first"
- "Use bash with `set -euo pipefail` at the top of any non-trivial script"
- "Don't run `rm -rf` or `git push --force` without explicit confirmation in the prompt"

These bind behavior. Each one is falsifiable — you can look at Claude's output and tell whether it followed the rule. Each one rules out a class of mistakes you've actually seen.

## Why "don'ts" beat "dos"

A "do" instruction adds one thing to a vast space of possible actions. "Write clean code" doesn't tell Claude which 99 things *not* to do.

A "don't" instruction removes a region from action space. "Don't use global variables" rules out a whole pattern. "Don't add new dependencies without asking" rules out an entire class of unwanted behaviors.

The model is going to do *something*; your job is to narrow what.

## The two-question test

For every line in your CLAUDE.md / AGENTS.md, ask:

1. **Is it falsifiable?** Can I look at Claude's output and tell whether it followed?
2. **Is it earned?** Have I actually seen the mistake this prevents, in real work?

If both yes, keep. If either no, cut.

The "earned" test matters because every line you add is in the context window forever. Adding lines that don't prevent real mistakes you've seen is just paying context tax for nothing.

## How to grow a CLAUDE.md

Start with maybe 10–15 lines. Use Claude for a week. When something goes wrong, write a session note. After a few session notes accumulate, you'll see patterns. Distill each pattern into a one-line "don't" and add it to CLAUDE.md.

After 3 months, your CLAUDE.md is tuned to your work. After 6 months, it's better than any template.

## My current CLAUDE.md philosophy

*Refine as you go. Initial principles:*

- Aspirations are noise; constraints are signal
- "Don'ts" outperform "dos"
- Every line must be earned by a real mistake
- Bias toward cutting; bias against adding
- Keep it under one screen if possible

## What I added this month

*Track new CLAUDE.md additions here, with the session note that earned them:*

- 

## Related

- [context-as-input](context-as-input.md) — CLAUDE.md is part of context, every line costs budget
- [prompts-as-artifacts](prompts-as-artifacts.md) — slash commands follow the same logic
- [feedback-loops](feedback-loops.md) — session notes are how you discover what constraints to add
