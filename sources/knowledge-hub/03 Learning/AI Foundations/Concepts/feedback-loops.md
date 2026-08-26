---
title: "Feedback loops"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Feedback loops

> The agent that learns from its own runs beats the agent that doesn't; logging and review are part of the workflow, not optional.

## Two loops, nested

There's the loop inside a session — plan, act, observe, repeat. That's [the-agent-loop](the-agent-loop.md).

There's a bigger loop *across* sessions:

```
   ┌─────────────────────────────────────────────┐
   │                                             │
   │   session runs                              │
   │        ↓                                    │
   │   session note captures what happened       │
   │        ↓                                    │
   │   notes accumulate                          │
   │        ↓                                    │
   │   patterns become visible                   │
   │        ↓                                    │
   │   patterns distilled into lessons           │
   │        ↓                                    │
   │   lessons inform CLAUDE.md / prompts        │
   │        ↓                                    │
   │   next session runs better  ────────────────┤
   │                                             │
   └─────────────────────────────────────────────┘
```

Most people skip this loop entirely. They use Claude Code, hit problems, complain about the problems, and live with them. The compounding move is to capture each problem and let the accumulated patterns push back into your setup.

## Why this is hard

This is the highest-leverage practice in the whole curriculum, and the hardest to maintain. Three reasons:

**1. Friction at the wrong moment.** A session ends, you feel done, the last thing you want is to write a note. The energy is gone.

**2. No immediate payoff.** Writing one session note doesn't help you. Writing 20 does. The first 19 feel like overhead.

**3. The benefit is invisible to your present self.** Future-you, looking back, sees the pattern. Present-you sees only the friction.

The trick: make the friction smaller than the urge to skip. A 2-minute note beats no note. A bullet-list session note beats a polished one. A `/log-session` slash command beats writing from scratch.

## What goes in a session note

Minimum viable session note:

```markdown
---
date: YYYY-MM-DD
tool: claude-code
project: <name>
outcome: success / partial / failed
---

## What I asked for
<one sentence>

## What worked
<2-4 bullets>

## What went sideways  
<2-4 bullets, OR "nothing significant">

## What I'd do differently
<1-2 bullets, OR blank>
```

That's it. Two minutes. The template is in `03 Learning/AI Foundations/Templates/session-note.md`.

## What goes in a lesson note

Lessons come from accumulated session notes. The shape:

```markdown
---
date: YYYY-MM-DD
type: lesson
tags: [lesson]
---

## The lesson (one sentence)
<the rule in distilled form>

## What happened that taught me this
<2-3 sessions that surfaced the pattern>

## What I'll do differently
<concrete change — a CLAUDE.md line, a prompt edit, a habit>
```

A lesson is *earned* — multiple sessions point at the same problem before you write the lesson. Lessons that come from a single session are usually noise.

## Weekly review (optional but powerful)

End of each week, ~15 minutes: skim the week's session notes. Look for:

- A failure mode that appeared more than once → candidate for a CLAUDE.md addition
- A prompt that worked unusually well → candidate for promotion to a slash command
- A pattern of friction → candidate for a hook or workflow change
- A tool that was wrong for the task → candidate for a "when to use what" note

Write a one-paragraph review note in `AI/Lessons/weekly-YYYY-MM-DD.md`. Even if all you wrote is "no patterns yet, mostly smooth," that's signal.

## What "evaluation" means here

In AI parlance, "evaluation" usually means formal benchmarks — running standardized tasks against models and measuring performance. That's not what matters for personal use.

For personal use, evaluation is just: of my last 20 sessions, how many produced work I'd ship as-is, how many needed cleanup, how many were worse than doing the task myself?

If you don't have session notes, you can't answer this question. You're guessing. If you have notes, the answer is in the tags and outcomes you wrote.

This is the closest thing to "is this tool actually working for me" that personal use offers. Most people don't have it because they don't write notes.

## My current discipline

*Track honestly — be willing to write "haven't been keeping up" if true:*

- Sessions notes written this week: 
- Lessons written this month: 
- Weekly review last completed: 
- Patterns I'm watching for: 

## Related

- [the-agent-loop](the-agent-loop.md) — the inner loop; this concept is the outer loop
- [instructions-as-constraints](instructions-as-constraints.md) — lessons turn into CLAUDE.md constraints
- [prompts-as-artifacts](prompts-as-artifacts.md) — lessons turn into prompt refinements
- [hooks](hooks.md) — automate the friction of capture
- Project brief: `AI/Projects/05-session-to-lessons-pipeline.md`
