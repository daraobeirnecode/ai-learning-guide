---
title: Master Learning Guide — Novice to AI Engineer and AI Services
type: master-learning-guide
status: claude-reviewed
authority: canonical
canonical_for: ai-engineering-and-ai-services-learning-curriculum
owner: Dara O'Beirne
created: 2026-08-26
updated: 2026-08-26
reviewed: 2026-08-26
review_record: Claude Code final rereview — PASS, no material findings; late source audits incorporated
review_cycle: quarterly
source_scope:
  - Knowledge Hub
  - Inish Labs
tags:
  - learning
  - ai-engineering
  - agents
  - automation
  - infrastructure
  - gis
  - ai-services
---

# Master Learning Guide — Novice to AI Engineer and AI Services

> [!abstract] Purpose
> This is the **single learning front door** for the technology, workflow, operations, security, GIS and commercial-service material documented across the Knowledge Hub and Inish Labs vaults. It starts with “what is an LLM?” and progresses to building, operating and selling bounded AI systems.
>
> It explains the mental models here and routes you to detailed notes. It does **not** replace live-state checks, product documentation, implementation runbooks or accountable professional review.

## Guide authority and scope

This public guide is authoritative for:

- the order in which to learn the material;
- the plain-English relationship between technologies;
- the canonical topic and workflow taxonomy;
- the preferred first links for deeper study;
- how to distinguish concepts, scaffolds, live systems, experiments and obsolete material.

Other notes remain authoritative for:

- **vault-wide navigation:** [Master Knowledge Map](../sources/knowledge-hub/01%20Home/Maps/Master%20Knowledge%20Map.md);
- **current local operations:** [Hermes Dashboard](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Hermes%20Dashboard.md) and product dashboards/runbooks;
- **detailed procedures:** linked build guides, runbooks and official documentation;
- **commercial catalogs:** the two 50-workflow guides and their supporting research;
- **customer work:** the signed scope, approved data boundary, acceptance criteria and professional reviewer.

### Included

- AI and LLM foundations;
- prompting, context, retrieval, memory and RAG;
- agents, harnesses, loop engineering and multi-agent orchestration;
- Claude, Claude Code, Codex and Hermes Agent;
- tools, skills, plugins, hooks, commands, subagents and MCP;
- APIs, OAuth, webhooks, browser automation and integrations;
- programming, Git, testing, software delivery and web applications;
- data engineering, SQL and database families;
- n8n and deterministic/AI-assisted/agentic workflows;
- Linux, Docker, networking, deployment, secrets and backups;
- observability, evaluation, security and operations;
- GIS, spatial AI and accountable review;
- service discovery, pilots, implementation, managed operations and commercialization.

### Excluded from the learning corpus

- private personal-life material unrelated to this technical curriculum;
- raw social captures when a synthesized guide exists;
- archived copies, backups and retired OpenClaw material except when explaining history;
- duplicate package READMEs when a package entry point or canonical guide exists;
- secret values, private keys, credential files and raw customer data.

## The one-sentence mental model

**A useful AI service combines a model that can reason over context, deterministic software and data systems that constrain what happens, tools that let the model act, loops that verify progress, infrastructure that keeps the system available, controls that protect people and data, and a commercial workflow tied to a measurable customer outcome.**

## How to use this guide

1. Read the chapter summary.
2. Learn the vocabulary and draw the system in your own words.
3. Complete the small practice exercise.
4. Open the linked vault notes only when you need depth.
5. Build one bounded artifact.
6. Verify it with tests, logs and a human reviewer.
7. Move on only when you can explain what failed and how you would recover.

### The four roles you grow through

| Role | Evidence of progress |
|---|---|
| **Student** | Can explain the concept and compare alternatives without jargon. |
| **Builder** | Produces a working artifact with tests and a readable diff or build record. |
| **Operator** | Can deploy, observe, secure, recover and control cost. |
| **Seller** | Connects the system to a buyer, bounded outcome, acceptance test and support model. |

Use this reusable evidence block after each module:

```md
## Learning Evidence
- Concept learned:
- Notes read:
- Build artifact:
- Verification result:
- Failure or blocker:
- Business use:
- Next step:
```

> [!tip] Do not confuse reading with competence
> “I understand it” means you can explain it simply, choose when to use it, build a small version, test it, identify its failure modes and operate it safely.

## Fast routes

| Question                                                  | Start here                                                                  |     |
| --------------------------------------------------------- | --------------------------------------------------------------------------- | --- |
| What is an LLM, token or embedding?                       | [1 — AI, machine learning and large language models](#chapter-1)                     |     |
| What is context engineering or RAG?                       | [2 — Prompting, context, retrieval and memory](#chapter-2)                           |     |
| What is an agent or agent loop?                           | [3 — Agents, harnesses and loop engineering](#chapter-3)                             |     |
| What are tools, skills, plugins, hooks and MCP?           | [4 — Extension vocabulary: tools, skills, plugins, hooks and MCP](#chapter-4)        |     |
| How do I learn programming and Git?                       | [5 — Software engineering foundations](#chapter-5)                                   |     |
| How should I use Claude Code?                             | [6 — Claude and Claude Code](#chapter-6)                                             |     |
| How should I use Codex?                                   | [7 — OpenAI Codex](#chapter-7)                                                       |     |
| How does Hermes Agent work?                               | [8 — Hermes Agent as a personal and operational agent system](#chapter-8)            |     |
| How do APIs, OAuth, webhooks and MCP connect systems?     | [9 — APIs, OAuth, webhooks, browser automation and MCP](#chapter-9)                  |     |
| Which database should I use?                              | [10 — Data systems and databases](#chapter-10)                                        |     |
| How do RAG, semantic search and knowledge systems differ? | [11 — RAG, semantic search and knowledge systems](#chapter-11)                        |     |
| What is n8n and how do workflows differ from agents?      | [12 — Workflow automation with n8n](#chapter-12)                                      |     |
| What workflow types exist in the vaults?                  | [13 — Master workflow-pattern taxonomy](#chapter-13)                                  |     |
| How do I deploy and operate systems?                      | [14 — Infrastructure and deployment](#chapter-14) and [17 — Production operations](#chapter-17) |     |
| How do I secure and evaluate AI?                          | [15 — Observability, evaluation and security](#chapter-15)                            |     |
| How do GIS and spatial AI fit?                            | [16 — GIS and spatial AI engineering](#chapter-16)                                    |     |
| How do I sell AI services?                                | [18 — Designing and selling AI services](#chapter-18)                                 |     |
| What should I build to prove mastery?                     | [19 — Capstone ladder](#chapter-19)                                                   |     |

## Maturity labels used throughout

| Label | Meaning | What you may claim |
|---|---|---|
| **Conceptual** | A mental model or educational note. | You understand an idea; no system claim. |
| **Documented scaffold** | Code, Compose, prompt, schema or plan exists locally. | A starting point exists; not deployed or proven. |
| **Installed but idle** | Software is installed or a server exists, but the application/workflow is inactive. | The prerequisite exists; not operational delivery. |
| **Verified live** | Runtime checks demonstrated the component or workflow operating. | Only the verified state and date. |
| **Experimental** | Prototype or incomplete implementation with known limits. | A test artifact exists; not production-ready. |
| **Planned/stubbed** | Design exists or functions return placeholders. | Future intent only. |
| **Obsolete/retired** | Superseded technology or archived operating model. | Historical learning only. |
| **Customer-specific** | Requires credentials, data mapping, acceptance criteria or professional review. | No reusable completion claim without customer validation. |

---

# Stage I — Foundations

<a id="chapter-0"></a>

## 0 — Computing foundations before AI

AI systems still run on ordinary computers. Learn these concepts first.

| Concept | Plain-English meaning | Why it matters |
|---|---|---|
| **Hardware** | CPU, memory, disk, GPU and network interfaces. | Sets capacity, speed and cost limits. |
| **Operating system** | Software that manages hardware, files, users and processes. | Claude Code, Codex, Hermes, Docker and servers all rely on OS behavior. |
| **File and directory** | Stored content and its location in a filesystem tree. | Configuration, code, skills and logs are files in specific paths. |
| **Process** | A running program with memory, permissions and an ID. | A service can be installed yet not running. |
| **Terminal** | Text interface for running commands. | The fastest way to inspect, build and operate systems reproducibly. |
| **Shell** | The command interpreter, such as zsh or bash. | Parses commands, variables, pipes and scripts. |
| **Program/code** | Instructions written for a computer. | Deterministic behavior belongs in code, not in hopeful prompting. |
| **Runtime** | The environment that executes code, such as Python or Node.js. | A file alone does nothing without the right runtime and dependencies. |
| **Dependency/package** | Reusable code installed from a package ecosystem. | Adds capability and supply-chain risk. |
| **Configuration** | Non-secret settings that change behavior. | Separates deployment choices from source code. |
| **Environment variable** | A value supplied to a process by its environment. | Common way to inject configuration and references to secrets. |
| **Secret** | Credential that grants access: password, API key, token or private key. | Must not enter prompts, Git, notes or logs. |
| **Server** | A program or machine providing a service to clients. | “The server exists” is different from “the application is deployed.” |
| **Client** | Software that requests a service. | Browser, CLI, MCP host and API caller are clients. |
| **Port** | Numbered network endpoint used by a service. | Listening does not by itself prove authentication or safety. |
| **Protocol** | Rules two systems use to communicate. | HTTP, SSH and MCP solve different communication problems. |
| **API** | A defined software interface for requesting data or actions. | Reliable integrations should use documented APIs where possible. |
| **JSON/YAML/TOML** | Structured text formats for data and configuration. | Common in tool schemas, APIs and agent configuration. |
| **Database** | System for storing and retrieving durable structured state. | The model is not the database. |
| **Container** | Packaged process and dependencies with isolation boundaries. | Makes deployments reproducible; it is not a full security boundary by default. |

### First practice

- Open a terminal.
- Print your working directory and list a safe project folder.
- Open a JSON file and explain its keys.
- Use a read-only HTTP request against a public API.
- Identify the difference between a file on disk, an installed program and a running process.

### Go deeper

- [Docker — Complete Practical Guide](../sources/knowledge-hub/03%20Learning/Technology/Docker/Docker%20-%20Complete%20Practical%20Guide.md)
- [LLM AI Automation Master Guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/General%20AI/LLM%20AI%20Automation%20Master%20Guide.md)
- [Backend-first workflow architecture guide](../sources/knowledge-hub/05%20AI%20Systems/Architecture/AI%20Stack/AI%20Automation%20Backend%20First%20Workflow%20Architecture%20Guide%20-%20Reddit%20r-AiAutomations%20-%202026-06-27.md)

<a id="chapter-1"></a>

## 1 — AI, machine learning and large language models

### The hierarchy

- **Artificial intelligence (AI):** broad category of systems performing tasks associated with human intelligence.
- **Machine learning (ML):** systems learn statistical patterns from data rather than receiving every rule explicitly.
- **Deep learning:** ML using large multi-layer neural networks.
- **Transformer:** neural-network architecture that processes relationships among tokens using attention.
- **Large language model (LLM):** a large transformer trained to predict tokens and then adapted to follow instructions, use tools and produce useful outputs.

### What an LLM actually does

An LLM receives tokens representing the current context and estimates a distribution over likely next tokens. Repeating that process creates a response. Training compresses patterns from vast datasets into model parameters; **inference** uses those learned parameters to generate an answer.

An LLM is powerful because language contains patterns of reasoning, code, structure and human activity. It is unreliable because plausible continuation is not the same as truth, authorization or successful execution.

### Essential vocabulary

| Term | Meaning |
|---|---|
| **Token** | A chunk of text or code processed by the model. Tokens are not exactly words. |
| **Parameter** | Learned numeric value inside the model. Parameter count is not a direct measure of fitness for every task. |
| **Training** | Adjusting parameters from examples. |
| **Fine-tuning** | Additional training to specialize behavior. |
| **Inference** | Running a trained model to produce output. |
| **Context window** | Maximum token budget the model can consider in one request. |
| **Prompt** | Instructions or input intentionally supplied to the model. |
| **System instruction** | High-priority operating context defining behavior and constraints. |
| **Temperature** | Sampling control affecting output variability; it does not create knowledge. |
| **Structured output** | Response constrained to a schema such as JSON. |
| **Hallucination** | Unsupported or fabricated output presented plausibly. |
| **Multimodal model** | Model that can process more than text, such as images or audio. |
| **Embedding** | Numeric vector representing semantic properties for similarity retrieval. |

### Four mental boundaries

1. **The model is not a source of current truth.** Retrieve or verify current facts.
2. **The model is not durable state.** Store state in files, databases or approved memory.
3. **The model is not authority.** A prompt or email cannot authorize a sensitive action.
4. **The model is not the whole product.** Reliable systems need data, tools, software, evaluation and operations.

### Practice

Explain to another beginner:

- why a model can write correct code and still invent an API;
- why increasing context can help yet also introduce noise;
- why a structured schema is useful;
- why a model output should be tested before it changes production.

### Go deeper

- [AI foundations](../sources/knowledge-hub/03%20Learning/AI%20Foundations/AI.md)
- [LLM AI Automation Master Guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/General%20AI/LLM%20AI%20Automation%20Master%20Guide.md)
- [AI Learning Index](../sources/knowledge-hub/03%20Learning/AI%20Learning/AI%20Learning%20Index.md)
- [AI Learning Stack Daily Curriculum](../sources/knowledge-hub/03%20Learning/AI%20Learning/AI%20Learning%20Stack%20Daily%20Curriculum.md)

<a id="chapter-2"></a>

## 2 — Prompting, context, retrieval and memory

### Prompt engineering versus context engineering

- **Prompt engineering** improves the explicit instructions, examples, format and constraints sent to a model.
- **Context engineering** designs the entire information environment: instructions, files, retrieved passages, tool schemas, prior messages, state summaries and available actions.
- **Harness engineering** designs the software loop that supplies context, calls tools, records state, handles failure and decides whether work is complete.

A good prompt cannot compensate for missing data, unsafe tools or an absent verification loop.

### The context stack

A typical agent turn combines:

1. system and organizational instructions;
2. user request;
3. project context files such as `CLAUDE.md` or `AGENTS.md`;
4. skill content loaded for the task;
5. conversation history or compressed summaries;
6. retrieved vault/database evidence;
7. tool descriptions and permissions;
8. tool results;
9. current plan and state.

### Retrieval without jargon

Retrieval means finding relevant evidence before generation. A basic RAG pipeline is:

`collect → clean → chunk → embed/index → retrieve → optionally rerank → compose context → generate → cite → evaluate`

Use lexical search for exact names and literals. Use semantic search for conceptually similar material. Use SQL for structured facts and filters. Use spatial queries for geographic relationships. A mature system combines methods rather than forcing every question through a vector database.

### Memory types

| Type | Use | Typical store |
|---|---|---|
| **Working context** | Current task and conversation. | Model context window. |
| **Session history** | What happened in prior turns. | Session database/log. |
| **Durable user preference** | Stable facts that affect future behavior. | Curated user memory. |
| **Procedural memory** | Reusable way to perform a task. | Skill. |
| **Project knowledge** | Architecture, decisions, runbooks and requirements. | Repository or Obsidian. |
| **Operational state** | Jobs, records, approvals and execution status. | Relational database or workflow system. |
| **Semantic index** | Retrieval over unstructured knowledge. | Vector index/database. |

### Practice

Take one question and answer it four ways: from model memory only, keyword search, semantic search and SQL/structured data. Compare accuracy, evidence and reproducibility.

### Go deeper

- [Context as input](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/context-as-input.md)
- [Retrieval without the jargon](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/retrieval-without-the-jargon.md)
- [Prompts as artifacts](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/prompts-as-artifacts.md)
- [Instructions as constraints](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/instructions-as-constraints.md)
- [Vector databases guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/Vector%20DBs/vector-databases-guide.md)
- [Agent Memory — Complete Management Guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/Agent%20Content/Agent%20Memory/Agent%20Memory%20%E2%80%94%20Complete%20Management%20Guide.md)
- [Hermes Obsidian semantic search setup](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Hermes%20Obsidian%20Semantic%20Search%20Setup%202026-05-02.md)

<a id="chapter-3"></a>

## 3 — Agents, harnesses and loop engineering

### What is an agent?

An agent is not merely an LLM with a personality. A practical agent combines:

- a model;
- instructions and context;
- tools with explicit schemas;
- a loop that observes, decides, acts and checks;
- state or memory;
- limits, permissions and stopping conditions;
- verification and human escalation.

The **agent harness** is the software surrounding the model. It owns the tool loop, context assembly, permissions, retries, timeouts, state transitions, observability and completion criteria.

### Workflow versus agent

| Deterministic workflow | Agentic workflow |
|---|---|
| Steps are mostly predefined. | The model chooses among actions at runtime. |
| Easy to test and audit. | Handles ambiguity and variable paths. |
| Best for repetitive, stable rules. | Best for research, diagnosis and open-ended reasoning. |
| Failure states can be enumerated. | Requires stronger limits and verification. |
| Example: validate CSV, write row, notify. | Example: inspect a repo, form hypotheses, run tests, repair. |

Use the **least-agentic system that solves the problem**.

### Loop engineering

Loop engineering is the design of repeated cycles that move from intent to verified completion.

1. **Prompt loop:** ask, inspect, revise.
2. **Tool loop:** observe → choose tool → execute → ingest result.
3. **Verification loop:** define evidence → run check → compare → repair.
4. **Orchestration loop:** decompose → delegate → aggregate → review.
5. **Operational loop:** monitor → detect change/failure → alert or remediate within policy.
6. **Learning loop:** capture stable lesson → update memory/skill → verify next reuse.

A good loop has:

- an explicit goal;
- observable state;
- bounded actions;
- a completion test;
- time/iteration/cost limits;
- failure handling;
- an escalation path;
- durable evidence.

A bad loop merely says “keep trying until done.”

### Multi-agent patterns

- **Parallel research:** independent workers investigate different sources.
- **Planner/implementer/reviewer:** separate reasoning roles reduce self-confirmation.
- **Specialist routing:** select an agent/profile based on domain.
- **Map/reduce:** process items independently, then synthesize.
- **Supervisor/worker:** supervisor assigns bounded tasks and checks outputs.

Multi-agent systems add coordination cost. Use them when tasks are separable, context would otherwise overflow or independent review matters.

### Graph engineering

Graph engineering makes the loop's states, transitions, retries and stop conditions explicit. A graph may be implemented in ordinary code, a state-machine library, LangGraph, n8n or a durable workflow engine such as Temporal. Use a graph when branching, resumability or long-running state matters; do not add a framework to a simple loop merely to make it look advanced.

### Practice

Draw one workflow as both a deterministic DAG and an agent loop. Mark:

- what can be predefined;
- what requires judgment;
- what tools can write;
- what evidence proves success;
- where a human must approve.

### Go deeper

- [The agent loop](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/the-agent-loop.md)
- [Feedback loops](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/feedback-loops.md)
- [Planning versus execution](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/planning-vs-execution.md)
- [Agents Master Document](../sources/knowledge-hub/05%20AI%20Systems/Agents/Agents%20Master%20Document.md)
- [Anatomy of an agent harness](../sources/knowledge-hub/03%20Learning/AI%20Learning/Agent%20Content/Agentic%20methods/Agentic%20Methods%20-%20Anatomy%20of%20an%20Agent%20Harness.md)
- [Agent Engineering Methods Lab](../sources/knowledge-hub/03%20Learning/AI%20Learning/Agent%20Engineering%20Methods%20Lab/README.md)
- [Applied Loop Engineering method](../sources/knowledge-hub/03%20Learning/AI%20Learning/Agent%20Engineering%20Methods%20Lab/methods/04_loop_engineering/CONTEXT.md)
- [Prompt, harness, loop and graph engineering guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/Engineering%20Agents/Prompt%2C%20Harness%2C%20Loop%2C%20and%20Graph%20Engineering%20for%20AI%20Agents%20%E2%80%94%20GIS%20Implementation%20Guide.md)
- [From prompting agents to loop engineering](../sources/knowledge-hub/03%20Learning/AI%20Learning/Agent%20Content/Agents/X%20Posts/From%20Prompting%20Agents%20to%20Loop%20Engineering%20-%20Omar%20X%20Article.md)
- [AI agent skills explained simply](../sources/knowledge-hub/03%20Learning/AI%20Learning/Agent%20Content/Agents/Articles/AI%20Agent%20Skills%20Explained%20Simply.md)

<a id="chapter-4"></a>

## 4 — Extension vocabulary: tools, skills, plugins, hooks and MCP

These concepts are related but not interchangeable.

| Concept | What it is | Use it when |
|---|---|---|
| **Instruction/context file** | Persistent guidance loaded into a session or project. | The agent must consistently understand conventions and boundaries. |
| **Tool** | Callable function with a schema and handler. | The model must read, calculate, search or act. |
| **Skill** | Reusable procedural knowledge, usually a `SKILL.md` plus optional supporting files. | A recurring task benefits from a proven workflow. |
| **Command/prompt** | User-invoked reusable interaction entry point. | A human wants a repeatable named action. |
| **Plugin** | Packaged software extension that may add tools, commands, hooks, skills or integrations. | Capability requires executable code or distribution as a package. |
| **Hook** | Deterministic callback triggered by a lifecycle event. | A check or side effect must happen reliably at a known event. |
| **MCP server** | External program exposing tools, resources or prompts through Model Context Protocol. | Multiple compatible clients need a standard connection to external capability. |
| **Subagent** | Isolated worker given a bounded task and context. | Work can be parallelized or independently reviewed. |
| **Memory** | Persisted facts or history that survive the current context. | Stable preferences, prior sessions or state must be recalled. |
| **Cron/job** | Scheduled execution defined outside conversational prompting. | Work must run at a known time or interval. |
| **Workflow** | Connected sequence of triggers, transformations, decisions and actions. | A repeatable business or technical process needs state and auditability. |

### Comparison across Claude Code, Codex and Hermes

| Need | Claude Code | Codex | Hermes Agent |
|---|---|---|---|
| Project instructions | `CLAUDE.md` | `AGENTS.md` | `AGENTS.md`, `CLAUDE.md`, project context plus profile `SOUL.md` |
| Personal skill | `~/.claude/skills/<name>/SKILL.md` | `~/.agents/skills/<name>/SKILL.md` | Current profile’s `skills/<name>/SKILL.md` |
| Project skill | `.claude/skills/<name>/SKILL.md` | `.agents/skills/<name>/SKILL.md` | Project context or project-local skill/plugin when deliberately enabled |
| Packaged extension | Plugin/marketplace | Plugin or integration package | Python plugin with `plugin.yaml`; opt-in for third-party code |
| Deterministic lifecycle action | Hook | Hook/configured automation | Plugin hook registered by code |
| External standard tools | MCP server | MCP server | Native MCP client/server support |
| Parallel specialist | Subagent/agent definition | Subagent | Delegated subagent or separate profile/bot |
| Durable personal agent state | Limited project/user config | Limited project/user config | Profile config, memory, sessions, skills, cron and gateway state |

> [!warning] Supply-chain boundary
> A skill's body is instructions the agent will follow and may bundle scripts the agent will execute; a plugin or MCP server always runs code. Treat all three as supply-chain decisions: read the full contents—including bundled scripts—before installing a third-party skill, plugin or MCP server; pin immutable versions where supported; grant least privilege; expose only needed tools; and never assume a marketplace or installer listing is an authorization decision.

### How to design a good skill

A skill should contain:

1. a narrow trigger description;
2. prerequisites and required inputs;
3. numbered steps;
4. exact tool/command examples where stable;
5. pitfalls and safety boundaries;
6. verification criteria;
7. linked scripts/templates only when they improve reuse.

A skill should **not** contain secrets, temporary task progress, stale runtime status or a giant dump of general knowledge.

### Installing a Claude Code skill

**Manual personal install**

```text
~/.claude/skills/my-skill/SKILL.md
```

**Project-scoped install**

```text
project-root/.claude/skills/my-skill/SKILL.md
```

A distributable skill may arrive inside a Claude Code plugin. Review the package and marketplace source before installation, then use Claude Code’s current plugin commands. Start a new session and verify the skill appears before relying on it.

Official references: [Claude Code skills](https://code.claude.com/docs/en/skills), [plugins](https://code.claude.com/docs/en/plugins), [hooks](https://code.claude.com/docs/en/hooks-guide), [MCP](https://code.claude.com/docs/en/mcp).

### Installing a Codex skill

**Personal scope**

```text
~/.agents/skills/my-skill/SKILL.md
```

**Repository scope**

```text
project-root/.agents/skills/my-skill/SKILL.md
```

Codex can also use the built-in skill installer for catalog or repository skills. Installer-fetched skills are third-party content: inspect the installed files, including bundled scripts, before first use. After installation, restart if necessary and inspect the available skill list before invoking it. Use `$skill-name` when explicitly selecting a skill.

Official references: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [customization](https://learn.chatgpt.com/docs/customization/overview), [`AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [basic configuration](https://learn.chatgpt.com/docs/config-file/config-basic).

### Installing a Hermes skill or plugin

Hermes skills are profile-scoped. Use the interactive catalog for community/bundled installation:

```bash
hermes skills
```

The agent can inspect or maintain skills through its skill tools. For a named profile, ensure you are operating that profile—not another profile’s directory.

Hermes plugins are executable Python extensions. A user plugin normally lives under:

```text
~/.hermes/plugins/my-plugin/
  plugin.yaml
  __init__.py
```

Third-party general plugins are opt-in; install, inspect, then explicitly enable only trusted code. A plugin may register tools, hooks, commands and namespaced skills.

Official references: [Hermes documentation](https://hermes-agent.nousresearch.com/docs/), [plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins), [MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp).

### Decision tree

- Need only durable guidance? **Instruction file.**
- Need a repeatable procedure the agent can learn? **Skill.**
- Need to call an existing external system? **Native tool/API or MCP.**
- Need deterministic enforcement at an event? **Hook.**
- Need executable packaged capability? **Plugin.**
- Need a scheduled repeat? **Cron or workflow orchestrator.**
- Need a separate reasoning worker? **Subagent.**
- Need a repeatable multi-step business process? **Workflow.**

### Practice

Create one read-only skill that summarizes a repository’s architecture and requires a link check. Do not build a plugin until instructions alone are insufficient.

### Go deeper

- [Hooks](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/hooks.md)
- [Tool use and MCP](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/tool-use-and-mcp.md)
- [Claude Code agents, MCP, commands and skills](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/03%20Agents%2C%20MCP%2C%20Commands%20%26%20Skills.md)
- [Claude Code starter skills](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/04%20The%2020%20Starter%20Skills.md)
- [Codex agents, MCP, commands and prompts](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/03%20Agents%2C%20MCP%2C%20Commands%20%26%20Prompts.md)
- [Configure a new Hermes agent safely](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Runbooks/Configure%20a%20New%20Hermes%20Agent%20From%20Scratch%20-%20No%20Private%20Profile%20Access%20or%20Secret%20File%20Editing.md)

---

# Stage II — AI engineering tools

<a id="chapter-5"></a>

## 5 — Software engineering foundations

### Learn the delivery loop

`understand → plan → isolate → implement → test → inspect diff → review → release → observe → improve`

AI can accelerate every step, but it does not remove the need for the steps.

### Core skills

| Skill | Why it matters |
|---|---|
| **Shell** | Reproducible inspection and automation. |
| **Git** | History, diff, branches and rollback. |
| **GitHub** | Collaboration, reviews, issues and CI—not the same as Git. |
| **Python** | Strong general-purpose language for AI, data, automation and GIS. |
| **JavaScript/TypeScript** | Web applications, Node.js integrations and n8n expressions. |
| **SQL** | Structured data querying and durable state. |
| **HTTP/API design** | Communication among services. |
| **Testing** | Evidence that behavior matches requirements. |
| **Debugging** | Form a hypothesis, gather evidence and isolate cause. |
| **Package management** | Reproducible dependencies and supply-chain control. |
| **Code review** | Detect defects, risk and unnecessary complexity before release. |
| **Documentation** | Preserve architecture, decisions, runbooks and recovery paths. |

### Git mental model

- **Working tree:** files currently on disk.
- **Staging area:** changes selected for the next commit.
- **Commit:** immutable snapshot plus message.
- **Branch:** movable name pointing to a commit line.
- **Remote:** another Git repository, often GitHub.
- **Pull request:** proposed change and review conversation.
- **Worktree:** isolated working directory for another branch.

Never equate “file saved” with “committed,” “committed” with “pushed,” or “pushed” with “deployed.”

### Testing pyramid for AI systems

- **Static checks:** syntax, types, schema, lint, secret scan.
- **Unit tests:** small deterministic functions.
- **Integration tests:** database/API/tool boundaries.
- **Contract tests:** inputs and outputs between systems.
- **Evaluation sets:** representative AI tasks with expected criteria.
- **End-to-end tests:** full user workflow.
- **Operational smoke checks:** health, permissions, logs and rollback.
- **Human acceptance:** accountable user confirms utility and limits.

### Web application anatomy

A typical AI-enabled web application is `browser/UI → frontend → API/backend → queue or worker → database/object store → model or agent tools`. Authentication identifies the user; authorization limits data and actions; the backend owns validation and durable state; long-running AI work belongs in jobs/workers rather than one fragile browser request. Treat UI polish, API correctness, data security and operational recovery as separate quality dimensions.

### Practice

Build a small CLI that reads a JSON file, validates it and writes a report. Put it in Git, add tests, use a branch, inspect the diff and write a recovery note.

### Go deeper

- [Planning versus execution](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/planning-vs-execution.md)
- [Trust and sandboxing](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/trust-and-sandboxing.md)
- [Claude Code, Obsidian and GitHub guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/ClaudeCode-Obsidian-GitHub-Guide.md)
- [Docker — Complete Practical Guide](../sources/knowledge-hub/03%20Learning/Technology/Docker/Docker%20-%20Complete%20Practical%20Guide.md)
- [Website and webmap generation procedures](../sources/knowledge-hub/06%20SOPs/Website%20and%20Webmap%20Generation%20Procedures.md)
- [Web-app development capability runbook](../sources/knowledge-hub/05%20AI%20Systems/GIS%20Agent%20Build/runbooks/R08-web-app-dev-capability.md)

<a id="chapter-6"></a>

## 6 — Claude and Claude Code

### What they are

- **Claude** is Anthropic’s model/product family.
- **Claude Code** is an agentic coding environment that can inspect projects, edit files, run commands, use MCP servers, load skills, delegate to subagents and follow project instructions.

Use Claude Code for repository-level engineering, architecture exploration, debugging, tests and bounded implementation. It is not a deployment authorization channel.

### Installation and verification

Installation methods change. Use the current [official overview](https://code.claude.com/docs/en/overview), then verify:

```bash
claude --version
claude doctor
```

Run Claude Code from the intended project root. Check Git status before edits.

### Project anatomy

| Surface | Purpose |
|---|---|
| `CLAUDE.md` | Repository/project instructions and conventions. |
| `.claude/settings.json` | Project settings and permissions where configured. |
| `.claude/skills/` | Project-specific procedural skills. |
| personal `~/.claude/skills/` | User-level procedural skills. |
| hooks | Deterministic lifecycle automation. |
| MCP servers | External tools/resources. |
| subagents | Bounded specialist workers. |
| plugins | Packaged commands, hooks, agents, skills or integrations. |

### Safe operating pattern

1. Open the correct repository.
2. Inspect `CLAUDE.md`, architecture and Git state.
3. Ask Claude to explain before editing.
4. Write a plan with files, tests and risks.
5. Use a branch or isolated worktree.
6. Implement the smallest coherent change.
7. Run real tests and inspect the diff.
8. Use an independent review for material changes.
9. Commit/push/deploy only within explicit approval.

### Good uses

- trace how a feature works across files;
- write or repair tests;
- refactor with behavior-preserving checks;
- create migration plans;
- generate bounded documentation from code;
- review architecture and security assumptions;
- build a project-specific skill after a workflow proves reusable.

### Common failure modes

- starting in the wrong directory;
- treating `CLAUDE.md` as a security sandbox;
- accepting a broad diff without reading it;
- letting generated tests confirm generated behavior rather than requirements;
- using plugins or MCP servers without supply-chain review;
- running unrestricted modes in sensitive repositories;
- claiming success without test output.

### Practice

Use Claude Code read-only to explain a small repository. Ask for a plan, then implement one test-covered change in an isolated branch. Have another agent review the diff.

### Go deeper

- [Claude Code map](../sources/knowledge-hub/01%20Home/Maps/Claude%20Code.md)
- [Claude Code Mastery Path](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/00%20START%20HERE%20%E2%80%94%20Claude%20Code%20Mastery%20Path.md)
- [Claude Code key concepts](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/01%20Key%20Concepts%20%26%20Definitions.md)
- [Claude Code setup and best practices](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/02%20Setup%20%26%20Best%20Practices.md)
- [Claude Code agents, MCP, commands and skills](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/03%20Agents%2C%20MCP%2C%20Commands%20%26%20Skills.md)
- [Claude Code tutorials](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/05%20Ten%20Tutorials.md)
- [Claude Code master guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/claude-code-master-guide.md)

<a id="chapter-7"></a>

## 7 — OpenAI Codex

### What it is

Codex is OpenAI’s coding-agent environment for local and cloud software tasks. It can inspect repositories, edit code, run commands under configured approval/sandbox controls, load instruction files and skills, connect to MCP, and support review/delegation patterns.

### Installation and verification

Use the current [Codex CLI documentation](https://learn.chatgpt.com/docs/codex/cli). Verify the installed client and authentication before depending on it:

```bash
codex --version
codex login status
```

### Project anatomy

| Surface | Purpose |
|---|---|
| `AGENTS.md` | Durable repository instructions, including nested scope. |
| `~/.codex/config.toml` | User configuration, models, approvals and integrations. |
| `.agents/skills/` | Repository-scoped skills. |
| `~/.agents/skills/` | User-scoped skills. |
| MCP configuration | External tool connections. |
| sandbox/approval policy | Limits what commands/files/network actions occur automatically. |
| plugins/hooks/subagents | Packaged capability, deterministic automation and delegated work where configured. |

### Safe operating pattern

- inspect Git state and instructions first;
- use a bounded prompt with explicit deliverables and tests;
- isolate substantial work in a worktree;
- prefer read-only review before edit mode;
- never use unrestricted “yolo” modes for safety-sensitive repositories;
- use `--full-auto` only when the repository and worktree are safely bounded;
- use a PTY for interactive authentication or CLIs that require one;
- request patch-only output on restricted hosts when sandbox behavior is unreliable;
- validate and inspect every patch before application.

### Claude Code versus Codex

They overlap. Choose based on task, model/tool quality, authentication, project conventions and the value of independent review. A strong pattern is one agent implements and the other reviews, but only if both are safely isolated and the review is actually independent.

### Practice

Use Codex to review the change from the Claude Code exercise without editing it. Require findings with file/line evidence and tests. Then reverse roles on another small change.

### Go deeper

- [Codex Mastery Path](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/00%20START%20HERE%20%E2%80%94%20Codex%20Mastery%20Path.md)
- [Codex key concepts](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/01%20Key%20Concepts%20%26%20Definitions.md)
- [Codex setup and best practices](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/02%20Setup%20%26%20Best%20Practices.md)
- [Codex agents, MCP, commands and prompts](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/03%20Agents%2C%20MCP%2C%20Commands%20%26%20Prompts.md)
- [Codex starter prompts and skills](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/04%20The%2020%20Starter%20Prompts%20%26%20Skills.md)
- [Codex tutorials](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/05%20Ten%20Tutorials.md)
- [Claude Code and Codex agents implementation guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/Claude%20Code%20and%20Codex%20Agents%20-%20Full%20Implementation%20Guide.md)

<a id="chapter-8"></a>

## 8 — Hermes Agent as a personal and operational agent system

### What Hermes adds

Hermes is a persistent agent system around a model. Beyond coding, it combines:

- profiles and identity;
- conversation sessions;
- memory and procedural skills;
- built-in tools and MCP tools;
- plugins and hooks;
- scheduled jobs;
- messaging gateways such as Telegram;
- delegation and parallel tool execution;
- terminal backends and sandboxes;
- web, browser, media and integration surfaces.

### Installation and initial setup

Current command-line installation for macOS/Linux/WSL is documented by Nous:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o /tmp/hermes-install.sh
less /tmp/hermes-install.sh
bash /tmp/hermes-install.sh
hermes setup --portal
```

Always verify the current [official documentation](https://hermes-agent.nousresearch.com/docs/) before installation or upgrades.

### Configuration anatomy

| Item | Role |
|---|---|
| `config.yaml` | Non-secret settings: models, terminal, tools, gateway, memory, plugins and limits. |
| `.env` | Secrets and environment values; never print or commit it. |
| `auth.json` | OAuth credentials; never print or copy casually. |
| `SOUL.md` | Primary identity, tone and operating doctrine. |
| `USER.md` | Compact stable facts about the user. |
| `MEMORY.md` | Compact stable environment/integration facts. |
| `skills/` | Reusable procedures. |
| `plugins/` | Executable extensions. |
| `cron/` | Scheduled jobs and outputs. |
| session/state database | Conversation history, current state and routing. |
| logs | Diagnostics; still treat as potentially sensitive. |

Use supported commands instead of hand-editing when available:

```bash
hermes auth
hermes config
hermes config get <key>
hermes config set <key> <value>
hermes config check
hermes doctor
```

### Profiles, workspaces and sandboxes are different

- A **profile** isolates Hermes config, memory, skills, sessions, cron and gateway state.
- A **workspace** is the project directory where tools start.
- A **sandbox/backend** limits or relocates command execution.

A profile is not a filesystem security boundary. Two processes must not write the same profile. Cross-profile edits require deliberate targeting.

### Memory doctrine

Put:

- stable preferences in user memory;
- stable environment facts in agent memory;
- reusable procedures in skills;
- current project truth in project files;
- task progress in sessions/tasks;
- long-form knowledge in Obsidian;
- durable business state in databases.

Do not put secrets, raw logs, temporary progress or large procedures in memory.

### Hermes tools, skills, plugins and MCP

- Built-in tools provide core actions.
- Skills teach the agent how to perform recurring work.
- Plugins add executable capabilities and hooks.
- MCP connects external tool servers.
- Toolsets limit which capability categories a task receives.
- Delegation isolates parallel reasoning tasks.

Keep the tool surface small. A model should not see destructive tools it does not need.

### Gateways and cron

A gateway lets a profile receive and send platform messages. Cron runs in fresh sessions, so prompts must be self-contained. Read-only briefs, silent watchdogs and bounded maintenance are safer than autonomous external writes.

### Applying maturity labels in your own environment

Before acting, verify live state and record the date. Do not infer deployment from architecture notes, Compose files or plans.

### Practice

In a non-production profile, inspect the profile path, config structure, available tools and skills. Run a read-only research task, locate its session history and explain which state is profile-scoped.

### Go deeper

- [Hermes Dashboard](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Hermes%20Dashboard.md)
- [Stable primary-agent configuration recap](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Hermes%20Primary%20Agent%20Configuration%20Recap%20-%20Stable%20Personal%20Assistant%20Setup.md)
- [Configure a new Hermes agent safely](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Runbooks/Configure%20a%20New%20Hermes%20Agent%20From%20Scratch%20-%20No%20Private%20Profile%20Access%20or%20Secret%20File%20Editing.md)
- [Expert Hermes setup and maintenance](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Runbooks/Expert%20Guide%20-%20Setting%20Up%20and%20Maintaining%20Hermes%20Agents%20for%20Operator%20and%20Clients.md)
- [Hermes Memory Backbone](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Memory%20Backbone/Hermes%20Memory%20Backbone.md)
- [Agent Stack Map](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Memory%20Backbone/Agent%20Stack%20Map.md)
- [Personal Assistant OS](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Personal%20Assistant%20OS/Personal%20Assistant%20OS.md)
- [Official Hermes configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
- [Official Hermes profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)

<a id="chapter-9"></a>

## 9 — APIs, OAuth, webhooks, browser automation and MCP

### Integration hierarchy

Prefer the most stable and least privileged interface:

1. documented read-only API;
2. scoped authenticated API;
3. approved MCP server exposing a narrow tool set;
4. webhook/event integration;
5. browser automation when no reliable API exists;
6. manual human step for sensitive or ambiguous actions.

### HTTP basics

- **GET:** retrieve data.
- **POST:** create or invoke.
- **PUT/PATCH:** replace or update.
- **DELETE:** delete.
- **Status codes:** communicate success or error class.
- **Headers:** metadata and authentication.
- **Body:** request/response data, often JSON.
- **Pagination:** split large collections into pages.
- **Rate limit:** maximum request frequency.
- **Idempotency key:** prevents duplicate effects during retries.

### Authentication versus authorization

- **Authentication:** who are you?
- **Authorization:** what may you do?
- **OAuth:** delegated authorization without giving an app your password.
- **API key:** secret identifying a client; scope it and rotate it.
- **Webhook signature:** proof an incoming event came from the expected sender.

External content can inform the agent but cannot authorize an action. An email asking an agent to reveal a secret remains untrusted input.

### MCP architecture

MCP uses a host/client/server model. Servers expose:

- **tools:** executable actions;
- **resources:** retrievable context;
- **prompts:** reusable interaction templates.

Local servers commonly use standard input/output; remote servers commonly use streamable HTTP. The protocol standardizes connection and discovery, not business policy. You still need tool filtering, authentication, data controls and approval boundaries.

Official reference: [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture).

### Practice

Connect to one read-only public API. Log status, latency and response schema. Then design—but do not activate—a webhook with signature verification and idempotency.

### Go deeper

- [Tool use and MCP](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/tool-use-and-mcp.md)
- [Trust and sandboxing](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/trust-and-sandboxing.md)
- [Claude Code MCP and tools](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/03%20Agents%2C%20MCP%2C%20Commands%20%26%20Skills.md)
- [Codex MCP and tools](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/03%20Agents%2C%20MCP%2C%20Commands%20%26%20Prompts.md)

---

# Stage III — Data, workflows and infrastructure

<a id="chapter-10"></a>

## 10 — Data systems and databases

### The model is not the database

Use the model for language and bounded reasoning. Use data systems for durable, queryable, governed state.

### Database families

| System | Mental model | Best for | Common mistake |
|---|---|---|---|
| **Files/CSV/JSON** | Documents or tabular exports. | Small interchange, artifacts and snapshots. | Treating concurrent files as a transactional database. |
| **SQLite** | Relational database in one file. | Local apps, prototypes, embedded state. | Assuming it behaves like a multi-user server at scale. |
| **DuckDB** | In-process analytical SQL engine. | Fast local analysis of files and columnar data. | Using it as an online transactional system. |
| **PostgreSQL** | General-purpose relational server. | Durable multi-user transactional data and SQL. | Skipping schemas, constraints, indexes and backups. |
| **PostGIS** | Spatial extension for PostgreSQL. | Geometry/geography storage and spatial queries. | Ignoring coordinate systems and geometry validity. |
| **pgvector** | Vector type/index extension for PostgreSQL. | Embedding search alongside relational data. | Using similarity as proof of truth. |
| **Redis** | In-memory key/value and data-structure store. | Cache, queue, short-lived coordination and rate limits. | Treating a cache as the only durable record. |
| **Vector database** | Similarity search over embeddings. | Large semantic retrieval workloads. | Storing authority/provenance only in vectors. |
| **Graph database/AGE** | Nodes, edges and relationship traversal. | Connected entities and relationship-heavy queries. | Adding graph complexity to simple relational data. |
| **Object storage/B2/S3** | Durable blobs addressed as objects. | Documents, media, backups and large artifacts. | Confusing object metadata with application records. |
| **Search engine** | Inverted index and ranking. | Full-text search, filtering and logs. | Replacing transactional state with a search index. |

### SQL essentials

Learn:

- table, row, column and data type;
- primary and foreign keys;
- `SELECT`, `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`;
- insert/update/delete;
- constraints and transactions;
- indexes and query plans;
- roles and permissions;
- migrations;
- backup and restore.

### How the data layer fits together

A private AI service may use:

- PostgreSQL for customers, cases, approvals and workflow state;
- pgvector for retrieved text chunks;
- object storage for original documents;
- Redis for queues or transient coordination;
- Langfuse for AI traces;
- n8n for orchestration;
- the model only for bounded language/reasoning steps.

A GIS service may add PostGIS for geometry, a tile server for approved map layers and spatial functions for proximity/intersection analysis.

### Non-negotiable data concepts

- **Schema:** defined structure and types.
- **Provenance:** where a value came from.
- **Validation:** whether input satisfies constraints.
- **Transaction:** all-or-nothing group of changes.
- **Idempotency:** retries do not duplicate effects.
- **Migration:** versioned change to schema/data.
- **Least privilege:** each service gets only required access.
- **Tenant isolation:** unrelated customers do not share access accidentally.
- **Backup/restore:** a backup is unproven until restoration is tested.
- **Retention:** keep data only as long as required.

### Practice

Create a local database with customers, source documents and workflow runs. Add keys and constraints. Write a query joining the three tables. Back it up and restore to a separate test database.

### Go deeper

- [Vector databases guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/Vector%20DBs/vector-databases-guide.md)
- [Retrieval without the jargon](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/retrieval-without-the-jargon.md)
- [GIS Tech Stack — Canonical Guide](../sources/knowledge-hub/03%20Learning/GIS/Inbox%20Guides%202026-08-20/GIS%20Tech%20Stack%20%E2%80%94%20Canonical%20Guide.md)
- [PostgreSQL architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Postgres.md)
- [PostGIS architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/PostGIS.md)
- [pgvector architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/pgvector.md)
- [Redis architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Redis.md)
- [Apache AGE architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Apache%20AGE.md)
- [LiteLLM architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/LiteLLM.md)
- [Langfuse architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Langfuse.md)
- [PostgreSQL beginner tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [PostGIS documentation](https://postgis.net/documentation/)

<a id="chapter-11"></a>

## 11 — RAG, semantic search and knowledge systems

### When to use which approach

| Need | Preferred approach |
|---|---|
| Exact file, name or literal | Filename/keyword search. |
| Structured filter or aggregation | SQL. |
| Conceptually similar passages | Embedding/vector search. |
| Relationships among entities | Graph query. |
| Spatial relation | PostGIS/spatial engine. |
| Curated reusable procedure | Skill. |
| Long-form human knowledge | Obsidian/source repository. |
| Current external fact | Live API or current web source. |

### Production RAG pipeline

1. identify authoritative sources;
2. preserve original document and metadata;
3. normalize safely;
4. chunk by meaningful boundaries;
5. generate embeddings;
6. index text and metadata;
7. retrieve with filters;
8. rerank when needed;
9. compose bounded context;
10. generate with citations;
11. evaluate retrieval and answer quality;
12. refresh or delete when sources change.

### Common RAG failures

- ingesting duplicates and obsolete documents;
- removing metadata/provenance;
- chunks too small to retain meaning or too large to rank;
- relying only on vectors for exact facts;
- returning an answer when evidence is weak;
- failing to enforce document permissions;
- never testing retrieval with a known question set.

### Obsidian’s role

Obsidian is a human-readable knowledge layer. The Master Knowledge Map routes topics; this guide routes learning; detailed notes preserve sources and decisions. Semantic search helps discovery but does not declare authority. Frontmatter, canonical maps and live verification determine status.

### Practice

Create a five-document RAG experiment. Write ten questions before ingestion, mark the expected source, run retrieval and record whether the correct passage appears in the top results.

### Go deeper

- [Master Knowledge Map](../sources/knowledge-hub/01%20Home/Maps/Master%20Knowledge%20Map.md)
- [Learning and Research map](../sources/knowledge-hub/01%20Home/Maps/Learning%20and%20Research.md)
- [Retrieval without the jargon](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/retrieval-without-the-jargon.md)
- [Hermes Obsidian semantic search setup](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Hermes%20Obsidian%20Semantic%20Search%20Setup%202026-05-02.md)
- [Hermes knowledge-vault design](../sources/knowledge-hub/05%20AI%20Systems/Hermes/How%20to%20Build%20Operator%27s%20Hermes%20Obsidian%20Knowledge%20Vault%20That%20Gets%20Smarter%20Every%20Day.md)

<a id="chapter-12"></a>

## 12 — Workflow automation with n8n

### What n8n is

n8n is a workflow orchestrator. A workflow is a graph of connected nodes. A trigger begins an execution; nodes fetch, transform, branch, wait or act; credentials authorize integrations; execution history supplies operational evidence.

Official references: [build a first workflow](https://docs.n8n.io/build-your-first-workflow/), [create and run workflows](https://docs.n8n.io/build/understand-workflows/create-and-run-workflows/), [understand executions](https://docs.n8n.io/build/understand-workflows/understand-executions/).

### Workflow anatomy

`trigger → validate → normalize → enrich → decide → approve if needed → write/send → record → observe`

### Manual versus production

- Build and test with manual executions.
- Keep workflows unpublished/inactive until inputs, credentials, failure paths and approval gates are verified.
- Production triggers may be schedules, webhooks, polling or external events.
- Each execution should have a stable run ID, source reference and outcome.

### What belongs where

| Concern | Best owner |
|---|---|
| Event trigger and app integration | n8n |
| Durable customer/case state | PostgreSQL |
| Short AI classification or draft | Model through LiteLLM/provider |
| Long autonomous coding/research task | Hermes/Claude Code/Codex worker |
| AI trace, latency and cost | Langfuse/observability layer |
| Human approval | Explicit approval/case state, not model confidence alone |
| Original documents | Approved file/object store |

### Production checklist

- validated input schema;
- scoped credentials;
- deterministic node names;
- idempotency and deduplication;
- timeout and retry policy;
- error workflow/dead-letter path;
- no secrets in execution output;
- human approval before irreversible effects;
- logs and alerts;
- documented rollback/deactivation;
- tested with realistic but safe data.

### Practice

Build an inactive workflow: manual trigger → sample JSON → schema validation → deterministic transformation → draft summary → manual approval branch → local audit record. Test success, invalid input and duplicate input.

### Go deeper

- [n8n complete learning guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/N8n/n8n-complete-learning-guide.md)
- [n8n AI learning roadmap synthesis](../sources/knowledge-hub/03%20Learning/AI%20Learning/N8n/Reddit%20n8n%20AI%20Learning%20Roadmap%20Synthesis%20-%202026-06-04.md)
- [n8n agent guardrails implementation guide](../sources/knowledge-hub/05%20AI%20Systems/n8n/n8n%20Agent%20Guardrails%20Implementation%20Guide%20-%205%20Projects.md)
- [n8n Personal Master Playbook](../sources/inish-labs/02%20Knowledge/AI%20Automation/n8n%20personal/00%20README%20-%20n8n%20Personal%20Master%20Playbook.md)
- [n8n SMB Master Playbook](../sources/inish-labs/02%20Knowledge/AI%20Automation/n8n%20smb/00%20README%20-%20n8n%20SMB%20Master%20Playbook.md)

<a id="chapter-13"></a>

## 13 — Master workflow-pattern taxonomy

Every workflow in the vaults can be understood as a combination of **trigger + processing pattern + control pattern + outcome + evidence**.

### A. Trigger patterns

| Pattern | Meaning | Typical example |
|---|---|---|
| Manual | Human starts the work. | Paid discovery analysis. |
| Scheduled | Runs at a defined time. | Daily brief or backup. |
| Polling | Checks for new state periodically. | New inbox item or changed file. |
| Webhook/event | External system announces a change. | Form submission or payment event. |
| Batch | Processes a finite collection. | Document backlog or GIS dataset. |
| Queue/worker | Jobs wait for bounded workers. | Long AI extraction tasks. |
| Streaming | Processes continuous events. | Telemetry or live updates. |
| Conversational | A user message starts a session. | Telegram assistant request. |

### B. Processing patterns

| Pattern | What happens |
|---|---|
| Ingestion | Acquire files, records, messages or events. |
| Validation | Check schema, quality, completeness and permissions. |
| Normalization | Convert inputs to standard structures. |
| ETL/ELT | Extract, transform and load data. |
| Deduplication/reconciliation | Match and resolve repeated or conflicting records. |
| Enrichment | Add external or derived attributes. |
| Classification/routing | Assign categories, priority or destination. |
| Extraction | Turn unstructured content into fields. |
| Summarization | Compress content with source references. |
| Draft generation | Produce a proposed email, report, document or code change. |
| Retrieval/Q&A | Find evidence and answer with citations. |
| Calculation/analysis | Compute metrics, forecasts or spatial relationships. |
| Transformation | Convert file formats, schemas, coordinate systems or representations. |
| Publication | Produce an approved artifact, dashboard, layer or message. |
| Monitoring | Inspect health, cost, quality or changes. |
| Backup/recovery | Preserve and restore state. |

### C. Control patterns

| Pattern | Use |
|---|---|
| Deterministic pipeline | Stable rules and predictable steps. |
| AI-assisted step | Model handles bounded ambiguity inside a deterministic workflow. |
| Agent loop | Model chooses tools and next steps until verified completion. |
| Human-in-the-loop | Person reviews or supplies judgment. |
| Approval-gated action | Irreversible or external effect waits for explicit approval. |
| Parallel fan-out | Independent items or research streams run concurrently. |
| Map/reduce | Process items independently, then combine. |
| Supervisor/worker | One controller delegates and checks bounded work. |
| Escalation | Uncertainty or risk routes to an accountable human. |
| Compensating action | Undo or reconcile after a partial failure. |

### D. Major business workflow families represented in the vaults

- research, source collection and cited synthesis;
- inbox/email triage and draft response;
- calendar, task and reminder support;
- document ingestion, extraction, comparison and reporting;
- customer onboarding and case tracking;
- lead research, qualification and proposal generation;
- project status, meeting notes and action tracking;
- invoice, expense and accounting preparation;
- construction submittal, RFI, change-order and document-control support;
- field-service dispatch, evidence and exception handling;
- data quality, ETL, migration and reconciliation;
- compliance evidence preparation with professional review;
- website/app content and support workflows;
- code planning, implementation, testing and review;
- system health, cost, backup and security monitoring;
- GIS ingestion, QA, spatial analysis, mapping and evidence dossiers;
- private RAG, knowledge support and executive briefings;
- agentic change-control and approval workflows.

### Workflow design contract

Before building any workflow, define:

1. **Buyer/user:** who owns the outcome?
2. **Trigger:** what starts it?
3. **Inputs:** source, schema, sensitivity and authority.
4. **Steps:** deterministic, AI-assisted, agentic and human.
5. **Writes:** exactly what may change or leave the system.
6. **Reviewer:** who approves and why?
7. **Artifact:** what is delivered?
8. **Metric:** how is value measured?
9. **Evidence:** logs, citations, tests and acceptance.
10. **Failure/recovery:** retry, rollback, escalation and retention.

### Canonical workflow catalogs

- [Private AI Operations Service — 50 Workflow Catalog](../sources/inish-labs/01%20Business/Inish%20Labs%20Private%20AI%20Operations%20Service%20%E2%80%94%2050%20Workflow%20Catalog%20and%20Business%20Opportunity.md)
- [GIS & AI Server — 50 Workflow Commercial Service Guide](../sources/inish-labs/01%20Business/Inish%20Labs%20GIS%20%26%20AI%20Server%20%E2%80%94%2050%20Workflow%20Commercial%20Service%20Guide.md)
- [GIS + AI 50-Offer Delivery Handbook](../sources/inish-labs/00%20Inbox/GIS%20%2B%20AI%2050-Offer%20Delivery%20Handbook%20%E2%80%94%202026-08-23/00%20%E2%80%94%20START%20HERE.md)

Treat catalogs as idea and implementation evidence. They are not proof of demand, deployment or customer acceptance.

### Practice

Choose one catalog workflow. Rewrite it using the ten-part design contract. Remove every agentic step that can be deterministic. Add a reviewer and failure path.

<a id="chapter-14"></a>

## 14 — Infrastructure and deployment

### Architecture layers

1. **User surface:** chat, web app, dashboard or GIS client.
2. **Integration/orchestration:** n8n, APIs, webhooks, MCP.
3. **Agent/runtime:** Hermes, Claude Code, Codex or application workers.
4. **Model gateway:** model provider or LiteLLM routing.
5. **Data:** PostgreSQL/PostGIS, object storage, Redis and indexes.
6. **Observability:** logs, metrics, traces and evaluation.
7. **Security/control:** identity, authorization, approvals, secrets and isolation.
8. **Infrastructure:** Linux host, containers, network, storage, backups and DNS.

### Core technologies

| Technology | Role |
|---|---|
| Linux/Ubuntu | Server operating system. |
| SSH | Authenticated remote shell; restrict and log it. |
| Docker | Container runtime. |
| Docker Compose | Declarative group of related containers. |
| Kubernetes | Cluster orchestrator for containers; unnecessary for many small services. |
| systemd/launchd/s6 | Supervises long-running services. |
| Tailscale | Private identity-aware network overlay. |
| Reverse proxy | Routes HTTP/TLS to approved services. |
| Cloudflare Tunnel/Funnel | Exposure mechanism; not a substitute for authorization. |
| SOPS/age | Encrypt configuration files for version control. |
| Git/GitHub | Versioned source and review. |
| Terraform/OpenTofu | Declarative infrastructure provisioning. |
| Ansible | Reproducible host configuration. |
| Volume | Persistent container data. |
| Snapshot/backup | Recovery copy; must be restorable. |
| CI/CD | Automated check and delivery pipeline. |

### Deployment progression

`local experiment → reproducible local build → isolated test environment → staging → approved production release → smoke check → monitoring → rollback readiness`

### Applying maturity labels in your own environment

Before acting, verify live state and record the date. Do not infer deployment from architecture notes, Compose files, plans or historical status reports.

### Security posture for these architectures

- private/Tailscale-only by default;
- no public root shell or raw Docker socket;
- no unrestricted SQL or secret-read tools;
- no production deployment, workflow activation or migration without separate approval;
- unrelated customers require deliberate tenant isolation;
- patches, migrations and backups require verification and recovery paths.

### Practice

Deploy a small non-sensitive local Compose application with an API and database. Persist data, restart it, inspect logs, back it up and restore into a separate test stack.

### Go deeper

- [Automation and Infrastructure map](../sources/knowledge-hub/01%20Home/Maps/Automation%20and%20Infrastructure.md)
- [Docker — Complete Practical Guide](../sources/knowledge-hub/03%20Learning/Technology/Docker/Docker%20-%20Complete%20Practical%20Guide.md)
- [Docker and Kubernetes — Practical Beginner Guide](../sources/knowledge-hub/03%20Learning/Technology/Docker/Docker%20and%20Kubernetes%20%E2%80%94%20Practical%20Beginner%20Guide.md)
- [Inish Labs Hetzner Architecture](../sources/inish-labs/01%20Business/Inish%20Labs%20Hetzner%20Architecture%20%E2%80%94%20Machine%20Specifications%2C%20Capabilities%20and%20Service%20Map.md)
- [Technical Lead Operating Guide](../sources/inish-labs/01%20Business/Inish%20Labs%20Technical%20Lead%20Operating%20Guide%20%E2%80%94%20People%2C%20Code%2C%20AI%20Access%20and%20AI%20OS.md)
- [AI automation architecture overview](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Architecture%20Overview.md)
- [Docker and Docker Compose](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Docker%20and%20Docker%20Compose.md)
- [Tailscale architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Tailscale.md)
- [Cloudflare Tunnel architecture note](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Cloudflare%20Tunnel.md)
- [Backups, cron and snapshots](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Backups%2C%20Cron%20and%20Snapshots.md)
- [AI Automation Master Deployment Guide](../sources/inish-labs/02%20Knowledge/AI%20Automation/AI%20Automation%20Master%20Guide%20deploy.md)
- [GIS + AI server deployment guide](../sources/inish-labs/02%20Knowledge/GIS/GIS%20%2B%20AI%20Server%20on%20Hetzner%20%E2%80%94%20Fable%205%20Deploy%20Guide.md)

<a id="chapter-15"></a>

## 15 — Observability, evaluation and security

### Observability

- **Log:** event record explaining what happened.
- **Metric:** numeric time series such as latency, errors or cost.
- **Trace:** path of one request through components.
- **AI trace:** prompt/context, model, response, tokens, latency, cost and evaluation metadata—with sensitive data controls.
- **Alert:** condition requiring attention.

Langfuse is used in the documented private stack for AI tracing. LiteLLM provides model routing, policy/cost control and a consistent model interface. Neither replaces application logs, database audit records or acceptance tests.

### Evaluation layers

1. input/data quality;
2. retrieval relevance;
3. answer groundedness and citation correctness;
4. structured-output/schema correctness;
5. tool-selection and tool-result accuracy;
6. workflow completion and side-effect correctness;
7. latency, cost and reliability;
8. human usefulness and acceptance;
9. safety and policy compliance.

### Threat model

| Risk | Control |
|---|---|
| Prompt injection in email/web/document | Treat content as data; separate authority; filter tools; require approval. |
| Secret leakage | Keep secrets out of prompts/Git/logs; redact; least privilege; rotate if exposed. |
| Excessive agent permissions | Small toolsets, sandbox, scoped credentials, read-only default. |
| Unsafe plugin/MCP package | Source review, immutable pin, capability filtering and isolated test. |
| Cross-customer exposure | Per-tenant data, credentials, storage, authorization and observability. |
| Hallucinated facts | Retrieval, citations, deterministic validation and human review. |
| Duplicate external action | Idempotency keys and durable action ledger. |
| Irrecoverable data loss | Backups, tested restores, migration rollback and retention controls. |
| Model/provider outage | Timeouts, queues, retries, fallback policy and degraded mode. |
| Autonomous drift | Iteration/time/cost limits, checkpoints and explicit completion tests. |

### Compliance and professional boundaries

Do not convert a technical workflow into an unsupported legal or regulatory claim. GxP, GMP, GDP, HIPAA, FDA, EMA, Part 11, licensed surveying, professional engineering, environmental certification, underwriting and legal determinations require separately funded controls and accountable reviewers.

### Practice

Threat-model the n8n exercise. Add five abuse cases, three metrics, an evaluation set, one alert, one rollback and one explicit approval boundary.

### Go deeper

- [AI Security — Comprehensive Guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/AI%20Security/AI%20Security%20%E2%80%94%20Comprehensive%20Guide.md)
- [Trust and sandboxing](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/trust-and-sandboxing.md)
- [Feedback loops](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/feedback-loops.md)
- [n8n agent guardrails implementation guide](../sources/knowledge-hub/05%20AI%20Systems/n8n/n8n%20Agent%20Guardrails%20Implementation%20Guide%20-%205%20Projects.md)
- [Technical Lead Operating Guide](../sources/inish-labs/01%20Business/Inish%20Labs%20Technical%20Lead%20Operating%20Guide%20%E2%80%94%20People%2C%20Code%2C%20AI%20Access%20and%20AI%20OS.md)

---

# Stage IV — Specialist systems and production design

<a id="chapter-16"></a>

## 16 — GIS and spatial AI engineering

### GIS foundations

- **GIS:** system for storing, analyzing and communicating information tied to location.
- **Vector data:** points, lines and polygons with attributes.
- **Raster data:** grid cells such as imagery or elevation.
- **Layer:** coherent geographic dataset rendered or analyzed together.
- **Feature:** one geographic object and its attributes.
- **CRS:** coordinate reference system defining how coordinates relate to Earth.
- **Topology:** rules about spatial relationships and connectivity.
- **Geoprocessing:** operations such as buffer, intersect, dissolve, clip and raster analysis.
- **Spatial database:** database supporting geometry, coordinate systems and spatial indexes.
- **Tile service:** efficient delivery of map representations.
- **Provenance:** source, date, license, transformation and confidence of spatial data.

### Esri and open-source layers

| Layer | Examples | Role |
|---|---|---|
| Desktop authoring | ArcGIS Pro, QGIS | Analysis, cartography and review. |
| Enterprise GIS | ArcGIS Online/Enterprise | Identity, hosted layers, apps and collaboration. |
| Automation | ArcPy, ArcGIS API for Python, REST | Repeatable Esri workflows. |
| Spatial database | PostGIS | Durable spatial data and queries. |
| Vector processing | GDAL/OGR, GeoPandas, Shapely, pyproj | Conversion, transformation and geometry operations. |
| Raster/elevation | Rasterio, xarray/rioxarray, PDAL | Raster, multidimensional and point-cloud workflows. |
| Map delivery | pg_tileserv, MapLibre | Approved vector tiles and web maps. |
| Agent interface | GIS tools/MCP/harness | Bounded access to approved GIS operations. |

### Spatial RAG

Spatial RAG combines semantic retrieval with spatial filters/relations. A reliable query may require:

1. identify place and coordinate system;
2. retrieve authoritative documents/features;
3. run deterministic spatial query;
4. preserve source/date/license;
5. generate an explanation with citations;
6. route judgment to a qualified reviewer.

The LLM should explain or orchestrate; PostGIS/GIS engines should perform geometry operations.

### GIS workflow families

- data inventory and metadata;
- format/CRS transformation;
- geometry and attribute QA;
- address/geocode/entity matching;
- spatial join, proximity and intersection;
- suitability/site screening;
- change detection and monitoring;
- asset/field evidence collection;
- map/layer publication;
- cited site or permit dossier;
- GIS support assistant and runbook retrieval;
- agentic change proposal with approval gate.

### Accountable review

Surveying, engineering, environmental, legal, underwriting and safety conclusions must remain professionally reviewed. A model-generated map is not a licensed determination.

### Practice

Load a small public dataset, inspect its CRS and provenance, validate geometry, run a buffered intersection in a GIS engine and write a cited report that explicitly separates computed facts from interpretation.

### Go deeper

- [GIS and AI map](../sources/knowledge-hub/01%20Home/Maps/GIS%20and%20AI.md)
- [GIS Tech Stack — Canonical Guide](../sources/knowledge-hub/03%20Learning/GIS/Inbox%20Guides%202026-08-20/GIS%20Tech%20Stack%20%E2%80%94%20Canonical%20Guide.md)
- [Dymaxion GIS Agent Harness entry point](../sources/knowledge-hub/05%20AI%20Systems/GIS%20Agent%20Build/Dymaxion%20Source%20Pack/gis%20agents/00%20README%20-%20Dymaxion%20GIS%20Agent%20Harness.md)
- [GIS Agent Harness — Core Components Guide](../sources/inish-labs/02%20Knowledge/GIS/Agent%20Docs/GIS%20Agent%20Harness%20%E2%80%94%20Core%20Components%20Guide.md)
- [Building a GIS Agent Harness](../sources/inish-labs/02%20Knowledge/GIS/Agent%20Docs/Building%20a%20GIS%20Agent%20Harness%20%E2%80%94%20Build%20Guide.md)
- [GIS & AI commercial workflow guide](../sources/inish-labs/01%20Business/Inish%20Labs%20GIS%20%26%20AI%20Server%20%E2%80%94%2050%20Workflow%20Commercial%20Service%20Guide.md)
- [GIS delivery handbook](../sources/inish-labs/00%20Inbox/GIS%20%2B%20AI%2050-Offer%20Delivery%20Handbook%20%E2%80%94%202026-08-23/00%20%E2%80%94%20START%20HERE.md)

<a id="chapter-17"></a>

## 17 — Production operations

### Environments

- **Development:** fast iteration with synthetic/non-sensitive data.
- **Test:** automated and manual verification.
- **Staging:** production-like environment for release checks.
- **Production:** customer/user-impacting system under change control.

### Production readiness questions

- Is ownership clear?
- Are requirements and acceptance criteria explicit?
- Are data classification and retention defined?
- Are credentials scoped and rotatable?
- Are migrations backed up and reversible?
- Are failures observable?
- Are alerts actionable?
- Are runbooks and escalation contacts available?
- Are RTO and RPO defined?
- Has restore been tested?
- Can the service degrade safely?
- Is customer isolation verified?
- Are model cost and limits controlled?
- Are external writes approval-gated where required?

### Operating loop

`observe → triage → contain → diagnose → recover → verify → communicate → learn`

- **Incident:** unplanned degradation or risk.
- **Runbook:** tested steps for a recurring operation.
- **SLO:** measurable reliability objective.
- **RTO:** target time to restore service.
- **RPO:** acceptable data-loss window.
- **Change record:** what changed, why, who approved, evidence and rollback.
- **Postmortem:** blame-free analysis and durable prevention.

### Cost operations

Track infrastructure, model tokens, storage, integrations, execution counts, support time and professional review. A technically successful workflow can still be commercially non-viable if per-run cost and support exceed value.

### Practice

Write a production-readiness review for a capstone. Include deployment diagram, data flow, threat model, test evidence, backup/restore proof, SLO, alert and rollback.

### Go deeper

- [Technical Lead Operating Guide](../sources/inish-labs/01%20Business/Inish%20Labs%20Technical%20Lead%20Operating%20Guide%20%E2%80%94%20People%2C%20Code%2C%20AI%20Access%20and%20AI%20OS.md)
- [Hetzner architecture and service map](../sources/inish-labs/01%20Business/Inish%20Labs%20Hetzner%20Architecture%20%E2%80%94%20Machine%20Specifications%2C%20Capabilities%20and%20Service%20Map.md)
- [AI Automation Master Deployment Guide](../sources/inish-labs/02%20Knowledge/AI%20Automation/AI%20Automation%20Master%20Guide%20deploy.md)
- [Hermes operations for an operator and clients](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Runbooks/Expert%20Guide%20-%20Setting%20Up%20and%20Maintaining%20Hermes%20Agents%20for%20Operator%20and%20Clients.md)

---

# Stage V — Commercial AI services

<a id="chapter-18"></a>

## 18 — Designing and selling AI services

### Sell the outcome, not the technology list

A buyer purchases faster turnaround, lower rework, reduced risk, better evidence or more capacity. Claude, n8n, Postgres and Hermes are implementation choices.

### Offer anatomy

Every credible offer defines:

- **buyer:** person with budget and responsibility;
- **trigger:** event making the problem urgent;
- **current workflow:** steps, systems, delays and failure points;
- **bounded intervention:** what the service changes;
- **reviewer:** accountable person for judgment;
- **artifact:** report, database, layer, workflow or decision packet;
- **metric:** time, error, backlog, revenue, risk or quality;
- **data boundary:** what enters and where it is stored;
- **acceptance:** evidence the buyer uses to approve delivery;
- **operating model:** one-time sprint, implementation or managed service.

### Commercial progression

1. **Discovery:** interview, sample data, workflow map and baseline.
2. **Paid pilot:** narrow dataset, one process, reversible/no external writes.
3. **Implementation:** production integration, security and acceptance.
4. **Managed operations:** monitoring, support, change control and recurring value.
5. **Productization:** repeatable package only after several paid validations.

### Service families

| Service | Example outcome |
|---|---|
| Workflow discovery and modernization | Map process and identify safe automation boundary. |
| Private knowledge/RAG | Faster cited answers over approved documents. |
| Data quality/ETL | Clean, reconciled and documented operational data. |
| Approval-gated automation | Draft or prepare actions without autonomous external writes. |
| Executive/operational brief | Reliable synthesis with evidence and exceptions. |
| GIS evidence workflow | QA, analysis and cited spatial dossier with expert review. |
| AI operations | Model routing, tracing, evaluation and incident support. |
| Agent engineering | Bounded tool-using agent with verification and controls. |
| Training and enablement | Client team can operate and govern the delivered system. |

### Pricing and demand

Market research can establish pain categories, substitute spend and buyer language. It does not prove willingness to buy from Inish Labs. Prices, niches and ranking remain hypotheses until a customer pays and accepts the outcome.

### Boundaries

- Begin single-tenant where possible.
- Never claim regulated readiness without the actual validation program.
- Keep external writes approval-first.
- Use customer-specific credentials and data controls.
- Preserve professional review for licensed judgments.
- Define support and change-request boundaries.
- Do not promise impossible accuracy or autonomous administration.

### Practice

Write a one-page offer using buyer, trigger, workflow, reviewer, artifact and metric. Validate it through five interviews and ask for a paid pilot, not praise.

### Go deeper

- [Inish Labs and Commercial Work map](../sources/knowledge-hub/01%20Home/Maps/Inish%20Labs%20and%20Commercial%20Work.md)
- [Private AI operations workflow catalog](../sources/inish-labs/01%20Business/Inish%20Labs%20Private%20AI%20Operations%20Service%20%E2%80%94%2050%20Workflow%20Catalog%20and%20Business%20Opportunity.md)
- [GIS & AI workflow commercial guide](../sources/inish-labs/01%20Business/Inish%20Labs%20GIS%20%26%20AI%20Server%20%E2%80%94%2050%20Workflow%20Commercial%20Service%20Guide.md)
- [From Nothing to Paying Customer](../sources/inish-labs/02%20Knowledge/AI%20Automation/AI%20Stack/From%20Nothing%20to%20Paying%20Customer%20%E2%80%94%20Hand-Holding%20Build%20Guide.md)
- [Technical Lead Operating Guide](../sources/inish-labs/01%20Business/Inish%20Labs%20Technical%20Lead%20Operating%20Guide%20%E2%80%94%20People%2C%20Code%2C%20AI%20Access%20and%20AI%20OS.md)

<a id="chapter-19"></a>

## 19 — Capstone ladder

Build these in order. Each capstone must have source, code/config, tests, usage note, security note and evidence.

### Capstone 1 — Deterministic local utility

- read structured input;
- validate schema;
- transform data;
- produce a report;
- unit tests and Git history.

### Capstone 2 — Read-only API integration

- authenticated or public API;
- pagination, timeout and rate-limit handling;
- normalized storage;
- provenance and error log.

### Capstone 3 — n8n approval workflow

- manual/webhook trigger;
- validation and idempotency;
- AI draft step;
- human approval;
- durable audit record;
- failure path.

### Capstone 4 — Database-backed service

- API plus PostgreSQL;
- migrations, constraints and roles;
- backup and tested restore;
- integration tests.

### Capstone 5 — Cited RAG system

- authoritative source pack;
- retrieval evaluation set;
- citations and abstention;
- permission model;
- refresh/delete procedure.

### Capstone 6 — Tool-using agent

- three narrow tools;
- one procedural skill;
- bounded tool loop;
- iteration/cost limit;
- verification and escalation;
- independent review.

### Capstone 7 — Deployed private service

- containerized staging deployment;
- private network;
- secrets separation;
- health checks, logs, traces and alerts;
- backup, restore and rollback;
- production-readiness review.

### Capstone 8 — GIS workflow

- authoritative spatial data;
- CRS/geometry QA;
- deterministic analysis;
- map or dossier;
- provenance and professional-review boundary.

### Capstone 9 — Paid pilot package

- validated buyer and trigger;
- current/future workflow map;
- one bounded deliverable;
- acceptance test;
- implementation and managed-operation options;
- signed data/security boundary.

<a id="chapter-20"></a>

## 20 — Study plan and mastery rubric

### Suggested 24-week sequence

| Weeks | Focus | Required output |
|---|---|---|
| 1–2 | Computing, terminal, files, APIs and Git | Capstone 1 |
| 3–4 | LLMs, tokens, prompting and context | Explained mental model + structured-output exercise |
| 5–6 | Retrieval, embeddings, memory and RAG | Retrieval experiment |
| 7–8 | Agents, tools, loops, skills, hooks and MCP | Bounded agent design |
| 9–10 | Claude Code and software delivery | Tested repository change |
| 11–12 | Codex and independent review | Cross-agent review evidence |
| 13–14 | Hermes profiles, memory, skills and cron | Read-only profile exercise |
| 15–16 | n8n, APIs and business workflows | Capstone 3 |
| 17–18 | SQL, PostgreSQL, Redis and data operations | Capstone 4 |
| 19–20 | Docker, deployment, observability and security | Capstone 7 staging version |
| 21–22 | GIS/spatial AI specialization | Capstone 8 |
| 23–24 | Discovery, offer design and paid validation | Capstone 9 package |

### Weekly learning loop

1. learn one concept;
2. explain it without jargon;
3. build one small artifact;
4. test the failure path;
5. record evidence and questions;
6. update the relevant canonical note—not a new duplicate guide;
7. select the next weakest competency.

### Mastery levels

| Level | Evidence |
|---|---|
| **Recognize** | Define the term and place it in the architecture. |
| **Explain** | Teach it with a diagram and compare alternatives. |
| **Build** | Implement a small working version. |
| **Verify** | Test correctness, security and failure behavior. |
| **Operate** | Deploy, monitor, recover and control cost. |
| **Design** | Choose architecture based on constraints and trade-offs. |
| **Lead** | Define standards, review others and manage risk. |
| **Commercialize** | Tie the system to a paid outcome and support model. |

---

# Appendix A — Technology encyclopedia

## AI and model layer

| Technology/concept | Role in the system |
|---|---|
| Transformer/LLM | Generates and reasons over token context. |
| Claude | Anthropic model/product family. |
| OpenAI models | Model family used directly or through Codex/LiteLLM. |
| Gemini | Google multimodal model family. |
| Local models/Ollama | Private/local inference for suitable workloads; requires hardware and evaluation. |
| LiteLLM | Model gateway/router, unified interface, policy and cost control. |
| Prompt | Explicit task input. |
| Context engineering | Selection and arrangement of all task information. |
| Structured output | Model response constrained to a schema. |
| Tool/function calling | Model emits a structured request to software. |
| Embedding | Vector representation used for semantic similarity. |
| RAG | Retrieval of evidence before generation. |
| Fine-tuning/LoRA | Additional training for specialized behavior; not a substitute for retrieval or tools. |
| Multimodal model | Processes text plus images/audio/video depending on capability. |

## Agent and extension layer

| Technology/concept | Role in the system |
|---|---|
| Agent harness | Runs the context/tool/verification loop. |
| Graph engineering | Makes states, transitions and stop conditions explicit. |
| LangGraph | Framework for stateful graph-based agent applications. |
| Temporal/durable workflow engine | Persists long-running workflow state and retries. |
| Tool | Executable function exposed to the model. |
| Skill | Reusable procedural memory. |
| Plugin | Executable packaged extension. |
| Hook | Deterministic lifecycle callback. |
| MCP | Standard client/server protocol for tools, resources and prompts. |
| Subagent | Isolated delegated reasoning worker. |
| Memory | Persisted user, procedural, session or project knowledge. |
| Cron | Scheduled agent task. |
| Approval gate | Human authorization before a sensitive effect. |
| Evaluation | Repeatable measurement of quality/safety. |
| Claude Code | Anthropic coding agent. |
| Codex | OpenAI coding agent environment. |
| Hermes Agent | Persistent multi-channel personal/operational agent platform. |
| Orgo | Remote computer-use environment; separate from local execution. |
| Composio | Connected-app integration layer; credentials and writes remain approval-controlled. |

## Workflow and application layer

| Technology/concept | Role in the system |
|---|---|
| n8n | Event/workflow orchestration. |
| Webhook | Event delivered by HTTP callback. |
| REST API | Resource/action interface over HTTP. |
| OAuth | Delegated authorization. |
| FastAPI | Python framework for APIs. |
| Pydantic | Typed validation and schemas in Python. |
| Python | General AI/data/automation/GIS language. |
| JavaScript/TypeScript | Web and Node.js integration language. |
| React/Next.js | Web UI/application frameworks. |
| Playwright/browser automation | UI control when APIs are absent; more brittle and higher risk. |
| NotebookLM | Source-grounded research/notebook product; verify UI writes after timeouts. |
| Obsidian | Human-readable Markdown knowledge system. |
| Google Workspace | Gmail, Calendar, Drive, Docs and Sheets integrations. |

## Data layer

| Technology | Role |
|---|---|
| PostgreSQL | Durable relational state and SQL. |
| PostGIS | Spatial types and queries in PostgreSQL. |
| pgvector | Embedding vectors and similarity search in PostgreSQL. |
| Apache AGE/graph database | Relationship traversal and graph queries. |
| SQLite | Embedded local relational database. |
| DuckDB | In-process analytical SQL. |
| Redis | Cache, queue and transient coordination. |
| Object storage/B2/S3 | Large files, artifacts and backups. |
| Search index | Lexical search and filtering. |
| Schema | Defined structure and constraints. |
| Migration | Versioned data/schema change. |
| ETL/ELT | Data movement and transformation. |

## Infrastructure and operations layer

| Technology | Role |
|---|---|
| Linux/Ubuntu | Server operating system. |
| macOS/launchd | Local workstation OS and service supervisor. |
| SSH | Remote shell and transport. |
| Docker | Container runtime. |
| Docker Compose | Multi-container definition. |
| systemd/launchd/s6 | Process supervision. |
| Tailscale | Private overlay network and identity. |
| Reverse proxy | HTTP/TLS routing. |
| Cloudflare Tunnel/Funnel | Controlled exposure path; requires separate approval. |
| SOPS/age | Encrypted configuration in Git. |
| Git/GitHub | Source history, collaboration and review. |
| Git worktree | Isolated branch workspace. |
| CI/CD | Automated checks and delivery. |
| Terraform/OpenTofu | Infrastructure as code. |
| Ansible | Host configuration automation. |
| Langfuse | AI trace/quality/cost observability. |
| Logs/metrics/traces | Operational evidence. |
| Backup/snapshot | Recovery copy. |
| RTO/RPO | Recovery time and data-loss objectives. |

## GIS and spatial layer

| Technology | Role |
|---|---|
| ArcGIS Pro | Desktop GIS authoring and analysis. |
| ArcGIS Online/Enterprise | Hosted/enterprise layers, apps and identity. |
| ArcPy | Python automation for ArcGIS Pro/geoprocessing. |
| ArcGIS API for Python/REST | Programmatic portal and feature-service operations. |
| QGIS | Open-source desktop GIS. |
| GDAL/OGR | Raster/vector conversion and processing. |
| GeoPandas | Tabular vector analysis in Python. |
| Shapely | Geometry operations. |
| pyproj | Coordinate transformations. |
| Rasterio/rioxarray/xarray | Raster and multidimensional processing. |
| PDAL | Point-cloud processing. |
| pg_tileserv | Vector-tile serving from PostGIS. |
| MapLibre | Open web map rendering. |
| Spatial RAG | Retrieval combining semantic and spatial constraints. |
| CRS | Coordinate reference framework. |
| Topology | Spatial relationship/connectivity rules. |
| Provenance | Source, license, date and transformation history. |

---

# Appendix B — Workflow selection cheatsheet

| If the problem is… | Start with… | Add AI only for… |
|---|---|---|
| Stable rule and known inputs | Deterministic function or n8n workflow | Language classification/drafting. |
| Many documents with known fields | Batch extraction pipeline | Ambiguous field extraction. |
| Questions over approved documents | RAG with citations | Answer synthesis. |
| Cross-system event handling | Webhook + durable state | Exception explanation. |
| Long coding task | Claude Code/Codex in worktree | Planning, implementation and review. |
| Open-ended multi-source research | Hermes/agent loop | Search strategy and synthesis. |
| Recurring health check | Silent script/watchdog | Summarize only failures/changes. |
| External message/action | Draft + approval gate | Drafting; not autonomous authorization. |
| Spatial relationship | PostGIS/GIS engine | Natural-language interface/explanation. |
| High-stakes professional decision | Deterministic evidence packet + qualified reviewer | Assist analysis; never replace accountable judgment. |

---

# Appendix C — Canonical source routes

## Navigation

- [Knowledge Hub Home](../sources/knowledge-hub/01%20Home/Home.md)
- [Learning Home](../sources/knowledge-hub/01%20Home/Learning%20Home.md)
- [Master Knowledge Map](../sources/knowledge-hub/01%20Home/Maps/Master%20Knowledge%20Map.md)
- [AI and Agents map](../sources/knowledge-hub/01%20Home/Maps/AI%20and%20Agents.md)
- [Claude Code map](../sources/knowledge-hub/01%20Home/Maps/Claude%20Code.md)
- [Automation and Infrastructure map](../sources/knowledge-hub/01%20Home/Maps/Automation%20and%20Infrastructure.md)
- [GIS and AI map](../sources/knowledge-hub/01%20Home/Maps/GIS%20and%20AI.md)
- [Inish Labs and Commercial Work map](../sources/knowledge-hub/01%20Home/Maps/Inish%20Labs%20and%20Commercial%20Work.md)

## Foundations and agents

- [AI Foundations Concepts index](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/Concepts.md)
- [Context as input](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/context-as-input.md)
- [Instructions as constraints](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/instructions-as-constraints.md)
- [Prompts as artifacts](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/prompts-as-artifacts.md)
- [The agent loop](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/the-agent-loop.md)
- [Feedback loops](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/feedback-loops.md)
- [Hooks](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/hooks.md)
- [Tool use and MCP](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/tool-use-and-mcp.md)
- [Trust and sandboxing](../sources/knowledge-hub/03%20Learning/AI%20Foundations/Concepts/trust-and-sandboxing.md)
- [Agents Master Document](../sources/knowledge-hub/05%20AI%20Systems/Agents/Agents%20Master%20Document.md)

## Coding agents

- [Claude Code Mastery Path](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/00%20START%20HERE%20%E2%80%94%20Claude%20Code%20Mastery%20Path.md)
- [Claude Code Setup and Best Practices](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/02%20Setup%20%26%20Best%20Practices.md)
- [Claude Code Extensions](../sources/knowledge-hub/03%20Learning/AI%20Learning/Claude%20Code/Guides/03%20Agents%2C%20MCP%2C%20Commands%20%26%20Skills.md)
- [Codex Mastery Path](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/00%20START%20HERE%20%E2%80%94%20Codex%20Mastery%20Path.md)
- [Codex Setup and Best Practices](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/02%20Setup%20%26%20Best%20Practices.md)
- [Codex Extensions](../sources/knowledge-hub/03%20Learning/AI%20Learning/Codex/Guides/03%20Agents%2C%20MCP%2C%20Commands%20%26%20Prompts.md)

## Hermes and automation

- [Hermes Dashboard](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Hermes%20Dashboard.md)
- [Stable primary-agent configuration recap](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Hermes%20Primary%20Agent%20Configuration%20Recap%20-%20Stable%20Personal%20Assistant%20Setup.md)
- [Hermes Memory Backbone](../sources/knowledge-hub/05%20AI%20Systems/Hermes/Memory%20Backbone/Hermes%20Memory%20Backbone.md)
- [n8n complete learning guide](../sources/knowledge-hub/03%20Learning/AI%20Learning/N8n/n8n-complete-learning-guide.md)
- [n8n agent guardrails](../sources/knowledge-hub/05%20AI%20Systems/n8n/n8n%20Agent%20Guardrails%20Implementation%20Guide%20-%205%20Projects.md)

## Inish technology and operations

- [Inish Labs — Start Here](../sources/inish-labs/00%20Start%20Here.md)
- [Inish Labs Master Plan](../sources/inish-labs/01%20Business/00%20START%20HERE%20%E2%80%94%20Inish%20Labs%20Master%20Plan.md)
- [Inish Labs Knowledge Index](../sources/inish-labs/02%20Knowledge/INDEX.md)
- [Inish Labs operating and infrastructure mental model](../sources/inish-labs/02%20Knowledge/inish%20labs%20mental%20model/00%20INDEX.md)
- [AI Automation Stack Source Index](../sources/inish-labs/02%20Knowledge/AI%20Automation/AI%20Automation%20Stack%20Source%20Index.md)
- [Architecture Overview](../sources/inish-labs/02%20Knowledge/AI%20Automation/Architecture/Architecture%20Overview.md)
- [AI Automation Master Deployment Guide](../sources/inish-labs/02%20Knowledge/AI%20Automation/AI%20Automation%20Master%20Guide%20deploy.md)
- [Hetzner Architecture and Service Map](../sources/inish-labs/01%20Business/Inish%20Labs%20Hetzner%20Architecture%20%E2%80%94%20Machine%20Specifications%2C%20Capabilities%20and%20Service%20Map.md)
- [Technical Lead Operating Guide](../sources/inish-labs/01%20Business/Inish%20Labs%20Technical%20Lead%20Operating%20Guide%20%E2%80%94%20People%2C%20Code%2C%20AI%20Access%20and%20AI%20OS.md)
- [GIS + AI Server Deploy Guide](../sources/inish-labs/02%20Knowledge/GIS/GIS%20%2B%20AI%20Server%20on%20Hetzner%20%E2%80%94%20Fable%205%20Deploy%20Guide.md)

## Workflow and commercial catalogs

- [Private AI Operations — 50 Workflow Catalog](../sources/inish-labs/01%20Business/Inish%20Labs%20Private%20AI%20Operations%20Service%20%E2%80%94%2050%20Workflow%20Catalog%20and%20Business%20Opportunity.md)
- [GIS & AI — 50 Workflow Commercial Service Guide](../sources/inish-labs/01%20Business/Inish%20Labs%20GIS%20%26%20AI%20Server%20%E2%80%94%2050%20Workflow%20Commercial%20Service%20Guide.md)
- [GIS + AI Delivery Handbook](../sources/inish-labs/00%20Inbox/GIS%20%2B%20AI%2050-Offer%20Delivery%20Handbook%20%E2%80%94%202026-08-23/00%20%E2%80%94%20START%20HERE.md)
- [From Nothing to Paying Customer](../sources/inish-labs/02%20Knowledge/AI%20Automation/AI%20Stack/From%20Nothing%20to%20Paying%20Customer%20%E2%80%94%20Hand-Holding%20Build%20Guide.md)

---

# Appendix D — Current first-party documentation

Use these for commands and product behavior that change faster than the vault:

- [Hermes Agent documentation](https://hermes-agent.nousresearch.com/docs/)
- [Hermes configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration)
- [Hermes plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)
- [Hermes MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [Hermes profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles)
- [Claude Code overview](https://code.claude.com/docs/en/overview)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp)
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli)
- [Codex customization](https://learn.chatgpt.com/docs/customization/overview)
- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-basic)
- [Codex `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture)
- [n8n documentation](https://docs.n8n.io/)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [PostGIS documentation](https://postgis.net/documentation/)

---

# Appendix E — Reconciliation and maintenance rules

## Reconciliation decisions

- This guide is the learning authority; the Master Knowledge Map remains the navigation authority.
- Existing Claude Code and Codex mastery paths remain the detailed academies.
- `Agents Master Document` remains the detailed agent-theory reference.
- The private AI and GIS 50-workflow guides remain commercial/workflow catalogs, not the learning curriculum.
- Live infrastructure claims require current tool verification; plans and Compose files are not runtime evidence.
- Machine-generated skill mirrors and retired OpenClaw material are supporting/historical, not current command authority.
- First-party docs win when platform commands or file locations change.
- Market evidence shows pain and purchase categories; customer demand and pricing require paid validation.

## How to maintain this guide

Update this guide—not a new competing master guide—when:

- a new major technology family enters the stack;
- a canonical source note moves;
- a product changes skill/plugin/hook configuration;
- a planned component becomes verified live or is retired;
- a recurring workflow pattern is not represented;
- a capstone or commercial offer becomes proven and changes the recommended sequence.

For each update:

1. verify the live file/path or current official documentation;
2. update the plain-English explanation and source route;
3. preserve live/scaffold/planned/obsolete status;
4. run internal-link and external-link checks;
5. scan for secrets and private infrastructure identifiers;
6. record the review date;
7. avoid adding a duplicate guide unless the content is truly an implementation artifact.

## Final standard

You are ready to sell an AI service when you can:

- explain the architecture to a non-technical buyer;
- build and test the bounded workflow;
- show data flow, permissions and professional-review boundaries;
- deploy and recover it safely;
- measure outcome, cost and reliability;
- support it under a defined operating model;
- state clearly what is not automated, not validated and not promised.
