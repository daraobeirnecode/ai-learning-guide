---
title: "Tool use and MCP"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Tool use and MCP

> Agents extend their reach by calling tools; MCP is the protocol that makes that portable.

## What "tool" means in agent-speak

A tool is a function the model can call. The model doesn't execute the function. It produces a structured request — "call `read_file` with argument `path='./main.py'`" — and the agent runtime executes the function. The result goes back into the model's context as a "tool result," and the model continues.

This is sometimes called "function calling" in API documentation. Same concept, different word.

## The full flow

```
1. User: "Find notes about retrieval"

2. Model thinks: I should search the vault.
   Produces: { "tool_call": "vault_search",
               "args": { "query": "retrieval" } }

3. Agent runtime: actually calls vault_search("retrieval")
   Gets back: ["notes/foo.md", "notes/bar.md"]

4. Result goes into model's context as a tool_result block

5. Model reads the tool result, thinks: now I should read those files.
   Produces: { "tool_call": "read_file",
               "args": { "path": "notes/foo.md" } }

6. ... and so on, until the model decides it has enough to answer ...

7. Model: "I found two notes about retrieval. Here's a summary..."
```

Every Claude Code action you've seen is a tool call:

- "Read file foo.py" → `read` tool
- "Edit foo.py" → `edit` tool  
- "Run pytest" → `bash` tool
- "Search the web" → `web_search` tool

The agent loop from [the-agent-loop](the-agent-loop.md) is *literally* a loop of tool calls.

## What MCP adds

Before MCP (Model Context Protocol), every agent had its own way of defining tools. Anthropic's tools, OpenAI's tools, Cursor's extensions, ChatGPT plugins — all incompatible.

MCP standardizes three things:

1. **How tools describe themselves** (name, args, return type)
2. **How agents discover available tools** (a `list_tools` capability)
3. **How agents call tools** (a `call_tool` capability with structured args)

A server written to MCP spec works with Claude Code, Codex, Cursor, and any future client that speaks MCP. You don't rewrite the integration when you switch tools.

## The three MCP primitives

MCP servers can expose three kinds of things:

**Tools** — functions with side effects (write files, run queries, send emails). The agent calls these and uses the results.

**Resources** — read-only data the agent can fetch (file contents, records, content blobs). Lighter weight than tools; no side effects.

**Prompts** — pre-built prompt templates the server provides. The user (or agent) can invoke them.

For most servers, tools are the main event. Resources are useful for "expose this content but don't make it a function call." Prompts are rarely used in practice.

## What this means for you

Two things:

**Consuming MCP servers.** When you install a GitHub MCP server, a Postgres MCP server, an Obsidian MCP server — you're handing your agent new tools. The agent loop gets bigger; the agent's reach expands. The cost is complexity (more failure modes, more trust analysis).

**Building MCP servers.** When you have a tool you wish Claude could call — a database query, a custom search, an API integration — you can build it once and use it with any MCP client. The protocol is small enough that a useful server is well under 100 lines.

Project 4 in this curriculum has you building one. Once you've built one, every other MCP server in the world becomes legible. The protocol stops being magic.

## Trust caveats

Every MCP tool inherits the trust questions from [trust-and-sandboxing](trust-and-sandboxing.md). Three to keep in mind:

1. **MCP servers run as you.** A buggy or malicious MCP server has all the permissions your user has. Vet sources.
2. **MCP credentials in config files are often unencrypted.** If a server needs an API token, that token sits in `~/.claude/settings.json` or `~/.codex/config.toml`. Scope tokens narrowly.
3. **Some MCP tools advertise themselves as "destructive."** These bypass the "never" approval policy and ask anyway. This is by design — don't try to disable it.

## My installed MCP servers

*Track what's running and why:*

- 

## Related

- [the-agent-loop](the-agent-loop.md) — tools are what "act" actually means
- [trust-and-sandboxing](trust-and-sandboxing.md) — each tool needs its own trust analysis
- [retrieval-without-the-jargon](retrieval-without-the-jargon.md) — most useful MCP servers do retrieval
- Project brief: `AI/Projects/04-vault-query-mcp-server.md`
