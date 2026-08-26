---
title: "PostGIS"
source_collection: "Inish Labs"
public_export: "sanitized 2026-08-26"
content_mode: "sanitized-copy"
---

# PostGIS

## Plain-English definition

PostGIS is an extension that teaches [Postgres](Postgres.md) to understand **geography**. Plain Postgres knows about numbers, text, and dates; PostGIS adds a new kind of data — shapes on the Earth's surface (points, lines, polygons) — plus hundreds of functions for asking spatial questions: *Which parcels are inside this flood zone? What's the nearest fire station to this address? Do these two roads intersect?* It is the standard open-source spatial database, used by governments and mapping companies worldwide, and it is the foundation of the GIS side of Inish Labs.

## How it actually works

- **Geometry as a column type.** PostGIS adds a `GEOMETRY` data type, so a table row can hold a parcel's boundary polygon right alongside its owner and zoning code. Each geometry carries a coordinate system (the GIS stack standardises on EPSG:4326 — plain latitude/longitude).
- **Spatial functions in SQL.** Questions become queries: `ST_Contains(boundary, parcel)` asks "is this parcel inside this boundary?"; `ST_DWithin(a, b, 500)` asks "are these within 500 metres of each other?"; `ST_Intersection` computes the overlapping area; `ST_Area`, `ST_Distance`, `ST_Touches` and hundreds more cover nearly any geometric question.
- **Spatial indexes.** A GIST index organises geometries by location (bounding boxes in a tree), so "what's near this point?" checks a handful of candidates instead of scanning millions of rows. This is what makes spatial queries fast at county scale.
- **Companion extensions.** The planned build also enables `postgis_topology` (shared-boundary modelling), `postgis_raster` (gridded imagery data), and `pg_trgm` (fuzzy text matching, used to conflate slightly-different names for the same place).

## What it's used for in the GIS + AI server

PostGIS is **the spine**. The design principle from the deploy guide: there is no separate spatial store, vector store, or graph store — one Postgres instance (image `postgis/postgis:18-3.5`) holds all three, with PostGIS handling geometry, [pgvector](pgvector.md) handling semantic search, and [Apache AGE](Apache%20AGE.md) handling graph relationships.

Concretely, PostGIS:

- stores every ingested spatial entity (parcels, roads, boundaries, incidents) in the `entities` table with a GIST-indexed geometry column;
- **generates the relationship edges deterministically** — `CONTAINED_IN` edges come from `ST_Contains` with the overlap fraction as a confidence score, `ADJACENT_TO` from `ST_Touches`, `ACCESSED_VIA` from nearest-road queries, `NEAREST_FIRE_5KM` from `ST_DWithin`. This matters because relationships are *computed facts from geometry*, not guesses by an AI model;
- pre-filters Spatial RAG searches by location (`ST_DWithin` narrows candidates to a radius before vector ranking);
- feeds pg_tileserv, which turns PostGIS tables directly into map tiles.

## A key safety rule

The build's non-negotiable: **the AI never writes raw spatial SQL.** Language models pick from a catalog of typed, pre-written spatial operations; PostGIS executes only vetted queries. This prevents both injection attacks and subtly wrong geometry math.

## Related

[Postgres](Postgres.md) · [pgvector](pgvector.md) · [Apache AGE](Apache%20AGE.md) · Spatial RAG · pg_tileserv · [Architecture Overview](Architecture%20Overview.md)
