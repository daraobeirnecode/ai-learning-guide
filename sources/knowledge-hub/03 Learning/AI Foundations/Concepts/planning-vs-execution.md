---
title: "Planning vs execution"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Planning vs execution

> Separating "decide what to do" from "do it" is the single highest-leverage workflow change.

## The pattern

Two-phase prompting. Phase 1: get the plan. Phase 2: execute the plan.

**Phase 1:**
> Before making any edits, propose a plan as a numbered list. Include: files you'll create or modify, the order, any decisions you need from me, and how you'll know it worked. Do not write code yet.

**Phase 2 (after you've read and approved the plan):**
> The plan looks good. Proceed.

That's it. The whole technique.

## Why it works

Agents are good at execution and mediocre at planning. The mediocre planning is hidden when planning and execution happen in the same turn — you only see the output, which makes the plan invisible. By the time you notice the plan was wrong, the implementation already exists and unwinding it is more expensive than starting over.

Separating the phases makes the plan inspectable. You can read it, push back on it, request alternatives, narrow it. Once approved, execution can be aggressive without you worrying that aggression is the wrong direction.

## Cost-benefit

Cost: one extra turn per task. Maybe 30 seconds of wall time.

Benefit: avoid the hour you would have spent unwinding a wrong implementation.

The ratio gets better as task complexity goes up. For one-line fixes, plan-then-execute is overhead. For anything involving multiple files or non-trivial decisions, it pays for itself the first time it catches a bad plan.

## When to skip it

- Trivial edits: "fix the typo on line 42"
- Pure read tasks: "what does this function do?"
- When you don't care about the result (rare)

When to use it:

- Anything touching more than one file
- Anything where you don't already know the right approach
- Anything you'd hate to redo
- First time in a new codebase
- Refactors

## The plan format

A good plan from Claude looks like:

```
Plan:
1. Read main.py to understand parse_args
2. Add validation in parse_args:
   - reject negative integers
   - reject non-integer strings
   - emit clear error messages
3. Add three test cases to test_main.py:
   - valid positive int → accepted
   - negative int → ValueError with message
   - non-integer → ValueError with message
4. Run pytest to confirm
5. If tests pass, you decide whether to commit

Decisions needed from you:
- Should the error message include the rejected value, or just the type of error?
- Should we use Python's argparse type= parameter, or do validation after parsing?

Success criterion: pytest passes with the three new tests.
```

A bad plan looks like:

```
I'll add validation to parse_args and add some tests.
```

If you get the bad version, push back: "give me a more detailed plan with specific decisions called out."

## The two anti-patterns

**Plan but execute regardless.** You ask for a plan, Claude gives you one, you skim and say "go." If you didn't actually read it, you got the cost without the benefit. Read it.

**Plan as performance.** Some prompts produce a "plan" that's just a paraphrase of the request. "I will fix the function. I will run the tests. I will tell you the result." That's not a plan, it's a rephrase. Reject it and ask for actual decisions and tradeoffs.

## My modifications to the standard pattern

*Add your own variations as you discover them:*

- 

## Related

- [the-agent-loop](the-agent-loop.md) — planning is the first step of the loop; this concept makes it explicit
- [prompts-as-artifacts](prompts-as-artifacts.md) — plan-then-execute is itself a reusable prompt pattern
- See also: `03 Learning/AI Foundations/Prompts/plan-then-execute.md` for the slash command form
