# ADR-0004 — Local-First, Zero-Cost Scope (No Docker, No Cloud)

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 0 — Planning (scope constraint)

---

## Decision

This project runs **100% locally** and costs **$0**. Docker, Docker Compose, Linux, VPS,
Nginx, Kubernetes, and automatic deployments are explicitly **out of scope**. The only
external services are the free Git hosts (GitHub and GitLab). No cloud resources are
provisioned at any point.

## Context & Problem

The project's mission is to understand the life of an API request — HTTP, FastAPI,
Pydantic, PostgreSQL, tests, and quality. Infrastructure concerns (containers, servers,
deployment) are a separate discipline that the student already explores in the **CI/CD
Pipeline Labs** project. Mixing them here would double the cognitive load, violate the
"Incremental Learning Rule", and break the zero-cost principle for no pedagogical gain.

## Alternatives Considered

- **Deploy to a free VPS from here** — rejected: that is the CICD project's job (its
  Phase 13 expects *this* API as input). Rejected also because it needs infra knowledge
  not yet built.
- **Use Docker locally** — rejected: the API runs fine on plain Python + Uvicorn +
  PostgreSQL; Docker would hide how the request actually reaches the application
  (violates "understand before automating").
- **Local-first (chosen)** — the simplest environment that lets every concept be visible
  and verifiable by hand.

## Why This Option

- Keeps the project at **$0** and zero infrastructure risk.
- Keeps every layer visible: you can watch Uvicorn receive the request, FastAPI route it,
  psql store the data.
- Guarantees a clean hand-off: Phase 5 delivers a pure application + repo that the CICD
  project can containerize and deploy without this project's constraints.

## Consequences

- No `Dockerfile`, no compose file, no SSH, no server steps anywhere in this project.
- The machine's Docker installation is intentionally unused here.
- The hand-off boundary is explicit: **this project builds and validates; the CICD
  project deploys.**

## If It Disappeared

The project would drift into infrastructure territory, blur its scope, add cost risk, and
duplicate work that the CICD project already performs.
