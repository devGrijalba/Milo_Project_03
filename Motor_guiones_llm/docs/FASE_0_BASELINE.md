# FASE_0_BASELINE

Congelado antes de tocar `ds_provider.py`. Sirve para distinguir fallos preexistentes
de los que introduced DeepSeek.

```text
FASE_0_BASELINE

VERSION:
1.4.0-llm

CONFIG:
provider         = deepseek_cdp
max_parallel_tabs = 5
canon            = knowledge/visual_language.json          (local)
worlds           = knowledge/worlds.json                     (local)
mining           = knowledge/mining.md                      (local)
characters       = knowledge/characters/milo2/canon.json    (local, nuevo)
anchors          = knowledge/anchors/registry.json         (local, nuevo)

CANON:
canon       = OK
worlds      = OK
mining      = OK
characters  = OK
anchors     = OK
  -> verificado en runtime: context() carga las 5 claves sin error

TEST_ENGINE:
PASS   13/13   (0.570s)

TEST_MULTIAGENT:
FAIL   33/36   (errors=3, skipped=1, 1.673s)

TEST_OPTIMIZATION:
PASS   11/11   (2.047s)

FULL_SUITE:
60 tests
57 passed
3 errors
1 skipped
(4.226s)
```

**Comando:** `python -m unittest discover -s tests -v`
(pytest no está instalado; `requirements.txt` declara "solo biblioteca estándar" y los
tests son `unittest`. Por eso NO se usó pytest.)

## Clasificación de los 3 errores

### C — OBSOLETO: `test_anchor_hashes_still_match_registry`

```
tests/test_multiagent.py:412
registry = read(PROJECT / '01_CANON/anchors/registry.json')
KeyError/IOError -> 01_CANON no existe en este layout
```

El test lee el canon externo `01_CANON/anchors/registry.json` y espera
`items[] con file+sha256`. Mi `registry.json` local tiene `{_nota, anclas}`.

**Clase: C (obsoleto).** Prueba que el canon externo siga byte-identico tras un update.
Ese canon ya no existe en el motor independiente. Se reescribe en Fase 1 para que
verifique el canon LOCAL, o se elimina si el registro de anclas sigue vacio.

### B — DEPENDENCIA HERMES: `test_critic_payload_has_hash_and_context_not_history_reuse`

```
src/orchestrator.py:51
report = cached_call(c['critic_command'], ...)
KeyError: 'critic_command'
```

`critic_command` se eliminó de la config en Fase 0 (era un argv al adapter externo
`hermes_adapter.py`). El test construye su propia config pero le falta esa clave.

**Clase: B (esperable).** Se migra en Fase 1: el test debe apuntar al provider DeepSeek
y_a_ asserts sobre el payload (hash + context, sin reuso de history), que es la garantia
que el test existe para proteger.

### B/A — DEPENDENCIA HERMES: `test_repair_payload_protects_approved_criteria`

```
tests/test_multiagent.py:329
self.assertIn('hook', captured['failed_criteria'][0]['criterion'])
KeyError: 'failed_criteria'
```

El payload de reparacion llego sin `failed_criteria`. Causa: sin `critic_command`
configurado, la ruta de reparacion no se ejecuta y el payload capturado queda vacio.

**Clase: B (esperable), raiz en el mismo sitio que el anterior.** Se migra en Fase 1.

## SKIPPED (no es fallo)

```
test_ep0001_request_still_readable ... skipped 'no prior episode in this checkout'
```

Compatibilidad con un episodio anterior. Este checkout no lo tiene. **Correcto**: no hay
episodio EP0001 generado todavia.

## Conclusion de Fase 0

- **Ningun fallo es real del motor.** Los 3 son dependencia del canon externo (1) o del
  adapter Hermes (2). Ningun test de logica de nucleo fallo: los gates de seed, hash,
  scorecard 89, dos pases, mundo desconocido, provider mal configurado y stress — todos
  pasan.
- **Fase 1 puede arrancar.** La base esta limpia y el fallo es esperado.

## Pendiente consciously diferido

`src/runtime.py:19` lista `['WORKER.md','hermes_adapter.py']` como entradas del hash de
sesion/cache. **No se borra a ciegas.** En Fase 1 se revisa que entra exactamente al hash
y se sustituye por el provider DeepSeek:

```text
src/ds_provider.py
tools/ds_session.py
tools/ds_inject.py
tools/ds_extract.py
```

`START_HERE.md` sigue documentando 1.3.0 y el flujo `prepare -> Hermes manual -> check`.
**Se deja asi** hasta terminar Fase 1: reescribirlo ahora seria documentar una
arquitectura que aun no existe.