# LEARNING ROADMAP

## Competency Map — "You are done when you can…"

**Project:** API-Learning-Lab
**Version:** 1.0 (2026 revision)

---

## How to Use This Document

This is the **competency map**. For every phase it defines the questions the student must
be able to answer and the skills they must demonstrate **without help**. It complements
[`execution-plan.md`](execution-plan.md) (the *what to do*) by defining *what "done"
means for your brain*.

The mentor uses these questions to validate understanding. The student uses them to
self-assess before marking a phase complete. If you cannot answer a question fluently,
the phase is **not** complete — regardless of how many checkboxes are ticked.

---

## Phase 0 — Planning & Setup

- [ ] I can explain the mission of the project in 3 sentences.
- [ ] I know the core documents and what each one is for.
- [ ] I understand the Definition of Done and why every session must update state.
- [ ] I understand why this project does **not** use Docker or deploy (ADR-0004).

---

## Phase 1 — API Fundamentals

- [ ] I can explain what an API is and what problem it solves.
- [ ] I can explain what HTTP is, what a method is, and what a status code is.
- [ ] I can draw the journey of a request: client → HTTP → Uvicorn → FastAPI → response.
- [ ] I can explain the role of Uvicorn vs the role of FastAPI.
- [ ] I can write a FastAPI application and run it with Uvicorn.
- [ ] I can build GET and POST endpoints.
- [ ] I can use path parameters, query parameters, and request bodies.
- [ ] I can explain what Pydantic does and why invalid data returns `422`.
- [ ] I can use Swagger/OpenAPI to explore and test the API.
- [ ] I can read and explain the meaning of the main HTTP status codes (200, 201, 204, 404, 422).

---

## Phase 2 — Real Project (IT Assets Inventory CRUD)

- [ ] I can organize a FastAPI project professionally (app package, routers, schemas).
- [ ] I can implement a full CRUD: Create, Read, Update, Delete.
- [ ] I can explain which HTTP verbs map to each CRUD operation.
- [ ] I can separate input schemas from output schemas with Pydantic.
- [ ] I can add real validations (field constraints, enums, custom validators).
- [ ] I can handle errors properly (`404`, `422`, `HTTPException`, consistent error JSON).
- [ ] I can explain the difference between `PUT` and `PATCH`.
- [ ] I can explain why the data is stored in memory in this phase and what the limits are.

---

## Phase 3 — PostgreSQL Persistence

- [ ] I can explain what a database, a table, a row, and a primary key are.
- [ ] I can connect to PostgreSQL and create a database with `psql`.
- [ ] I can write `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.
- [ ] I can connect FastAPI to PostgreSQL using a driver and environment variables.
- [ ] I can explain why a connection pool is used instead of one connection per query.
- [ ] I can migrate the CRUD from the in-memory list to PostgreSQL.
- [ ] I can prove persistence: restart the app and the data is still there.
- [ ] I can explain what happens if the database is down.

---

## Phase 4 — Code Quality & CI

- [ ] I can explain the responsibility of each tool: Pytest, Ruff, Black, Mypy, Bandit, pip-audit.
- [ ] I can write unit tests and API tests with Pytest and the FastAPI TestClient.
- [ ] I can explain why Black runs as `--check` in CI instead of modifying files.
- [ ] I can explain why a professional pipeline never ships broken code.
- [ ] I can configure a CI pipeline on GitHub Actions and GitLab CI (quality only).
- [ ] I can explain why this project's CI **does not deploy** (ADR-0003).
- [ ] I can explain how secrets and variables are stored in CI (not in the repo).

---

## Phase 5 — Closure & Handoff

- [ ] I can walk the full journey end to end: client → HTTP → Uvicorn → FastAPI → PostgreSQL → response.
- [ ] I can demonstrate the API works: tests green, tools green, manual + Swagger proof.
- [ ] I can explain exactly what a deployment pipeline will consume from this repository.
- [ ] I can defend every major decision using the ADRs.

---

## Progress Tracker

| Phase | Self-assessment | Mentor validation | Date |
|---|---|---|---|
| 0 Planning | ⬜ | ⬜ | |
| 1 API Fundamentals | ⬜ | ⬜ | |
| 2 Real Project | ⬜ | ⬜ | |
| 3 PostgreSQL | ⬜ | ⬜ | |
| 4 Code Quality & CI | ⬜ | ⬜ | |
| 5 Closure & Handoff | ⬜ | ⬜ | |
