# Stage 01 — API Fundamentals

> **Phase:** Phase 1 — API Fundamentals
> **Estimated duration:** ~2.5 weeks (12 sessions)
> **Status:** ⬜ Pending
> **Prerequisites:** Phase 0 complete (plan + repos bootstrapped: `C:\API-Learning-Lab`
> pushed to GitHub and GitLab). This stage is **concept-first**: we build the mental model
> before the first endpoint.

---

## Objective

Understand completely how an API works — what HTTP is, what travels between a client and a
server, what Uvicorn and FastAPI do, and how to build and test small endpoints (GET, POST,
path, query, body) with Swagger — so that everything in Phase 2 makes sense instead of
being copy-paste.

## Scenario (real world)

A company tells you: *"we need our data exposed so other systems can consume it over
HTTP."* Before writing the inventory API, you must understand the rules of the road
(HTTP), who receives the traffic (Uvicorn), who decides what happens (FastAPI), and how to
try it yourself (Swagger + `requests`). A backend junior who cannot explain these layers
cannot diagnose why a request fails in production.

## Concepts (why first)

- **Why APIs exist.** Applications need to exchange data. An API is a contract: "send me
  this request, I give you this response." REST is a style for organizing those contracts
  over HTTP.
- **HTTP = the language.** Every request/response is text with a method (GET, POST…), a
  URL, headers, and a body. Status codes tell the client what happened (200, 201, 404, 422…).
- **Uvicorn = the doorman.** A program that listens on a port, receives raw HTTP, and
  hands it to your app. FastAPI is an *application framework* that runs *inside* Uvicorn.
- **FastAPI = the router.** It maps URLs and methods to functions and uses type hints +
  Pydantic to validate data automatically.
- **Parameters: where data lives.** In the URL path (`/assets/1`), in the query string
  (`?status=active`), or in the body (JSON payload). Each has a different use.
- **Swagger = free documentation.** FastAPI generates interactive docs from your code —
  proof that code and docs never drift apart.
- **JSON = the envelope.** Clients and servers exchange JSON; Python dicts and JSON are
  nearly the same thing.

## Pre-flight

- [ ] You can answer: "What problem does an API solve?" in one sentence.
- [ ] You know the difference between client and server.
- [ ] Git works and the repo `C:\API-Learning-Lab` is pushed to GitHub + GitLab.
- [ ] Python 3.11 is confirmed as the project standard (via `py -3.11 --version`).

> ⚠️ **Rule for this stage:** no ORM, no database, no Docker. Small endpoints and full
> understanding only.

---

## Sessions

### Session 01 — What is an API? The request journey (no code)

- [ ] Explain (with the mentor, no code): what an API is and why a company would expose one
- [ ] Draw the journey: Client → HTTP → Uvicorn → FastAPI → response
- [ ] Identify every layer in the drawing and what it is responsible for
- [ ] Compare: a webpage request vs an API request (JSON vs HTML)
- [ ] Write the mental model in the Report

### Session 02 — HTTP: methods, status codes, request anatomy

- [ ] Explain what a method (GET, POST, PUT, DELETE) means and when each is used
- [ ] Explain the anatomy of a request: method, URL, headers, body
- [ ] Explain the anatomy of a response: status code, headers, body
- [ ] Read the meaning of 200, 201, 204, 404, 422, 500 (and why they matter)
- [ ] Practice: identify the method/URL/status in a few made-up examples

### Session 03 — Environment + first app

- [ ] Create the venv: `py -3.11 -m venv .venv` inside `C:\API-Learning-Lab` (why: isolated deps)
- [ ] Activate it and verify `python --version` is 3.11
- [ ] Create `requirements.txt` with `fastapi` and `uvicorn` (why: reproducible deps)
- [ ] Install: `pip install -r requirements.txt` (why: one command installs everything)
- [ ] Write the first `main.py`: `app = FastAPI()` + `@app.get("/")` returning a message
- [ ] Run it: `uvicorn main:app --reload` (why: `--reload` restarts on changes)
- [ ] Open `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/docs` (Swagger appears — already!)
- [ ] Verify the journey: your browser (client) → HTTP → Uvicorn → FastAPI → response

### Session 04 — GET endpoints + path parameters

- [ ] Create `@app.get("/hello")` and test it in the browser and in Swagger
- [ ] Explain why `/hello` is a "path"
- [ ] Add a path parameter: `@app.get("/items/{item_id}")`
- [ ] Explain that `{item_id}` is a variable *inside* the URL
- [ ] Test with different values in Swagger (why: Swagger shows the parameter)
- [ ] Explain the difference between the URL path and the data the client sends

### Session 05 — Query parameters

- [ ] Add a query parameter: `@app.get("/items/")` with `q: str | None = None`
- [ ] Test with `?q=servidor` and without it (why: query = optional filters)
- [ ] Combine path + query: `/items/{item_id}?verbose=true`
- [ ] Explain when a value belongs in the path vs the query string
- [ ] Document the examples in the Report

### Session 06 — POST + JSON body + Pydantic

- [ ] Explain what a request body is and when it is used (why: you cannot put complex data in a URL)
- [ ] Create a Pydantic model: `class Item(BaseModel)` with typed fields
- [ ] Create `@app.post("/items/")` that receives the model as parameter
- [ ] Send JSON from Swagger and verify the API echoes it back
- [ ] Explain: JSON in → Pydantic validates → dict → response
- [ ] Compare: dictionary vs Pydantic model (why Pydantic validates, a dict does not)

### Session 07 — Path + query + body together; validation and 422

- [ ] Create one endpoint that uses path + query + body at the same time
- [ ] Send invalid data (e.g., wrong type) and observe the `422` response
- [ ] Explain what `422 Unprocessable Entity` means and who produced it (Pydantic/FastAPI)
- [ ] Add simple constraints (`min_length`, `gt`) and verify validation again
- [ ] Explain why validation happens *before* your function runs

### Session 08 — Status codes and response models

- [ ] Return different status codes from endpoints: `200`, `201`, `204`, `404`
- [ ] Explain when each code should be used (why: codes are a contract with the client)
- [ ] Use `response_model=` to declare the shape of the response
- [ ] Verify Swagger documents the response models automatically
- [ ] Explain the difference between the data you return and what the client sees

### Session 09 — The `requests` library (client side)

- [ ] Add `requests` to `requirements.txt` and install it
- [ ] Write a small script that does `requests.get(...)` and prints `status_code` + `.json()`
- [ ] Write a script that does `requests.post(..., json={...})`
- [ ] Verify the scripts work against the running API (why: this is how real clients talk to APIs)
- [ ] Compare: Swagger vs `requests` script — same request, two ways to make it

### Session 10 — Swagger/OpenAPI deep dive

- [ ] Open `/docs` and explore the generated schema of every endpoint
- [ ] Explain how FastAPI generates OpenAPI from the code (type hints + docstrings)
- [ ] Use Swagger to call every endpoint built so far
- [ ] Explain why auto-generated docs never get out of date
- [ ] Save screenshots: `01-swagger-list.png`, `02-swagger-request.png`

### Session 11 — Lab: a small in-memory list API

- [ ] Build a mini API around a simple Python list: `GET /grupo1/` returns the list
- [ ] `POST /grupo1/` adds an element (JSON body)
- [ ] `PUT /grupo1/` replaces an element at a position
- [ ] `DELETE /grupo1/?indice=0` removes an element
- [ ] Test every operation with `requests` scripts AND Swagger
- [ ] Verify a full flow: create → read → update → delete

### Session 12 — Phase 1 checkpoint

- [ ] Answer the Mentor Questions in your own words in the Report
- [ ] Save evidence (screenshots) in `screenshots/stage-01/`
- [ ] Write an ADR if a meaningful decision was made (e.g., Python 3.11 standard)
- [ ] Session log entry appended
- [ ] Execution plan Phase 1 checkboxes + Current Status updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

---

## Mentor Questions

1. What is an API, and what problem does it solve?
2. Walk through what happens between the browser sending `GET /items/1` and the response arriving.
3. What does Uvicorn do, and what does FastAPI do? Why do you need both?
4. What is the difference between a path parameter and a query parameter?
5. When do you use a request body instead of parameters in the URL?
6. What does Pydantic do? Why does invalid data produce a `422`?
7. What do `200`, `201`, `204`, `404`, and `422` mean, and when would you return each?
8. How does Swagger generate its documentation? Why can't it go out of date?

---

## Report (student fills after the session)

### What I did

### How it works / why

(Your answers to the Mentor Questions.)

### Commands I used

| Command | Why I used it |
|---|---|
| `py -3.11 -m venv .venv` | Create an isolated environment with the project-standard Python |
| `pip install -r requirements.txt` | Install the pinned dependencies |
| `uvicorn main:app --reload` | Run the API; reload on code changes |
| `requests.get('http://127.0.0.1:8000/...')` | Exercise the API from a real client |
| … | … |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| … | … | … |

### Lessons learned / self-explanation

> Write 5–10 sentences explaining what an API is **now that you understand it**. If you
> can explain the journey to a friend, you understood the stage.

### Evidence

- [ ] Screenshots saved in `screenshots/stage-01/` (e.g., `01-swagger-list.png`, `02-requests-script.png`)
- [ ] ADR written (if a decision was made)
- [ ] Session log entry appended
- [ ] Execution plan updated
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab

> 🚀 **Next:** Stage 02 — Real Project: turn the mini API into the structured IT Assets
> Inventory with a full CRUD.
