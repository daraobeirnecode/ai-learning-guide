---
title: "Retrieval without the jargon"
source_collection: "Knowledge Hub"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Retrieval without the jargon

> "Retrieval" is the broader name for "find the relevant context and put it in front of the model." It is much less mystical than the term suggests.

## What it actually is

When you do `@file.py` in Claude Code, you're doing retrieval. The file gets pulled into context. The model now has access to its contents.

When you ask Claude Code to find functions matching a pattern, the bash grep call is retrieval.

When an MCP server's `vault_search` tool returns matching notes, that's retrieval.

When a "RAG" (Retrieval-Augmented Generation) system uses embeddings to find semantically similar documents — that's also retrieval. But the embeddings are an implementation detail, not the concept itself.

## The three flavors

| Flavor | How it finds things | When it's enough |
|---|---|---|
| **Direct reference** | You name the file explicitly | You know what you want |
| **Substring / pattern match** | grep, ripgrep, SQL LIKE, etc. | You can describe what you want in keywords |
| **Semantic / embedding** | Vector similarity over learned representations | The thing you want is described differently than how it's written |

Most people reach for embeddings first because that's what the blog posts talk about. But the order of usefulness is roughly the reverse: most retrieval tasks are solved by direct reference, the next chunk by pattern match, and only the residual needs semantic.

## Why semantic isn't always better

Embedding-based retrieval has real costs:

- Indexing infrastructure (a vector DB, an embedding model, periodic re-indexing)
- Embeddings drift when the underlying model changes
- Debugging is hard (why did *this* doc match? semantic similarity is opaque)
- The "match" can be subtly wrong in ways grep wouldn't be

For a personal vault of a few thousand notes, ripgrep with good scoping rules will outperform a poorly-tuned vector setup. It also costs zero infrastructure.

When embeddings actually pay off: large corpora where users phrase queries differently than authors phrased content, and where the cost of indexing infrastructure is amortized over many users.

## The pattern that matters

What unifies all retrieval is: **what you index determines what the agent can find**. Three implications:

1. **Index the right things.** A vault search that indexes filenames only will miss content. A search that indexes everything including media metadata will be noisy. Tune what's in the index.

2. **Scope queries.** Searching "Python" across your whole vault returns hundreds of hits. Searching "Python" within `AI/Sessions/` from the last month returns five. Scope is the cheapest precision-boost.

3. **Return enough context, not too much.** Tool results go into the agent's context window. A tool that returns 50 full files exhausts the budget. A tool that returns 5 file paths plus 200-character previews is much more usable.

## Implications for your MCP server

Project 4 has you building a vault search tool. The design choices that matter:

- **Index**: just search file contents, or include filenames and frontmatter? (Include all three.)
- **Scope**: should the tool accept a folder filter? a tag filter? (Yes to both, optional.)
- **Return shape**: full file contents, or paths plus snippets? (Paths plus snippets, with a separate `vault_get` tool for full retrieval.)

These choices have nothing to do with embeddings. They're what makes the retrieval useful in practice.

## Where to go next (only if needed)

If you ever want to add semantic retrieval to your vault:

- Embed each note with a small local embedding model (e.g., a sentence-transformers model running via Ollama)
- Store vectors alongside files; re-embed on file change
- Query: embed the search term, find nearest neighbors

This is a 2-day project, not a 2-week one. But don't do it until you've used the simpler version for at least a month and identified specific queries that fail.

## What I noticed about retrieval in my workflow

*Fill this in over time:*

- 

## Related

- [tool-use-and-mcp](tool-use-and-mcp.md) — tools are how retrieval is exposed to agents
- [context-as-input](context-as-input.md) — retrieval is the act of choosing what enters context
- Project brief: `AI/Projects/04-vault-query-mcp-server.md`
