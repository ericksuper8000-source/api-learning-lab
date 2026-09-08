# Stage 01 — API Fundamentals

> **Phase:** Phase 1 — API Fundamentals
> **Estimated duration:** ~2.5 weeks (12 sessions)
> **Status:** 🔄 In progress
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

- [x] Explain what a method (GET, POST, PUT, DELETE) means and when each is used
- [x] Explain the anatomy of a request: method, URL, headers, body
- [x] Explain the anatomy of a response: status code, headers, body
- [x] Read the meaning of 200, 201, 204, 404, 422, 500 (and why they matter)
- [x] Practice: identify the method/URL/status in a few made-up examples

### Session 03 — Environment + first app

- [x] Create the venv: `py -3.11 -m venv .venv` inside `C:\API-Learning-Lab` (why: isolated deps)
- [x] Activate it and verify `python --version` is 3.11
- [x] Create `requirements.txt` with `fastapi` and `uvicorn` (why: reproducible deps)
- [x] Install: `pip install -r requirements.txt` (why: one command installs everything)
- [x] Write the first `main.py`: `app = FastAPI()` + `@app.get("/")` returning a message
- [x] Run it: `uvicorn main:app --reload` (why: `--reload` restarts on changes)
- [x] Open `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/docs` (Swagger appears — already!)
- [x] Verify the journey: your browser (client) → HTTP → Uvicorn → FastAPI → response

### Session 04 — GET endpoints + path parameters

- [x] Create `@app.get("/hello")` and test it in the browser and in Swagger
- [x] Explain why `/hello` is a "path"
- [x] Add a path parameter: `@app.get("/items/{item_id}")`
- [x] Explain that `{item_id}` is a variable *inside* the URL
- [x] Test with different values in Swagger (why: Swagger shows the parameter)
- [x] Explain the difference between the URL path and the data the client sends

### Session 05 — Query parameters

- [x] Add a query parameter: `@app.get("/items/")` with `q: str | None = None`
- [x] Test with `?q=laptop` and without it (why: query = optional filters)
- [x] Combine path + query: `/items/{item_id}?verbose=true` and `/items/{item_id}?formato=largo`
- [x] Explain when a value belongs in the path vs the query string
- [x] Document the examples in the Report

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
- Session 02 — HTTP: methods, status codes, request/response anatomy.
- Learned the anatomy of the request note: method + path + version (`GET /assets/7 HTTP/1.1`) + headers (`Host`, `Accept`).
- Learned the anatomy of the response note: status line + headers (`Content-Type`) + body (JSON, can be empty).
- Learned the status codes 200, 201, 204, 404, 422, 500 and their categories (2/4/5).
- Practiced reading a real request/response pair (`GET /assets/7` → `404`).
- Confirmed the 4 methods: GET (read), POST (create), PUT (update), DELETE (delete).
- Session 03 — Environment + first app (FIRST CODE SESSION).
- Created the venv with `py -3.11 -m venv .venv` and activated it (`source .venv/Scripts/activate`).
- Created `requirements.txt` (fastapi, uvicorn) and installed with `pip install -r requirements.txt`.
- Wrote the first `main.py` with `@app.get("/")` returning a JSON message.
- Ran `uvicorn main:app --port 8000 --reload` and saw `200 OK` in the browser + Swagger at `/docs`.
   - Fixed a real error: uvicorn was running from the wrong project's terminal (see Problems).
- Session 04 — GET endpoints + path parameters.
- Created `@app.get("/hello")` and `@app.get("/items/{item_id}")` with `item_id: int` in `main.py`.
- Tested `/`, `/hello` and `/items/15` in the browser and in Swagger (`/docs`).
- Saw FastAPI convert the path segment to `int` and validate it: `/items/abc` returned `422`, and a valid but missing id returned `404`.
- Understood that the path identifies the resource (like apartment 15 in a building) and that data outside the path is extra information, not the address.
- Session 05 — Query parameters.
- Added `@app.get("/items/")` with `q: str | None = None` as a query parameter for filtering.
- Tested `?q=laptop` and without it — query = optional filters.
- Combined path + query in `@app.get("/items/{item_id}")` with `verbose: bool = False` and `formato: str = "normal"`.
- Tested `/items/15`, `/items/15?verbose=true`, `/items/15?formato=corto`, `/items/15?formato=largo`.
- Understood the difference: path = resource address (obligatory), query = extra instructions (optional, has default value).
- Session 06 — POST + JSON body + Pydantic models.
- Explained why complex data can't go in the URL (size limits, structure, convention).
- Created `class Item(BaseModel)` with typed fields (name, brand, serial, status).
- Created `POST /items/` endpoint that receives the Item model and returns 201.
- Tested in Swagger: POST creates item, GET /items/lista shows the list.
- Understood Pydantic: validates data automatically before your code runs, returns 422 if invalid.
- Fixed route ordering: `/items/lista` must come before `/items/{item_id}`.

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
   A path parameter (`/items/{item_id}`) identifies **which resource** you want — it's the
   address. Without it, you can't reach the resource. A query parameter (`?verbose=true`)
   tells the server **how** you want the response — it's extra information that doesn't change
   the resource itself. In code: path parameters go inside `{}` in the route; query parameters
   are function parameters with a default value, and FastAPI detects them automatically.

5. **When do you use a request body instead of parameters in the URL?**
   When the client needs to send complex or structured data. URLs have size limits (~2000 chars), can't represent nested objects, and by REST convention, query parameters are for filtering, not for sending resource data. The body is a JSON payload with no practical size limit and full structure.

6. **What does Pydantic do? Why does invalid data produce a `422`?**
   Pydantic is the inspector that validates data automatically before your code runs. It checks: are all required fields present? Is each field the correct type (str, int, bool)? Does it meet constraints (min_length, gt, etc.)? If anything is wrong, it returns `422 Unprocessable Entity` — meaning "I understood your request but the data is malformed." Your function never executes with bad data.

7. **What do `200`, `201`, `204`, `404`, and `422` mean, and when would you return each?**
   A status code is the contract's signature: it tells the client the outcome **without
   reading the body**. The first digit is the category:
   - **2** = everything went well (e.g., `200` = OK).
   - **4** = the server is fine but the client's request had an error (e.g., `404` = the
     resource does not exist).
   - **5** = the problem is on the server side.
   Sending a wrong code (e.g., `200` when the request could not be fulfilled) breaks the
   contract because both parties agreed on what each code means.
   *(Specific codes `201`, `204`, `422` were covered in detail in Session 02.)*

8. **How does Swagger generate its documentation? Why can't it go out of date?**
   *(Covered in a later session — pending answer.)*

### Commands I used

| Command | Why I used it |
|---|---|
| `py -3.11 -m venv .venv` | Create the project venv with Python 3.11 (isolated deps) |
| `source .venv/Scripts/activate` | Activate the venv (prompt shows `(.venv)`) |
| `py --version` | Verify Python 3.11.9 (in this Git Bash, `python` is not found — `py` works) |
| `pip install -r requirements.txt` | Install dependencies from the recipe |
| `uvicorn main:app --port 8000 --reload` | Run the server; `--reload` restarts on code changes |
| Swagger UI (`/docs`) | Test POST and GET endpoints visually |

### Problems encountered

| Problem | Investigation | Solution |
|---|---|---|
| I initially placed the API "inside" the journey drawing as if it were a communication layer | I reviewed the library/catalog analogy with the mentor | The API is the **contract/menu**, not a layer: the client and the server both consult it before talking |
| I struggled with "webpage vs API" — I thought there was no difference | We compared who asks (browser vs program) and what comes back (HTML vs JSON) | Same journey, different passenger and different luggage: selected by the `Accept` header |
| I said the client "discovers" the method+URL on the spot | Mentor clarification | The method + URL are already written in the menu; the client reads that line and copies it into the note |
| I thought `HTTP/1.1` was the URL | We broke down the request line | It is the protocol version: the line is method + path + version |
| I called `api.inventario.com` "the route" | Compared Host vs path | `Host` is the building (which server receives the note); the path `/assets/7` is what FastAPI reads |
| I was not sure if 404 meant the route or the resource was missing | Discussion with the mentor | The route exists; the 404 is returned because the asset does not exist — category 4, client error |
| `Error loading ASGI app. Could not import module "main"` | Checked `pwd`, `ls main.py`, `which uvicorn`; ran an import test with the venv python | Uvicorn was run from PyCharm's terminal in the OTHER project (`C:\FastAPI\vtasks\ProyectoFastAPI1`, venv `PythonProject1`). Fixed: run from `C:\API-Learning-Lab` with `.venv` active. Lesson: uvicorn resolves `main:app` relative to the current folder and uses the active venv's Python |
| Al principio leí `/items/abc` como `404` en vez de `422` | Observé el cuerpo JSON real que devolvió FastAPI | `/items/abc` da `422` con `loc:["path","item_id"]` (dato mal formado); el `404` es para un id válido pero inexistente. Lección: validar observando el JSON, no asumiendo el código |
| `items` list not defined when POST endpoint used it | Checked the code — `items = []` was missing | Added `items = []` before the POST endpoint. Lesson: variables must be defined before use |
| GET `/items/lista` returned 422 | Route `/items/{item_id}` was catching "lista" as item_id | Moved `/items/lista` before `/items/{item_id}`. Lesson: route order matters — static routes first |

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

**Session 02:** The HTTP note has two halves. On the way out: method + path + version + headers (`Host` = which building, `Accept` = what format I expect). On the way back: a status line with a code whose first digit is the category, headers like `Content-Type`, and a body. `HTTP/1.1` is the protocol version, not the URL. The path is what FastAPI reads to route; the `Host` only decides which server receives the note. A `404` means the route exists but the resource does not — the client asked for something that is not there, so it is a category 4 error. Each method is a verb with a clear job (GET read, POST create, PUT update, DELETE delete), and the status code I return is part of the contract with the client.

**Session 03:** The first code session made the mental model real. A venv is an isolated "toy box" per project: activating it only changes that terminal, and closing the terminal (or `deactivate`) closes it without affecting other projects. Uvicorn resolves `main:app` relative to the folder where you run it and uses the active venv's Python — that is why running it from the wrong project produced *"Could not import module main"*. FastAPI generates Swagger automatically from the decorators, so documentation never drifts from the code. I now understand why `requirements.txt` exists: one command (`pip install -r requirements.txt`) reproduces the whole environment.

**Session 04:** Los parámetros de ruta (`{item_id}`) son variables dentro de la URL que FastAPI captura y pasa a la función. El type hint `int` hace dos cosas automáticas: convierte el texto de la URL a entero y lo valida; si no es entero (`/items/abc`) devuelve `422` antes de ejecutar la función. El `404` es distinto: la petición es válida pero el recurso no existe. La ruta identifica el recurso —como el número de apartamento 15 en un edificio—; los datos fuera de la ruta son instrucciones extra, no la dirección.

**Session 05:** Los parámetros de query son la forma de enviar filtros e instrucciones extra al servidor sin cambiar la dirección. La sintaxis es siempre la misma: `nombre: tipo = valor_por_defecto` en la función. FastAPI los detecta automáticamente porque tienen valor por defecto y no están en la ruta `{}`. Se pueden combinar varios query parameters en la misma función (`verbose: bool = False, formato: str = "normal"`). La diferencia clave: la ruta identifica el recurso (obligatorio), el query modifica la respuesta (opcional). Ejemplo real: un cliente móvil quiere datos ligeros (`?formato=corto`) y uno de escritorio quiere todo detallado (`?formato=largo`).

**Session 06:** El request body existe para enviar datos estructurados (JSON) de forma segura, sin límite de tamaño y con jerarquía. Pydantic es el inspector que valida automáticamente que los campos obligatorios estén presentes y sean del tipo correcto; si falta algo o está mal, devuelve `422` antes de que la función se ejecute. La sintaxis es: `class Item(BaseModel)` con campos tipados, y el endpoint recibe el modelo como parámetro (`item: Item`). FastAPI se encarga de convertir el JSON a un objeto Pydantic, validarlo, y entregarlo a tu función. El orden de las rutas importa: las rutas estáticas (`/items/lista`) deben definirse ANTES que las rutas con parámetros (`/items/{item_id}`), de lo contrario FastAPI intentará emparejar "lista" como un `item_id`.

**Analogía del Restaurante (Path, Query, Body):**
- **Path** = La dirección del restaurante (`/ViaMontana/RestauranteBonito/Mesa5`). Te dice **a dónde vas**. Sin ella, no llegas.
- **Query** = Instrucciones extras al mesero (`/Mesa5?velocidad=rápido&porcion=grande`). Son **extras opcionales** — si no los pones, te atienden con valores normales.
- **Body** = El pedido que le das al mesero (`{"platillo": "Tacos al pastor", "cantidad": 2, "sin_cebolla": true}`). Es **la información real** de lo que quieres. No va en la URL, se lo das directamente al mesero en un papel.

| ¿Qué? | Ejemplo | ¿Para qué? |
|---|---|---|
| **Path** | `/items/5` | Decir **a qué recurso** voy |
| **Query** | `?formato=corto` | Dar **instrucciones extra** (opcionales) |
| **Body** | `{"name": "Laptop"}` | Enviar **los datos reales** del recurso |

### Evidence

- [x] Answers drafted by the student (`Respuesta.txt` → transferred here by the mentor)
- [x] Session log entry appended (2026-08-13)
- [x] Execution plan updated (Sessions 01 + 02 + 03 marked complete)
- [x] Screenshots saved in `screenshots/stage-01/` (Swagger de `/items/{item_id}` y error `422` de `/items/abc`) — 2026-08-24
- [ ] Session log entry appended (2026-08-26 — Session 06) — pendiente validación Pydantic (corregido 2026-09-08)
- [ ] Execution plan updated (Session 06 marked complete) — revertido 2026-09-08: Pydantic pendiente
- [ ] ADR written (if a decision was made) — none this session
- [x] Memory folder synced to `C:\API-Learning-Lab`, committed and pushed to GitHub + GitLab `develop` (`main` también alineada) — 2026-08-24 ✅

> 🚀 **Next:** Session 06 — POST + JSON body + Pydantic models (dict → model) — Pydantic pendiente.
