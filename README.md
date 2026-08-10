# API-Learning-Lab

> From a single HTTP request to a row in PostgreSQL — build a complete, documented FastAPI REST API (an IT Assets Inventory), tested and quality-gated by a Continuous Integration pipeline. No Docker, no server, no magic: **understanding before coding.**

**Type:** Practical learning project + professional portfolio
**Duration:** ~10–14 weeks total (5 h/week — 1 h/day, Mon–Fri)
**Language:** English (public documentation)

---

## The Story

This is the repository of a **future DevOps Junior** learning the *complete life of an
API request* by building a real REST service with his own hands. It does not start with a
finished product — it starts with a question: *"what really happens between the moment a
client sends a request and the moment a database stores the data and the response comes
back?"*

Then, stage by stage, the story unfolds:

1. First, the **fundamentals**: what an API is, what HTTP is, and how a request travels
   from client to server (Phase 1).
2. A real project is born: the **IT Assets Inventory API** — a CRUD for Laptops, Servers,
   Switches, Monitors, Printers, and Licenses (Phase 2).
3. Data stops living in memory: **PostgreSQL** replaces the list, and the API learns to
   persist, query, and survive restarts (Phase 3).
4. The code becomes professional: **Pytest, Ruff, Black, Mypy, Bandit, pip-audit** and a
   **quality-only CI pipeline** on GitHub and GitLab (Phase 4).
5. The project closes: full documentation, final validation, and a hand-off — the API is
   **ready to be consumed by a deployment pipeline** (Phase 5).

Every step is documented with evidence, screenshots, and the reasoning behind each
decision. This is not a tutorial; it is a complete engineering journey.

Every session begins with a **recap mini-session**: the student explains back what was
learned, one question at a time, so understanding is real — not memorized.

---

## Why This Project Exists

This project is not about memorizing FastAPI decorators. It is about building **technical
judgment** — the ability to explain why a REST API is structured the way it is, how the
components communicate (Client → HTTP → Uvicorn → FastAPI → PostgreSQL → Response), and how
to diagnose a problem when something breaks.

The goal is that after finishing, when asked *"What is an API?"*, *"Why Pydantic?"*, *"What
is the difference between path and query parameters?"*, *"Why does the database need to be
separate from the application?"*, or *"Why does your CI only check quality and not deploy?"*,
the answer comes from real understanding, not from a copied tutorial.

---

## Scope

This project **only** covers:

- Python (FastAPI, Uvicorn, Pydantic, Requests)
- PostgreSQL and basic SQL (INSERT, SELECT, UPDATE, DELETE)
- Swagger / OpenAPI
- Pytest, Ruff, Black, Mypy, Bandit, pip-audit
- Git, GitHub, GitLab (mirrored repositories)
- Continuous Integration — **quality only, no deployment**

This project deliberately does **NOT** cover:

- Docker, Docker Compose, containers
- Linux, VPS, Nginx, Kubernetes
- Automatic deployments

Those technologies belong to independent projects (see the **CI/CD Pipeline Labs**
project). This project prepares an application of professional quality so that *another*
project can later deploy it.

---

## Cost Policy

The project costs **$0**. All tools and services are free: Python, PostgreSQL, Git,
GitHub, GitLab, and local execution. Nothing is paid, nothing is provisioned in the cloud.

---

## Repository Layout

```
.
├── AGENTS.md                     # Operating manual for any AI mentor working on this repo
├── docs/
│   ├── project-specification.md  # Vision, scope, success criteria
│   ├── mentor-constitution.md    # Pedagogical & technical principles of the mentor
│   ├── learning-roadmap.md       # Competency map — "you are done when you can..."
│   ├── execution-plan.md         # ⭐ THE status file — phases, checklists, current state
│   ├── session-log.md            # Daily diary (reverse-chronological)
│   ├── environment.md            # Local environment (Windows host, Python, PostgreSQL)
│   ├── adr/                      # Architecture Decision Records
│   └── stages/                   # One document per stage
├── screenshots/                  # Evidence, one folder per stage
├── scripts/                      # Scripts created during stages
└── .gitignore
```

> The **code itself lives in `C:\API-Learning-Lab`** (the real repository, mirrored to
> GitHub and GitLab). This folder is the **memory/planning** folder and stays in sync
> with it.

---

## Phase Map

| Phase | Topic | Status |
|---|---|---|
| 0 | Planning & Documentation Architecture | ✅ Complete (repo bootstrapped + SSH auth) |
| 1 | API Fundamentals | 🔄 Next |
| 2 | Real Project — IT Assets Inventory CRUD | ⬜ Pending |
| 3 | PostgreSQL Persistence | ⬜ Pending |
| 4 | Code Quality & CI | ⬜ Pending |
| 5 | Closure & Handoff | ⬜ Pending |

> **Live status:** see [`docs/execution-plan.md`](docs/execution-plan.md) — the single
> source of truth for what is done and what is next.

---

## How This Repository Is Maintained

- **Single source of truth:** [`docs/execution-plan.md`](docs/execution-plan.md) stores
  the current phase, the current stage, and every checkbox. It is updated at the end of
  every session.
- **Daily recap ritual:** every day starts with a recap mini-session — the AI summarizes
  the journey simply and validates understanding with one question at a time before any
  progress (see [`AGENTS.md`](AGENTS.md)).
- **AI-friendly:** Any AI agent that joins the project follows the bootstrap protocol in
  [`AGENTS.md`](AGENTS.md), which guarantees instant recall of what exists, what is done,
  and what is next.
- **Definition of Done:** a stage is finished only when it is understood, documented,
  evidenced, committed, and pushed to **both** GitHub and GitLab.
- **Mirrored repositories:** the project lives in `C:\API-Learning-Lab` and is pushed to
  GitHub and GitLab in parallel.
- **Zero cost:** everything runs locally on free tools (see Cost Policy).

---

## First Steps

1. Read [`docs/execution-plan.md`](docs/execution-plan.md) → **Current Status**.
2. ✅ **Phase 0 repo bootstrap complete** (`C:\API-Learning-Lab` live, GitHub + GitLab
   repos `api-learning-lab`, SSH auth working — no password on push).
3. Next: **Stage 01 — API Fundamentals** ([`docs/stages/stage-01-api-fundamentals.md`](docs/stages/stage-01-api-fundamentals.md)).

---

## Author

**Erick Perez** — Aspiring DevOps Engineer building hands-on experience with FastAPI,
PostgreSQL, testing, code quality, and the software delivery lifecycle.
