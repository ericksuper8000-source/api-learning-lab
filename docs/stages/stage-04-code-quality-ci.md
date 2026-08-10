# Stage 04 — Code Quality & CI

> **Phase:** Phase 4 — Code Quality & CI
> **Estimated duration:** ~2.5 weeks (12 sessions)
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 03 complete (PostgreSQL-backed CRUD). Tools are added gradually
> — never all at once (ADR-0003: quality-only CI, no deployment).

---

## Objective

Guarantee the project can be maintained professionally: automated tests with Pytest,
code quality with Ruff, Black, and Mypy, security with Bandit and pip-audit, and a
**quality-only CI pipeline** on GitHub Actions and GitLab CI that runs all of them on
every push.

## Scenario (real world)

The API works, but the team cannot trust *changes*. A junior pushes a "small fix" that
breaks formatting, type checks, or a test. The company asks: *"make every push prove that
the code is still correct and clean."* This stage builds that safety net — without a
single deployment, because deployment belongs to the CICD project.

## Concepts (why first)

- **Why quality gates.** A professional pipeline never ships broken code. Tests and linters
  turn "I think it works" into "it is proven to work".
- **Pytest.** The testing framework. **Unit tests** check functions in isolation;
  the **TestClient** lets you test the whole API (requests in, responses out).
- **Ruff.** Fast linter: catches bugs, unused imports, and style problems in one tool.
- **Black.** The formatter. It is the *uncompromising* style. In CI it runs as
  `--check` so it reports problems instead of silently rewriting your files.
- **Mypy.** Static type checking: catches whole classes of bugs that only appear at
  runtime, by checking the type hints *before* running.
- **Bandit.** Security scanner for Python code (e.g., hard-coded secrets, unsafe calls).
- **pip-audit.** Checks installed dependencies against known vulnerability databases.
- **CI = the automatic referee.** On every push, GitHub Actions and GitLab CI run:
  install → Ruff → Black --check → Mypy → Pytest → Bandit → pip-audit. Green = the API is
  considered ready to keep evolving. No Docker, no deploy (ADR-0003).

## Pre-flight

- [ ] Stage 03 validated (PostgreSQL CRUD works).
- [ ] The API runs with `uvicorn app.main:app --reload`.
- [ ] `requirements.txt` is complete and the venv works.

> ⚠️ **Rule for this stage:** each tool is added one session at a time, and only when its
> problem is understood. The CI pipelines contain **quality jobs only**.

---

## Sessions

### Session 01 — Why quality gates exist

- [ ] Explain what could break if a team merges code with no checks (why: regressions)
- [ ] List the six tools and the single problem each one solves
- [ ] Explain the difference between CI (this stage) and CD (out of scope, ADR-0003)
- [ ] Draw what the pipeline will do on every push
- [ ] Document the plan in the Report

### Session 02 — Pytest: first unit tests

- [ ] Add `pytest` to `requirements.txt` (dev) and install it
- [ ] Write a small pure unit test for a helper function (if none exists, create one)
- [ ] Run `pytest` and see it pass
- [ ] Explain what a unit test is and what makes a *good* one (why: isolated, fast, clear)
- [ ] Save a screenshot of the green output

### Session 03 — TestClient: API tests

- [ ] Use FastAPI's `TestClient` to test the running app *in memory*
- [ ] Write tests for `GET /assets` and `GET /assets/{id}` (200 and 404)
- [ ] Write tests for `POST /assets` (201 and 422)
- [ ] Run the whole suite with `pytest`
- [ ] Explain the difference: unit test vs API test

### Session 04 — Fixtures, parametrize, test strategy

- [ ] Use a `fixture` to create the app/TestClient once and reuse it
- [ ] Use `@pytest.mark.parametrize` to test many cases with less code
- [ ] Define the test strategy for the database (e.g., dedicated test database or per-test
      cleanup)
- [ ] Explain how tests stay independent of each other (why: no shared state)
- [ ] Ensure the suite passes consistently

### Session 05 — Ruff: linting

- [ ] Add `ruff` and run `ruff check .`
- [ ] Understand the errors it reports (unused imports, undefined names, style)
- [ ] Fix the reported issues **by hand** (why: understand each rule)
- [ ] Configure Ruff in `pyproject.toml` (or `ruff.toml`) with the project's rules
- [ ] Verify `ruff check .` is clean

### Session 06 — Black: formatting

- [ ] Add `black` and run `black --check .` (why: check first, then format)
- [ ] Run `black .` to format the code
- [ ] Explain why Black has almost no options (why: the point is zero debate about style)
- [ ] Run both Ruff and Black together and confirm they pass
- [ ] Explain why CI will use `--check`

### Session 07 — Mypy: type checking

- [ ] Add `mypy` and run `mypy app/`
- [ ] Fix type errors — add type hints to functions and variables (why: types document and protect)
- [ ] Explain what a "static type check" is and what bugs it prevents
- [ ] Configure Mypy (target Python version, strictness level) in `pyproject.toml`
- [ ] Verify `mypy app/` is clean

### Session 08 — Bandit: security

- [ ] Add `bandit` and run `bandit -r app/`
- [ ] Explain what Bandit looks for (why: secrets, unsafe functions, injection risks)
- [ ] Review any findings with the mentor and fix them if real
- [ ] Configure Bandit exclusions/skip levels if justified
- [ ] Verify the scan reports no high-severity issues

### Session 09 — pip-audit: dependencies

- [ ] Add `pip-audit` and run `pip-audit`
- [ ] Explain what it checks (why: known vulnerabilities in installed packages)
- [ ] Update dependencies if it reports issues (verify tests still pass)
- [ ] Explain the difference: Bandit scans *your* code, pip-audit scans *your dependencies*
- [ ] Verify the audit is clean

### Session 10 — GitHub Actions (quality-only)

- [ ] Create `.github/workflows/ci.yml` (why: this file defines the pipeline)
- [ ] Trigger on `push` to `develop` and `pull_request` to `master`
- [ ] Job `quality`: install → Ruff → Black --check → Mypy → Bandit → pip-audit
- [ ] Job `test`: install → Pytest (against the test database strategy)
- [ ] Push and watch the pipeline run green on GitHub
- [ ] Explain each element: triggers, jobs, steps, needs

### Session 11 — GitLab CI + secrets/variables

- [ ] Create `.gitlab-ci.yml` with the same quality + test jobs (why: mirrored platforms)
- [ ] Push and verify the pipeline runs green on GitLab
- [ ] Store test database credentials as CI variables (GitHub Secrets / GitLab Variables),
      never in the repo
- [ ] Explain why secrets live in the platform, not in `requirements.txt` or `.env`
- [ ] Compare how both platforms express the same pipeline

### Session 12 — Professional README + checkpoint

- [ ] Rewrite the project README: what it is, architecture, how to run, how to test
- [ ] Add the setup/run/test commands and a small diagram of the request journey
- [ ] Answer the Mentor Questions in your own words in the Report
- [ ] Save evidence in `screenshots/stage-04/` (tool outputs + both pipelines green)
- [ ] Session log entry appended
- [ ] Execution plan Phase 4 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

---

## Mentor Questions

1. What is the responsibility of each tool: Pytest, Ruff, Black, Mypy, Bandit, pip-audit?
2. Why does Black run as `--check` in CI and not as `black .`?
3. What is the difference between a unit test and an API test with the TestClient?
4. Why does this project's CI **not deploy**? (Reference ADR-0003.)
5. How are secrets stored in CI variables and why not in the repository?
6. What does it mean for a pipeline to be "green", and why does it matter on every push?

---

## Report (student fills after the session)

### What I did

### How it works / why

(Your answers to the Mentor Questions.)

### Commands I used

| Command | Why I used it |
|---|---|
| `pytest` | Run the test suite |
| `ruff check .` | Lint the code |
| `black --check .` | Verify formatting without changing files |
| `mypy app/` | Static type checking |
| `bandit -r app/` | Security scan of the application code |
| `pip-audit` | Vulnerability audit of dependencies |
| … | … |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> Write 5–10 sentences explaining why a team needs automated quality gates **now that you
> have built your own pipeline**.

### Evidence

- [ ] Screenshots saved in `screenshots/stage-04/` (e.g., `01-pytest-green.png`, `02-github-actions-green.png`, `03-gitlab-ci-green.png`)
- [ ] ADR written (if a decision was made)
- [ ] Session log entry appended
- [ ] Execution plan updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

> 🚀 **Next:** Stage 05 — Closure & Handoff: final review, final documentation, and
> leaving the API ready for the deployment pipeline.
