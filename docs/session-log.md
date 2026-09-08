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

## 2026-09-08 — Memory update (FASTAPI 1.txt concepts integrated)

**Phase / Stage:** Phase 1 — API Fundamentals · Stage 01 — Query params variations already seen

**Daily recap (start of day):** N/A — memory integration (no recap).

**Deck (pending questions for next sessions):**
- Pydantic: what it does, why 422 — Session 06 pending.

**Worked on:**
- Student provided `C:\Users\XPC\Desktop\FASTAPI 1.txt` (2026-08-31, 1666 bytes) with query-param patterns already seen: `Texto: str = 'Juanita'` (default), `Texto: str | None = None` (optional/null), `Texto: str` (required, error if missing), `Numero: int | None = 15` (int with default), path vs query distinction (`@app.get("/usuarios/{id}")` vs `@app.get("/usuarios")`), and simple conditional `if (Numero > 5)`.
- Integrated file into memory: copied to `E:\Datos\IA\FastApi - Project\_archive\FASTAPI 1 - conceptos vistos (2026-08-31).txt` and to `C:\API-Learning-Lab\docs\FASTAPI 1 - conceptos vistos (2026-08-31).txt` for AI recall.
- Confirms Session 05 query concepts are already validated beyond basic `q: str | None = None` — student can distinguish required vs optional vs default query params.

**Concepts learned / reinforced:**
- Query param = `param: type = default` → optional with default; `param: type | None = None` → optional nullable; `param: type` → required (422 if missing). Path param = inside `{}` in route, always required.

**Commands / tools used:**
- File integration — why: keep single source of truth including student's prior notes

**Errors encountered:**
- None

**Questions still open:**
- None

**Next session (target):**
- Stage 01 — Session 06: POST + JSON body + Pydantic (still pending) — recap will cover path/query variations from FASTAPI 1.txt as known

**Commit / push:** pending — will be `docs: integrate FASTAPI 1.txt concepts`

---

## 2026-09-08 — Doc correction (Pydantic pending — student clarification)

**Phase / Stage:** Phase 1 — API Fundamentals · Stage 01 — Session 06 pending (Pydantic not yet validated)

**Daily recap (start of day):** N/A — documentation sync session (no recap).

**Deck (pending questions for next sessions):**
- Pydantic: what it does, why 422 before function — Session 06 pending.
- PUT vs PATCH — Fase 2.
- 201/204 usage — fases siguientes.

**Worked on:**
- Student clarified on 2026-09-08 that Pydantic has not been seen — only GET, POST, path and query were seen (POST without Pydantic model).
- Corrected docs to reflect reality (Incremental Learning Rule): unchecked Session 06 in `execution-plan.md` and `stage-01-api-fundamentals.md`, updated Current Status to Session 05 complete / Session 06 next, corrected `session-log` and `stage-01` Evidence, updated `execution-plan` General Status (Application: Sessions 03–05).
- Main.py still contains `class Item(BaseModel)` (`C:\API-Learning-Lab\main.py:22`) from previous sync — will be treated as not yet validated until Session 06 is done live (or reverted if student prefers `dict` version).
- Synced `E:\Datos\IA\FastApi - Project\docs\` → `C:\API-Learning-Lab\docs\` and committed `b340487` + `2fde8cd` already pushed; this correction will be committed as `docs: correct S06 to pending (Pydantic)`.

**Concepts learned / reinforced:**
- Documentation must reflect what the student can explain, not what the file contains — updated to honor student's statement.

**Commands / tools used:**
- Manual edits to `execution-plan.md`, `stage-01-api-fundamentals.md`, `session-log.md` — why: keep single source of truth honest

**Errors encountered:**
- Docs marked Session 06 complete while student had not yet validated Pydantic → corrected by unchecking S06 and moving Current Status back to S05.

**Questions still open:**
- None — pending Pydantic validation in next live Session 06.

**Next session (target):**
- Stage 01 — Session 06: POST + JSON body + Pydantic models (dict → model) — live validation

**Commit / push:** pending — will be `docs: correct S06 to pending (Pydantic)` → push to `develop` (GitHub+GitLab)

---

## 2026-08-26 — Session 06 (Phase 1 · Session 06 — POST + JSON body + Pydantic)

**Phase / Stage:** Phase 1 — API Fundamentals · Stage 01 — Session 06 (POST + JSON body + Pydantic)

**Daily recap (start of day):**
- Passed ✅ — Q1 Uvicorn vs FastAPI (portero vs recepcionista, se necesitan ambos). Q2 `/items/abc` devuelve `422` porque `abc` no es entero. Q3 diferencia entre `404` (recurso no existe) y `422` (datos mal formados).

**Deck (pending questions for next sessions):**
- PUT vs PATCH (reemplazo completo vs parcial) — Fase 2, Sesión 06.
- Uso práctico de 201/204 en endpoints reales — fases siguientes.

**Worked on:**
- Explained the request body: why complex data can't go in the URL (size limits, structure, convention).
- Introduced Pydantic: automatic data validation before the function runs.
- Created `class Item(BaseModel)` with fields: name, brand, serial, status (optional).
- Created `POST /items/` that receives the Item model and returns 201.
- Explained the full request journey: Client → HTTP → Uvicorn → FastAPI → Pydantic → Code → DB → back.
- Created restaurant analogy for Path/Query/Body and saved it in stage-01 report.
- Fixed route ordering issue: `/items/lista` had to be defined before `/items/{item_id}`.

**Concepts learned / reinforced:**
- Request body = JSON sent separate from the URL, for complex/structured data.
- Pydantic = the inspector that validates data before your code runs.
- Path identifies the resource, Query adds instructions, Body carries the real data.
- Route order matters in FastAPI: static routes must come before parameterized routes.
- 422 = "I understood your request but the data is wrong" (Pydantic validation).

**Commands / tools used:**
- `uvicorn main:app --reload` — server with auto-reload.
- Swagger UI to test POST and GET endpoints.

**Errors encountered:**
- `items` list was not defined → fixed by adding `items = []`.
- GET `/items/lista` returned 422 → route `/items/{item_id}` was catching "lista" as item_id → fixed by reordering routes.

**Questions still open:**
- None (deck de sesiones futuras permanece).

**Next session (target):**
- Stage 01 — Session 07: Path + query + body together; validation and 422.

**Commit / push:** `2fde8cd` docs(stage-01): sync S05-S06, fixes + pin deps — pushed 2026-09-08 to GitHub ✅ GitLab ✅ (`develop`) — (sync realizado 2026-09-08 para corregir duplicado S07, triplicación lección y deuda de `main.py`/`requirements.txt`)

---

## 2026-08-25 — Session 05 (Phase 1 · Session 05 — Query parameters)

**Phase / Stage:** Phase 1 — API Fundamentals · Stage 01 — Session 05 (Query parameters)

**Daily recap (start of day):**
- Passed ✅ — Q1 diferencia entre path parameter y query parameter (recordó parcialmente, reforzado con la analogía del edificio/apartamento). Q2 `/items/abc` devuelve `422` porque `abc` no es entero — "entendí tu petición pero los datos están mal". Q3 FastAPI es quien decide a qué función dirigirse (el recepcionista que busca la combinación método + URL).

**Deck (pending questions for next sessions):**
- POST + cuerpo (JSON body) — Sesión 06.
- PUT vs PATCH (reemplazo completo vs parcial) — Fase 2, Sesión 06.
- Uso práctico de 201/204 en endpoints reales — fases siguientes.

**Worked on:**
- Added `@app.get("/items/")` with `q: str | None = None` — query parameter for filtering.
- Tested `?q=laptop` and without it — confirmed query = optional filters.
- Combined path + query in `@app.get("/items/{item_id}")` with `verbose: bool = False` and `formato: str = "normal"`.
- Tested `/items/15`, `/items/15?verbose=true`, `/items/15?formato=corto`, `/items/15?formato=largo`.
- Understood the syntax: query parameters are function parameters with a default value; FastAPI detects them automatically.

**Concepts learned / reinforced:**
- Query parameters are extra instructions, not the address. Path = resource, query = how you want it.
- Syntax: `nombre: tipo = valor_por_defecto` in the function. No decorator change needed.
- Multiple query parameters can coexist: `verbose: bool = False, formato: str = "normal"`.
- Real use case: mobile client wants light data (`?formato=corto`), desktop wants full detail (`?formato=largo`).

**Commands / tools used:**
- `uvicorn main:app --reload` — server with auto-reload.
- Browser/Swagger to test `/items/15`, `/items/15?verbose=true`, `/items/15?formato=corto`, `/items/15?formato=largo`.

**Errors encountered:**
- Created a separate `/formatos/` endpoint with wrong logic (compared int with string) → fixed by the mentor. Lesson: query parameters go in the existing function, not a new endpoint; the type must match the comparison.

**Questions still open:**
- None (deck de sesiones futuras permanece).

**Next session (target):**
- Stage 01 — Session 06: POST + JSON body + Pydantic models.

**Commit / push:** pendiente del estudiante.

---

## 2026-08-24 — Session 04 (Phase 1 · Session 04 — GET endpoints + path parameters)

**Phase / Stage:** Phase 1 — API Fundamentals · Stage 01 — Session 04 (GET endpoints + path parameters)

**Daily recap (start of day):**
- Passed ✅ — Q1 ¿qué es una API? (contrato/menú que definen cliente y servidor; resuelve el lenguaje común sobre HTTP). Q2 anatomía de la petición HTTP (línea = método + ruta + `HTTP/1.1`; cabeceras `Host` y `Accept`). Q3 `venv` (caja aislada de Python por proyecto; requiere carpeta correcta + venv activo; distinción `.venv` ≠ `.env`).

**Deck (pending questions for next sessions):**
- POST + cuerpo (JSON body) — Sesión 06.
- PUT vs PATCH (reemplazo completo vs parcial) — Fase 2, Sesión 06.
- Uso práctico de 201/204 en endpoints reales — fases siguientes.

**Worked on:**
- `@app.get("/hello")` y `@app.get("/items/{item_id}")` con `item_id: int` en `C:\API-Learning-Lab\main.py`.
- Verificado en navegador y Swagger (`/`, `/hello`, `/items/15`).
- Validación automática: FastAPI convierte el segmento de texto a `int` y valida; `/items/abc` → `422` (cuerpo `loc:["path","item_id"]`); `/items/999` (válido, inexistente) → `404`.
- Diferencia ruta vs datos aparte: la ruta identifica el recurso (ej. `/items/15` = "apartamento 15 en el edificio items"); los datos aparte son instrucciones extra (filtros), no la dirección.

**Concepts learned / reinforced:**
- Un parámetro de ruta `{item_id}` es una variable dentro de la URL que FastAPI captura y pasa a la función.
- El type hint `int` no solo etiqueta: FastAPI **convierte** (texto → entero) y **valida** (si no es entero → `422` antes de ejecutar la función).
- `422` = datos mal formados (cliente); `404` = datos válidos pero recurso no encontrado. Ambos son error de cliente (categoría 4), distintos.
- La ruta nombra el recurso; los datos fuera de la ruta son información adicional (se verá en query/body, Sesiones 05–06).

**Commands / tools used:**
- `uvicorn main:app --reload` (corriendo desde `C:\API-Learning-Lab` con `.venv` activo) — servidor con recarga.
- Navegador / Swagger para probar `GET /`, `/hello`, `/items/15`, `/items/abc`.

**Errors encountered:**
- Estudiante leyó `/items/abc` como `404` → al observar el cuerpo real, confirmó `422`. Lección: validar observando el JSON, no asumir el código.

**Questions still open:**
- None (deck de sesiones futuras permanece).

**Next session (target):**
- Stage 01 — Session 05: query parameters (`?q=...`), combinar path + query.

**Commit / push:** ✅ subido 2026-08-24 a GitHub + GitLab (`develop`; `main` alineada vía `git push origin main`).

---

## 2026-08-13 — Session 03 (Phase 1 · Sessions 02 + 03 — HTTP + Environment & first app)

**Phase / Stage:** Phase 1 — API Fundamentals · Stage 01 — Sessions 02 (HTTP) + 03 (Environment + first app)

**Daily recap (start of day):**
- Passed ✅ — Q1 Uvicorn vs FastAPI (portero vs recepcionista; el cliente siempre inicia; se necesitan mutuamente). Q2 Host/Accept + aclaración URL vs Host (edificio vs oficina).

**Deck (pending questions for next sessions):**
- POST + cuerpo (JSON body) — se verá en la Sesión 06.
- PUT vs PATCH (reemplazo completo vs parcial) — Fase 2, Sesión 06.
- Uso práctico de 201/204 en endpoints reales — fases siguientes.

**Worked on:**
- Sesión 02 — HTTP: anatomía request (`GET /assets/7 HTTP/1.1`, cabeceras `Host`/`Accept`), anatomía response (`200 OK`, `Content-Type`, cuerpo), códigos 200/201/204/404/422/500, métodos GET/POST/PUT/DELETE.
- Sesión 03 — PRIMERA SESIÓN CON CÓDIGO: creó el venv (`py -3.11 -m venv .venv`), `requirements.txt` (fastapi, uvicorn), `pip install -r requirements.txt`, escribió `main.py` con `@app.get("/")`, corrió `uvicorn main:app --port 8000 --reload`.
- Verificó en el navegador: `http://127.0.0.1:8000/` → `200 OK` con `{"Mensaje": "Hola API"}` y `/docs` → Swagger mostrando `GET / Root`.

**Concepts learned / reinforced:**
- Un venv es una "caja de juguetes" aislada por proyecto; activarlo solo afecta a esa terminal y no toca otros proyectos; se cierra con `deactivate` o cerrando la terminal.
- Uvicorn resuelve `main:app` **relativo a la carpeta actual** y usa el Python del entorno activo — si corres desde otro proyecto, no encuentra `main.py`.
- FastAPI genera Swagger automáticamente desde el código (el decorador `@app.get("/")`); código y docs nunca se desfasan.
- `--reload` reinicia el servidor solo al detectar cambios.
- `requirements.txt` es la receta: un solo `pip install -r` reproduce el entorno completo.

**Commands / tools used:**
- `py -3.11 -m venv .venv` — crear el entorno con Python 3.11
- `source .venv/Scripts/activate` — activar el venv en Git Bash
- `py --version` — verificar versión (3.11.9; en esta máquina `python` no funciona en Git Bash, se usa `py`)
- `pip install -r requirements.txt` — instalar dependencias desde la receta
- `uvicorn main:app --port 8000 --reload` — correr el servidor

**Errors encountered:**
- `Error loading ASGI app. Could not import module "main"` → investigado con `pwd`, `ls main.py`, `which` y prueba de import con el Python del venv → el uvicorn se ejecutaba desde la terminal de PyCharm del OTRO proyecto (`C:\FastAPI\vtasks\ProyectoFastAPI1`) con su venv `PythonProject1` → resuelto corriendo desde `C:\API-Learning-Lab` con `.venv` activo.
- Confusión URL vs Host (creyó que "la ruta" era `api.inventario.com`) → resuelta con la analogía edificio/oficina.
- Dijo "HTTP/1.1 es la url" → corregido: es la versión del protocolo.
- Nota de entorno: PyCharm se usa para FastAPI (cómo el estudiante aprendió); VS Code como editor general.

**Questions still open:**
- None.

**Next session (target):**
- Stage 01 — Session 04: GET endpoints + path parameters.

**Commit / push:** ✅ pushed to GitHub + GitLab (2026-08-13) — `develop`.

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

**Commit / push:** ✅ pushed to GitHub + GitLab (2026-08-10) — `main`/`develop`.

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
- Phase 0 — repo bootstrap: create `C:\API-Learning-Lab`, `git init` (`main` + `develop`),
  create GitHub + GitLab `api-learning-lab` repos, configure remotes, first push to both.

**Commit / push:** N/A — memory folder; will be synced to `C:\API-Learning-Lab` and pushed
in the first commit of the Phase 0 bootstrap.
