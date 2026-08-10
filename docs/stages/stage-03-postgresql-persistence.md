# Stage 03 — PostgreSQL Persistence

> **Phase:** Phase 3 — PostgreSQL
> **Estimated duration:** ~2.5 weeks (12 sessions)
> **Status:** ⬜ Pending
> **Prerequisites:** Stage 02 complete (CRUD working over the in-memory store). PostgreSQL
> 18 is installed and running locally (ADR-0004: local-first, no Docker).

---

## Objective

Replace the in-memory list with **real persistent storage**: create the database and the
`assets` table, learn the basic SQL (CREATE, INSERT, SELECT, UPDATE, DELETE), connect
FastAPI to PostgreSQL, and prove that data survives restarts.

## Scenario (real world)

The API works, but every restart loses the data — the "spreadsheet problem" returns.
The company now asks: *"make the data survive and be queryable by the database team."*
You must connect the API to a real database without hiding how the connection and the SQL
work. Persistence is the moment the API becomes useful in production.

## Concepts (why first)

- **Why a database.** An in-memory list lives and dies with the process. A database keeps
  data on disk, survives restarts, and is shared, concurrent, and queryable.
- **Relational model.** A database contains **tables**; a table is a grid of **rows**
  (records) and **columns** (fields); a **primary key** uniquely identifies each row.
- **SQL = the language of the database.** DDL (CREATE TABLE) defines structure; DML
  (INSERT, SELECT, UPDATE, DELETE) manipulates data. The CRUD verbs map 1-to-1 to SQL.
- **PostgreSQL.** A mature open-source relational database. Running locally as a service
  (`postgresql-x64-18`); `psql` is the client to talk to it.
- **Connecting from Python.** A driver (e.g., `psycopg`) speaks the PostgreSQL protocol.
  The connection string (host, port, user, password, dbname) is configuration, not code —
  it lives in a `.env` file that is never committed.
- **Connection management.** Opening one connection per query is wasteful; a **pool**
  reuses connections. Correctly closing/returning connections is a production habit.
- **Persistence is the test.** Restart the app → data is still there. That is the moment
  the in-memory store dies for good.

## Pre-flight

- [ ] Stage 02 validated (full CRUD over the in-memory store).
- [ ] PostgreSQL service is running (`Get-Service postgresql-x64-18` → Running).
- [ ] `psql` is available (`C:\Program Files\PostgreSQL\18\bin\psql.exe`).
- [ ] You understand what a table/row/column is at a conceptual level.

> ⚠️ **Rule for this stage:** raw SQL first. No ORM yet — the goal is to *see* the SQL.
> The ORM decision is recorded as ADR-0007 if adopted.

---

## Sessions

### Session 01 — Databases vs memory

- [ ] Explain the difference between a list in RAM and a table on disk (why: RAM is
      ephemeral, disk is persistent)
- [ ] Explain tables, rows, columns, and primary keys
- [ ] Explain what "relational" means and why assets are a natural table
- [ ] Identify the failure that motivates this stage (the restart that erases data)
- [ ] Document the model in the Report

### Session 02 — PostgreSQL intro and first database

- [ ] Verify the service is running and locate `psql`
- [ ] Connect: `psql -U postgres` (or the configured superuser)
- [ ] Create the project database: `CREATE DATABASE api_learning_lab;`
- [ ] Connect to it: `\c api_learning_lab`
- [ ] Explain: server vs database vs table (why: a server hosts many databases)
- [ ] Save a screenshot of the psql session

### Session 03 — SQL DDL: CREATE TABLE assets

- [ ] Write `CREATE TABLE assets (...)` with the fields from Stage 02
- [ ] Choose the right types: `SERIAL`/`BIGSERIAL` or `GENERATED` for `id`, `TEXT`/`VARCHAR`,
      `DATE`, and a `status` constraint
- [ ] Declare `PRIMARY KEY (id)`
- [ ] Run it in psql and inspect with `\d assets`
- [ ] Explain what a schema (the table's blueprint) is

### Session 04 — SQL DML: INSERT, SELECT, UPDATE, DELETE

- [ ] Practice `INSERT INTO assets (...) VALUES (...);`
- [ ] Practice `SELECT * FROM assets;` and `SELECT ... WHERE id = 1;`
- [ ] Practice `UPDATE assets SET status = 'retired' WHERE id = 1;`
- [ ] Practice `DELETE FROM assets WHERE id = 1;`
- [ ] Explain each command in your own words (why: these are the four verbs the API will use)
- [ ] Document the SQL in the Report

### Session 05 — Connecting FastAPI to PostgreSQL

- [ ] Add the driver (`psycopg[binary]` or equivalent) to `requirements.txt`
- [ ] Create `app/database.py` holding the connection settings
- [ ] Read settings from environment variables / a local `.env` (never committed)
- [ ] Write a function that opens a connection and returns it
- [ ] Test the connection from a small script (why: verify before wiring the API)
- [ ] Explain what the connection string contains and why it is secret

### Session 06 — Connection management

- [ ] Explain the problem with opening one connection per query (why: slow, wasteful)
- [ ] Implement a small connection **pool** (or a request-scoped connection helper)
- [ ] Explain where connections are created and where they are returned/closed
- [ ] Explain what happens when the database is down (fail fast, clear error)
- [ ] Document the connection lifecycle in the Report

### Session 07 — Migrate Create: INSERT mapped to POST /assets

- [ ] Replace the in-memory append with an `INSERT` in `POST /assets`
- [ ] Return the new asset including the id generated by the database
- [ ] Verify a row appears in psql: `SELECT * FROM assets;`
- [ ] Keep the `201` response and validation intact
- [ ] Explain how the SQL command and the endpoint map to each other

### Session 08 — Migrate Read: SELECT mapped to GET /assets

- [ ] Replace the list return with `SELECT ... ORDER BY id` in `GET /assets`
- [ ] Replace the single lookup with `SELECT ... WHERE id = %s` in `GET /assets/{asset_id}`
- [ ] Keep the `404` behavior when no row matches
- [ ] Explain how a Python driver result (rows) becomes the JSON response
- [ ] Verify with psql that the returned data matches the table

### Session 09 — Migrate Update: UPDATE mapped to PUT / PATCH

- [ ] Replace `PUT /assets/{asset_id}` with an `UPDATE` statement
- [ ] Replace `PATCH /assets/{asset_id}` with a partial `UPDATE`
- [ ] Detect "row not found" and return `404`
- [ ] Explain why `UPDATE` affects the row but keeps the `id` intact
- [ ] Verify changes in psql

### Session 10 — Migrate Delete: DELETE mapped to DELETE /assets/{asset_id}

- [ ] Replace the in-memory delete with `DELETE FROM assets WHERE id = %s`
- [ ] Return `204` when a row was deleted, `404` when not found
- [ ] Explain how "rows affected" tells you whether the asset existed
- [ ] Verify the row disappears from psql
- [ ] Run the full CRUD cycle once more, now on PostgreSQL

### Session 11 — Persistence proof

- [ ] Create assets via the API
- [ ] **Restart the app** (stop and start uvicorn)
- [ ] `GET /assets` again — the data is still there (why: it lives in PostgreSQL now)
- [ ] Query the same data directly in psql to prove it is real storage
- [ ] Explain what would have happened with the old in-memory store

### Session 12 — Phase 3 checkpoint

- [ ] Answer the Mentor Questions in your own words in the Report
- [ ] Save evidence in `screenshots/stage-03/` (psql sessions + API output)
- [ ] Write ADR-0007 if the ORM decision is made (or record why raw SQL is kept)
- [ ] Session log entry appended
- [ ] Execution plan Phase 3 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

---

## Mentor Questions

1. What is a table, a row, a column, and a primary key?
2. Why does persistence matter? What exactly was wrong with the in-memory list?
3. What does each SQL command do — INSERT, SELECT, UPDATE, DELETE?
4. How does the FastAPI app connect to PostgreSQL? Why are the settings in environment
   variables and not in the code?
5. Why a connection pool instead of one connection per query?
6. What happens to the API if PostgreSQL is down? How should it behave?
7. How do you know (in code) that an UPDATE/DELETE found the row or not?

---

## Report (student fills after the session)

### What I did

### How it works / why

(Your answers to the Mentor Questions.)

### Commands I used

| Command | Why I used it |
|---|---|
| `psql -U postgres` | Connect to the local PostgreSQL server |
| `CREATE DATABASE api_learning_lab;` | Create the project database |
| `CREATE TABLE assets (...)` | Define the table structure |
| `SELECT * FROM assets;` | Inspect stored rows |
| `uvicorn app.main:app --reload` | Run the app now connected to PostgreSQL |
| … | … |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> Write 5–10 sentences explaining the difference between memory and a database, **now
> that you have seen the data survive a restart**.

### Evidence

- [ ] Screenshots saved in `screenshots/stage-03/` (e.g., `01-create-table.png`, `02-persistence-restart.png`)
- [ ] ADR written (if a decision was made)
- [ ] Session log entry appended
- [ ] Execution plan updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

> 🚀 **Next:** Stage 04 — Code Quality & CI: tests, linters, type checking, security, and a
> quality-only pipeline on GitHub and GitLab.
