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

---

## Entries

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
