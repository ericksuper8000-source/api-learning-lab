# ADR-0006 — In-Memory Store First, PostgreSQL When the Need Is Real

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 0 — Planning / Phase 2–3 (implemented)

---

## Decision

The API is first built with an **in-memory store** (a Python list/dict) during Phases 1–2.
**PostgreSQL** is introduced in Phase 3, only when the need is real: data must survive
restarts and be queryable by SQL. Persistence is added deliberately, not at the start.

## Context & Problem

New concepts must be introduced only when a real technical need exists (Incremental
Learning Rule; see `AGENTS.md`). Adding a database on day one would hide the fundamentals
that Phases 1–2 must build: HTTP, routing, parameters, validation, CRUD logic. The
in-memory store keeps every one of those layers visible and debuggable.

## Alternatives Considered

- **PostgreSQL from day one** — rejected: buries the HTTP/FastAPI mental model under
  connection and SQL concerns before it is built.
- **In-memory first (chosen)** — the simplest store that works, then replaced when the
  limitation (ephemerality) becomes the teaching moment.
- **File-based storage (JSON/CSV)** — rejected as an unnecessary middle step; the jump
  from "list in memory" to "table in PostgreSQL" makes the value of a database clearer.

## Why This Option

When the student watches the in-memory list vanish on restart, the *need* for persistence
becomes obvious — exactly the moment a database should be introduced (Phase 3). This also
mirrors how real applications grow: start simple, evolve storage when required.

## Consequences

- Phases 1–2 use a plain Python store; CRUD is implemented twice (memory → SQL).
- Phase 3 introduces psql, SQL, and the driver connection step by step.
- An **open candidate ADR** (ADR-0007) exists for whether a SQL ORM (e.g., SQLAlchemy)
  is adopted after raw SQL is mastered — decided during Phase 3.

## If It Disappeared

Either the fundamentals would be buried under database complexity (PostgreSQL from day
one) or the project would ship without real persistence (never migrating), failing the
project's own objective of "a request that ends in a database row".
