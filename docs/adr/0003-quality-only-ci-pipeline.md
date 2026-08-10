# ADR-0003 — Quality-Only CI Pipeline (No Deployment)

**Status:** Accepted
**Date:** 2026-08-04
**Context:** Phase 0 — Planning / Phase 4 (implemented)

---

## Decision

This project's Continuous Integration pipeline is **quality-only**: every push runs
installation of dependencies, Ruff, Black `--check`, Mypy, Pytest, Bandit, and pip-audit.
The pipeline **never deploys**, never builds images, and never publishes anything.

## Context & Problem

The scope of this project (see `docs/project-specification.md`) explicitly excludes
Docker, servers, and automatic deployment — those belong to the **CI/CD Pipeline Labs**
project. The deployment project will take exactly this API and containerize and deploy it.
Here, CI exists to answer one question on every push: *"is this code still good?"*

## Alternatives Considered

- **No CI at all** — rejected: quality would depend on manual memory.
- **CI + CD (build and deploy)** — rejected: deployment is out of scope (ADR-0004);
  the infra project does it.
- **Quality-only CI (chosen)** — the exact need of this phase: automated, repeatable
  quality gates on both GitHub Actions and GitLab CI.

## Why This Option

A professional pipeline never ships broken code. By the end of Phase 4, every push is
checked by the six quality tools, and only a green pipeline lets the project evolve.
This makes the hand-off clean: when the deployment project receives the repo, it inherits
an application that is continuously proven correct.

## Consequences

- `.github/workflows/ci.yml` and `.gitlab-ci.yml` contain only quality jobs.
- No registry credentials, no Docker steps, no deploy jobs in this project.
- "Green pipeline" becomes the Definition of Done for Phase 4 onward.

## If It Disappeared

The repository would lose its quality guarantee and the hand-off to the deployment
project would inherit untested, unvalidated code.
