# Stage 02 — Real Project: IT Assets Inventory CRUD

> **Phase:** Phase 2 — Real Project
> **Estimated duration:** ~2.5 weeks (12 sessions)
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 01 complete (fundamentals validated). Data stays **in memory**
> in this stage — PostgreSQL arrives in Stage 03 (ADR-0006).

---

## Objective

Build the **IT Assets Inventory API** as a fully functional, professionally organized
FastAPI application: full CRUD, input/output schemas, real validations, and consistent
error handling — over an in-memory store, with every layer understood.

## Scenario (real world)

The company keeps its equipment (Laptops, Servers, Switches, Monitors, Printers,
Licenses) in spreadsheets. You are asked to build an **API** so other internal systems can
register, query, update, and remove assets programmatically. The API must validate data
before storing it, answer clearly when an asset does not exist, and be organized so that a
team can maintain it. This is a real feature-delivery task, not an exercise.

## Concepts (why first)

- **Why structure matters.** A single-file app dies as it grows. Splitting into `app/`,
  schemas, and routers mirrors how real projects are organized.
- **CRUD = the four verbs.** Create (POST), Read (GET), Update (PUT/PATCH), Delete (DELETE).
  Each maps to one operation and one status code.
- **Input vs output schemas.** What the client sends and what the API returns are
  different contracts. Pydantic models let you define both (and hide internal fields).
- **Validation = the front door.** Constraints (length, ranges, enums) and custom
  validators reject bad data before business logic runs. `422` is the "I understood your
  request but the data is wrong" answer.
- **Errors are a contract too.** A missing asset must be a clean `404`, never a crash. A
  consistent error JSON makes consumers' lives easy.
- **Routers = separation of concerns.** Grouping endpoints (`/assets`) into their own
  module keeps `main.py` readable as the app grows.
- **In-memory store (for now).** A Python list/dict is enough in this phase; its
  limitation (data vanishes on restart) is exactly what Stage 03 fixes.

## Pre-flight

- [ ] Stage 01 validated (you can explain the request journey and build small endpoints).
- [ ] You can use Swagger and `requests` to test an endpoint.
- [ ] You can explain what a Pydantic model and `HTTPException` are.

> ⚠️ **Rule for this stage:** no database yet. Everything lives in memory. No ORM.

---

## Sessions

### Session 01 — Project organization

- [ ] Explain why a growing app needs a package structure (why: maintainability)
- [ ] Create `app/` with `app/__init__.py` and `app/main.py`
- [ ] Move the FastAPI instance into `app/main.py`
- [ ] Run `uvicorn app.main:app --reload` (note the new import path)
- [ ] Draw the planned tree: `app/main.py`, `app/models.py`, `app/routers/`

### Session 02 — Data modeling: what is an IT asset

- [ ] List the asset types: Laptop, Server, Switch, Monitor, Printer, License
- [ ] Define the fields an asset needs (e.g., `id`, `name`, `type`, `status`,
      `brand`, `model`, `serial`, `assigned_to`, `purchase_date`)
- [ ] Explain why some fields are required and others optional
- [ ] Decide the value of each field's type (str, int, date…)
- [ ] Document the data model in the Report

### Session 03 — Pydantic schemas: AssetCreate vs AssetRead

- [ ] Explain why input and output are different contracts
- [ ] Create `AssetCreate` (client sends: name, type, brand, model, serial…)
- [ ] Create `AssetRead` (API returns: all of the above + `id`)
- [ ] Explain why the client should not send `id` (why: the system owns identifiers)
- [ ] Verify Swagger shows two different schemas

### Session 04 — Create: POST /assets

- [ ] Build `POST /assets` that receives `AssetCreate`
- [ ] Generate the `id` in the store (why: server-owned identifiers)
- [ ] Return the created asset with status `201 Created`
- [ ] Test in Swagger and with `requests.post(..., json=...)`
- [ ] Explain why `201` (not `200`) is the correct code

### Session 05 — Read: GET /assets and GET /assets/{asset_id}

- [ ] Build `GET /assets` returning the full list (why: listing is the common view)
- [ ] Build `GET /assets/{asset_id}` returning one asset
- [ ] Raise `HTTPException(status_code=404, ...)` when the asset does not exist
- [ ] Test: existing id → asset; missing id → clean `404`
- [ ] Explain why the API never crashes on a bad id

### Session 06 — Update: PUT vs PATCH

- [ ] Explain the difference: `PUT` replaces the whole resource; `PATCH` updates part of it
- [ ] Build `PUT /assets/{asset_id}` (full replacement, `AssetCreate`)
- [ ] Build `PATCH /assets/{asset_id}` (partial update, optional fields)
- [ ] Handle the missing-asset case with `404`
- [ ] Test both with `requests.put(...)` and `requests.patch(...)`

### Session 07 — Delete: DELETE /assets/{asset_id}

- [ ] Build `DELETE /assets/{asset_id}`
- [ ] Return `204 No Content` on success (why: nothing to return)
- [ ] Raise `404` when the asset does not exist
- [ ] Verify the list no longer contains the deleted asset
- [ ] Test the full cycle: create → read → update → delete

### Session 08 — Validations

- [ ] Add constraints: `name` with `min_length`, `serial` optional, `purchase_date` as date
- [ ] Constrain `type` and `status` with a Pydantic enum or literal
- [ ] Add a custom validator (e.g., `serial` unique or normalized format)
- [ ] Send invalid data and verify `422` responses explain the problem
- [ ] Explain the difference between a `422` (bad data) and a `404` (not found)

### Session 09 — Error handling

- [ ] Replace ad-hoc `HTTPException`s with a consistent error JSON shape
- [ ] Register a custom exception handler (e.g., a global 404 shape)
- [ ] Explain why consistent error bodies help clients (why: they can parse errors)
- [ ] Verify Swagger documents the possible error codes
- [ ] Document the error contract in the Report

### Session 10 — Routers

- [ ] Move asset endpoints into `app/routers/assets.py`
- [ ] Create `APIRouter(prefix="/assets", tags=["assets"])`
- [ ] Include the router in `app/main.py`
- [ ] Verify all endpoints still work at the same URLs
- [ ] Explain what `prefix` and `tags` do (why: organization + Swagger grouping)

### Session 11 — Lab: full CRUD with edge cases

- [ ] Exercise every operation with `requests` scripts (create, list, get one, update,
      patch, delete)
- [ ] Exercise edge cases: missing id, invalid body, invalid enum, delete twice
- [ ] Verify each edge case returns the expected status code
- [ ] Save screenshots of Swagger and script output
- [ ] Confirm the app still runs cleanly end to end

### Session 12 — Phase 2 checkpoint

- [ ] Answer the Mentor Questions in your own words in the Report
- [ ] Save evidence in `screenshots/stage-02/`
- [ ] Write an ADR if a meaningful decision was made
- [ ] Session log entry appended
- [ ] Execution plan Phase 2 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

---

## Mentor Questions

1. Why separate `AssetCreate` from `AssetRead`? What could go wrong if you used one model?
2. What is CRUD, and which HTTP verbs map to each operation?
3. What is the difference between `PUT` and `PATCH`? When do you use each?
4. Why does a missing asset return `404` and invalid data return `422`? Who produces each?
5. What is a router, and why split the application into modules?
6. Why is the data stored in memory in this phase? What is the limitation?
7. How would a client know, from the status code alone, whether a request succeeded?

---

## Report (student fills after the session)

### What I did

### How it works / why

(Your answers to the Mentor Questions.)

### Commands I used

| Command | Why I used it |
|---|---|
| `uvicorn app.main:app --reload` | Run the organized application |
| `requests.post('http://127.0.0.1:8000/assets/', json={...})` | Create an asset from a client |
| `requests.patch('http://127.0.0.1:8000/assets/1', json={...})` | Partially update an asset |
| … | … |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> Write 5–10 sentences explaining how a real CRUD API is organized **now that you have
> built one**.

### Evidence

- [ ] Screenshots saved in `screenshots/stage-02/` (e.g., `01-swagger-crud.png`, `02-requests-flow.png`)
- [ ] ADR written (if a decision was made)
- [ ] Session log entry appended
- [ ] Execution plan updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

> 🚀 **Next:** Stage 03 — PostgreSQL: replace the in-memory list with real, persistent storage.
