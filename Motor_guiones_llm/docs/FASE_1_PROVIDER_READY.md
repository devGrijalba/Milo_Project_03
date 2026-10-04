# FASE_1_PROVIDER_READY

Provider DeepSeek implementado y testeado. DeepSeek **real todavía no**: toda la suite corre
con el navegador stubbeado.

```text
FASE_1_PROVIDER_READY

provider unit tests       = PASS   33/33
engine core               = PASS   14/14   (era 13/13: +1 test del dispatch)
multiagent                = 33/36  (3 errores = los MISMOS de Fase 0)
optimization              = PASS   11/11
no hermes config refs     = PASS
runtime cache refs        = DeepSeek (ds_provider/ds_session/ds_extract)

full suite                = 94 tests -> 90 passed, 3 errors, 1 skipped
DeepSeek real             = TODAVIA NO
```

Comparado con la baseline de Fase 0 (60 tests / 57 pass / 3 err):
**+34 tests, 0 regresiones.** Los 3 errores son los mismos de antes.

## Archivos nuevos

```text
src/ds_provider.py     UNA llamada LLM: build prompt, inyectar, extraer, validar
tools/ds_session.py    UNA pestana: abrir, reutilizar, enviar, cerrar
tools/ds_extract.py    esperar la respuesta y devolver el texto
tools/ds_pool.py       (Fase 1.2) N pestanas, concurrencia acotada
tests/test_ds_provider.py   33 tests, sin navegador
```

## Capas (no colapsar)

```text
src/ds_provider.py   una llamada      <- no sabe de pestanas ni de pool
tools/ds_session.py  una pestana      <- no sabe de pool ni de JSON
tools/ds_extract.py  la espera        <- no sabe de JSON
src/ds_provider.py   parseo de JSON   <- no sabe de pestanas
multiagent.py        decide concurrencia
```

`ds_provider.py` NO tiene thread pool. Si algun dia hace falta, va en `ds_pool.py`.

## El seam

`src/provider.py` ahora despacha por config:

```python
provider = "deepseek_cdp"      -> src.ds_provider.call
provider = ausente             -> call_subprocess  (route original intacto)
```

`orchestrator` y `multiagent` siguen importando `call` de `provider` y **no saben que
provider esta activo**. Cambiar de backend es un valor de config, no un cambio en 14 modulos.

`call_subprocess` se conserva con su comportamiento original, byte a byte.

## runtime.py — cache

Sustituido conscientemente:

```python
# ANTES (route Hermes, eliminado en Fase 0)
for name in ['WORKER.md','hermes_adapter.py']   # leia agente/ de otro proyecto

# AHORA
PROVIDER_SOURCES=('src/ds_provider.py','tools/ds_session.py','tools/ds_extract.py')
result['active_provider']=config.get('provider')
```

El hash de cache cambia cuando cambia el contenido real del provider, no cuando cambia
un archivo de otro proyecto.

## Colision de diseño encontrada

Al integrar, **3 tests que pasaban empezaron a fallar**. No era el provider: los tests
invocaban `provider.call(argv, ...)` esperando el route subprocess, y con
`provider: deepseek_cdp` en la config real ya no iban ahi.

```text
test_engine.test_provider_not_configured
test_engine.test_provider_bad_json
test_multiagent.test_provider_propagates_task_blocked
```

Solucion aplicada: esos tests ahora apuntan a `call_subprocess` explicito (el route que
realmente prueban) y se anadio `test_active_provider_reads_config` para fijar que el
provider activo se lee de la config.

**No se relajo ningunUmbral ni se borro ningun test.** Se explicito la intencion.

## Tests del provider (33, sin navegador)

| Grupo | Cubre |
|---|---|
| `validate_payload` | 8 — no-objeto, base_package, 5 reports, candidate+candidate_hash, candidato vacio |
| `build_prompt` | 5 — instrucciones, "solo JSON", payload al final, acentos, llaves en valores |
| `extract_json` | 12 — plano, fenced, con prosa, anidado, llaves en strings, comillas escapadas, truncado, array, nunca parcial |
| `call` | 8 — parseo, cierre de sesion, payload bloqueado no abre pestana, sin JSON, worker blocked, reply vacio, fallo de transporte, argv ignorado |

Guaranteas que fijan:
- un payload invalido **no abre pestana** (no se gasta nada)
- una respuesta sin JSON **lanza**, no devuelve medio objeto
- la sesion se cierra **siempre**, incluso en excepcion

## 3 errores restantes (identicos a Fase 0, NO tocados)

| Test | Clase | Razón |
|---|---|---|
| `test_anchor_hashes_still_match_registry` | C obsoleto | lee `01_CANON/anchors/registry.json`; el canon local no tiene `items[]/sha256` |
| `test_critic_payload_has_hash_and_context_not_history_reuse` | B depend. Hermes | `KeyError: 'critic_command'` |
| `test_repair_payload_protects_approved_criteria` | B depend. Hermes | `KeyError: 'failed_criteria'` |

Los 2 clase B se migran cuando el test apunte a DeepSeek. El clase C se reescribe aparte
para validar el canon local.

Skipped: `test_ep0001_request_still_readable` — "no prior episode in this checkout".

## Siguiente

1. `tools/ds_pool.py` — 5 pestanas, concurrencia acotada
2. Migrar los 2 tests clase B a DeepSeek
3. Reescribir el test clase C contra el canon local
4. Gate con DeepSeek real: 1 especialista, luego los 5 en paralelo

`START_HERE.md` sigue sin tocar, como se acordo.