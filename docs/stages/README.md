# Stages

## Index & Evidence Rules

**Project:** API-Learning-Lab

---

## Index

| Stage | Title | Phase | Status |
|---|---|---|---|
| 01 | [API Fundamentals](stage-01-api-fundamentals.md) | 1 | ⬜ Pending |
| 02 | [Real Project — IT Assets Inventory CRUD](stage-02-real-project-crud.md) | 2 | ⬜ Pending |
| 03 | [PostgreSQL Persistence](stage-03-postgresql-persistence.md) | 3 | ⬜ Pending |
| 04 | [Code Quality & CI](stage-04-code-quality-ci.md) | 4 | ⬜ Pending |
| 05 | [Closure & Handoff](stage-05-closure-handoff.md) | 5 | ⬜ Pending |

> Each stage corresponds to one phase (1 stage = 1 phase), the same structure used by the
> reference project (CI/CD Pipeline Labs). Detailed checklists and status live in
> [`docs/execution-plan.md`](../execution-plan.md).

---

## Evidence Rules

Every stage produces **evidence** — proof that the work happened and can be reproduced.

### Screenshots

- One folder per stage: `screenshots/stage-01/`, `screenshots/stage-02/`, …
- Name files descriptively: `01-first-app-swagger.png`, `02-pytest-green.png`, …
- Capture what matters (commands + output), not the whole screen.

### Command logs

- Save meaningful command output as text files under `screenshots/stage-NN/` when a
  screenshot is not practical.

### Reproducibility

- Another person must be able to follow the stage document and get the same result.
- Include every command with a one-line "why".

---

## Definition of Done (applies to every stage)

A stage is complete when **all** are true:

- [ ] All checklist items in the stage document are ticked.
- [ ] The **Report** section at the bottom of the stage is filled by the student.
- [ ] Evidence exists in `screenshots/stage-NN/`.
- [ ] ADR written if a meaningful decision was made.
- [ ] `session-log.md` has a new entry.
- [ ] `execution-plan.md` checkboxes + Current Status updated.
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to **both**
      GitHub and GitLab.
- [ ] The student can explain the stage back to the mentor (mentor validation passed).

---

## Stage Template

Every stage file follows `_template.md`. The template guarantees consistency, which makes
the repository easy to read for an interviewer and easy to resume for an AI.
