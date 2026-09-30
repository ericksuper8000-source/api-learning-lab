# REQUEST JOURNEY STORY — El Edificio API

> **Type:** Interactive living story (memory aid, not spec)
> **Version:** v1.3 (2026-09-30: S07 triple validated)
> **Scope:** Only validated concepts up to S07 (2026-09-30). No future concepts.
> **Rule:** This story is told at the start of EVERY work session, BEFORE the summary.
> Every time a new concept is validated, this file grows (v1.2, v1.3...). Never shrink it,
> never introduce unvalidated tech. Rest of the session workflow stays unchanged.

---

## How to use

1. Mentor tells the full story in simple language (60-120 seconds detailed version).
2. Then Part 1 summary (where we stand), then question round.
3. When S07 (path + query + body together, `min_length`, `gt`) is validated, append it
   as a new chapter keeping the same characters. Same for future stages.

**Mantras (never change, only grow):**
- *Portero no lee, recepcionista sí. Inspector revisa antes.*
- *Path = dirección, query = filtro, body = pedido.*
- *Sin `=` es mandatorio. Omitir → default, mandar → valida.*
- *Sin `=` adelante, con `=` atrás (obligatorios primero).*

---

## EL EDIFICIO API - v1.1 detallada (para niño)

Había una vez un **edificio** donde vive la información. Tú eres el **cliente**, un niño
que siempre inicia el juego. Nadie te habla primero, tú mandas una **notita HTTP**
al edificio.

### 0. El menú (la API)

Antes de escribir, tú y el edificio miran el mismo menú pegado en la pared. El menú dice
qué puedes pedir y cómo pedirlo: *"si quieres un juguete, escribe GET + /items/15"*.
La API no es un pasillo ni una puerta, es solo el menú, el contrato. Si pides algo fuera
del menú, no te entienden.

### 1. Tú escribes la notita HTTP

Es un papelito con 3 pisos:

- Arriba: **MÉTODO + DIRECCIÓN + VERSIÓN**. Ejemplo: `GET /assets/7 HTTP/1.1`.
  El método es el verbo: `GET` = préstame para leer, `POST` = guarda esto nuevo que te
  mando. (Existen `PUT` y `DELETE` como palabras, pero solo hemos jugado con `GET` y `POST`).
- En medio: **cabeceras**. `Host` = a qué edificio va (ej: `127.0.0.1:8000`, como decir
  "edificio azul"). `Accept` = qué maleta espero de vuelta (`application/json` = cajita
  de juguetes ordenada, no una carta HTML para humanos).
- Abajo opcional: **`?filtros` y la caja**. `?formato=corto` es un post-it pegado.
  La **caja** es el pedido grande que no cabe en el sobre.

¿Qué se logra? Que el mensaje viaje completo y cualquiera lo pueda leer.

### 2. El portero Uvi (Uvicorn)

En la puerta está Uvi, un portero con audífonos. Escucha en el puerto `8000`. Toma tu
sobre **sin abrirlo, sin leerlo** y lo lleva corriendo a recepción. Cuando hay respuesta,
la toma **sin mirarla** y te la entrega.

Uvi solo trabaja si estás en la carpeta correcta (`C:\API-Learning-Lab`, donde vive
`main.py`) y con tu caja de juguetes puesta (`.venv` activo). Si corres desde otro barrio,
grita *"Could not import module main"*. Con `--reload` es como si parpadeara: si cambias
el código, él solito se despierta de nuevo.

¿Qué hace? Recibir y devolver tráfico. ¿Qué logra? Que FastAPI no tenga que gritar
a la calle.

### 3. La recepcionista Fasti (FastAPI)

Fasti sí lee. Mira MÉTODO + RUTA y busca en su libretita qué función atiende eso.
Ejemplo: ve `GET /hello` y dice *"¡ah, es la función say_hello!"*. Si nadie atiende esa
combinación, no hay fiesta. Después de que la cocina termina, Fasti mete el resultado
en una cajita JSON y se la da a Uvi.

¿Qué hace? Dirigir y traducir. ¿Qué logra? Que cada petición llegue a la función correcta.

### 4. La dirección (path)

Si escribes `/items/15`, el `15` es el número de apartamento dentro del edificio items.
**Sin número no llegas**, es obligatorio, es la dirección.

Fasti además es maga: si la función dice `item_id: int`, ella convierte el texto `"15"`
en número `15`. Si le mandas `/items/abc`, no puede convertirlo y te devuelve `422` con
una notita `loc: ["path","item_id"]` = *"te equivocaste en la dirección"*. Si mandas un
número válido pero vacío como `/items/999`, te devuelve `404` = *"la dirección existe,
el apartamento está vacío"*.

¿Qué se logra? Saber exactamente a qué recurso vas.

### 5. El post-it extra (query)

Son instrucciones al mesero que no cambian a dónde vas, solo **cómo lo quieres**.
`?verbose=true`, `?formato=corto`, `?q=laptop`.

En código siempre se ven igual: `nombre: tipo = valor_por_defecto`. Ese `=` es la señal
secreta que le dice a Fasti *"esto es un post-it, no una dirección"*.

Ya jugamos 4 sabores (de `FASTAPI 1.txt`):

- `Texto='Juanita'` = si no dices nada, te doy Juanita.
- `Texto=None` = si no dices nada, te doy cajita vacía `null`.
- `Texto` sin `=` = estás obligado a decirlo o `422`.
- `Numero=15` = número con default 15.

Ejemplo real: el hermanito del celular quiere poquito (`?formato=corto`) y el de la
computadora quiere todo (`?formato=largo`), van al mismo apartamento pero piden distinto.

¿Qué se logra? Filtrar sin crear direcciones nuevas.

### 6. La caja con el pedido (body JSON)

Cuando quieres guardar algo grande (un laptop con nombre, marca, serial), no cabe en el
sobre ni en el post-it, y sería peligroso gritarlo en la calle. Lo pones en una **caja
aparte** de cartón JSON.

Si usas `item: dict`, es una caja sin revisor: entra basura (`additionalProp1`) y nadie
dice nada, solo para trucos rápidos. Si usas `class Item(BaseModel)`, llamas al
**inspector Pydan (Pydantic)**.

¿Qué hace Pydan? Revisa la caja **antes** de que la cocina encienda el fuego. Mira:
¿están todos los campos obligatorios? ¿cada uno es del tipo correcto? Si algo falla,
grita `422` = *"te entendí, pero tu caja está mal armada"* y la cocina **ni se prende**.
Te devuelve un papel que dice exactamente dónde: `loc: ["body","location"]` +
`msg: "Field required"` + `input` = lo que mandaste. Si la caja llegó rota por una coma
faltante, dice `json_invalid`, distinto a `missing` que es campo faltante.

¿Qué se logra? Que nunca se cocine con ingredientes malos.

### 7. Las dos perillitas mágicas

Cada línea del inspector tiene dos perillas separadas, como la ducha fría/caliente:

- Perilla `| None` (tipo): *"¿acepto cajita vacía `null` si me la mandas?"*.
  `str` dice NO, `str | None` dice SÍ.
- Perilla `= ...` (default): *"¿qué pongo si omites el campo, sin revisar?"*.
  Sin `=` eres obligatorio. Con `= 'active'` pongo active. Con `= None` pongo null.

Estado validado S06 refuerzo: `name,brand,serial,location` sin `=` = obligatorios.
`assigned_to: str | None = None` = si omites da `null`, si mandas `"Erick"` da Erick,
si mandas `null` da null (el tipo lo permite). Cambio `status='active'` → `status=null`:
el cliente viejito que nunca manda status antes recibía `active`, ahora recibe `null`
sin haber cambiado nada. **Cambiar un default le cambia el regalo a todos los que no
piden nada.**

¿Qué se logra? Predecir el `201` o `422` solo mirando qué campos tienen `=`.

### 8. La cocina, la caja de juguetes y el sello

Si Pydan dice OK, la **función-cocina** corre: hace `caja.append(item.model_dump())`.
`model_dump()` es sacar una **fotocopia** del juguete validado a diccionario para
guardarla en la `caja: list[dict]`, nuestra caja de autos en la memoria RAM. Es efímera:
si apagas el edificio (reinicias uvicorn), se vacía.

**Regla de la fila (Python, aprendida 2026-09-30 en S07):** en la puerta de la cocina
(`def`) los niños sin lonchera van primero, los con lonchera al final. O sea:
obligatorios (sin `=`) adelante, opcionales (con `=`) atrás. Si pones
`def revisar_item(item_id: int, verbose: bool = False, item: Item):` Python grita
`SyntaxError: non-default argument follows default argument` = *"pusiste un obligatorio
después de un opcional"*. Lo bueno es `def revisar_item(item_id: int, item: Item,
verbose: bool = False):` → `item_id` e `item` (sin lonchera) primero,
`verbose = False` (con lonchera) al final.

La cocinera pone un **sello-código**: `200` = *"te respondo"*, `201` = *"te lo creé
y guardé"*. El método sugiere, pero lo que pasó decide. Por eso pusimos
`status_code=201` en el POST.

Truco de orden: la puerta `/items/lista` (estática) debe estar **antes** que
`/items/{item_id}` en el código, o Fasti cree que `"lista"` es un número y da
`422 int_parsing`. Para verificar, hacemos `GET /items/lista` y vemos la caja.

¿Qué se logra? Crear y comprobar que se guardó.

### 9. El espejo mágico (Swagger en /docs)

Fasti tiene un espejo que dibuja solo el menú desde los `@app.get/post` y los tipos.
Nunca se desfasa porque nace del código. Ahí probamos bueno (`201`) y malo (`422`)
sin escribir programas.

Más la base: tu **caja de juguetes `.venv`** aislada por proyecto
(`source .venv/Scripts/activate`, solo afecta esa terminal), la **receta
`requirements.txt`** (`fastapi, uvicorn`, instalas con `pip install -r`), y usas `py`
porque en este Git Bash `python` no existe. Todo cuesta $0 en tu compu.

### Final del cuento

Cliente manda nota → Uvi la lleva sin leer → Fasti busca método+ruta → si hay dirección
la valida, si hay post-it lo lee, si hay caja llama a Pydan antes → cocina guarda
fotocopia en caja RAM → Fasti pone JSON + sello (200/201/404/422) → Uvi devuelve sin
leer. Y tú lo ves en el espejo Swagger.

### 10. El triple (S07, validado 2026-09-30)

Un día pedimos las 3 cosas en una sola nota: `POST /items/15/revisar?verbose=true` con
caja `Item`. Fasti junta: `15` (dirección) + `?verbose` (post-it) + caja (pedido).
La función es `def revisar_item(item: Item, item_id: int = Path(gt=0),
verbose: bool = False):` — la caja obligatoria primero por la regla de la fila,
`Path` en la puerta y `Field` en la caja.

Probamos bueno (`200` con `id:15, verbose:true`, `status:null`) y 3 malos sin prender
la cocina: sin `location` → `422 missing ["body","location"]`, `name:"AB"` →
`422 string_too_short ctx min_length:3`, `item_id:0` → `422 greater_than loc
["path","item_id"] ctx gt:0`. `200` = respondo/reviso, `201` = creé. Pydan siempre
antes, `caja` intacta si falla.

---

## Changelog

- **v1.1 (2026-09-30):** First approved detailed version. Covers S01-S06 + S06 refuerzo.
  Characters: Uvi, Fasti, Pydan. Mantras fixed.
- **v1.2 (2026-09-30):** Added Python fila rule (sin `=` adelante, con `=` atrás) learned
  fixing `revisar_item` SyntaxError. New mantra added.
- **v1.3 (2026-09-30):** S07 validated — triple `POST /items/{item_id}/revisar`
  (path + query + body), `422` body vs path, `Field(min_length=3)` + `Path(gt=0)`,
  `200` vs `201`, validation before function. New chapter 10.
- **Next (v1.4):** Add S08 when validated — status codes and response models.
