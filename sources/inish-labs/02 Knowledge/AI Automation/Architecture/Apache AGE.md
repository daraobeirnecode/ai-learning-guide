---
title: "Apache AGE"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# Apache AGE

## Plain-English definition

Apache AGE ("A Graph Extension") turns [Postgres](Postgres.md) into a **graph database** — a database organised around *things and the relationships between them*, rather than rows in tables. In a graph, entities are **nodes** (a parcel, a road, a fire station) and relationships are **edges** connecting them (`ADJACENT_TO`, `CONTAINED_IN`, `ACCESSED_VIA`). Graphs excel at questions that hop across multiple relationships: "which parcels are adjacent to a parcel that borders the burn zone and are accessed via the same road?" — awkward in normal SQL, natural in a graph.

## How it actually works

- **Nodes and edges as first-class data.** AGE stores a "property graph" inside Postgres: nodes and edges each carry a label (their type) and arbitrary properties (attributes). You create graphs with functions like `create_graph('spatial_graph')` and define labels for node types (`Parcel`, `Road`, `Fire`) and edge types (`ADJACENT_TO`, `NEAREST_FIRE_5KM`).
- **The Cypher query language.** AGE implements **openCypher**, the standard graph query language, embedded inside SQL. A pattern like `MATCH (p:Parcel)-[r*1..2]-(n)` reads almost like a diagram: "find parcels, follow any relationships one to two hops out, return what's connected." Multi-hop traversals that would take a tangle of self-joins in SQL become one readable pattern.
- **Still just Postgres.** The graph lives in the same database instance as everything else — same backups, same transactions, same access controls. (One quirk: AGE needs a `LOAD 'age'` and a `search_path` setting per session before use.)

## What it's used for in the GIS + AI server

AGE is the **multi-hop reasoning** leg of the retrieval trio ([PostGIS](PostGIS.md) = geometry, [pgvector](pgvector.md) = meaning, AGE = relationships):

- The relationships themselves are **derived by PostGIS spatial math**, not invented: a `CONTAINED_IN` edge exists because `ST_Contains` proved it, with a confidence score and provenance recorded. AGE is where those proven relationships become traversable.
- During a Spatial RAG query, after vector search finds candidate entities, the **graph expansion** step walks 1–2 hops of edges around each candidate to pull in connected context — the road that serves a parcel, the boundary that contains it, the hazard zone nearby. This connected neighbourhood is what lets the AI compose answers grounded in real relationships.
- The build treats AGE as an upgrade path: the stack starts with a plain `edges` table walked by recursive SQL, and promotes to a real AGE graph when questions need deeper multi-hop reasoning.

## Why a graph *inside* Postgres matters

The alternative — running a separate graph database like Neo4j — would mean a second system to secure, back up, and keep synchronized with the spatial data. The deploy guide's core principle is that spatial data, embeddings, and the graph live in **one database**, so a single query (and a single nightly backup) covers all three.

## Related

[Postgres](Postgres.md) · [PostGIS](PostGIS.md) · [pgvector](pgvector.md) · Spatial RAG · [Architecture Overview](Architecture%20Overview.md)
