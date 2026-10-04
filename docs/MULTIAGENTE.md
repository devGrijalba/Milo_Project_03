# Multiagente — Milo_Project_03

> Cargar solo cuando la tarea requiera delegar o paralelizar.

## Límites reales (verificados en `config.yaml`, no los de la documentación)

| Clave | Valor | Significado |
|---|---|---|
| `delegation.max_concurrent_children` | 27 | hijos en paralelo por llamada |
| `delegation.max_spawn_depth` | 3 | niveles de anidamiento |
| `delegation.max_iterations` | 400 | iteraciones por hijo |
| `delegation.orchestrator_enabled` | true | un hijo puede delegar |
| `delegation.child_timeout_seconds` | 0 | sin límite |
| `kanban.dispatch_in_gateway` | true | despachador activo |

## Reglas

1. **`delegate_task` es síncrono y NO durable.** Si el padre se interrumpe, el hijo
   muere. Para trabajo que debe sobrevivir al turno: `cronjob` o
   `terminal(background=True, notify_on_complete=True)`.
2. **Lotes**: cuando la tarea se repite N veces o se divide en flujos, delegar en vez de
   hacer el bucle a mano. El techo es 27 hijos, pero **un** hijo por etapa del pipeline
   rinde más que 27 hijos haciendo el mismo trabajo.
3. **Un hijo por episodio** cuando se produzcan varios: cada episodio es independiente
   (semilla, hash y snapshot distintos).
4. `max_spawn_depth: 3` permite que un nieto lance un bisnieto. No usarlo para encadenar
   síntesis de guiones: es un juego multiagente, no una garantía de calidad.
5. **Los resultados de hijos son auto-reportes, no hechos.** Un hijo que dice "subí el
   archivo" puede ser falso. Para efectos externos —subidas, escrituras remotas,
   publicaciones— exigir un identificador verificable (URL, ID, ruta absoluta) y
   comprobarlo antes de informarlo.
6. **No seguir artefactos de hijos.** Nunca esperes ni sondeos transcripciones, archivos
   o CI de un hijo esperando su mensaje de resultado.

## Panorámica de las 35 skills del proyecto

| Capacidad | Skills |
|---|---|
| Motor | `milo-episode-production`, `milo-story-success-engine`, `milo-repair-boundary` |
| Orquestación | `milo-batch-production`, `milo-subagent-orchestrator`, `multiagent-policy`, `workflow-persistence` |
| Guion | `script-revision-chatgpt`, `reel-contest-arena`, `contest-scoring-method`, `textopia-duracion`, `milo-animated-hook` |
| Visual | `milo-flow-pipeline`, `flow-image-generation`, `flow-bridge-operation`, `reference-authority`, `quota-preflight-and-completion`, `layered-lighting-resolution`, `generation-canon-gates`, `packs-de-flujo-no-son-canon`, `cinematic-visual-consistency` |
| Voz | `elevenlabs-voice-generation`, `milo-voice-casting`, `milo-dialogue-audio` |
| Edición | `milo-reel-editing`, `milo-caption-narrative`, `milo-thumbnail`, `cinematic-thumbnail`, `fb-reel-gate`, `evidence-delivery` |
| QA | `generation-qa-and-regression`, `e2e-validation` |
| Navegador | `chrome-cdp-automation`, `universal-dom-injector`, `llm-browser-injection` |

Detalle de cada una: `.agents/skills/README.md`. Sincronización: `docs/SKILLS.md`.

## Skills y multiagente

Cada skill de este proyecto está vendorizada en `.agents/skills/` y el catálogo de Hermes
es el maestro. Cuando un hijo necesite una skill:

- **No** copies la skill a mano del catálogo: lee la copia del proyecto.
- Si modificas una skill, hazlo en el catálogo de Hermes y luego
  `python .agents/skills/sync_skills.py --apply`. Editar la copia del proyecto directamente
  significa que `--apply` sobrescriba tu cambio.
- Cuando delegues, incluye en el `context` del hijo la ruta exacta de la skill que debe
  cargar (`skill_view(name=...)` con el nombre categorizado si hay colisión).