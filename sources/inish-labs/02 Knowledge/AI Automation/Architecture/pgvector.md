---
title: "pgvector"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# pgvector

## Plain-English definition

pgvector is an extension that lets [Postgres](Postgres.md) store and search **embeddings** — the long lists of numbers that AI models use to represent meaning. With pgvector installed, the database can answer "find me the rows most *similar in meaning* to this query", not just "find rows where the name equals X". It turns the ordinary database into a semantic search engine, removing the need for a separate specialised "vector database" product.

## How it actually works

- **What an embedding is.** An embedding model (here Voyage) reads a piece of text and outputs a fixed-length list of numbers — in this stack, 1,024 of them — positioned so that texts with similar meaning get numerically similar lists. "Vacant parcel near a school" and "empty lot beside an elementary campus" land close together even though they share almost no words.
- **A vector column type.** pgvector adds a `VECTOR(n)` column type, so each row in the `entities` table stores its geometry, its attributes, *and* its 1024-number meaning-fingerprint together. One critical rule from the guide: **dimensions are sticky** — every embedding in a column must come from the same model at the same size; you can never mix.
- **Similarity search.** The `<=>` operator computes cosine distance between vectors (how far apart two meanings are). `ORDER BY embedding <=> :query LIMIT 50` returns the 50 most semantically similar rows.
- **Approximate indexes.** Comparing a query against millions of 1024-number vectors one-by-one would be slow, so pgvector builds an **HNSW index** — a "small world" graph structure that hops between neighbourhoods of similar vectors and finds near-matches in milliseconds, trading a sliver of exactness for enormous speed. (IVFFlat is the simpler alternative index for smaller datasets.)

## What it's used for in the GIS + AI server

pgvector is the **semantic recall** leg of the three-legged retrieval design (geometry via [PostGIS](PostGIS.md), meaning via pgvector, relationships via [Apache AGE](Apache%20AGE.md)):

1. At ingestion, every spatial entity gets a short normalized text descriptor ("parcel: 123 Main St. Attributes: zoning R-1, 0.2 acres…") which Voyage turns into a `VECTOR(1024)` embedding stored on the row.
2. At query time, Spatial RAG embeds the user's question the same way and asks pgvector for the top-50 most similar entities — optionally pre-filtered by PostGIS to a geographic radius first.
3. Those candidates then flow into graph expansion and re-ranking.

The design win: because embeddings live *in the same database and the same rows* as the geometry, one SQL query can combine "near this location" and "similar to this meaning" — something that's clumsy and slow when the vector store is a separate system.

## Related

[Postgres](Postgres.md) · [PostGIS](PostGIS.md) · [Apache AGE](Apache%20AGE.md) · Voyage AI Embeddings · Spatial RAG · [Architecture Overview](Architecture%20Overview.md)
