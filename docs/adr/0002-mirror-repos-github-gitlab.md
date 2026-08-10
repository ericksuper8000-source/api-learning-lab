# ADR-0002 — Mirror Repositories on GitHub and GitLab

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 0 — Planning

---

## Decision

The project is published as a **mirrored pair**: the same repository is pushed to both
GitHub (`api-learning-lab`) and GitLab (`api-learning-lab`). The canonical working copy
lives in `C:\API-Learning-Lab`; both platforms receive every push.

## Context & Problem

The broader learning journey (CI/CD Pipeline Labs project) practices **multi-platform
delivery**: GitHub Actions and GitLab CI run pipelines. This project applies the same
discipline — a quality-only CI pipeline will run on both platforms in Phase 4. Hosting the
code on both platforms is the natural home for that comparison, and provides redundancy —
if one platform disappears, the project survives on the other.

## Alternatives Considered

- **GitHub only** — simpler, but loses GitLab CI experience and platform breadth.
- **GitLab only** — same, reversed.
- **Both, mirrored (chosen)** — one working copy, two remotes, minimal extra effort.

## Why This Option

Mirroring costs almost nothing (one extra remote) and doubles the portfolio surface.
Both CI systems are used in Phase 4, so both accounts are needed regardless.

## Consequences

- `git remote -v` shows two remotes; every push goes to both.
- Both repositories stay public and in sync.
- Pipelines are developed and compared on both platforms.

## If It Disappeared

The portfolio would lose the multi-platform story and the direct GitHub Actions vs
GitLab CI comparison that interviewers value.
