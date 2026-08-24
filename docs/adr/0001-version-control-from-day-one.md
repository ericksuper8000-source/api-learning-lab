# ADR-0001 — Version Control from Day One

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 0 — Planning (documentation architecture)

---

## Decision

The project is versioned with Git from the very beginning and published publicly on
GitHub and GitLab. The commit history is part of the portfolio: an interviewer can watch
the API evolve in real time instead of seeing only a finished result.

## Context & Problem

The project's value is its *evolution*. If version control had arrived late, the earliest
work (the first HTTP mental model, the first endpoint, the migration to PostgreSQL) would
be invisible. A portfolio that only shows the end state cannot demonstrate process.

## Alternatives Considered

- **No public version control** — rejected: no evidence of learning, no portfolio.
- **Version control late in the project** — rejected: the most valuable part of the story would be lost.
- **Version control from day one (chosen)** — the natural need (protecting and sharing work) is present from the first commit.

## Why This Option

Versioning from day one is what makes this a portfolio instead of a folder. It also gives
practice with the tool the industry depends on (Git) from the very start.

## Consequences

- Commit history is the project narrative.
- Branches (`main`, `develop`) and feature branches are part of daily practice.
- Definition of Done includes "committed and pushed".

## If It Disappeared

The portfolio would lose its most honest asset: visible, incremental, real learning.
