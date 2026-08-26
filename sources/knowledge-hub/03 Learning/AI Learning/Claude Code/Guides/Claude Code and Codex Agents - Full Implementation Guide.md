---
title: "Claude Code and Codex Agents - Full Implementation Guide"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Claude Code and Codex Agents: Full Implementation Guide

> [!summary]
> **The short version:** An agent is a reusable worker definition with a role, instructions, model, tools, and operating boundaries. Claude Code defines reusable subagents as Markdown files with YAML frontmatter. Codex defines custom agents as TOML configuration files. Both run workers in isolated context windows, but Claude also has an experimental **agent teams** layer with a team lead, shared tasks, and direct teammate communication.

## Purpose

This guide explains how to design, create, configure, invoke, supervise, test, and share agents in **Claude Code** and **OpenAI Codex**. It focuses on local CLI and IDE workflows, with examples that apply to ordinary software development and GIS projects.

It covers:

- What an agent is and is not
- Agents versus instructions, skills, MCP servers, hooks, and permissions
- Claude Code custom subagents and experimental agent teams
- Codex subagents, agent threads, and custom TOML agents
- Global, project, session, and organization scopes
- Agent file structure and field-by-field configuration
- Invocation, parallelism, context isolation, and handoffs
- Safe read-only, implementation, and review roles
- Testing, debugging, versioning, and team governance
- Reusable GIS-oriented examples

## Local compatibility note

Verified on this Mac on 2026-07-31:

- Claude Code: `2.1.215`
- Codex CLI: `0.137.0`
- Codex `multi_agent`: stable and enabled locally
- Codex hooks: stable and enabled locally

The vendor documentation is newer than the local binaries. In particular:

- Claude Code features explicitly marked `2.1.216` or later in this guide require an upgrade from the currently installed `2.1.215`.
- The current Codex documentation includes standalone custom-agent files under `~/.codex/agents/` and `.codex/agents/`. Upgrade Codex and test a disposable agent before relying on every current schema field in production.
- Do not copy a current example into an older CLI and assume it loaded. Always test discovery, permissions, and the selected model.

---

# 1. The mental model

## 1.1 Main agent

The **main agent** owns the user conversation. It receives requirements, makes decisions, delegates work, combines results, and presents the final answer.

Keep the main agent focused on:

- User intent
- Scope and constraints
- Architecture decisions
- Approval boundaries
- Integration of worker results
- Final verification and reporting

Do not fill its context with thousands of lines of logs, broad search output, or repetitive test output when a subagent can summarize that material.

## 1.2 Subagent

A **subagent** is a delegated worker with its own context window. It receives a bounded task, uses its assigned tools, and returns a result or summary.

Good subagent tasks are:

- Self-contained
- Easy to verify
- Narrow enough to avoid role drift
- Independent of other concurrent tasks
- Clear about whether changes are allowed
- Clear about the expected output

Examples:

- Map the authentication code path without editing files.
- Run the test suite and report only failures.
- Review a diff for security regressions.
- Inspect a spatial ETL pipeline for CRS and geometry risks.
- Implement one module while another agent owns a different module.

## 1.3 Agent team

An **agent team** is more than several subagents. Team members are separate sessions that can coordinate through shared tasks and direct messages.

Claude Code currently provides an experimental agent-team system. Codex provides orchestrated subagent threads, but it does not use Claude's exact lead/task-list/mailbox architecture.

Use a team only when workers need to coordinate, challenge one another, or own separate workstreams for an extended period. Teams have more overhead and consume more tokens.

## 1.4 Agent definition

An agent definition describes a reusable role. It normally contains:

1. **Identity** — a stable name
2. **Routing description** — when the parent should use it
3. **Instructions** — how it works and what it returns
4. **Model** — inherited or explicitly selected
5. **Tools** — what it can access
6. **Permissions or sandbox** — what it can change
7. **Domain capabilities** — skills and MCP servers
8. **Lifecycle controls** — hooks, turn limits, memory, or isolation

## 1.5 Orchestrator

An **orchestrator** decomposes the task, launches workers, tracks dependencies, evaluates outputs, and assigns follow-up work.

A reliable orchestrator should:

- Define non-overlapping tasks
- State file ownership before parallel edits
- Give every worker enough context
- Wait for requested workers to finish
- Require evidence, not unsupported success claims
- Run independent review after implementation
- Reconcile conflicting findings
- Preserve human approval for dangerous or external actions

---

# 2. Agents versus adjacent features

| Feature | Purpose | Runs in separate context? | Usually reusable? | Should contain |
|---|---|---:|---:|---|
| Main project instructions | Persistent project rules | No | Yes | Architecture, commands, conventions, constraints |
| Agent | Specialized worker role | Yes | Yes | Role, behavior, model, tools, boundaries |
| Skill | Reusable procedure or domain workflow | Usually no; product-dependent | Yes | Steps, scripts, templates, references |
| MCP server | External tool/data connection | No by itself | Yes | Tool implementation and authentication wiring |
| Hook | Deterministic lifecycle control | No | Yes | Validation, logging, policy enforcement |
| Prompt | One requested outcome | No | Sometimes | Task, context, constraints, acceptance criteria |
| Worktree | Isolated Git working copy | No | Temporary | Separate branch/filesystem for concurrent edits |

## 2.1 Instructions are not agents

- Claude Code project guidance normally lives in `CLAUDE.md`, `.claude/CLAUDE.md`, rules, or managed instructions.
- Codex project guidance lives in `AGENTS.md` and optional nested or override files.
- Instructions affect normal work in that scope. They do not create a separately running worker.

## 2.2 Skills are not agents

A skill explains **how to perform a recurring workflow**. An agent defines **who performs a class of tasks and under what boundaries**.

A useful pattern is:

- Agent: `gis-data-reviewer`
- Skills loaded by that agent: `crs-forensics`, `geometry-validation`, `spatial-lineage`
- MCP tools available to that agent: PostGIS or ArcGIS read-only connections

## 2.3 MCP is not an agent

MCP supplies tools. An agent decides when and how to use them.

Do not put credentials in agent files. Configure secrets through supported environment variables, keychains, OAuth stores, or secret managers.

## 2.4 Hooks are deterministic backstops

Prompts describe intended behavior. Hooks enforce mechanical checks.

Examples:

- Block destructive SQL.
- Run a linter after edits.
- Reject completion if required tests did not run.
- Record agent start/stop events.
- Prevent writes outside an approved directory.

A prompt saying “never modify production” is useful. A sandbox and hook that make production modification impossible are stronger.

---

# 3. Choosing the right execution pattern

| Situation | Recommended pattern |
|---|---|
| One small edit | Main agent only |
| Noisy codebase search | One read-only subagent |
| Tests produce large logs | Test-runner subagent |
| Three independent review lenses | Three parallel subagents |
| Implementation followed by independent review | Sequential implementer → reviewer |
| Parallel changes to separate modules | Agents with explicit file ownership; use worktrees when available |
| Competing debugging hypotheses | Parallel investigators, then synthesis |
| Workers must debate or coordinate directly | Claude agent team |
| Task is sequential and shares heavy context | Main agent or one resumable subagent |
| Same procedure repeats across many tasks | Skill, optionally preloaded into an agent |

## Avoid agents when

- The task takes less time than delegation overhead.
- Workers need constant conversational context from the main thread.
- Multiple agents would edit the same file.
- The task is inherently sequential.
- The output cannot be independently verified.
- You are using parallelism only because it sounds sophisticated.

---

# 4. Anatomy of a good agent

Use this design checklist before writing product-specific syntax.

## 4.1 Name

Use a narrow role name, not a vague persona.

Good:

- `api-contract-reviewer`
- `gis-data-validator`
- `test-failure-triager`

Weak:

- `helper`
- `genius`
- `senior-engineer`

## 4.2 Description

The description is a routing rule. It should answer:

- What tasks should trigger this agent?
- Should it be used proactively?
- What should not be delegated to it?

Example:

> Reviews changed geospatial ETL code for CRS mistakes, geometry loss, schema drift, and missing validation. Use after modifying ingestion or export pipelines. Read-only; never edits files.

## 4.3 Instructions

A robust instruction body includes:

1. Role and objective
2. Inputs to inspect
3. Ordered workflow
4. Prohibited behavior
5. Verification requirements
6. Output schema
7. Escalation conditions

## 4.4 Capabilities

Grant only what the role needs:

- Explorer: read/search tools
- Reviewer: read/search plus safe test commands
- Implementer: read/edit/write/test
- Database analyst: read-only database tool or validated SQL shell
- Browser tester: browser MCP, screenshots, console and network evidence

## 4.5 Completion contract

Every agent should know what “done” means.

Example:

```text
Return:
1. Findings ordered by severity.
2. Exact file and line references.
3. Evidence or reproduction steps.
4. Recommended fix.
5. Tests that prove the fix.
If no issue is found, state what you inspected and any coverage gaps.
```

---

# 5. Claude Code custom subagents

## 5.1 How Claude subagents work

Each Claude Code subagent runs with:

- A fresh context window
- Its own system prompt
- A tool set narrowed from the parent session
- Independent tool calls and results
- The parent session's applicable permission context
- A task message composed by the parent

A normal custom subagent does **not** inherit the main conversation transcript. It receives the delegated task and the configuration/context Claude loads for that subagent.

Claude's built-in `Explore` and `Plan` agents in are special: current documentation says they skip `CLAUDE.md` and the parent session's Git status. Other built-in and custom subagents load applicable `CLAUDE.md` context and a Git-status snapshot.

## 5.2 Built-in Claude subagents

| Agent | Purpose | Typical capabilities |
|---|---|---|
| `Explore` | Fast codebase search and analysis | Read-only |
| `Plan` | Research during plan mode | Read-only |
| `general-purpose` | Complex multi-step work | Broad subagent tools |

Additional internal helpers may be invoked automatically for particular Claude Code features.

## 5.3 File locations and precedence

Claude subagent files are Markdown with YAML frontmatter.

| Location | Scope | Priority |
|---|---|---:|
| Managed settings `.claude/agents/` | Organization-wide | 1, highest |
| `--agents` JSON | Current session | 2 |
| `.claude/agents/` | Project | 3 |
| `~/.claude/agents/` | User/global | 4 |
| Plugin `agents/` | Wherever plugin is enabled | 5 |

Project definitions should be committed when the team should share them. Personal roles belong under `~/.claude/agents/`.

Claude scans project and user agent directories recursively. The `name` field, not the folder name, is the agent identity. Keep names unique.

## 5.4 Recommended Claude project structure

```text
my-project/
├── CLAUDE.md
├── .claude/
│   ├── settings.json
│   ├── settings.local.json        # private local overrides; usually ignored
│   ├── agents/
│   │   ├── research/
│   │   │   └── codebase-explorer.md
│   │   ├── implementation/
│   │   │   └── feature-implementer.md
│   │   └── review/
│   │       ├── code-reviewer.md
│   │       └── gis-data-reviewer.md
│   └── skills/
│       └── project-workflow/
│           └── SKILL.md
├── scripts/
│   └── validate-readonly-query.sh
└── src/
```

## 5.5 Minimal Claude agent definition

Create `.claude/agents/code-reviewer.md`:

```markdown
---
name: code-reviewer
description: Reviews changed code for correctness, security, regressions, and missing tests. Use after implementation. Read-only.
tools: Read, Grep, Glob, Bash
model: inherit
permissionMode: plan
---

You are an independent code reviewer.

Workflow:
1. Inspect the relevant diff and surrounding code.
2. Identify correctness, security, compatibility, and test risks.
3. Run only read-only inspection and test commands.
4. Do not edit files.

Return findings ordered by severity. For every finding include:
- File and line
- Evidence
- User impact
- Recommended fix
- Test that would catch the regression

If no findings are present, list what you reviewed and any unverified areas.
```

Only `name` and `description` are required, but an unrestricted default is usually too broad for a reviewer.

## 5.6 Claude frontmatter reference

| Field | Purpose |
|---|---|
| `name` | Required unique lowercase/hyphen identifier |
| `description` | Required routing guidance |
| `tools` | Allowlist of tools |
| `disallowedTools` | Tools removed from the inherited pool |
| `model` | `inherit`, alias, or supported full model ID |
| `permissionMode` | Agent permission behavior |
| `maxTurns` | Maximum agentic turns |
| `skills` | Skills preloaded in full at startup |
| `mcpServers` | Referenced or inline MCP servers for this agent |
| `hooks` | Agent-scoped lifecycle hooks |
| `memory` | Persistent `user`, `project`, or `local` agent memory |
| `background` | Prefer background execution |
| `effort` | Agent-specific effort level when supported |
| `isolation` | `worktree` for an isolated Git worktree |
| `color` | UI display color |
| `initialPrompt` | First turn when agent runs as the main session |

### Tool rules

- `tools` is an allowlist.
- `disallowedTools` removes tools from inherited or allowed capabilities.
- If both are present, denied tools remain unavailable.
- Omit edit tools for read-only roles.
- Omitting `Agent` prevents that role from spawning nested subagents.
- `AskUserQuestion` is not available to normal subagents; the parent should supply complete context.
- Background subagents receive a reduced built-in tool set, though supported MCP tools remain available.

### Permission modes

Current documented modes include:

- `default` or `manual`: normal permission checks
- `acceptEdits`: accept ordinary workspace edits
- `auto`: classifier reviews protected actions
- `dontAsk`: deny actions that would require a prompt
- `bypassPermissions`: skip ordinary prompts; high risk
- `plan`: read-only planning

Use `plan` or `dontAsk` for reviewers and analysts when practical. Avoid `bypassPermissions` unless an external sandbox makes the environment disposable and the scope is explicitly authorized.

## 5.7 Create a Claude agent

### Project agent

```bash
mkdir -p .claude/agents
$EDITOR .claude/agents/code-reviewer.md
```

Or ask Claude Code:

```text
Create a project-level code-reviewer subagent in .claude/agents/. Make it read-only, use the inherited model, review the current diff, cite files and lines, and return prioritized findings without editing.
```

### Personal/global agent

```bash
mkdir -p ~/.claude/agents
$EDITOR ~/.claude/agents/code-reviewer.md
```

### Session-only agent

Claude can accept JSON with `--agents` for temporary experiments:

```bash
claude --agents '{
  "quick-reviewer": {
    "description": "Read-only reviewer for a one-session experiment.",
    "prompt": "Inspect the requested changes and return evidence-backed findings only.",
    "tools": ["Read", "Grep", "Glob"],
    "model": "inherit"
  }
}'
```

Session JSON uses `prompt` where a file-based definition uses the Markdown body.

## 5.8 Discover and invoke Claude agents

Current Claude Code behavior:

- `/agents` lists/reminds you about available agents; recent versions removed the old interactive creation wizard.
- Name the role in natural language for ordinary delegation.
- Use the `@` agent picker to guarantee a particular role is invoked.
- Launch a whole session under a role with `claude --agent <name>`.
- Set a project default agent with `"agent": "name"` in `.claude/settings.json`.

Examples:

```text
Use the code-reviewer subagent to review the current branch against main.
```

```text
Run the gis-data-reviewer and test-runner in parallel. Wait for both, then combine their findings.
```

```bash
claude --agent code-reviewer
```

If the first `agents/` directory was created after the session started, restart Claude Code. Existing watched directories usually detect edits within a few seconds.

## 5.9 Models and cost

A subagent can inherit the main model or specify its own. Use:

- Faster/cheaper model for broad search, file inventory, or log reduction
- Stronger model for security review, architecture, ambiguous debugging, or integration decisions
- Inherited model when operational simplicity matters more than cost tuning

Do not send every task to the strongest model. Parallel workers multiply token usage.

## 5.10 Preload skills

```markdown
---
name: gis-etl-reviewer
description: Reviews geospatial ETL changes for data-integrity risks.
tools: Read, Grep, Glob, Bash
skills:
  - crs-forensics
  - geometry-validation
  - spatial-lineage
---
```

Preloading injects full skill content into the agent's startup context. Use it only for skills the role almost always needs. Otherwise let the agent discover skills when needed.

## 5.11 Scope MCP servers to one Claude agent

```markdown
---
name: browser-tester
description: Reproduces web UI failures and returns browser evidence.
tools: Read, Grep, Glob
mcpServers:
  - playwright
---

Reproduce the requested browser flow. Capture exact steps, console errors,
failed requests, and screenshots. Do not edit application files.
```

Agent-only MCP configuration reduces irrelevant tool descriptions in the parent context and limits access to the role that needs it.

Never embed credentials directly in the Markdown file.

## 5.12 Persistent agent memory

Claude supports agent memory scopes:

| Scope | Typical location | Use |
|---|---|---|
| `user` | `~/.claude/agent-memory/<agent>/` | Cross-project personal learning |
| `project` | `.claude/agent-memory/<agent>/` | Team-shareable project knowledge |
| `local` | `.claude/agent-memory-local/<agent>/` | Private project knowledge |

Use memory for durable patterns, not task status or raw logs. Review project memory before committing it. Never store credentials or production data.

## 5.13 Worktree isolation

For concurrent implementation roles:

```markdown
---
name: api-implementer
description: Implements isolated API tasks with tests.
tools: Read, Grep, Glob, Edit, Write, Bash
isolation: worktree
---
```

A temporary Git worktree reduces file collisions. It does not remove the need to:

- Assign non-overlapping ownership
- Review the resulting diff
- Reconcile branches deliberately
- Avoid force-pushes or destructive Git operations

## 5.14 Hooks for Claude subagents

Agent-scoped hook example:

```markdown
---
name: database-reader
description: Runs read-only database diagnostics.
tools: Bash
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate-readonly-query.sh"
---

Use read-only queries. Never modify rows, schemas, roles, or extensions.
```

Session/project hooks can also observe `SubagentStart` and `SubagentStop`.

Test hooks by attempting a known-disallowed operation in a disposable environment. A policy that has never been tested is only an assumption.

## 5.15 Background, resume, and nesting

- Current Claude versions run many subagents in the background by default.
- Foreground workers block the parent until completion.
- Background permission prompts surface in the main session.
- Completed custom/general-purpose agents can be resumed with their prior context.
- Built-in `Explore` and `Plan` are one-shot and are not resumable.
- Current documentation supports nested subagents with a configurable depth on newer versions.

The locally installed Claude `2.1.215` predates the newest documented nesting controls. Upgrade before relying on version-marked depth-limit behavior.

Use nesting sparingly. Deep agent trees are harder to observe, cost more, and can dilute the original acceptance criteria.

---

# 6. Claude Code agent teams

## 6.1 What agent teams add

Claude agent teams provide:

- One fixed team lead
- Multiple independent Claude Code sessions
- Shared task list with dependencies
- Direct teammate messaging
- User interaction with individual teammates
- In-process or split-pane display

Teams are experimental and disabled by default.

## 6.2 Enable agent teams

In `settings.json`:

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Or set the environment variable for one shell/session.

Do not enable experimental teams across an organization without testing cost, permissions, resume behavior, and cleanup.

## 6.3 Start a team

```text
Create an agent team for this change:
- Call one teammate mapper; it must map affected code and make no edits.
- Call one teammate implementer; it owns src/api/ only.
- Call one teammate verifier; it owns tests/ and independently validates behavior.
Require a plan before implementation. Wait for every teammate. Synthesize evidence and unresolved risks before reporting completion.
```

If Claude launches ordinary subagents instead, explicitly say “use an agent team, not subagents.”

## 6.4 Reuse subagent definitions as teammate roles

```text
Spawn a teammate using the security-reviewer agent type to audit the authentication module.
```

When a Claude subagent definition is reused as a teammate:

- Its role instructions are appended to the teammate's system instructions.
- Its `tools` and `model` apply.
- Team coordination tools remain available.
- Current documentation says `skills` and `mcpServers` fields from the subagent definition do not apply through this teammate path; the teammate loads normal project/user configuration instead.

## 6.5 Team architecture and state

Claude manages runtime team state under the user Claude directory, including:

```text
~/.claude/teams/<session-derived-team>/
~/.claude/tasks/<session-derived-team>/
```

Mailbox files and task state are runtime internals. Do not pre-author or hand-edit team configuration as if it were a reusable project manifest. Define reusable roles in agent files instead.

## 6.6 Team best practices

- Start with 3–5 teammates.
- Give each one separate files or separate review lenses.
- Require plan approval for risky implementation.
- Ask the lead to wait for all workers.
- Intervene if the lead starts doing a worker's assigned task.
- Use independent review rather than self-certification.
- Stop idle or drifting teammates.
- Expect materially higher token use.

## 6.7 Current limitations

The official documentation describes limitations including:

- Experimental behavior
- One team per session
- Fixed lead
- No nested teams
- In-process teammate resume limitations
- Possible task-status lag
- Slow shutdown while tools finish
- File conflicts if ownership is unclear
- Split panes requiring tmux or supported iTerm2 integration

Use ordinary subagents for focused tasks unless direct teammate communication adds real value.

---

# 7. Codex subagents and custom agents

## 7.1 How Codex multi-agent work operates

Codex can spawn specialized agents in parallel, keep their tool output out of the main thread, and combine their results.

Key terms:

- **Subagent workflow:** one request split across agents
- **Subagent:** delegated worker
- **Agent thread:** the inspectable thread where that worker operates

Current Codex documentation says delegation occurs when:

- You explicitly request subagents or parallel work
- Applicable `AGENTS.md` instructions request delegation
- An applicable skill instructs Codex to delegate

Do not assume Codex will parallelize silently. Ask directly when it matters.

## 7.2 Built-in Codex agents

Current documentation lists:

| Agent | Purpose |
|---|---|
| `default` | General fallback |
| `worker` | Implementation and fixes |
| `explorer` | Read-heavy codebase exploration |

A custom agent with the same name can override a built-in, so choose names deliberately.

## 7.3 Codex configuration scopes

| Location | Scope |
|---|---|
| `~/.codex/config.toml` | User/global configuration |
| `.codex/config.toml` | Project or nested project configuration; trusted projects only |
| `~/.codex/<profile>.config.toml` | Named user profile selected with `--profile` |
| `~/.codex/agents/*.toml` | Personal custom agents |
| `.codex/agents/*.toml` | Project custom agents |
| `~/.codex/AGENTS.md` | Global guidance |
| `AGENTS.md` / nested variants | Project guidance |
| `.agents/skills/` | Project skills |
| `~/.agents/skills/` | User/global skills |

Project `.codex/` configuration loads only for a trusted project.

## 7.4 Recommended Codex project structure

```text
my-project/
├── AGENTS.md
├── .codex/
│   ├── config.toml
│   ├── hooks.json
│   └── agents/
│       ├── code-mapper.toml
│       ├── feature-implementer.toml
│       ├── code-reviewer.toml
│       └── gis-data-reviewer.toml
├── .agents/
│   └── skills/
│       └── project-workflow/
│           └── SKILL.md
├── scripts/
└── src/
```

## 7.5 Global Codex multi-agent settings

Current documentation uses `[agents]` in `config.toml`:

```toml
[agents]
enabled = true
max_concurrent_threads_per_session = 6
default_subagent_reasoning_effort = "medium"
interrupt_message = true
```

Optional keys include:

| Field | Purpose |
|---|---|
| `enabled` | Enable or disable multi-agent tools |
| `max_concurrent_threads_per_session` | Concurrent spawned thread cap |
| `default_subagent_model` | Default worker model |
| `default_subagent_reasoning_effort` | Default worker effort |
| `interrupt_message` | Preserve a model-visible interruption record |

Older/current local configurations may expose related controls as:

```toml
[features]
multi_agent = true

[agents]
max_threads = 6
max_depth = 1
```

`max_threads` is documented as a legacy alias in newer material. Prefer the current schema after upgrading, but do not rewrite a working older config blindly.

## 7.6 Minimal standalone Codex custom agent

Create `.codex/agents/code-reviewer.toml`:

```toml
name = "code_reviewer"
description = "Read-only reviewer for correctness, security, regressions, and missing tests. Use after implementation."
sandbox_mode = "read-only"
model_reasoning_effort = "high"

developer_instructions = """
Act as an independent code reviewer.

Workflow:
1. Inspect the relevant diff and surrounding execution paths.
2. Identify correctness, security, compatibility, and test risks.
3. Do not modify files.
4. Return findings ordered by severity.

For each finding include the file, line, evidence, user impact, recommended fix,
and a test that proves the correction. If there are no findings, state what was
reviewed and what could not be verified.
"""
```

Current Codex custom-agent files require:

- `name`
- `description`
- `developer_instructions`

The file may also contain ordinary supported Codex configuration keys, including:

- `model`
- `model_reasoning_effort`
- `sandbox_mode`
- Approval or permission settings supported by that Codex version
- `mcp_servers`
- `skills.config`

The `name` field is the identity. Matching the filename is a convention, not the source of truth.

## 7.7 How Codex agent settings inherit

A custom agent file is a configuration layer for the spawned session.

For model and reasoning settings, current documentation describes a resolution order broadly equivalent to:

1. Explicit values supplied for the spawn
2. Agent-file values
3. `[agents]` defaults
4. Parent values or model defaults where applicable

Other omitted session settings, such as sandbox, MCP, and skill configuration, inherit from the parent/session configuration. Therefore, specify only deliberate differences, but set a read-only sandbox explicitly for read-only roles.

## 7.8 Create Codex agents

### Project agent

```bash
mkdir -p .codex/agents
$EDITOR .codex/agents/code-reviewer.toml
```

### Personal agent

```bash
mkdir -p ~/.codex/agents
$EDITOR ~/.codex/agents/code-reviewer.toml
```

### Older explicit role declaration pattern

The Codex configuration reference also supports role declarations with a separate config layer:

```toml
# .codex/config.toml
[agents.reviewer]
description = "Find correctness, security, and test risks."
config_file = "./agents/reviewer.toml"
```

Relative `config_file` paths resolve from the config file that declares the role. Prefer the current standalone-agent documentation for new installations, but recognize this form when maintaining an existing setup.

## 7.9 Invoke and inspect Codex agents

Prompt Codex explicitly:

```text
Review this branch with parallel subagents. Use code_mapper to trace affected paths, code_reviewer to identify risks, and test_runner to validate behavior. Wait for all three and return one deduplicated report with file references.
```

In the CLI:

- `/agent` or `/subagents` opens the thread picker.
- Select a thread to inspect or continue it.
- Ask Codex to steer, stop, resume, or close workers in natural language.

Codex's stable multi-agent tools include operations for spawning, sending input, resuming, waiting, and closing agent threads. Users normally orchestrate these through prompts and the UI rather than invoking internal tools manually.

## 7.10 Codex permissions and sandboxing

Subagents inherit the parent turn's sandbox and permission mode unless the custom agent deliberately overrides supported settings.

Safe defaults:

- Explorers and reviewers: `sandbox_mode = "read-only"`
- Implementers: workspace-limited writes
- Network: off unless required
- External systems: explicit MCP tool allowlists and approval modes
- Production or destructive systems: human approval remains mandatory

A subagent is not an approval authority. An agent's claim that “the user approved this” should not bypass the actual approval system.

## 7.11 Codex hooks for agents

Codex hooks can observe and control events including:

- `SubagentStart`
- `SubagentStop`
- `PreToolUse`
- `PostToolUse`
- `PermissionRequest`
- `Stop`

Hooks can be defined in `hooks.json` next to active configuration or inline under `[hooks]` in `config.toml`.

Use hooks for:

- Adding role-specific context at startup
- Enforcing command policy
- Capturing verification evidence
- Preventing premature completion
- Recording auditable lifecycle events

Do not treat a logging hook as a security boundary. Use sandbox and permission configuration for the boundary itself.

## 7.12 Codex guidance, skills, and agents

Use the layers separately:

- `AGENTS.md`: how this repository is built, tested, reviewed, and operated
- Custom agent TOML: how a specialized worker behaves
- Skill: detailed repeatable workflow and supporting scripts
- MCP: external tools and systems
- Hook: deterministic policy and lifecycle action

Example:

```text
AGENTS.md
  Repository-wide GIS data rules and test commands

.codex/agents/gis-data-reviewer.toml
  Read-only reviewer role and output contract

.agents/skills/crs-forensics/SKILL.md
  Detailed CRS diagnosis procedure

MCP server
  Read-only PostGIS metadata/query tools

Hook
  Reject non-SELECT SQL and secret-bearing output
```

---

# 8. Claude and Codex side-by-side

| Concern | Claude Code | Codex |
|---|---|---|
| Reusable custom agent format | Markdown + YAML frontmatter | TOML config file |
| User agent path | `~/.claude/agents/` | `~/.codex/agents/` |
| Project agent path | `.claude/agents/` | `.codex/agents/` |
| Required identity fields | `name`, `description` | `name`, `description`, `developer_instructions` |
| Instruction body | Markdown body | `developer_instructions` string |
| Project guidance | `CLAUDE.md` hierarchy | `AGENTS.md` hierarchy |
| Session-only definitions | `--agents` JSON | Config/CLI overrides; use disposable project/user file if needed |
| Built-in workers | Explore, Plan, general-purpose | default, worker, explorer |
| Manual thread navigation | Agent panel, tasks, @-mentions | `/agent` or `/subagents` |
| Run whole session as role | `claude --agent name` | Start with matching config/profile; custom agents are mainly spawned roles |
| Read-only boundary | Tool allowlist + `permissionMode` | `sandbox_mode = "read-only"` and permissions |
| Agent-only skills | `skills` frontmatter | `skills.config` in agent config layer |
| Agent-only MCP | `mcpServers` frontmatter | `mcp_servers` in agent config layer |
| Worktree field | `isolation: worktree` | Use Codex/app worktree support or separate Git worktrees operationally |
| Direct worker-to-worker team | Experimental agent teams | Orchestrated agent threads; not Claude's exact team model |
| Lifecycle hooks | Agent frontmatter and settings hooks | `hooks.json` or config hooks |
| Nested workers | Supported with depth controls, version-dependent | `agents.max_depth`, version-dependent |

## Translation example

### Claude

```markdown
---
name: gis-data-reviewer
description: Reviews geospatial data pipeline changes for CRS, geometry, schema, and lineage risks. Read-only.
tools: Read, Grep, Glob, Bash
model: inherit
permissionMode: plan
skills:
  - crs-forensics
  - geometry-validation
---

Review the changed GIS pipeline. Cite files, commands, and evidence. Do not edit.
Return prioritized findings, coverage gaps, and recommended tests.
```

### Codex

```toml
name = "gis_data_reviewer"
description = "Reviews geospatial pipeline changes for CRS, geometry, schema, and lineage risks. Read-only."
sandbox_mode = "read-only"
model_reasoning_effort = "high"

developer_instructions = """
Review the changed GIS pipeline. Cite files, commands, and evidence. Do not edit.
Return prioritized findings, coverage gaps, and recommended tests.
"""

# Enable only skills that exist in the actual installation.
# [[skills.config]]
# path = ".agents/skills/crs-forensics/SKILL.md"
# enabled = true
```

The semantics should match even though the syntax differs.

---

# 9. Three production-ready agent patterns

## 9.1 Explorer → implementer → reviewer

This is the safest default for medium-sized work.

1. Explorer maps files, architecture, risks, and tests. No writes.
2. Main agent decides the plan.
3. Implementer makes the smallest scoped change.
4. Reviewer independently examines the diff and tests.
5. Main agent resolves findings and verifies the final state.

Prompt:

```text
Use three phases:
1. Run the read-only explorer to map the affected code and return a proposed scope.
2. After reviewing that result, run the implementer on only the approved files.
3. Run the reviewer independently against the final diff.
Do not let the implementer review its own work. Report actual test output and unresolved risks.
```

## 9.2 Parallel review lenses

Use independent read-only agents for:

- Security
- Correctness/data integrity
- Performance
- Test coverage
- Documentation/API compatibility

Require the main agent to deduplicate and reconcile contradictions.

## 9.3 Competing debugging hypotheses

Ask workers to test distinct explanations rather than all pursuing the first plausible cause.

```text
Spawn three read-only investigators:
- One tests the data/schema hypothesis.
- One tests concurrency and lifecycle behavior.
- One tests environment and dependency differences.
Each must provide disconfirming evidence, not just supporting evidence. Wait for all three, then rank hypotheses and propose the smallest confirming experiment.
```

---

# 10. GIS-oriented agent starter set

## 10.1 GIS codebase explorer

Purpose:

- Find map initialization, layer configuration, spatial APIs, ETL jobs, schemas, and tests
- Identify CRS assumptions and data boundaries
- Never edit

Expected output:

- Architecture map
- File/symbol references
- Data flow
- Risk list
- Suggested implementation boundaries

## 10.2 CRS and geometry reviewer

Review for:

- Missing or incorrect CRS metadata
- Axis-order mistakes
- Silent reprojection
- Geometry validity loss
- Dimensionality loss: Z/M
- Precision and snapping changes
- Empty/null geometry handling
- Antimeridian or polar edge cases

## 10.3 Spatial database reviewer

Review for:

- Missing spatial indexes
- Non-sargable spatial predicates
- Accidental Cartesian joins
- SRID mismatches
- Geometry/geography confusion
- Transaction scope
- Locking and long-running edits
- Unsafe DDL or data modification

Default this role to read-only.

## 10.4 Web-map implementer

Own only a defined UI/module boundary. Require:

- Exact SDK/version verification
- Loading, empty, and error states
- Accessible controls
- Mobile behavior
- Layer cleanup and lifecycle handling
- Performance checks for large data
- Tests or reproducible manual verification

## 10.5 GIS acceptance verifier

Independently validate:

- Expected map extent and CRS
- Correct features and attributes
- Styling and legend behavior
- Popup/query behavior
- Export/download integrity
- No console errors
- Network request failures
- Representative large and malformed datasets

---

# 11. Writing effective orchestration prompts

A good orchestration prompt specifies six things.

## 11.1 Goal

> Add GeoParquet export while preserving geometry, CRS metadata, schema, and current API compatibility.

## 11.2 Roles

> Use a pipeline explorer, implementation worker, and independent data-integrity reviewer.

## 11.3 Partition

> Explorer is read-only. Implementer owns `src/export/` and related tests. Reviewer makes no edits.

## 11.4 Dependencies

> Wait for exploration before implementation. Wait for implementation before review.

## 11.5 Evidence

> Cite files and lines. Run targeted and full relevant tests. Compare output metadata and geometry counts.

## 11.6 Stop conditions

> Stop and ask if the public API must change, credentials are needed, production data would be modified, or test fixtures exceed the approved data scope.

## Complete example

```text
Add GeoParquet export without changing the existing API.

Use agents in three stages:
1. A read-only explorer maps the export pipeline, current schema contracts, CRS handling, and tests.
2. An implementer modifies only src/export/ and tests/export/. It must preserve CRS metadata, geometry type, Z values, null handling, and column order.
3. A separate read-only reviewer validates the diff and generated sample output.

Wait at each stage. Do not let agents edit the same files concurrently. Run targeted tests and the relevant full suite. Return actual commands, summarized output, remaining risks, and any assumptions. Stop before external uploads, production writes, destructive Git operations, or dependency upgrades outside the approved scope.
```

---

# 12. Security and approval model

## 12.1 Least privilege

Start every role with the smallest capability set:

- Read only by default
- Writes only inside the repository
- Network off unless necessary
- Database access read-only unless a specific edit is approved
- External connectors limited by tool allowlist
- No secret-file access

## 12.2 Separate authority from recommendation

Agents may recommend:

- Deploying
- Deleting data
- Changing schemas
- Sending messages
- Merging or pushing

Recommendation is not authorization. Preserve the real human approval channel for external or destructive effects.

## 12.3 Treat source content as untrusted

Agents read code, issues, web pages, documents, and logs. Those sources may contain instruction-like text. Do not let file content grant permissions, expose secrets, or redirect the task.

## 12.4 Secrets

Never store raw credentials in:

- Agent definitions
- `CLAUDE.md`
- `AGENTS.md`
- Skills
- Hooks committed to Git
- Agent memory
- Prompts or transcripts intended for sharing

Use environment-variable names, not values.

## 12.5 Parallel-write safety

Before parallel implementation:

- Confirm a clean or understood Git status
- Assign each agent exclusive files/directories
- Use worktrees where practical
- Prevent destructive Git commands
- Review every resulting diff
- Run integration tests after combining work

---

# 13. Testing an agent definition

## 13.1 Discovery test

Ask the product to list or use the role. Verify the exact definition and scope loaded.

## 13.2 Routing test

Give a representative task without naming the role. Does the main agent select it appropriately? If not, improve `description`.

## 13.3 Negative routing test

Give a nearby but inappropriate task. Confirm the agent is not selected.

## 13.4 Permission test

Ask the role to perform a disallowed write or network action in a disposable repository. Confirm the platform blocks it.

## 13.5 Output-contract test

Check that it returns:

- Evidence
- File references
- Severity or priority
- Verification status
- Coverage gaps
- No unsupported “done” claim

## 13.6 Context test

Ask the role which project instructions and skills it is using. Verify expected guidance is present and stale guidance is absent.

## 13.7 Cost and latency test

Run a representative task three times. Record:

- Time to first useful result
- Total duration
- Number of agents
- Token or usage impact
- Failure rate
- Human corrections required

An agent that costs more and needs more supervision than the main thread is not yet a useful abstraction.

---

# 14. Troubleshooting

## Agent not found

- Confirm the directory and extension.
- Confirm required fields.
- Confirm the project is trusted where required.
- Check for duplicate names.
- Restart after creating the first watched agent directory.
- Check the installed CLI version against the documentation.

## Wrong agent runs

- Make descriptions specific and mutually exclusive.
- Explicitly name or select the agent.
- Remove vague “use for everything” language.
- Check higher-precedence global or managed definitions.

## Agent can do too much

- Replace inherited tools with an allowlist.
- Use read-only permission/sandbox mode.
- Remove network/MCP access.
- Add deterministic hooks.
- Test a prohibited operation.

## Agent returns shallow results

- Supply exact scope and acceptance criteria.
- Ask for evidence and line references.
- Increase reasoning effort only for roles that need it.
- Give the agent the relevant skill.
- Resume the same worker rather than repeatedly starting from zero.

## Parallel agents conflict

- Stop concurrent edits.
- Revert or isolate conflicted work carefully.
- Assign file ownership.
- Use worktrees.
- Parallelize research/review instead of writes.

## Parent reports completion too early

Use explicit orchestration language:

```text
Wait for every requested agent to finish. Do not report completion until the final diff, tests, and independent review are verified.
```

## Current docs do not match the CLI

- Check `claude --version` or `codex --version`.
- Check feature flags.
- Read version annotations in vendor docs.
- Test with a disposable definition.
- Upgrade deliberately; do not overwrite working config without a backup.

---

# 15. Team governance and version control

## Commit project agents when

- The role encodes shared team workflow.
- Everyone should use the same checks.
- Paths and commands are repository-specific.
- Changes can be reviewed like code.

## Keep an agent personal when

- It reflects individual style.
- It contains private local paths.
- It is experimental.
- The team has not accepted its behavior.

## Review agent changes like code

A pull request modifying an agent can change:

- Tool access
- Network access
- Model cost
- Sandbox behavior
- MCP access
- Hooks
- Memory scope
- Automatic delegation

Require special review for changes that widen capabilities.

## Suggested ownership

```text
CODEOWNERS
.claude/agents/          @platform-team @security
.codex/agents/           @platform-team @security
.claude/settings.json    @platform-team @security
.codex/config.toml       @platform-team @security
```

## Agent changelog questions

- What task does this role improve?
- What permissions changed?
- What model/cost changed?
- What tests prove routing and restrictions?
- Does it overlap an existing role?
- Can the same behavior be a skill instead?

---

# 16. Recommended starter architecture

For most teams, start with four project roles:

1. `codebase-explorer` — read-only mapping
2. `feature-implementer` — scoped writes and tests
3. `code-reviewer` — independent read-only review
4. `test-runner` — noisy test execution and concise failure reporting

For GIS teams, add:

5. `gis-data-reviewer` — CRS, geometry, schema, and lineage integrity
6. `spatial-database-reviewer` — PostGIS/query/index/transaction risks
7. `web-map-verifier` — runtime UI, console, network, rendering, and accessibility evidence

Do not begin with 30 overlapping agents. Start with roles that have clear boundaries and measurable value.

---

# 17. Quick-start checklists

## Claude Code

- [ ] Upgrade if required by the desired documented feature.
- [ ] Create `.claude/agents/`.
- [ ] Add one Markdown file with `name` and `description`.
- [ ] Restrict tools and permission mode.
- [ ] Add explicit workflow and output contract.
- [ ] Restart if this is the first agent directory in the running session.
- [ ] Invoke the role explicitly.
- [ ] Test a prohibited action.
- [ ] Verify results and Git diff.
- [ ] Commit the definition after review.

## Codex

- [ ] Check `codex --version` and `codex features list`.
- [ ] Upgrade before relying on newer standalone-agent fields.
- [ ] Confirm `multi_agent` is enabled.
- [ ] Create `.codex/agents/`.
- [ ] Add one TOML file with `name`, `description`, and `developer_instructions`.
- [ ] Set `sandbox_mode = "read-only"` for reviewers/explorers.
- [ ] Request the agent explicitly.
- [ ] Inspect it with `/agent` or `/subagents`.
- [ ] Test a prohibited action.
- [ ] Verify results and Git diff.
- [ ] Commit the definition after review.

---

# 18. Official sources

Research checked 2026-07-31. Vendor documentation changes quickly; version annotations in the live pages override this note.

## Claude Code

- [Create custom subagents](https://code.claude.com/docs/en/sub-agents)
- [Agent teams](https://code.claude.com/docs/en/agent-teams)
- [Settings](https://code.claude.com/docs/en/settings)
- [Tools reference](https://code.claude.com/docs/en/tools-reference)
- [Permissions](https://code.claude.com/docs/en/permissions)
- [Hooks](https://code.claude.com/docs/en/hooks)
- [Skills](https://code.claude.com/docs/en/skills)
- [MCP](https://code.claude.com/docs/en/mcp)

## OpenAI Codex

- [Subagents](https://developers.openai.com/codex/subagents)
- [Subagent concepts](https://developers.openai.com/codex/concepts/subagents)
- [Configuration basics](https://developers.openai.com/codex/config-basic)
- [Configuration reference](https://developers.openai.com/codex/config-reference)
- [Sample configuration](https://developers.openai.com/codex/config-sample)
- [AGENTS.md guidance](https://developers.openai.com/codex/guides/agents-md)
- [CLI slash commands](https://developers.openai.com/codex/cli/slash-commands)
- [Hooks](https://developers.openai.com/codex/hooks)
- [Customization](https://developers.openai.com/codex/concepts/customization)

---

# 19. Final operating rule

> Use the main agent for intent and decisions. Use subagents for bounded noisy work. Use teams only for real coordination. Give every worker least privilege, exclusive scope, explicit evidence requirements, and an independent verification path.

A good multi-agent system is not the one with the most agents. It is the one that produces a more reliable result with less human cognitive load and a clear audit trail.
