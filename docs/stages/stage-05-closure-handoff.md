# Stage 05 — Closure & Handoff

> **Phase:** Phase 5 — Closure & Handoff
> **Estimated duration:** ~1 week (5 sessions)
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 04 complete (quality tools + both CI pipelines green).

---

## Objective

Close the project with complete confidence: review the whole journey, run the final
validation, produce the final documentation (including the 11 study documents), and leave
the API **ready to be consumed by a deployment pipeline** — the exact boundary where the
CI/CD Pipeline Labs project takes over.

## Scenario (real world)

Delivery time. The team asks: *"is this API ready for production deployment?"* You must
demonstrate it: tests green, quality tools green, manual + Swagger proof, complete
documentation, and a precise hand-off — *here is what the deployment project will consume,
and here is why it is safe to deploy.* No new features. A professional close-out.

## Concepts (why first)

- **Why closure matters.** A project is not finished when it "works" — it is finished when
  it is **proven and understood**. This stage converts work into a portfolio story.
- **The full journey, end to end.** Client → HTTP → Uvicorn → FastAPI → Pydantic →
  logic → PostgreSQL → response → (CI validates it all). Being able to narrate this is the
  real outcome of the project.
- **The 11 study documents.** The original plan defined one document per topic: API, HTTP,
  Requests, Uvicorn, FastAPI, Swagger, PostgreSQL, CRUD, Testing, CI, and Final Summary.
  Each one is a teaching artifact an interviewer can read.
- **Evidence of readiness.** Green pipeline + green tests + working Swagger + reproducible
  README = the API is "ready for a deployment process".
- **The hand-off boundary.** This project builds and validates; the **CI/CD Pipeline Labs**
  project containerizes and deploys. Defining exactly what it consumes (repo, README,
  requirements, tests, CI) makes the boundary clean (ADR-0003, ADR-0004).

## Pre-flight

- [ ] Stage 04 validated (quality tools + both pipelines green).
- [ ] The API runs locally and all CRUD works on PostgreSQL.
- [ ] The repository is clean and synced between the memory folder and `C:\API-Learning-Lab`.

---

## Sessions

### Session 01 — Full review: the request journey

- [ ] Explain, out loud and on paper, the complete journey of one request from client to
      PostgreSQL and back (why: narration is the proof of understanding)
- [ ] Trace one real request: run it, and point at each layer that handled it
- [ ] Review the ADRs and explain each decision
- [ ] Identify any weak spot found during the narration and reinforce it
- [ ] Note the weak spot (if any) in the Report

### Session 02 — Final validation pass

- [ ] Run `pytest` → all green
- [ ] Run `ruff check .`, `black --check .`, `mypy app/`, `bandit -r app/`, `pip-audit` → all green
- [ ] Trigger the CI on a final commit and confirm **both** GitHub and GitLab are green
- [ ] Manual pass: create, list, get, update, delete via Swagger and `requests`
- [ ] Restart the app and confirm persistence one last time
- [ ] Save the final evidence

### Session 03 — Final documentation (the 11 study documents)

- [ ] Write/consolidate `docs/study/01-what-is-an-api.md`
- [ ] `02-http.md` · `03-requests.md` · `04-uvicorn.md` · `05-fastapi.md` · `06-swagger.md`
- [ ] `07-postgresql.md` · `08-crud.md` · `09-testing.md` · `10-continuous-integration.md`
- [ ] `11-final-summary.md`
- [ ] Each document contains: simple explanation, diagram, examples, lab, FAQ (why: this is
      the manual of the project)
- [ ] Link the study documents from the README

### Session 04 — Final README and architecture

- [ ] Finalize the README: what, why, architecture diagram (user → HTTP → Uvicorn → FastAPI
      → PostgreSQL), quick start, testing, CI badges
- [ ] Add the request-journey diagram and the hand-off note
- [ ] Verify the repository is readable by an interviewer (structure, docs, evidence)
- [ ] Take the final screenshots of the whole project state

### Session 05 — Hand-off and close

- [ ] Write the "Hand-off statement": *"The API is completely built, documented, tested,
      and validated to be consumed by a deployment process."*
- [ ] Define exactly what the deployment project will consume: the repo, `requirements.txt`,
      the FastAPI app, tests, and the green CI as proof
- [ ] Answer the Mentor Questions in your own words in the Report
- [ ] Save evidence in `screenshots/stage-05/`
- [ ] Final session log entry; execution plan marked complete
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab
- [ ] Celebrate: the API is handed to the CI/CD Pipeline Labs project 🚀

---

## Mentor Questions

1. Walk through the entire journey of a request, end to end, without notes.
2. What proves the API is "ready to be consumed by a deployment process"?
3. What exactly will the CI/CD Pipeline Labs project receive and do with this API?
4. Which decision in this project was the hardest, and why did you make it?
5. Defend one ADR of your choice as if you were in an interview.

---

## Report (student fills after the session)

### What I did

### How it works / why

(Your answers to the Mentor Questions.)

### Commands I used

| Command | Why I used it |
|---|---|
| `pytest` | Final test run |
| `ruff check . && black --check . && mypy app/` | Final quality pass |
| `bandit -r app/ && pip-audit` | Final security pass |
| `uvicorn app.main:app --reload` | Final manual run |
| … | … |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> Write 10+ sentences: what this project taught you, what the API is now, and why you can
> say with confidence that it is ready for a deployment pipeline.

### Evidence

- [ ] Screenshots saved in `screenshots/stage-05/` (e.g., `01-final-tests.png`, `02-both-ci-green.png`, `03-architecture.png`)
- [ ] ADR written (if a decision was made)
- [ ] Final session log entry appended
- [ ] Execution plan fully checked + Current Status updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

> 🚀 **This project is done.** The next chapter happens in the **CI/CD Pipeline Labs**
> project: repository → pipeline → image → registry → VPS → deployment.
