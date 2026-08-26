---
title: "LLM AI Automation Master Guide"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# LLM AI Automation Master Guide

This is the consolidated guide for becoming practically fluent in LLMs and AI automation: the concepts, terminology, current model landscape, coding agents, Hermes, n8n, and how to turn the stack into useful systems or a productized service.

It is written for the operator's current goal: understand the field deeply enough to build, operate, explain, sell, and safely implement AI-agent and workflow-automation systems.

## Source notes reviewed

I searched the Knowledge Hub for LLMs, Claude Code, Codex, Hermes, n8n, AI automation, agent services, model costs, RAG, embeddings, context windows, MCP, and workflow orchestration. The strongest source notes were:

- AI Complete Mastery Business Guide
- The Comprehensive AI & Agents Learning Guide
- AI Mastery Guide: Claude Code, Codex, Obsidian, Agents, MCP, Skills, and Automation
- Claude Code — Consolidated Master Guide
- [Claude Code — Master Guide](../Claude%20Code/claude-code-master-guide.md)
- Hermes Agent: A Beginner's Guide
- Hermes Agent + Telegram, with existing OpenClaw integration
- [n8n Complete Learning Guide](../N8n/n8n-complete-learning-guide.md)
- Claude Code × n8n: Complete Zero-to-Production Guide
- n8n CPA Integration Service Plan
- Managed AI Agent Service for Home Service Businesses
- AI Agent Service - 7 Day Operational Launch Plan
- AI Agent Architect Mastery Curriculum - Esri Edition v2

## How to use this guide

Use this in four passes:

1. **Concept pass:** Learn the vocabulary and mental models.
2. **Tool pass:** Understand Claude Code, Codex, Hermes, n8n, MCP, RAG, Obsidian, and APIs.
3. **Implementation pass:** Build small systems in the recommended order.
4. **Business pass:** Turn repeatable implementations into service offers.

Do not try to memorize every model or price. Learn how to evaluate models, check current pricing, measure cost, and choose the right model for a job.

---

# Part 1 — The master mental model

## The simplest useful AI-system formula

Most real AI systems can be understood as:

```text
LLM + context + tools + workflow + memory + evaluation + human approval
```

Each piece matters:

- **LLM:** the reasoning/text/code model.
- **Context:** the information placed in the model's prompt or retrieved for it.
- **Tools:** actions the model can call: terminal, file edits, APIs, browser, Gmail, calendar, CRM, n8n, databases.
- **Workflow:** the ordered process around the model: triggers, routing, approvals, retries, logging.
- **Memory:** durable facts, preferences, notes, embeddings, session history, or project documentation.
- **Evaluation:** how you check whether the output is correct, safe, useful, and cost-effective.
- **Human approval:** the safety boundary for money, customer contact, accounting, deletes, deployments, and sensitive data.

## LLMs are not magic employees

An LLM is a statistical model that predicts tokens. It can appear to reason because very large transformer models learn patterns of language, logic, code, and tool use. But it does not automatically know your current system, your business rules, or the truth of a claim unless you give it context or verify externally.

The practical stance:

- Treat the LLM as a **fast reasoning and drafting engine**.
- Treat tools/APIs/databases as the **ground truth**.
- Treat workflow and approvals as the **safety system**.
- Treat logs/evals/tests as the **quality system**.

## Three levels of mastery

### Level 1 — Operator

You can use ChatGPT, Claude, Claude Code, Codex, Hermes, and n8n to complete tasks safely.

You know:

- what to ask for;
- what context to provide;
- how to verify output;
- when not to trust it;
- how to keep human approval in the loop.

### Level 2 — System builder

You can design repeatable workflows:

- email summary to task list;
- meeting transcript to CRM notes;
- QuickBooks data to dashboard or reports;
- Obsidian notes to daily plan;
- customer intake to draft response;
- GIS data to web app.

You understand APIs, auth, triggers, webhooks, JSON, retry logic, error handling, and cost control.

### Level 3 — AI architect

You can choose models, build agentic systems, evaluate quality, design memory/RAG, create deployment architecture, secure data, and explain tradeoffs to clients.

You know when to use:

- simple automation instead of an agent;
- RAG instead of long context;
- a cheap model instead of a frontier model;
- human review instead of full automation;
- local/private processing instead of cloud APIs.

---

# Part 2 — LLM foundations

## What an LLM is

A **Large Language Model** is a neural network trained to predict the next token given previous tokens.

A token can be:

- a word;
- part of a word;
- punctuation;
- whitespace;
- a code fragment;
- a special control marker.

When you ask a model a question, it repeatedly predicts the next token until it reaches a stopping condition. Everything else — answers, code, plans, summaries, apparent reasoning — emerges from that loop plus training and post-training.

## Transformer

A **transformer** is the architecture behind modern LLMs. Its key idea is **attention**: the model learns which earlier tokens matter for predicting the next token.

Practical meaning:

- The model can connect concepts across a prompt.
- It can follow instructions, refer back to earlier details, and write coherent multi-step outputs.
- Long context is expensive and imperfect because every token competes for attention.

## Parameters

**Parameters** are the learned numbers inside the model. More parameters often mean more capability, but not always. Architecture, training data, post-training, tool use, context length, and inference strategy matter too.

Do not choose a model only by size. Choose by observed performance on your task.

## Pretraining

**Pretraining** is the broad initial training phase where a model learns language, code, facts, reasoning patterns, and structure from huge datasets.

## Post-training / instruction tuning

After pretraining, models are refined to be more useful and safer through:

- instruction tuning;
- supervised fine-tuning;
- reinforcement learning from human feedback or AI feedback;
- preference optimization;
- tool-use training;
- safety training.

This is why a chat model behaves differently from a raw base model.

## Inference

**Inference** is the act of running the model to generate output. When you pay per token, you are paying for inference.

Important inference settings:

- **temperature:** randomness/creativity;
- **top_p:** sampling cutoff;
- **max tokens:** output length limit;
- **reasoning effort:** how much hidden/visible thinking budget a reasoning model uses;
- **stop sequences:** strings that tell generation to stop.

## Context window

The **context window** is the maximum amount of input plus output the model can consider at once.

Practical implications:

- More context is not always better.
- Long context costs more.
- The model may miss details buried in the middle.
- For a large vault or codebase, retrieval and summaries often beat dumping everything into the prompt.

## Long context vs RAG

Use **long context** when:

- the source set is small enough;
- exact wording matters;
- you need cross-document comparison;
- the provider has strong long-context reliability.

Use **RAG** when:

- the knowledge base is large;
- only a few sections are relevant;
- notes change over time;
- you need citations/paths;
- cost matters.

## RAG

**Retrieval-Augmented Generation** means:

1. Store documents as chunks.
2. Embed chunks into vectors.
3. Search for relevant chunks at question time.
4. Put only the top results into the prompt.
5. Ask the LLM to answer from that retrieved context.

Good RAG depends more on data prep and retrieval quality than on model cleverness.

## Embeddings

An **embedding** is a numeric vector representing meaning. Similar text has vectors close together.

Use embeddings for:

- semantic search;
- duplicate detection;
- clustering notes;
- routing tasks;
- finding related examples;
- RAG retrieval.

the operator's Hermes/primary-agent profile already has a local Obsidian semantic-search bridge that indexes the Knowledge Hub with local Ollama embeddings when available.

## Vector database

A **vector database** stores embeddings and finds nearest neighbors quickly.

Options:

- SQLite + vector extension or custom table for small local systems;
- Chroma/Qdrant for local or small hosted RAG;
- Pinecone/Weaviate/Supabase pgvector for managed systems;
- cloud provider-native vector search for enterprise deployments.

## Prompt engineering

Prompt engineering means structuring instructions and context so the model produces reliable output.

A good prompt often includes:

- role or task;
- objective;
- inputs;
- constraints;
- required output format;
- examples;
- verification criteria;
- safety boundaries;
- what not to do.

## Context engineering

Context engineering is broader than prompting. It is deciding **what information reaches the model, in what order, at what level of detail, and with what trust level**.

It includes:

- system prompts;
- user messages;
- retrieved notes;
- tool schemas;
- memory;
- scratchpads;
- summaries;
- source citations;
- policy and safety rules;
- hidden implementation context.

For agent systems, context engineering is usually more important than clever wording.

## Tool use / function calling

Tool use lets a model call external functions with structured arguments.

Examples:

- read a file;
- search the web;
- run tests;
- create an n8n workflow;
- send email;
- query QuickBooks;
- update a CRM;
- create an Obsidian note.

Tool use turns an LLM from a text generator into an operator. That makes it more powerful and more dangerous.

## Agents

An **agent** is an LLM wrapped in a loop that can observe, reason, call tools, update state, and continue until a goal is complete.

A simple agent loop:

```text
receive task → inspect context → choose tool → call tool → observe result → continue or answer
```

Agent systems need:

- permission boundaries;
- logging;
- retries;
- error handling;
- tool restrictions;
- cost limits;
- tests/evals;
- human approval for risky actions.

## Workflows vs agents

A **workflow** follows predetermined steps. An **agent** decides steps dynamically.

Use a workflow when:

- the process is predictable;
- correctness matters;
- the same steps repeat;
- you need auditability;
- a client is paying for reliability.

Use an agent when:

- the task is open-ended;
- the path is uncertain;
- you need research, debugging, or planning;
- the system must choose tools based on observations.

The best systems combine both:

```text
n8n workflow trigger → LLM/agent step → validation → human approval → deterministic action
```

## MCP

**MCP** means Model Context Protocol. It is a standard way for tools and data sources to expose capabilities to LLM agents.

Mental model:

- MCP server = tool provider.
- Agent = client that connects to tools.
- Tools = functions such as search docs, create issue, query database, run workflow.

MCP is useful because it reduces one-off integrations, but it does not remove the need for permissions, secrets management, validation, and approval rules.

## Evaluations

An **evaluation** is a repeatable test of model/system behavior.

Examples:

- Did the model extract every invoice field correctly?
- Did the support-draft agent avoid sending without approval?
- Did the RAG system cite the correct source note?
- Did a workflow handle missing data?
- Did a coding agent pass tests?

For a business, evals are how you stop demos from becoming unreliable production systems.

## Guardrails

Guardrails are controls that prevent bad outcomes.

Examples:

- read-only mode by default;
- draft-first emails;
- approvals before writes;
- allowlisted tools;
- spending limits;
- customer-data isolation;
- logging;
- schema validation;
- rollback plans;
- manual review for accounting, tax, medical, legal, or customer-facing actions.

---

# Part 3 — Core LLM terminology glossary

## Must-know terms

- **API:** a way for software systems to communicate.
- **API key:** a secret credential used to access an API.
- **Autoregressive generation:** producing one token at a time based on previous tokens.
- **Base model:** pretrained model not necessarily optimized for chat/instructions.
- **Batch inference:** processing many requests asynchronously at lower cost or higher efficiency.
- **Benchmark:** standardized test of model performance; useful but often gamed or incomplete.
- **Cache hit:** reused context/input that costs less because the provider cached it.
- **Chain of thought:** hidden or visible intermediate reasoning; do not rely on seeing it for correctness.
- **Chunking:** splitting documents into retrieval-sized pieces.
- **Completion:** generated output.
- **Context window:** max tokens available for prompt plus output.
- **Embedding:** vector representation of meaning.
- **Fine-tuning:** training a model further on specialized data.
- **Function calling:** structured tool invocation by a model.
- **Grounding:** tying model output to retrieved sources or external facts.
- **Hallucination:** plausible but unsupported or false output.
- **Inference:** running a model to get output.
- **Instruction tuning:** training a model to follow instructions.
- **Latency:** time from request to response.
- **Mixture of experts:** architecture where only parts of a model activate for each token.
- **Model router:** logic that sends tasks to different models based on cost, capability, speed, or privacy.
- **Multimodal:** handles text plus images, audio, video, or files.
- **Output tokens:** tokens generated by the model.
- **Prompt injection:** malicious/untrusted content that tries to override instructions.
- **Quantization:** compressing model weights to run with less memory/compute.
- **RAG:** retrieval-augmented generation.
- **Reasoning model:** model designed to spend more compute on multi-step problems.
- **Sampling:** choosing tokens from probability distributions.
- **Schema validation:** checking output matches a required JSON/data shape.
- **System prompt:** high-priority instructions given to the model.
- **Temperature:** randomness setting.
- **Token:** unit of text processed by a model.
- **Tool call:** model-requested external action.
- **Vector search:** semantic similarity search over embeddings.

## Terms specific to coding agents

- **AGENTS.md:** instruction file often used by Codex/OpenAI-style coding agents.
- **CLAUDE.md:** instruction file used by Claude Code to understand project conventions.
- **Checkpoint:** restorable file state before edits.
- **Diff:** line-by-line code change.
- **Lint:** static check for style or likely errors.
- **PR:** pull request.
- **Repo:** code repository.
- **Test suite:** automated checks that prove code still works.
- **Worktree:** separate working copy of a git repo for isolated agent work.

## Terms specific to automation

- **Cron:** scheduled job.
- **Credential:** stored auth connection to an external service.
- **Execution:** one run of a workflow.
- **Idempotency:** safe to retry without duplicate side effects.
- **Node:** one step in n8n.
- **Retry policy:** what happens after failure.
- **Trigger:** event that starts a workflow.
- **Webhook:** URL that receives events from another system.
- **Workflow:** ordered automation steps.

---

# Part 4 — Current model landscape

## Important warning about model facts

Model availability, names, context windows, and pricing change constantly. Treat this section as a snapshot dated **2026-05-23**. Before building client pricing, check the provider pricing page directly.

The durable skill is not memorizing prices. The durable skill is knowing how to select and route models.

## Major model families

### OpenAI

Representative models/products:

- GPT-5 family / ChatGPT models;
- GPT-4.1 / 4o-era API models where still available;
- reasoning models;
- embeddings;
- image/audio models;
- Codex / coding-agent integrations.

Strengths:

- strong general reasoning and coding;
- broad tool ecosystem;
- excellent developer adoption;
- good structured output/tool calling;
- strong multimodal options;
- Codex-style coding workflows.

Weaknesses:

- pricing and model names change often;
- some ChatGPT/OAuth routes are separate from normal API usage;
- frontier models can be costly;
- behavior may vary by product surface.

Best use:

- general assistant workflows;
- coding agents;
- structured extraction;
- multimodal tasks;
- high-value reasoning.

### Anthropic Claude

Representative models/products:

- Claude Opus;
- Claude Sonnet;
- Claude Haiku;
- Claude Code;
- Claude Cowork / collaborative product surfaces;
- Claude web and desktop plans.

Strengths:

- strong writing, analysis, and coding;
- excellent long-document handling;
- strong instruction following;
- Claude Code is mature for agentic coding;
- good safety posture.

Weaknesses:

- API and subscription product limits differ;
- Opus-class models can be expensive;
- Claude Code may require careful project instructions and permissions.

Best use:

- codebase refactors;
- long document synthesis;
- careful writing;
- agentic development;
- planning and review.

Current pricing reference checked:

- Anthropic plan page showed Claude Free, Pro at about $17/month annual or $20 monthly, and Max from about $100/month, with Claude Code included in Pro/Max-style plans. API pricing should still be verified from Anthropic's developer/API pricing before estimating client workloads.

### Google Gemini

Representative models:

- Gemini Pro / Flash families;
- Gemini long-context models;
- Google Search grounding;
- multimodal models.

Strengths:

- very large context options;
- strong integration with Google ecosystem;
- competitive Flash pricing/speed;
- search grounding can be useful;
- good multimodal support.

Weaknesses:

- model/product naming changes often;
- quality can vary by task;
- grounding/search has separate pricing/limits;
- enterprise privacy settings must be understood.

Best use:

- long-context document tasks;
- Google Workspace-adjacent workflows;
- cost-sensitive high-volume summarization;
- multimodal tasks.

Current pricing reference checked:

- Google Gemini pricing page showed paid-tier examples around $1.50 per 1M input tokens and $9.00 per 1M output tokens for a high-end Gemini tier, with lower batch/flex pricing around $0.75 input and $4.50 output per 1M tokens in some modes. It also listed context caching and grounding/search charges. Verify exact model rows before use.

### xAI Grok

Representative models:

- Grok family models;
- xAI API models;
- X/Twitter-integrated surfaces.

Strengths:

- useful for X/Twitter-adjacent research and fast general chat;
- competitive frontier-model positioning;
- potentially useful for social/current-event workflows.

Weaknesses:

- ecosystem and enterprise tooling are less mature than OpenAI/Anthropic/Google;
- pricing and model docs should be checked directly;
- may not be the first choice for regulated client systems.

Best use:

- social-media-aware research;
- general assistant tasks;
- experimentation in model routing.

### Mistral

Representative models/products:

- Mistral Large / Medium / Small family;
- Le Chat;
- Mistral Vibe coding product;
- open-weight and enterprise deployment options.

Strengths:

- strong European provider option;
- open-weight models and deployment flexibility;
- good for privacy/custom deployment discussions;
- increasingly broad product suite.

Weaknesses:

- API pricing pages can be more complex to parse;
- model quality varies across tasks;
- ecosystem smaller than OpenAI/Anthropic.

Best use:

- European/privacy-sensitive deployments;
- self-host/open-weight strategies;
- cost-controlled assistants;
- coding/productivity experiments.

Current pricing reference checked:

- Mistral's pricing page showed Le Chat Free, Pro around $14.99/month, and Team around $24.99/user/month, plus API/enterprise sections. Verify API model prices directly for production estimates.

### DeepSeek

Representative models:

- DeepSeek chat/reasoning families;
- DeepSeek V4 Flash/Pro pricing page as checked;
- OpenAI-compatible and Anthropic-format APIs.

Strengths:

- very low token prices;
- strong reasoning/coding value for cost;
- OpenAI-compatible endpoints simplify integration;
- useful fallback/cheap routing option.

Weaknesses:

- privacy/compliance must be evaluated carefully for client data;
- geopolitical/provider-risk considerations;
- model names and discounts change;
- not ideal for sensitive accounting/client workflows unless policy allows.

Best use:

- cost-sensitive experimentation;
- non-sensitive coding/reasoning;
- background summarization;
- fallback routing.

Current pricing reference checked:

- DeepSeek pricing page showed per-1M-token pricing with very low cache-hit input prices, cache-miss input around $0.14 for one Flash row and higher for Pro, and output around $0.28 for one Flash row and higher for Pro, with promotional discounts noted. Verify exact row/model before using.

### OpenRouter

OpenRouter is not a model family. It is a routing platform that gives one API surface for many providers.

Strengths:

- compare models quickly;
- route by cost/quality;
- fallback across providers;
- easy experimentation.

Weaknesses:

- adds another vendor layer;
- privacy/data handling depends on routed provider and settings;
- pricing can differ from direct provider;
- not always ideal for regulated/client-sensitive data.

Best use:

- experimentation;
- non-sensitive routing;
- fallback models;
- rapid model comparisons.

### Local/open-weight models

Examples:

- Llama-family models;
- Qwen-family models;
- Mistral open models;
- DeepSeek distilled/open variants;
- embedding models like nomic-embed-text.

Strengths:

- privacy and local control;
- no per-token API bill;
- good for embeddings, classification, simple extraction, local RAG;
- useful offline or on private systems.

Weaknesses:

- hardware requirements;
- setup complexity;
- slower than cloud frontier models;
- quality may lag for hard reasoning;
- maintenance burden.

Best use:

- local semantic search;
- private notes;
- draft classification;
- simple automations;
- experimentation.

---

# Part 5 — How to choose a model

## The model-selection questions

Ask these before choosing:

1. Does the task involve sensitive/private/client data?
2. Does it require frontier reasoning or just summarization/classification?
3. Is latency important?
4. Is cost important?
5. Does it need long context?
6. Does it need tool use or structured JSON?
7. Does it need images/audio/files?
8. Does it need code edits?
9. Will the output be reviewed by a human?
10. What happens if the model is wrong?

## Default routing strategy

Use this default strategy for the operator-style systems:

- **High-stakes reasoning/coding:** Claude Sonnet/Opus, GPT-5-class, or the strongest available coding model.
- **Routine summaries/extraction:** cheaper fast model such as Gemini Flash-class, Haiku-class, mini-class, or local model if privacy matters.
- **Embeddings/search:** local embeddings where possible for private notes; managed embeddings for client systems when allowed.
- **Draft-first customer communication:** strong mid/high model with human approval.
- **Accounting/tax/QuickBooks:** read-only/draft/reporting first; no live writes without approval.
- **Large vault/codebase:** retrieval first, then model answer with citations.

## Cost mental model

Most API LLMs charge by:

```text
input tokens + output tokens + optional cached tokens + optional tool/search/image/audio charges
```

Cost goes up when:

- prompts are long;
- outputs are long;
- agents loop many times;
- tools return huge data;
- you use frontier models for trivial tasks;
- you fail/retry often;
- you include raw HTML, full logs, or whole vault dumps.

Cost goes down when:

- you retrieve only relevant chunks;
- you summarize intermediate data locally;
- you use cheaper models for easy tasks;
- you cache stable context;
- you validate early;
- you stop loops when success criteria are met.

---

# Part 6 — Claude Code

## What Claude Code is

Claude Code is Anthropic's agentic coding tool. It reads a codebase, follows instructions, edits files, runs commands/tests, and helps implement changes.

Mental model:

```text
Claude Code = senior pair programmer + terminal operator + codebase navigator
```

## What Claude Code is good for

- understanding existing codebases;
- refactoring;
- writing tests;
- debugging;
- implementing features;
- updating docs;
- working across many files;
- using project instructions from `CLAUDE.md`;
- running shell commands and tests under supervision.

## What Claude Code is not

- not a replacement for requirements;
- not automatically safe with secrets;
- not a production deployment authority unless explicitly approved;
- not guaranteed correct without tests/review;
- not ideal for deterministic workflow orchestration.

## Claude Code operating pattern

Use this sequence:

1. Create or update `CLAUDE.md` with project rules.
2. Ask it to inspect before editing.
3. Ask for a plan.
4. Approve the plan.
5. Let it edit in small steps.
6. Run tests.
7. Review diff.
8. Commit only after verification.

## Claude Code best prompts

Examples:

```text
Inspect this repo and explain the architecture. Do not edit files yet.
```

```text
Find the root cause of this failing test. Do not patch until you can explain the failure path.
```

```text
Implement this feature in the smallest safe diff. Add or update tests. Run the relevant test suite. Summarize files changed.
```

## Claude Code safety rules

- Do not let it commit secrets.
- Do not let it deploy production without approval.
- Do not let it run destructive commands without understanding them.
- Keep project instructions current.
- Use git branches/worktrees for bigger changes.

---

# Part 7 — Codex

## What Codex is

Codex is OpenAI's coding-agent family/product surface for terminal or IDE-based software work. In the operator's Hermes setup, some profiles use OpenAI Codex OAuth and GPT-5.5-style access through Hermes.

Mental model:

```text
Codex = fast coding/execution partner, especially useful in terminal-driven workflows
```

## What Codex is good for

- code generation;
- terminal-driven edits;
- quick implementation loops;
- debugging;
- repo inspection;
- structured patches;
- pairing with tests;
- agent workflows using `AGENTS.md` guidance.

## Codex vs Claude Code

Use Claude Code when:

- long codebase reasoning matters;
- writing quality and planning depth matter;
- you want mature Anthropic coding workflow behavior.

Use Codex when:

- you want OpenAI model behavior;
- you are already in a Codex/Hermes profile;
- fast terminal patch/test loops matter;
- a project has `AGENTS.md` guidance.

Use both when:

- one implements and the other reviews;
- one investigates and the other patches;
- you want model diversity for hard bugs.

## Codex safety rules

- Keep `AGENTS.md` accurate.
- Require tests and diff review.
- Use branch/worktree isolation.
- Do not let it modify auth files or secrets.
- Do not deploy or push without explicit approval.

---

# Part 8 — Hermes Agent

## What Hermes is

Hermes Agent is a provider-agnostic AI agent framework that runs through CLI, Telegram, and other gateways. It can use tools, memory, skills, MCP servers, cron jobs, local files, shell commands, browser automation, and messaging integrations.

Mental model:

```text
Hermes = personal operating agent + tool harness + memory/skills system + gateway
```

the operator's current pattern:

- primary-agent = main Telegram-first personal agent.
- service-agent = sober-living/operations counterpart.
- gis-agent = GIS counterpart.
- coding-agent = coding/profile counterpart.
- Obsidian Knowledge Hub = durable second brain.
- Telegram = practical control surface.

## Hermes concepts

### Profile

A separate Hermes identity/config with its own memory, skills, sessions, tools, gateway, and sometimes bot token.

### Toolset

A category of tools: terminal, file, web, browser, memory, cron, messaging, etc.

### Skill

Procedural memory: a reusable workflow saved as Markdown that Hermes loads when relevant.

### Memory

Durable compact facts about the user, environment, or stable preferences.

### Session

A conversation thread with history and token usage.

### Gateway

Messaging bridge: Telegram, Discord, Slack, email, etc.

### Cron

Scheduled autonomous run.

## What Hermes is good for

- personal assistant workflows;
- Obsidian note creation/search/synthesis;
- scheduled daily/weekly briefs;
- tool orchestration;
- profile-specific agents;
- local automation;
- coding with terminal/file tools;
- agent-service prototypes.

## Hermes weaknesses/pitfalls

- Too many tools/MCP schemas can bloat context.
- Long Telegram sessions can trigger compression/timeouts.
- Profiles need separate auth/gateway setup.
- Tool access is powerful and must be bounded.
- Gateway writes/actions should be approval-first.

## Hermes best practices

- Use low-token web scraping: scripts/APIs/RSS/static fetch first, browser only if needed.
- Save durable procedures as skills, not long memories.
- Keep profile SOUL files concise and role-specific.
- Use read-only/draft-first for external systems.
- Verify after writes/actions.
- Restart gateways after config/tool/skill changes.

---

# Part 9 — n8n

## What n8n is

n8n is a workflow automation platform. It connects apps, APIs, triggers, conditions, transformations, AI nodes, and webhooks.

Mental model:

```text
n8n = visual workflow engine for repeatable business processes
```

## Core n8n concepts

### Workflow

The whole automation.

### Node

One step in the workflow.

### Trigger

The event that starts the workflow: schedule, webhook, email, form submission, app event.

### Connection

The wiring between nodes.

### Expression

Dynamic value pulled from previous data, like `{{$json.email}}`.

### Credential

Stored connection/auth to an external app.

### Execution

One run of the workflow.

### Error workflow

A separate workflow that handles failures.

### Webhook

A URL that lets another system call n8n.

## What n8n is good for

- predictable automations;
- app-to-app workflows;
- scheduled syncs;
- webhooks;
- simple ETL;
- notifications;
- approval pipelines;
- AI steps embedded in deterministic flows.

## What n8n is not good for by itself

- fully flexible reasoning;
- deep codebase edits;
- complex long-running agent tasks;
- secure multi-tenant SaaS isolation without careful architecture;
- replacing application code for complex products.

## n8n + agents

Best pattern:

```text
n8n handles trigger, routing, credentials, retries, logging
Hermes/Claude/Codex handles reasoning or code-heavy steps
Human approves risky output
n8n performs deterministic final action
```

Example:

```text
New email → n8n fetches metadata → LLM drafts summary/actions → human approves → n8n creates task/calendar draft
```

## n8n production rules

- Use Docker for production-like deployment.
- Back up the database.
- Separate credentials per client.
- Use error workflows.
- Log executions.
- Avoid raw secrets in workflow JSON.
- Use staging/test workflows before production.
- Keep high-risk actions approval-gated.

## QuickBooks/n8n correction

For the operator's current interest, the main direction is not "pull random data into QuickBooks." It is often:

```text
QuickBooks → CRM/dashboard/portal/tasks/reporting/migration-prep
```

Examples:

- QuickBooks invoices → client dashboard;
- QuickBooks customer/payment status → CRM enrichment;
- QuickBooks aging/open invoices → weekly report;
- QuickBooks vendor/customer data → migration prep;
- QuickBooks events → Slack/Telegram approval or task;
- QuickBooks data → CPA/client portal.

Safety rule:

- Start read-only.
- No live QuickBooks/tax/accounting writes without explicit human approval.
- Treat accounting data as sensitive.
- Log every data movement.

---

# Part 10 — Claude Cowork and collaborative AI work

## What Claude Cowork means in practice

Claude Cowork refers to Anthropic's collaborative/workplace AI direction: Claude embedded into team workflows, shared projects, files, connectors, and enterprise contexts.

Even if the product surface changes, the concept matters:

```text
AI cowork = AI working inside shared team context, not just a private chat
```

## Why this matters

For clients, the value is not "chat with a bot." The value is:

- shared project context;
- company docs connected;
- team workflows assisted;
- meeting/action follow-up;
- drafting and review;
- knowledge retrieval;
- role-specific assistants;
- governed access.

## How to think about it for service work

A client AI coworker needs:

- clear role;
- data boundaries;
- allowed sources;
- allowed actions;
- escalation rules;
- audit trail;
- human owner;
- onboarding docs;
- offboarding/revocation process.

This maps directly to Hermes profiles, Claude projects, custom GPTs, n8n workflows, and client-specific Obsidian/Notion/Drive knowledge bases.

---

# Part 11 — AI automation service architecture

## The practical stack

For the operator, a realistic service stack is:

```text
Client communication surface
  Telegram / Slack / email / web portal

Workflow layer
  n8n / cron / webhooks / FastAPI

Agent layer
  Hermes profiles / Claude Code / Codex / custom agents

Knowledge layer
  Obsidian / Google Drive / Notion / client docs / vector index

Application layer
  CRM / QuickBooks / calendar / email / GIS / dashboards

Safety layer
  approvals / logs / backups / permissions / evals
```

## What customers are buying

They are not buying "LLMs" or "Hermes."

They are buying:

- fewer missed leads;
- faster follow-up;
- less admin chaos;
- better reporting;
- cleaner handoffs;
- organized tasks;
- fewer open loops;
- owner time back;
- safer decision support.

## Best first service offer

A strong first offer:

```text
Private AI Operations Assistant
```

Promise:

> I install and operate a private AI assistant that turns scattered messages, meetings, calendars, documents, and business notes into organized tasks, drafts, reminders, reports, and weekly open-loop reviews.

## Why operator-led first

Do not start by selling full autonomy. Start with human-supervised, read-only/draft-first service.

This is safer because:

- you catch model errors;
- clients build trust;
- you learn real workflows;
- you avoid accidental external actions;
- you can charge for operation, not just software.

## Starter workflows

### 1. Daily brief

Inputs:

- email;
- calendar;
- tasks;
- recent notes.

Output:

- what matters today;
- open loops;
- meetings;
- suggested replies;
- blocked items.

### 2. Meeting notes to tasks/SOPs

Inputs:

- transcript;
- notes;
- agenda.

Output:

- action items;
- owners;
- deadlines;
- SOP updates;
- follow-up drafts.

### 3. Customer follow-up drafts

Inputs:

- inbox/CRM messages;
- customer record;
- job status.

Output:

- draft reply;
- next task;
- escalation flag.

Human approves before sending.

### 4. Open-loop report

Inputs:

- messages;
- project notes;
- tasks;
- calendar.

Output:

- unresolved questions;
- waiting-on items;
- stale leads;
- missed follow-ups.

### 5. QuickBooks outbound reporting

Inputs:

- QuickBooks invoices/customers/payments/vendors;
- read-only API access;
- schedule.

Output:

- aging report;
- dashboard;
- CRM enrichment;
- client portal update;
- task list for follow-up.

Human approves any writeback.

---

# Part 12 — Implementation path from beginner to expert

## Phase 0 — Setup discipline

Goal: know where things live and how not to break them.

Learn:

- terminal basics;
- file paths;
- git basics;
- environment variables;
- API keys vs OAuth;
- Obsidian structure;
- how to verify work.

Build:

- one project folder;
- one learning log;
- one glossary note;
- one test repo.

## Phase 1 — LLM fundamentals

Goal: understand how LLM systems work.

Learn:

- tokens;
- context windows;
- prompts;
- embeddings;
- RAG;
- tool use;
- agents vs workflows;
- model cost;
- hallucination and verification.

Build:

- a prompt library;
- a model-cost calculator;
- a small RAG search over notes;
- a glossary quiz.

## Phase 2 — Coding agents

Goal: use Claude Code and Codex safely.

Learn:

- `CLAUDE.md`;
- `AGENTS.md`;
- git diff;
- tests;
- lint;
- debugging workflow;
- worktrees;
- code review.

Build:

- a small FastAPI app;
- a bugfix with tests;
- a simple dashboard;
- a repo with both Claude and Codex guidance.

## Phase 3 — Hermes operations

Goal: operate personal/profile agents.

Learn:

- profiles;
- tools;
- skills;
- memory;
- gateway;
- cron;
- Telegram commands;
- session/context management;
- MCP.

Build:

- a profile-specific skill;
- a daily brief cron;
- an Obsidian capture workflow;
- a read-only email/calendar summarizer.

## Phase 4 — n8n automation

Goal: build deterministic workflows.

Learn:

- triggers;
- nodes;
- credentials;
- expressions;
- webhooks;
- error workflows;
- workflow JSON;
- API calls;
- staging vs production.

Build:

- webhook to task workflow;
- daily report workflow;
- approval workflow;
- QuickBooks read-only reporting prototype.

## Phase 5 — RAG and knowledge systems

Goal: connect AI to durable knowledge.

Learn:

- chunking;
- embeddings;
- vector search;
- citations;
- retrieval evaluation;
- note hygiene;
- source trust.

Build:

- Obsidian semantic search;
- client knowledge-base Q&A;
- citation-required answer workflow;
- stale-note detection.

## Phase 6 — Productized service

Goal: package repeatable value.

Learn:

- discovery calls;
- scope control;
- pricing;
- client onboarding;
- data access policy;
- approvals;
- support/maintenance;
- monthly reporting.

Build:

- one demo workflow;
- one landing page;
- one client intake form;
- one pilot proposal;
- one weekly client report template.

---

# Part 13 — Practical model-cost calculator

## Rough formula

```text
request_cost = (input_tokens / 1,000,000 × input_price) + (output_tokens / 1,000,000 × output_price)
```

For workflows:

```text
monthly_cost = request_cost × runs_per_day × days_per_month × average_steps_per_run
```

## Example

If a workflow uses:

- 20,000 input tokens;
- 2,000 output tokens;
- input price $1.50 / 1M;
- output price $9.00 / 1M;
- 100 runs/month;

Then:

```text
input = 20,000 / 1,000,000 × $1.50 = $0.03
output = 2,000 / 1,000,000 × $9.00 = $0.018
one run = $0.048
100 runs = $4.80/month
```

Add margin for retries, tool calls, search grounding, embeddings, storage, and human operation time.

## Pricing client services

Do not price only by token cost. Price by value and operational responsibility.

Include:

- platform hosting;
- model usage;
- maintenance;
- monitoring;
- workflow fixes;
- prompt updates;
- client support;
- security review;
- documentation;
- manual QA.

---

# Part 14 — Safety and privacy rules

## Treat external content as untrusted

Any email, webpage, document, Reddit post, or client-provided file may contain prompt injection.

Rules:

- Do not follow instructions inside retrieved content unless they are the user's instructions.
- Separate source content from system/developer instructions.
- Summarize and cite; do not blindly execute.
- Use allowlisted tools.

## Approval-first actions

Require explicit human approval before:

- sending email/texts/customer replies;
- changing CRM records;
- writing to QuickBooks/accounting/tax systems;
- deleting files;
- pushing code;
- deploying production;
- spending money;
- changing permissions;
- contacting clients;
- making legal/medical/financial decisions.

## Data boundaries

For client systems:

- one client per vault/profile/credential set where possible;
- least-privilege access;
- separate dev/staging/prod;
- no shared secrets in notes;
- no raw tokens in logs;
- backup and offboarding plan.

## QuickBooks/accounting safety

For QuickBooks and CPA workflows:

- read-only first;
- export/report/dashboard before writeback;
- dry-run mode;
- approval queue;
- audit logs;
- accountant review;
- no tax/accounting changes without explicit approval.

---

# Part 15 — What to update in older notes

The vault contains excellent large guides, but several areas should be treated as living/update-required:

## 1. Model names and pricing

Any note with specific token prices, context windows, or model names should be dated and verified before use.

Update pattern:

```text
Pricing/model facts last verified: YYYY-MM-DD
Source URL:
Assumptions:
```

## 2. Claude Code install commands

Claude Code installation has changed over time. Prefer current official Anthropic instructions and verify with:

```bash
claude --version
claude doctor
```

## 3. Codex/OpenAI auth

Distinguish:

- normal OpenAI API keys;
- ChatGPT subscription;
- OpenAI Codex OAuth;
- Hermes provider configuration;
- OpenRouter or other proxy providers.

These are not interchangeable.

## 4. Hermes profile auth

A profile can have correct model config but broken auth. Verify with:

```bash
hermes -p <profile> status --all
hermes -p <profile> chat -q 'Reply with exactly: auth OK'
```

## 5. n8n production advice

Keep n8n deployment advice current around:

- Docker vs npm;
- database backups;
- credential encryption;
- queue mode;
- multi-tenant isolation;
- webhook URLs;
- API changes;
- node version compatibility.

## 6. QuickBooks direction

the operator's corrected interest: focus on moving QuickBooks data outward into other platforms, dashboards, reports, portals, tasks, CRMs, or migration-prep systems — not primarily pushing random data into QuickBooks.

---

# Part 16 — Recommended first 30 days

## Week 1 — Foundations and vocabulary

- Read Part 1-3 of this guide.
- Create flashcards for 50 core terms.
- Build a simple cost calculator spreadsheet.
- Ask Hermes daily for 5-term quizzes.
- Read The Comprehensive AI & Agents Learning Guide sections on LLMs, tokens, context, embeddings, RAG, and agents.

## Week 2 — Coding agents

- Read Claude Code — Consolidated Master Guide.
- Create a tiny repo.
- Add `CLAUDE.md` and `AGENTS.md`.
- Use Claude Code for one feature.
- Use Codex or Hermes for review.
- Run tests and inspect diffs.

## Week 3 — Hermes and Obsidian

- Read Hermes Agent: A Beginner's Guide.
- Learn profiles, skills, memory, tools, gateway, cron.
- Create one small skill.
- Build one Obsidian capture workflow.
- Use semantic search over Knowledge Hub.

## Week 4 — n8n and service prototype

- Read [n8n Complete Learning Guide](../N8n/n8n-complete-learning-guide.md).
- Build a webhook workflow.
- Add an LLM summarization step.
- Add human approval.
- Build one demo: email/calendar/meeting notes to tasks.
- Draft the offer based on AI Agent Service - 7 Day Operational Launch Plan.

---

# Part 17 — Practice projects

## Beginner projects

1. Build an LLM glossary note with examples.
2. Create a model-cost calculator.
3. Summarize one long note with citations.
4. Build a prompt template for customer follow-up drafts.
5. Use Claude Code to create a simple FastAPI app.

## Intermediate projects

1. Obsidian semantic search assistant.
2. n8n webhook to Telegram approval workflow.
3. Meeting transcript to tasks/SOPs workflow.
4. QuickBooks read-only invoice aging report.
5. Client open-loop report generator.

## Advanced projects

1. Multi-profile Hermes client assistant.
2. RAG system with evals and citations.
3. n8n + FastAPI + Hermes approval platform.
4. GIS AI assistant for ArcGIS workflows.
5. Productized AI operations assistant pilot.

---

# Part 18 — Expert checklist

You are becoming expert when you can:

- explain tokens, context, embeddings, RAG, tool use, agents, and evals simply;
- choose models based on task, privacy, cost, and quality;
- build deterministic workflows and agentic workflows;
- use Claude Code/Codex safely with tests;
- operate Hermes profiles, skills, memory, cron, and gateway;
- build n8n workflows with error handling and approvals;
- design read-only/draft-first client systems;
- estimate token and platform costs;
- create audit logs and rollback plans;
- turn recurring workflows into service offers;
- explain risks and limits honestly.

---

# Part 19 — One-page reference

## Model choice

- Hard coding/reasoning: Claude/GPT-5-class/frontier coding model.
- Cheap summarization: Flash/mini/Haiku/local.
- Long context: Gemini/Claude long-context class, but still retrieve where possible.
- Private notes: local embeddings/local models where possible.
- Experimentation: OpenRouter or sandbox provider.

## Tool choice

- Codebase work: Claude Code or Codex.
- Personal operating agent: Hermes.
- Repeatable app automation: n8n.
- Knowledge base: Obsidian + semantic search/RAG.
- APIs/products: FastAPI + database + auth.
- Client service: simple messaging/portal + approvals + reports.

## Safety default

```text
Read → summarize → draft → ask approval → write/send/update
```

Never jump directly from AI suggestion to external write in sensitive systems.

## Best next move

Build one demo that combines the whole stack:

```text
Inbox/calendar/meeting notes → AI summary → task list → human approval → Obsidian/client report
```

Then adapt the same pattern to a niche: home services, CPA/QuickBooks reporting, GIS operations, or sober-living operations.
