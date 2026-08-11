# SESSION LOG

## Daily Diary — reverse chronological order

**Project:** API-Learning-Lab

---

## How to Write an Entry

Append every entry at the **top** of this file (under this header). One entry per session.
Keep it honest and specific: this log is the "memory" that any AI (and you) uses to resume
work instantly. The mentor reviews the latest entry at the start of every session.

### Template

```markdown
## YYYY-MM-DD — Session NN

**Phase / Stage:** Phase X — <phase name> · Stage NN — <stage title>

**Daily recap (start of day):**
- Passed ✅ / Areas to reinforce ⚠️: <what was asked and how it went>

**Deck (pending questions for next sessions):**
- <pending question 1> · <pending question 2> (or "None")

**Worked on:**
- <what was done this session>

**Concepts learned / reinforced:**
- <concept, in your own words>

**Commands / tools used:**
- <command> — why

**Errors encountered:**
- <error> → <what you investigated> → <resolution>

**Questions still open:**
- <question> (if none, write "None")

**Next session (target):**
- <exact next checkbox to complete>

**Commit / push:** `docs(stage-00): ...` — pushed to GitHub ✅ GitLab ✅
```

> **Recap budget:** max 15 minutes (2-min summary + 10-min questions + 3-min gate).
> Max **3 questions/day** (typically 2 fresh + 1 spaced repetition). The stage's Mentor
> Questions are distributed across sessions, never asked all at once. Weak/skipped
> questions go to the **Deck** line above so the next session resumes the queue.

---

## Entries

---

## 2026-08-11 — Session 02 (Phase 1 · Session 01 — What is an API?)

**Phase / Stage:** Phase 1 — API Fundamentals · Stage 01 — Session 01 (What is an API? The request journey — no code)

**Daily recap (start of day):**
- Passed ✅ — no technical syllabus existed yet (recap protocol refined: covers ONLY the
  technical syllabus — API/HTTP/FastAPI/PostgreSQL — never Git/SSH from the other project).

**Deck (pending questions for next sessions):**
- Cabeceras de la nota HTTP (`Host` = a qué dirección; `Accept` = qué formato quiere la respuesta).
- Pendiente de ver en sesiones futuras: POST + cuerpo, códigos de estado en detalle (201, 204, 404, 422).

**Worked on:**
- Built the full mental model of the request journey: Client → HTTP → Uvicorn → FastAPI → response.
- Clarified that the API is the **contract/menu**, not a layer of the journey.
- Explained the 4 roles with real-life analogies (library: catalog, request slip, desk clerk, librarian).
- Status codes: first digit = category (2 success / 4 client error / 5 server error); codes are a contract.
- Webpage vs API request: `Accept: text/html` (human) vs `Accept: application/json` (program); `Host` header.
- Recap scope rule written into `AGENTS.md` (technical syllabus only).

**Concepts learned / reinforced:**
- An API is a contract: it defines what operations exist and their rules; it is not a communication layer.
- Uvicorn receives and forwards without understanding; FastAPI routes on method + URL and executes.
- HTTP note anatomy: first line = method + URL; below = headers (`Host`, `Accept`).
- A status code lets the client know the outcome without reading the body.

**Commands / tools used:**
- None (no code — concept session).

**Errors encountered:**
- None.

**Questions still open:**
- The student drafted the Report answers in `Respuesta.txt` (Desktop); pending transfer to the stage-01 Report section.

**Next session (target):**
- Stage 01 — Session 02: HTTP — methods, status codes, request/response anatomy.

**Commit / push:** Pending end-of-day (student task) — `main`/`develop` not yet pushed today.

---

## 2026-08-10 — Session 01 (Repo Bootstrap + SSH Auth)

**Phase / Stage:** Phase 0 — Planning · Repo bootstrap & SSH authentication

**Daily recap (start of day):** N/A — first session with technical work; recap protocol
clarified with the student (recap covers technical content worked the previous day, not
memory-file trivia). Starts applying from Phase 1.

**Worked on:**
- Created `C:\API-Learning-Lab`, `git init` with branches `main` + `develop`.
- Copied the memory/documentation files into the repo, first commit, created the
  `api-learning-lab` repos on GitHub + GitLab, configured remotes, first push to both.
- Set up SSH auth so pushes no longer ask for a password: enabled the Windows `ssh-agent`
  service (startup Automatic), loaded both keys with `ssh-add`, and made Git Bash use
  Windows OpenSSH via `git config --global core.sshCommand`.
- Added a multi-push remote strategy: `origin` has two push URLs (GitHub + GitLab), so
  `git push origin <branch>` sends to both platforms.
- Updated the docs regarding folder names: corrected every reference to `FAST API - BORRADOR`
  → the real `FastApi - Project`, and excluded `INSTRUCCIONES...` from the repo `.gitignore`
  (internal-only material, per ADR-0005).

**Concepts learned / reinforced:**
- Git Bash ships its own SSH which ignores the Windows agent → `core.sshCommand` fixes it.
- A remote can hold multiple push URLs → one push reaches mirrored platforms.
- Branches need a first commit to be real; `git push -u` records tracking.

**Commands / tools used:**
- `Set-Service ssh-agent -StartupType Automatic` + `Start-Service ssh-agent` — enable agent
- `ssh-add` — load keys into agent
- `ssh -T git@github.com` / `git@gitlab.com` — verify auth
- `git remote set-url --add --push origin <url>` — multi-push to GitHub + GitLab
- `git push -u origin/... + git push -u gitlab/...` — publish branches

**Errors encountered:**
- `Enter passphrase ... Permission denied (publickey)` from Git Bash → Git Bash not using the
  Windows agent → resolved with `core.sshCommand "C:/Windows/System32/OpenSSH/ssh.exe"`.
- (Earlier) `LF would be replaced by CRLF` blocked a commit → resolved in the workflow of
  Session 01; noted for future stages.

**Questions still open:**
- None.

**Next session (target):**
- Phase 1 — Session 01: What is an API? The request journey mental model (no code).

**Commit / push:** `main` + `develop` → GitHub ✅ GitLab ✅ (push done during session).

---

## 2026-08-04 — Session 00 (Documentation Architecture)

**Phase / Stage:** Phase 0 — Planning · Created the memory/documentation architecture

**Daily recap (start of day):** N/A — first session with the new structure.

**Worked on:**
- Reviewed the 2 original draft files (`FASTAPI Project.txt`, `Project Tree.txt`) to
  capture the vision, scope, 5 phases, and methodology of the project.
- Moved the original drafts to `_archive/` to keep the root clean.
- Created the full documentation architecture following the **CI/CD Pipeline Labs** memory
  folder as template: `AGENTS.md`, `README.md`, `.gitignore`,
  `INSTRUCCIONES SESION DIARIA - IA.txt`, `docs/` (specification, mentor constitution,
  execution plan, learning roadmap, session log, environment, ADRs, stages).
- Recorded decisions as ADRs: 0001 version control from day one, 0002 mirror GitHub +
  GitLab, 0003 quality-only CI (no deployment), 0004 local-first zero-cost scope,
  0005 English documentation, 0006 in-memory store first, PostgreSQL when needed.
- Defined the roadmap: Phase 1 (Fundamentals) → Phase 2 (CRUD) → Phase 3 (PostgreSQL) →
  Phase 4 (Quality + CI) → Phase 5 (Closure & hand-off).

**Concepts learned / reinforced:**
- A portfolio is stronger when the repository shows the *evolution*, not just the result.
- An AI mentor can recall project state instantly if a single status file is maintained.
- The API project stays **local-only** (no Docker/VPS); its CI guarantees quality, not deployment.

**Commands / tools used:**
- None (documentation/planning only).

**Errors encountered:**
- None.

**Questions still open:**
- Whether to introduce a SQL ORM (e.g., SQLAlchemy) after raw SQL is mastered (candidate ADR in Phase 3).
- Confirm the Python version standard (3.11 planned) on the first code session.

**Next session (target):**
- Phase 0 — repo bootstrap: create `C:\API-Learning-Lab`, `git init` (`master` + `develop`),
  create GitHub + GitLab `api-learning-lab` repos, configure remotes, first push to both.

**Commit / push:** N/A — memory folder; will be synced to `C:\API-Learning-Lab` and pushed
in the first commit of the Phase 0 bootstrap.
