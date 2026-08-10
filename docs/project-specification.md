# PROJECT SPECIFICATION

> **Project:** API-Learning-Lab
> **Version:** 1.0 (2026 revision)
> **Status:** Active
> **Type:** Documented practical learning + professional portfolio

---

## 1. Vision

API-Learning-Lab is a practical learning project that builds the technical competencies
required to understand and build a **modern REST API from scratch**. It follows the
complete life of a request: a client sends an HTTP request, Uvicorn receives it, FastAPI
routes it, Pydantic validates it, the application logic processes it, PostgreSQL stores
it, and the response travels back to the client.

The project does not teach isolated endpoints or tutorial completion. Its purpose is to
develop the ability to understand, build, structure, test, and guarantee the quality of a
real API — from the first `@app.get` to a PostgreSQL-backed CRUD validated by a quality-only
CI pipeline.

Everything is built publicly as professional evidence of learning. At the end, this
repository hands a **production-ready-quality API** to the **CI/CD Pipeline Labs** project,
which is the one responsible for deploying it.

---

## 2. Main Objective

Build, step by step, a real REST API: the **IT Assets Inventory** — a service that
registers, queries, updates, and deletes IT assets (Laptops, Servers, Switches, Monitors,
Printers, Licenses) — backed by PostgreSQL, documented end to end, and protected by a CI
pipeline that guarantees code quality.

The student must understand each component **before** automating it.

---

## 3. Scope

Included:

- Python fundamentals applied to web services
- FastAPI, Uvicorn, Pydantic, Requests
- HTTP, REST, JSON, Swagger / OpenAPI
- CRUD operations and professional project organization
- PostgreSQL and basic SQL (INSERT, SELECT, UPDATE, DELETE)
- Code quality: Ruff, Black, Mypy, Bandit, pip-audit
- Automated testing with Pytest
- Git, GitHub, and GitLab (mirrored repositories)
- Continuous Integration — **quality only, no deployment**

Explicitly out of scope (they belong to independent projects):

- Docker, Docker Compose, containers
- Linux, VPS, Nginx, Kubernetes
- Automatic deployments / CD
- Cloud infrastructure of any kind

---

## 4. Project Story

A company keeps track of its IT equipment in spreadsheets. It asks you to build an **API**
so that other internal systems can register, query, update, and remove assets
programmatically. You must decide: how to structure the application, how to validate the
data, how to store it reliably (PostgreSQL), how to prove the API works (tests), and how
to guarantee quality automatically on every push (CI).

Every stage is a task that could exist in a professional environment. No isolated
exercises. Every stage leaves the project in a better state than before.

---

## 5. Philosophy

### Understand before coding

> *Comprender antes de programar.* No code is written before the concept is explained.

### Understand before abstracting

No ORM, framework magic, or automation may hide how the API actually works.

### Learn by doing

Every concept is applied immediately in a real stage and verified by hand.

### Document everything

Nothing is finished until documented with evidence.

### One evolving application

The same inventory API evolves across the entire journey. No throwaway projects.

---

## 6. Initial State

Phase 0 (Planning & Documentation Architecture) is being completed with this document set.
The student already has basic exposure to FastAPI from prior practice projects
(`C:\FastAPI\vtasks\ProyectoFastAPI1` and `ProyectoFastAPI2`), but nothing is assumed:
Phase 1 rebuilds the fundamentals from the mental model upward.

What will be built from here:

- HTTP and request/response mental model
- A working FastAPI application with Uvicorn and Swagger
- The IT Assets Inventory API (full CRUD, validated, organized)
- PostgreSQL persistence with real SQL
- Tests and quality tools (Pytest, Ruff, Black, Mypy, Bandit, pip-audit)
- A quality-only CI pipeline on GitHub Actions and GitLab CI
- Final documentation and the hand-off to the deployment project

---

## 7. Resources

Current infrastructure:

- Windows 10/11 host
- Visual Studio Code + Git Bash
- Python 3.11 (project standard; 3.14 also available on the machine)
- PostgreSQL 18 installed and running locally (`postgresql-x64-18` service)
- Git
- Repositories on GitHub (`api-learning-lab`) and GitLab (`api-learning-lab`), mirrored
- No cloud services are used

Future infrastructure: none for this project. The API is handed to the CI/CD Pipeline
Labs project, which will containerize and deploy it.

### Zero-cost principle

The project must stay at **$0 cost**. Everything runs locally with free tools. Nothing is
provisioned in the cloud.

---

## 8. Methodology

Every session follows the same structure:

1. Daily recap & validation mini-session (one question at a time, before any progress).
2. Review of the previous session.
3. Conceptual explanation (why first).
4. Professional scenario.
5. Practical stage.
6. Technical discussion.
7. Documentation and evidence.
8. State update and definition of the next stage.

Do not advance while conceptual gaps exist. Understanding gates progress.

---

## 9. Learning Architecture

Knowledge is built in layers, and each layer depends on full understanding of the
previous one:

```
Client / HTTP Request
  ↓
Uvicorn (receives the request)
  ↓
FastAPI (routes, validates, builds the response)
  ↓
Pydantic (validates data)
  ↓
Application Logic (CRUD)
  ↓
PostgreSQL (persistence)
  ↓
HTTP Response back to the client
  ↓
Quality: Pytest · Ruff · Black · Mypy · Bandit · pip-audit
  ↓
CI (GitHub Actions + GitLab CI) — quality only
  ↓
Hand-off: "ready for a deployment pipeline" (CICD project)
```

---

## 10. Roadmap (Phases)

| # | Phase | Description | Status |
|---|---|---|---|
| 0 | Planning | Documentation architecture, methodology, decisions | 🔄 |
| 1 | API Fundamentals | HTTP, Uvicorn, FastAPI, GET/POST, Path/Query/Body, Swagger | ⬜ |
| 2 | Real Project | IT Assets Inventory CRUD, organization, validation, errors | ⬜ |
| 3 | PostgreSQL | Databases, SQL, connection, persistence | ⬜ |
| 4 | Code Quality & CI | Pytest, Ruff, Black, Mypy, Bandit, pip-audit, CI | ⬜ |
| 5 | Closure & Handoff | Review, final docs, ready-for-deploy | ⬜ |

> Detailed checklists and current status: [`execution-plan.md`](execution-plan.md)

---

## 11. Expected Competencies

By the end of the project, the student can:

- Explain the complete journey of an HTTP request: client → Uvicorn → FastAPI → PostgreSQL → response
- Build a structured FastAPI application with routers and schemas
- Design and validate data models with Pydantic
- Persist and query data with PostgreSQL and real SQL
- Write meaningful tests with Pytest and the TestClient
- Operate the quality tools and a quality-only CI pipeline on both GitHub and GitLab
- Diagnose errors by reading validation, SQL, and CI output
- Hand the API to a deployment pipeline knowing it is ready

---

## 12. Documentation

Professional documentation is produced for the whole project. Each stage includes, when
applicable: objective, context, procedure, technical explanation, commands used,
screenshots, problems encountered, solutions, and conclusions.

Reasoning behind decisions is captured as **Architecture Decision Records (ADRs)** in
`docs/adr/`, making the "why" interview-ready.

By the end, the repository also contains the 11 study documents defined in the original
draft: API, HTTP, Requests, Uvicorn, FastAPI, Swagger, PostgreSQL, CRUD, Testing,
Continuous Integration, and Final Summary.

---

## 13. Repositories

The project is published on **GitHub** and **GitLab** (mirrored). The real repository
lives in `C:\API-Learning-Lab`; this folder (`FastApi - Project`) is the memory and
planning folder and stays in sync with it.

Every commit represents meaningful progress. Documentation carries the same weight as
technical implementation.

---

## 14. Restrictions

- No tool is introduced before the problem it solves is understood.
- No tutorial is copied without understanding.
- No command memorization.
- No skipped documentation.
- No rushing that sacrifices understanding.
- No Docker, VPS, or deployment tooling in this project (ADR-0004).
- No ORM before raw SQL is understood.

---

## 15. Success Criteria

The project is successful when there is evidence that the student can:

- Operate a REST API with judgment, not copy-paste
- Justify every design and pipeline decision
- Diagnose problems in the API, the database, and the CI pipeline
- Document professionally
- State with confidence: *"This API is completely built, documented, tested, and validated
  to be consumed by a deployment process."*

The result must constitute a portfolio that shows the full evolution of learning and lets
an interviewer understand the technical level reached.

---

## 16. Related Documents

This project is supported by the following coherent document set:

- **`AGENTS.md`** — operating manual for any AI mentor on this repo
- **`docs/mentor-constitution.md`** — pedagogical and technical principles of the mentor
- **`docs/execution-plan.md`** — sequential execution state and checklists
- **`docs/learning-roadmap.md`** — competency map and progress
- **`docs/session-log.md`** — daily session diary
- **`docs/environment.md`** — local environment documentation

All are part of a single documentation architecture and must stay coherent with each other.

---

## Guiding Principle

> The goal of this project is not to learn how to copy endpoints.
> The goal is to develop the technical judgment to think, act, and solve problems like a
> Backend Engineer — using a real, PostgreSQL-backed API as public evidence of that learning.
