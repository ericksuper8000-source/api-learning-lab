# EXECUTION PLAN

## Sequential Execution State & Checklists

**Project:** API-Learning-Lab
**Version:** 1.0 (2026 revision)
**Status:** In Progress

---

## How to Use This File

This is the **single source of truth** for project status. It does not contain theory or
stages — it tells you exactly where the project is and what to do next.

- **Every day starts with the recap mini-session** (see `AGENTS.md` — Daily Recap &
  Validation), then reads the **Current Status** block below.
- **Every session ends** by updating the **Current Status** block and ticking every
  checkbox completed during that session.
- A phase or stage is only marked complete when it is **understood, documented,
  evidenced, committed, and pushed** (see Definition of Done in `AGENTS.md`).
- Any AI agent joining the project reads this file first (see `AGENTS.md`).

> **Cadence:** 1 h/day, Monday–Friday (≈5 h/week). Total ≈ 12 weeks of work
> (58 sessions planned). Understanding gates progress — timing is an estimate, not a limit.

---

## 📌 CURRENT STATUS

> **This block is updated at the end of every session.**

- **Current phase:** Phase 1 — API Fundamentals 🔄 (in progress)
- **Current stage / task:** Stage 01 — Session 04 complete: `@app.get("/hello")` + path param `@app.get("/items/{item_id}")` with `item_id: int`; automatic conversion/validation (`422` on bad type), `404` vs `422` distinction, path = resource address. **Next: Session 05 — Query parameters**
- **Phases 2–5:** ⬜ Pending
- **Last completed item:** Phase 1 — Session 04 (GET endpoints + path parameters, type validation, 422/404) ✅
- **Daily recap status:** Protocol refined 2026-08-11 — recap covers ONLY the technical syllabus (API/HTTP/FastAPI/PostgreSQL/etc.), never Git/SSH (from the other project). See `AGENTS.md`.
- **Next session target:** Stage 01 — Session 05: query parameters (`?q=...`), path + query combined
- **Blockers / open questions:** None.
- **Last session:** 2026-08-24 — Phase 1, Session 04 (GET + path parameters) + daily recap (Sessions 01–03)
- **Last commit / push:** ✅ pushed 2026-08-24 (Session 04 docs + screenshots) to GitHub + GitLab (`develop`; `main` también alineada vía `git push origin main`)

---

## General Status

| Item | State |
|---|---|
| Project | ☒ In progress |
| Plan | ☒ Defined |
| Zero-cost policy | ☒ Active (ADR-0004) |
| Version control | ☒ Live (repo `C:\API-Learning-Lab`, ramas `main` + `develop`) |
| Application (FastAPI) | ⬜ Not started (Phase 1) |
| Database (PostgreSQL) | ⬜ Not started (Phase 3) |
| Code quality | ⬜ Not started (Phase 4) |
| CI (quality only) | ⬜ Not started (Phase 4) |
| Deployment | ⬜ Out of scope (CICD project) |

---

## Phase 0 — Planning & Documentation Architecture

**Objective:** Fully define the project before writing a single line of code.

**Estimated duration:** ~1 week (4–5 sessions)

- [x] Define the general objective
- [x] Define the methodology
- [x] Define the project philosophy
- [x] Define the mentor role
- [x] Define the student role
- [x] Create the Project Specification
- [x] Create the Execution Plan
- [x] Create the Learning Roadmap
- [x] Define the documentation strategy
- [x] Define the repository structure
- [x] Decide to version from day one (see ADR-0001)
- [x] Decide to mirror GitHub + GitLab (see ADR-0002)
- [x] Decide quality-only CI, no deployment (see ADR-0003)
- [x] Adopt local-first scope: no Docker, no cloud, $0 (see ADR-0004)
- [x] Decide public documentation in English (see ADR-0005)
- [x] Decide in-memory store first, PostgreSQL when the need is real (see ADR-0006)
- [x] Define the daily recap & validation ritual

### Repo bootstrap (completed 2026-08-10)

- [x] Create the local repository `C:\API-Learning-Lab`
- [x] `git init` with branches `main` (stable) + `develop` (integration)
- [x] Create GitHub repo `api-learning-lab` (ericksuper8000-source)
- [x] Create GitLab repo `api-learning-lab` (ericksuper80-group)
- [x] Configure both remotes and verify `git remote -v`
- [x] Add `.gitignore` and the memory files, first commit, push to **both** remotes
- [x] Verify both repositories are in sync
- [x] SSH auth configured (ssh-agent + claves cargadas + `core.sshCommand`) — no password on push
- [x] Push a `origin` en ambos destinos (GitHub + GitLab) con `git push origin <rama>`

**Status:** ✅ COMPLETE (Phase 0 done — same flow as CICD reference: `main` estable + `develop` integración)

---

## Phase 1 — API Fundamentals

**Objective:** Understand completely how an API works before building the real product.

**Estimated duration:** ~2.5 weeks (12 sessions)

**Stage document:** [`stages/stage-01-api-fundamentals.md`](stages/stage-01-api-fundamentals.md)

- [x] Session 01 — What is an API? The request journey mental model (no code)
- [x] Session 02 — HTTP: methods, status codes, request/response anatomy
- [x] Session 03 — Environment: venv, install fastapi + uvicorn + requests, first app, run it
- [x] Session 04 — GET endpoints + path parameters
- [ ] Session 05 — Query parameters; combining path + query
- [ ] Session 06 — POST + JSON body + Pydantic models (dict → model)
- [ ] Session 07 — Path + query + body together; automatic validation and `422`
- [ ] Session 08 — HTTP status codes in the API (200, 201, 204, 404, 422); response models
- [ ] Session 09 — The `requests` library: client scripts that consume the API
- [ ] Session 10 — Swagger/OpenAPI: how it is generated and how to use it
- [ ] Session 11 — Lab: small in-memory list API with GET + POST
- [ ] Session 12 — Phase 1 checkpoint: explain back, document, evidence

**Status:** ⬜ Pending

---

## Phase 2 — Real Project: IT Assets Inventory CRUD

**Objective:** Build a completely functional, organized API with professional structure.

**Estimated duration:** ~2.5 weeks (12 sessions)

**Stage document:** [`stages/stage-02-real-project-crud.md`](stages/stage-02-real-project-crud.md)

- [ ] Session 01 — Project organization: `app/` package, `main.py`, why structure matters
- [ ] Session 02 — Data modeling: what is an IT asset; asset fields and types
- [ ] Session 03 — Pydantic schemas: `AssetCreate` vs `AssetRead` (input/output separation)
- [ ] Session 04 — Create: `POST /assets` → `201`
- [ ] Session 05 — Read: `GET /assets` (list) + `GET /assets/{id}` (with `404`)
- [ ] Session 06 — Update: `PUT` vs `PATCH` (`/assets/{id}`)
- [ ] Session 07 — Delete: `DELETE /assets/{id}` → `204`
- [ ] Session 08 — Validations: field constraints, status enum, custom validators
- [ ] Session 09 — Error handling: `HTTPException`, custom handlers, consistent error JSON
- [ ] Session 10 — Routers: split the app into `app/routers/` (separation of concerns)
- [ ] Session 11 — Lab: full CRUD exercised via `requests` + Swagger + edge cases
- [ ] Session 12 — Phase 2 checkpoint: explain back, document, evidence

**Status:** ⬜ Pending

---

## Phase 3 — PostgreSQL Persistence

**Objective:** Replace the in-memory list with real, persistent storage.

**Estimated duration:** ~2.5 weeks (12 sessions)

**Stage document:** [`stages/stage-03-postgresql-persistence.md`](stages/stage-03-postgresql-persistence.md)

- [ ] Session 01 — Databases: why a DB vs a list; tables, rows, columns, primary keys
- [ ] Session 02 — PostgreSQL intro: what it is, local service, `psql`, create database
- [ ] Session 03 — SQL DDL: `CREATE TABLE assets`, data types
- [ ] Session 04 — SQL DML: `INSERT`, `SELECT`, `UPDATE`, `DELETE` (practice in psql)
- [ ] Session 05 — Connect FastAPI to PostgreSQL: driver, connection string, env vars
- [ ] Session 06 — Connection management: pool vs one connection per query
- [ ] Session 07 — Migrate Create: `INSERT` mapped to `POST /assets`
- [ ] Session 08 — Migrate Read: `SELECT` mapped to `GET /assets` + `GET /assets/{id}`
- [ ] Session 09 — Migrate Update: `UPDATE` mapped to `PUT` / `PATCH`
- [ ] Session 10 — Migrate Delete: `DELETE` mapped to `DELETE /assets/{id}`
- [ ] Session 11 — Persistence proof: restart the app, data remains; verify with psql
- [ ] Session 12 — Phase 3 checkpoint: explain back, document, evidence

**Status:** ⬜ Pending

---

## Phase 4 — Code Quality & CI

**Objective:** Guarantee the project can be maintained professionally via automated quality gates.

**Estimated duration:** ~2.5 weeks (12 sessions)

**Stage document:** [`stages/stage-04-code-quality-ci.md`](stages/stage-04-code-quality-ci.md)

- [ ] Session 01 — Why quality gates exist; what a CI pipeline should check
- [ ] Session 02 — Pytest: first unit tests, pytest basics
- [ ] Session 03 — TestClient: API tests (GET, POST, errors)
- [ ] Session 04 — Fixtures, parametrize, and a test strategy for the database
- [ ] Session 05 — Ruff: linting, configuration, fixing issues
- [ ] Session 06 — Black: formatting and `--check`
- [ ] Session 07 — Mypy: type checking, type hints in the codebase
- [ ] Session 08 — Bandit: security scanning
- [ ] Session 09 — pip-audit: dependency vulnerability audit
- [ ] Session 10 — GitHub Actions: `.github/workflows/ci.yml` (quality only)
- [ ] Session 11 — GitLab CI: `.gitlab-ci.yml`; secrets/variables in both platforms
- [ ] Session 12 — Professional README + final docs; Phase 4 checkpoint

**Status:** ⬜ Pending

---

## Phase 5 — Closure & Handoff

**Objective:** Review everything, finalize the documentation, and leave the API ready for a deployment pipeline to consume it.

**Estimated duration:** ~1 week (5 sessions)

**Stage document:** [`stages/stage-05-closure-handoff.md`](stages/stage-05-closure-handoff.md)

- [ ] Session 01 — Full review: the request journey end to end
- [ ] Session 02 — Final test pass: pytest + all quality tools green + manual + Swagger
- [ ] Session 03 — Final documentation: the 11 study documents (API, HTTP, Requests, Uvicorn,
      FastAPI, Swagger, PostgreSQL, CRUD, Testing, CI, Summary)
- [ ] Session 04 — Final README + architecture diagram + evidence
- [ ] Session 05 — Hand-off: define what the deployment project (CICD) will consume; close

**Status:** ⬜ Pending

---

## Timeline (1 h/day, Mon–Fri ≈ 5 h/week)

| Phase | When | Sessions | Stage doc |
|---|---|---|---|
| 0 Planning & Setup | Week 1 | 4–5 | (this plan) |
| 1 API Fundamentals | Weeks 2–4 | 12 | stage-01 |
| 2 Real Project (CRUD) | Weeks 4–7 | 12 | stage-02 |
| 3 PostgreSQL | Weeks 7–9 | 12 | stage-03 |
| 4 Code Quality & CI | Weeks 9–12 | 12 | stage-04 |
| 5 Closure & Handoff | Week 12 | 5 | stage-05 |

> Total ≈ 58 sessions ≈ **12 weeks**. Cadence may be adjusted — understanding is the only
> fixed requirement. The source plan estimated 10–14 weeks; this schedule fits inside it.

---

## Session Workflow

**Daily recap mini-session (before anything else, every day — 15 minutes max):**

1. Simple summary of the journey so far (~2 min).
2. Question round: **maximum 3 questions, one at a time** (commands, decisions,
   processes — 2 recent + 1 spaced repetition) (~10 min). The stage's Mentor Questions
   are spread across sessions, never asked all at once.
3. Gate: pass → progress; gaps → reinforcement, no new material; pending/weak
   questions are queued to the deck (~3 min).
4. Result recorded in `session-log.md` (passed ✅ / reinforce ⚠️), **plus the deck** of
   pending questions so the next session can resume the queue.

**Start of the progress session (10 min):**

1. Read **Current Status** above.
2. Read the last entry of `session-log.md`.
3. Read the current stage document.
4. Tell the mentor what you remember from the previous session.

**During the session:**

5. Work the stage checklist. The mentor guides with questions.

**End of session (20 min):**

 6. The agent fills the stage report section in the stage document from the session conversation (the student does not edit it by hand).
7. Save screenshots/evidence in `screenshots/stage-NN/`.
8. Append an entry to `session-log.md`.
9. Tick completed checkboxes in this file and update **Current Status**.
10. Write an ADR if a meaningful decision was made.
11. Sync this folder with `C:\API-Learning-Lab`, commit with a conventional message, push
    to **both** GitHub and GitLab.
12. Confirm the next session's target.

---

## Related Documents

- [`AGENTS.md`](../AGENTS.md) — AI operating manual & Definition of Done
- [`project-specification.md`](project-specification.md) — vision and scope
- [`mentor-constitution.md`](mentor-constitution.md) — mentoring principles
- [`learning-roadmap.md`](learning-roadmap.md) — competency map
- [`session-log.md`](session-log.md) — daily diary
- [`environment.md`](environment.md) — local environment preparation
