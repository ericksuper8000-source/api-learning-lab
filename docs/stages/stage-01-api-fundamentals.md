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

- [x] Explain (with the mentor, no code): what an API is and why a company would expose one
- [x] Draw the journey: Client → HTTP → Uvicorn → FastAPI → response
- [x] Identify every layer in the drawing and what it is responsible for
- [x] Compare: a webpage request vs an API request (JSON vs HTML)
- [x] Write the mental model in the Report (drafted in `Respuesta.txt`, Desktop — pending final transfer)

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

- Session 01 — What is an API? The request journey (no code).
- Built the mental model of the request journey: Client → HTTP → Uvicorn → FastAPI → response.
- Compared a webpage request vs an API request (HTML vs JSON, `Accept` header).
- Understood HTTP status codes and why the first digit matters.
- Drafted the answers to the Mentor Questions (see below) — based on my own words, validated with the mentor.

### How it works / why

(My answers to the Mentor Questions, in my own words.)

1. **What is an API, and what problem does it solve?**
   An API is the **contract between the client and the server** that defines the rules of
   communication between the two. It solves the problem of two programs needing to exchange
   data: it tells the client *what requests are available* and *how to make them*, without
   exposing how the server does the work.

2. **Walk through what happens between the browser sending `GET /items/1` and the response arriving.**
   The client (browser/program) writes an HTTP note with a method (`GET`) and a URL
   (`/items/1`). The note travels to Uvicorn, the "doorman", who receives it **without
   reading it** and passes it to FastAPI. FastAPI reads the method + URL combination, finds
   the matching function in the application, executes it, and produces the response (JSON).
   The response goes back through Uvicorn, who returns it to the client **without reviewing
   it** — like a desk clerk who passes the slip to the librarian and back without reading it.

3. **What does Uvicorn do, and what does FastAPI do? Why do you need both?**
   Uvicorn is the doorman: it listens for raw HTTP and forwards it, and returns the response.
   It decides nothing. FastAPI is the receptionist: it reads the note, validates the
   method + URL, routes to the right function, and builds the response. You need both because
   receiving/forwarding traffic (Uvicorn) and understanding/routing requests (FastAPI) are
   two separate jobs — keeping them separate is what makes the API clean and debuggable.

4. **What is the difference between a path parameter and a query parameter?**
   *(Covered in a later session — pending answer.)*

5. **When do you use a request body instead of parameters in the URL?**
   *(Covered in a later session — pending answer.)*

6. **What does Pydantic do? Why does invalid data produce a `422`?**
   *(Covered in a later session — pending answer.)*

7. **What do `200`, `201`, `204`, `404`, and `422` mean, and when would you return each?**
   A status code is the contract's signature: it tells the client the outcome **without
   reading the body**. The first digit is the category:
   - **2** = everything went well (e.g., `200` = OK).
   - **4** = the server is fine but the client's request had an error (e.g., `404` = the
     resource does not exist).
   - **5** = the problem is on the server side.
   Sending a wrong code (e.g., `200` when the request could not be fulfilled) breaks the
   contract because both parties agreed on what each code means.
   *(Specific codes `201`, `204`, `422` are covered in detail in later sessions.)*

8. **How does Swagger generate its documentation? Why can't it go out of date?**
   *(Covered in a later session — pending answer.)*

### Commands I used

No commands — this was a no-code concept session.

| Command | Why I used it |
|---|---|
| *(None)* | Concept session: mental model only, first session of Phase 1 |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| I initially placed the API "inside" the journey drawing as if it were a communication layer | I reviewed the library/catalog analogy with the mentor | The API is the **contract/menu**, not a layer: the client and the server both consult it before talking |
| I struggled with "webpage vs API" — I thought there was no difference | We compared who asks (browser vs program) and what comes back (HTML vs JSON) | Same journey, different passenger and different luggage: selected by the `Accept` header |
| I said the client "discovers" the method+URL on the spot | Mentor clarification | The method + URL are already written in the menu; the client reads that line and copies it into the note |

### Lessons learned / self-explanation

An API is a contract. It does not transmit anything: it defines what operations exist and
their rules — like a library catalog. The client reads the catalog, picks a method + URL,
writes an HTTP note in a universal format, and hands it to the doorman (Uvicorn), who passes
it without reading it. The receptionist (FastAPI) reads the method + URL, finds the matching
function, executes it, and sends the JSON response back through Uvicorn to the client. What
confused me at first is that the API never appears "inside" the journey — it is the shared
knowledge both sides consult before they talk. Status codes are the contract's signature: the
first digit tells you if it went well (2), if the client made a mistake (4), or if the server
failed (5). A webpage request and an API request use the same road and the same building; the
difference is who asks (browser vs program) and what they get (HTML vs JSON), chosen via the
`Accept` header. Now I can explain the whole journey to a friend.

### Evidence

- [x] Answers drafted by the student (`Respuesta.txt` → transferred here by the mentor)
- [x] Session log entry appended (2026-08-11)
- [x] Execution plan updated (Session 01 marked complete)
- [ ] Screenshots saved in `screenshots/stage-01/` (e.g., `01-swagger-list.png`, `02-requests-script.png`) — pending (no code yet)
- [ ] ADR written (if a decision was made) — none this session
- [ ] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab — pending end-of-day push

> 🚀 **Next:** Stage 02 — Real Project: turn the mini API into the structured IT Assets
> Inventory with a full CRUD.
