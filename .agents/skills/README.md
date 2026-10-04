# Skills del proyecto — Milo_Project_03

35 skills vendorizadas desde `C:\Users\Ivan\AppData\Local\hermes\skills`, copiadas
*verbatim* (nunca editadas aquí) con su ruta de origen preservada.

No son las 316 del catálogo: son las que **este proyecto** necesita. El criterio fue que
cada skill cubra una capacidad concreta que el motor exige — una regla de
`Motor_guiones/AGENTS.md`, del `config/engine.json` o de la cadena de producción.

## Por qué `.agents/skills/`

Es la ruta **project-local** que Hermes escanea en un repo git, y tiene la precedencia más
alta: `project → local (~/.hermes/skills/) → external_dirs`.

La alternativa `.hermes/skills/` no sirve aquí: `.hermes/` está en `.gitignore` y Git
**no puede re-incluir archivos bajo un directorio excluido** (comprobado: las skills
quedaban invisibles al repo).

El repo está registrado en `skills.trusted_project_dirs`. Sin ese registro Hermes avisa
en el banner y **no** las carga.

## Índice por capacidad

### Motor narrativo
| Skill | Por qué |
|---|---|
| `milo-episode-production` | Producción de un episodio desde el banco canónico |
| `milo-story-success-engine` | Elegir la semilla correcta antes de producir |
| `milo-repair-boundary` | Reparar defectos sin romper la intención |

### Orquestación
| Skill | Por qué |
|---|---|
| `milo-batch-production` | N episodios sin intervención humana |
| `milo-subagent-orchestrator` | Fan-out de episodios en subagentes |
| `multiagent-policy` | Política de multiagente |
| `workflow-persistence` | Continuar trabajo entre sesiones |

### Guion
| Skill | Por qué |
|---|---|
| `script-revision-chatgpt` | Revisión quirúrgica vía LLM web |
| `reel-contest-arena` | Arena de guiones (duelo de LLMs) |
| `contest-scoring-method` | Método de puntuación de la arena |
| `textopia-duracion` | Preflight aritmético de duración |
| `milo-animated-hook` | Hook animado de 4 s |

### Visual (Flow)
| Skill | Por qué |
|---|---|
| `milo-flow-pipeline` | Generar/auditar imágenes MILO en Flow |
| `flow-image-generation` | Generación de imágenes |
| `flow-bridge-operation` | Flow vía extension + bridge |
| `reference-authority` | Qué imagen de referencia manda |
| `quota-preflight-and-completion` | Preflight de cuota pagada |
| `layered-lighting-resolution` | Resolver conflicto de luces |
| `generation-canon-gates` | Lock canónico que alimenta el prompt builder |
| `packs-de-flujo-no-son-canon` | Un pack de Flow no es canon |
| `cinematic-visual-consistency` | Mantener un universo visual |

### Voz
| Skill | Por qué |
|---|---|
| `elevenlabs-voice-generation` | Generar voz |
| `milo-voice-casting` | Casting de voces MILO |
| `milo-dialogue-audio` | Audio de diálogo |

### Edición y entrega
| Skill | Por qué |
|---|---|
| `milo-reel-editing` | Editar stills en reel cinematográfico |
| `milo-caption-narrative` | Subtítulos narrativos |
| `milo-thumbnail` | Thumbnail de episodio |
| `cinematic-thumbnail` | Thumbnail CTR |
| `fb-reel-gate` | Gate antes de generar imagen de reel |
| `evidence-delivery` | Entrega de trabajo terminado |

### QA
| Skill | Por qué |
|---|---|
| `generation-qa-and-regression` | Auditar imágenes generadas |
| `e2e-validation` | Validación end-to-end del pipeline |

### Navegador / CDP
| Skill | Por qué |
|---|---|
| `chrome-cdp-automation` | Transporte CDP |
| `universal-dom-injector` | Inyectar prompts en web chats |
| `llm-browser-injection` | Consultar LLM web vía navegador |

## Sincronización

La copia de este proyecto es la que se usa al producir. El catálogo de Hermes es el
maestro. `MANIFEST.json` guarda el origen y el SHA256 de cada archivo.

```bash
# ¿hay deriva? (solo informa, no escribe)
python .agents/skills/sync_skills.py

# resincronizar lo que difiera
python .agents/skills/sync_skills.py --apply
```

Probado en ambas direcciones: detecta una línea inyectada, la repara con `--apply`, y
`diff -r` contra el origen queda idéntico.

Si alguna vez se edita una skill aquí dentro, `--apply` sobrescribe ese cambio: la
edición correcta se hace en el catálogo de Hermes.

## Aviso: repo público

Este proyecto está conectado a un repositorio **público** de GitHub. Las skills son
código público y no contienen secretos, pero cualquier archivo con credenciales, tokens
o cookies que se añada a esta carpeta terminaría publicado. Si alguna vez hace falta
guardar un perfil de navegador o un `.env`, va **fuera** de este árbol (como
`D:\03_Pruebas\cdp-chrome-clean`, hermano del repo y que git no ve).