# ENVIRONMENT — Local Development Setup

**Phase:** Phase 0 — Planning (environment reference)
**Objective:** Document the local environment where the project lives, so every stage can
assume a verified baseline instead of unknown state.

**Last verified:** 2026-08-13

---

## Host Machine

- **OS:** Windows (10/11) — `C:\Users\XPC`
- **Terminal:** VS Code integrated terminal / PowerShell / Git Bash
- **Shell (Git):** Git Bash (also used for Git operations)

## Tools Installed

| Tool | Purpose in this project | Verified |
|---|---|---|
| Visual Studio Code | General editor | — |
| PyCharm | FastAPI practice editor (how the student learned FastAPI; used daily for the reference project) | — |
| Git 2.52 | Version control | `git --version` ✅ |
| Python 3.11 (project standard) | The application runtime | `py -0` ✅ (3.11 and 3.14 installed) |
| PostgreSQL 18 | The persistence layer (local service `postgresql-x64-18`, running) | `Get-Service postgresql-x64-18` ✅ |
| pip / venv | Dependencies and virtual environments | part of Python ✅ |

> ⚠️ **Python note:** the Windows launcher is used: `py -3.11 -m venv .venv`. Both 3.11
> and 3.14 exist on the machine. **3.11 is the project standard** (confirmed in Session 01,
> verified as 3.11.9 in Session 03).
> Docker is installed on the machine but is **not part of this project** (ADR-0004).
>
> ⚠️ **Git Bash quirk (verified 2026-08-13):** in Git Bash on this machine, `python` is not
> found by default — use the `py` launcher (`py --version` → `Python 3.11.9`). Inside the
> active venv, `uvicorn` and `pip` work normally.
>
> ✅ **Run the app (verified 2026-08-13):** open Git Bash in `C:\API-Learning-Lab`, then
> `source .venv/Scripts/activate`, then `uvicorn main:app --port 8000 --reload`. The app must
> be started from `C:\API-Learning-Lab` with `.venv` active, or uvicorn reports *"Could not
> import module `main`"* (it looks for `main.py` in the current folder and uses the active
> venv's Python). To stop/leave: `Ctrl+C` and `deactivate` (or just close the terminal).

## Repositories & Folders

| Path | Role |
|---|---|
| `C:\API-Learning-Lab` | **The real repository** — live (2026-08-10): initialized `git init`, branches `main` (estable) + `develop` (integración), pushed to GitHub + GitLab. Code + tests + CI will live here. |
| `E:\Datos\IA\FastApi - Project` | **Memory/planning folder** — documentation, session log, execution plan. Kept in sync with `C:\API-Learning-Lab`. |
| `C:\FastAPI\vtasks` | Prior practice environment (venv, Python 3.14) with `ProyectoFastAPI1/2`. Reference only — not the repo. |
| `C:\Repo2` + `Desktop\CICD - BORRADOR` | The CI/CD Pipeline Labs project — this API is handed off to it in Phase 5. |
| `C:\Repo` | Git practice repo (hello-world) — unrelated, reference only. |

## The Real Repository (C:\API-Learning-Lab)

Planned key files (created progressively by stage):

```
C:\API-Learning-Lab\
├── app/                      # Phase 2 — the FastAPI application package
│   ├── main.py
│   ├── models.py             # Pydantic schemas (input/output)
│   ├── routers/
│   └── database/             # Phase 3 — connection + SQL
├── tests/                    # Phase 4 — pytest
├── docs/                     # synced from the memory folder
├── screenshots/              # evidence
├── .github/workflows/ci.yml  # Phase 4 — GitHub Actions (quality only)
├── .gitlab-ci.yml            # Phase 4 — GitLab CI (quality only)
├── requirements.txt
├── README.md
└── .git/
```

Branches: `main` (stable) and `develop` (integration) — same strategy as the CICD project.
`origin` tiene dos push URLs (GitHub + GitLab), así que `git push origin <rama>` publica en ambas.

### SSH authentication (2026-08-10)

- Service Windows `ssh-agent` → `Running` / `Automatic`.
- Keys: `~/.ssh/id_ed25519` (GitHub) y `~/.ssh/id_ed25519_gitlab` (GitLab), cargadas con `ssh-add`.
- `git config --global core.sshCommand "C:/Windows/System32/OpenSSH/ssh.exe"` — Git Bash usa el agente de Windows.
- Verify: `ssh -T git@github.com` · `ssh -T git@gitlab.com`

## PostgreSQL (local, Phase 3)

- Service: `postgresql-x64-18` — currently **Running**
- Client: `C:\Program Files\PostgreSQL\18\bin\psql.exe`
- A dedicated database for the project (e.g., `api_learning_lab`) is created in Phase 3,
  never on the system `postgres` database.
- Connection settings (host, port, user, password, dbname) will live in a local `.env`
  file that is **never committed** (see `.gitignore`).

## External Services (free tier)

| Service | Account / resource | Purpose |
|---|---|---|
| GitHub | `ericksuper8000-source` / repo `api-learning-lab` | Hosting + Actions (CI) |
| GitLab | `ericksuper80-group` / repo `api-learning-lab` | Hosting + CI (mirror) |

No cloud services are used. The project is 100% local and $0.

## Sync Rule

- **Real work and commits** happen in `C:\API-Learning-Lab`.
- **Planning and AI memory** live in the Desktop folder `FastApi - Project`.
- At the end of every session, the memory folder and `C:\API-Learning-Lab` must show the
  **same** documentation state (the docs are copied into `C:\API-Learning-Lab\docs/` and committed).

---

## Assumptions Being Eliminated

By the end of this setup, the following are **not assumed** — they are verified facts:

- The user can run Python (3.11), Git, and pip/venv locally.
- PostgreSQL 18 runs locally and the project database can be created.
- GitHub and GitLab `api-learning-lab` repositories exist and are mirrored.
- The memory folder structure matches the real repository structure.

## Definition of Done (Phase 0 environment)

- [x] Tools verified (Git, Python 3.11, PostgreSQL 18).
- [ ] `C:\API-Learning-Lab` created and initialized with `main` + `develop`.
- [ ] Both remotes configured and first push done.
- [ ] GitHub + GitLab `api-learning-lab` repos created and in sync.
- [x] Memory folder created and synced with `C:\API-Learning-Lab`.
- [x] SSH auth configured (sin contraseña en los pushes).
