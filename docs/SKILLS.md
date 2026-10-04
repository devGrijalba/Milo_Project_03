# Skills del proyecto — Milo_Project_03

> Cargar solo cuando la tarea toque skills: elegir una, sincronizarla o añadirla.

## Ubicación

`.agents/skills/` — la ruta **project-local** que Hermes escanea en un repo git, con la
precedencia más alta: `project → local (~/.hermes/skills/) → external_dirs`. Una skill
del proyecto gana a una del perfil con el mismo nombre.

**Por qué no `.hermes/skills/`**: `.hermes/` está en `.gitignore` y Git **no puede
re-incluir archivos bajo un directorio excluido** (comprobado: las skills quedaban
invisibles al repo).

El repo está en `skills.trusted_project_dirs`. Sin ese registro Hermes avisa en el banner
y **no** las carga.

## Carga progresiva — obligatorio

| Nivel | Herramienta | Cuándo |
|---|---|---|
| 0 | `skills_list()` | Para decidir si aplica (~3k tokens) |
| 1 | `skill_view(name)` | Solo si aplica de verdad |
| 2 | `skill_view(name, path)` | El archivo de referencia exacto |

No leer un `SKILL.md` completo "por si acaso". Un archivo cargado sin necesidad es
contexto que no se puede usar para el trabajo.

## Sincronización

El catálogo de Hermes es el maestro. `MANIFEST.json` guarda origen + SHA256 de cada
archivo.

```bash
python .agents/skills/sync_skills.py           # ¿hay deriva? (informa, no escribe)
python .agents/skills/sync_skills.py --apply   # resincronizar
```

**No editar skills dentro de `.agents/skills/`.** La edición correcta se hace en el
catálogo de Hermes y `--apply` la trae. Si se edita aquí, `--apply` sobrescribe el cambio.

## Las 35 skills

Índice completo por capacidad: `.agents/skills/README.md`. Resumen por etapa:

| Capacidad | Skills |
|---|---|
| Motor narrativo | `milo-episode-production`, `milo-story-success-engine`, `milo-repair-boundary` |
| Orquestación | `milo-batch-production`, `milo-subagent-orchestrator`, `multiagent-policy`, `workflow-persistence` |
| Guion | `script-revision-chatgpt`, `reel-contest-arena`, `contest-scoring-method`, `textopia-duracion`, `milo-animated-hook` |
| Visual (Flow) | `milo-flow-pipeline`, `flow-image-generation`, `flow-bridge-operation`, `reference-authority`, `quota-preflight-and-completion`, `layered-lighting-resolution`, `generation-canon-gates`, `packs-de-flujo-no-son-canon`, `cinematic-visual-consistency` |
| Voz | `elevenlabs-voice-generation`, `milo-voice-casting`, `milo-dialogue-audio` |
| Edición y entrega | `milo-reel-editing`, `milo-caption-narrative`, `milo-thumbnail`, `cinematic-thumbnail`, `fb-reel-gate`, `evidence-delivery` |
| QA | `generation-qa-and-regression`, `e2e-validation` |
| Navegador / CDP | `chrome-cdp-automation`, `universal-dom-injector`, `llm-browser-injection` |

No son las 316 del catálogo: son las que **este proyecto** necesita. Una skill entra si
cubre una capacidad concreta que el motor exige, no por catálogoTemática.

## Al delegar a un subagente

Incluye en su `context` la ruta exacta de la skill que debe cargar. Si hay colisión de
nombre —dos skills con el mismo `name`, típico cuando una tiene un `.bak` junto a la
otra—, usa la forma categorizada con la ruta relativa completa dentro de la categoría
(por ejemplo `categoria/nombre-de-la-skill`) en lugar del nombre suelto.