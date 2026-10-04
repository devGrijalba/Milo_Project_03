# CLASS_C_LOCAL_CANON — suite offline cerrada

```text
145 tests
145 pass  (1 skipped, justificado)
0 errors
0 regressions
DeepSeek real = NO
```

Cierre por archivo:

| Archivo | Tests | Estado |
|---|---|---|
| `test_ds_provider.py` | 34 | OK |
| `test_ds_pool.py` | 19 | OK |
| `test_pool_integration.py` | 18 | OK |
| `test_engine.py` | 14 | OK |
| `test_multiagent.py` | 49 | OK (1 skipped) |
| `test_optimization.py` | 11 | OK |

Skipped: `test_ep0001_request_still_readable` — "no prior episode in this checkout".
Correcto: aun no hay episodio generado.

## Qué cambió en el test clase C

**No se tocó código productivo.** Fue una migracion del test al contrato local.

El test viejo validaba una estructura externa que ya no existe:

```python
# ANTES -- leia otro proyecto
registry = read(PROJECT / '01_CANON/anchors/registry.json')
for item in registry['items']:            # items[] con file + sha256
```

Ese contrato desaparecio en Fase 0 (el canon local no tiene `items[]`). En vez de
doblar el test hasta que pasara, se declaro lo que el registry LOCAL debe garantizar hoy:

| Test | Garantia |
|---|---|
| `test_local_registry_parses` | parsea y expone `anclas` |
| `test_declared_anchors_exist` | cada ancla declarada existe en disco |
| `test_no_duplicate_anchor_ids` | sin ids duplicados |
| `test_no_duplicate_logical_names` | sin nombres logicos duplicados |
| `test_anchor_paths_stay_inside_anchors_dir` | ninguna ruta escapa de `knowledge/anchors` |
| `test_anchor_hash_is_verified_when_present` | si hay `sha256`, se valida |
| `test_local_canon_has_no_external_paths` | portabilidad: sin `..` ni `01_CANON` |
| `test_local_canon_context_loads` | el contexto completo carga offline |

### El hash es condicional, no inventado

`test_anchor_hash_is_verified_when_present` verifica `sha256` **solo si la entrada lo
declara**. El registry local esta vacio y no declara hashes, asi que no se invento un
requisito para hacerlo pasar: un vacio que cumple el contrato actual no necesita hashes.

Si manana se rellena `anclas` con hashes, el test los verifica sin cambiar una linea.

### Portabilidad como test propio

`test_local_canon_has_no_external_paths` es el test que faltaba. El problema de fondo era
que el motor dependia de `01_CANON/`, un proyecto ajeno. Ahora el contrato dice, de forma
verificable, que ningun path de canon sale del motor.

## Bugs reales encontrados en esta fase

Ninguno en esta migracion, pero la fase B anterior dejo dos que ya estan corregidos y
cubiertos:

1. `orchestrator.py` accedia a `c['critic_command']` directo → `KeyError` bajo DeepSeek.
2. `_apply_repairs` hacia `continue` silencioso → **toda reparacion se saltaba sin error**
   cuando `command` era `None`, que es el caso legitimo de `deepseek_cdp`.

El segundo era el grave: el motor|reportaba "reparado" sin haber reparado nada.
Cubierto por `test_repair_is_not_silently_skipped_without_argv`.

## Proximo paso: DeepSeek real

Ya no queda refactor offline que justifique. El gate minimo, en este orden:

1. **Una pestana, un especialista.** `script_hook_specialist` con la seed `MILO-S0001`,
   verificando que el modelo devuelve JSON valido y que el pool devuelve el tab.
2. **Los 5 en paralelo.** Medir wall-clock real y confirmar cero contamination.
3. **Sintetizador.** El unico agente que escribe el candidato completo.
4. **Critico.** Verificar el gate de exactamente 1 review.
5. Episodio completo `EP0001`.

En cada paso se mide duracion real. `response_timeout_s` esta en 300s y `timeout_s` en
2700: si DeepSeek no sostiene el ritmo, el limite se ajusta con evidencia, no a ojo.