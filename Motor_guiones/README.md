# SCRIPT_ENGINE 1.3.0

Leer docs/OPTIMIZATION_1.3.0.md: cinco especialistas acotados, síntesis, revisión única/segunda condicional, repair selectivo, cache y progreso. Esta actualización sustituye el recorrido histórico descrito a continuación. No cambiar umbrales ni otros motores.

# SCRIPT_ENGINE — Milo 1.2.0

Motor modular portable para preparar, generar mediante runtime de agentes, validar y exportar historias dirigidas. Python 3.10+, sin dependencias externas. Copiar esta carpeta en `<proyecto>/02_ENGINES/SCRIPT_ENGINE/`. No altera los motores existentes ni contiene secretos.

## MILO SCRIPT ENGINE = MULTIAGENT PARALLEL CREATION + SYNTHESIS + DETERMINISTIC VALIDATION + INDEPENDENT CRITIC + CONDITIONAL REPAIR

La creación del guion ya no es una sesión monolítica. Cinco especialistas estrechos responden en **paralelo** a un mismo paquete autocontenido, un sintetizador integra, Python valida antes de gastar una sesión de crítico, y un crítico independiente juzga.

```
                     ┌─ script_hook_specialist
                     ├─ script_structure_specialist
SEMILLA + CONTEXTO ──┼─ script_milo_voice_specialist      (los 5 en paralelo)
                     ├─ script_novelty_specialist
                     └─ script_ending_specialist
                              │
                              ▼
                      script_synthesizer      ← único que redacta el candidato
                              │
                              ▼
                  VALIDACIÓN DETERMINISTA    ← local, antes de pagar sesión
                              │
                              ▼
                    script_critic            ← sesión nueva e independiente
                              │
              ┌───────────────┴───────────────┐
          APPROVED                         FAILED
              │                                │
              ▼                                ▼
       SCRIPT_APPROVED           repair por criterio fallido
                          (hook/structure/milo_voice/ending)
                              │
                              ▼
                     nuevo script_critic
```

### Paralelismo para latencia, no para duplicar trabajo

Los especialistas no escriben cinco guiones: cada uno responde una pregunta. El fan-out usa `script_parallel_agents` (5) y **no** el `max_parallel_tasks` global, que sigue en 1 para las etapas que tocan medios, locks y APIs pagadas.

**Medición real** con dobles locales a duraciones observadas hoy (150 s por especialista):

```
serial  (suma)          :  12.5 min
paralelo (real medido)  :   2.5 min   acotado por el especialista más lento
speedup                 :   5.00x
```

Cada episodio guarda `script_stage_metrics.json` con `wall_clock_ms`, `sum_agent_ms`, `slowest_agent_ms`, tiempos por especialista, síntesis, validación, crítico y reparación. La optimización se evalúa por wall clock, no por suma.

### Un crítico por defecto, segundo condicional

`required_review_passes` ya no es el gate. Ahora:

```
min_review_passes   = 1
second_review_mode  = conditional
```

Un crítico independiente aprobado basta. El segundo se compra solo ante una condición **objetiva**: puntuación en la franja 90–92, confianza distinta de `high`, desacuerdo declarado, o candidato ya reparado. El desacuerdo entre jueces (`max_judge_disagreement`) sigue evaluándose cuando existen dos revisiones. **Los umbrales 90 no se tocan.**

### Reparación selectiva

Si un criterio falla, no se reescribe el guion entero: se elige el agente estrecho de ese criterio, recibe los fallos exactos y la lista de criterios protegidos, y devuelve el candidato completo. `max_revisions: 3` se reinterpretó como 3 ciclos de reparación registrados.

### Payload autocontenido y bloqueo estructural

`provider.validate_payload` rechaza un payload stub **antes** de lanzar el subproceso: gastar 2-5 min de sesión para descubrir que falta contexto es desperdicio detectable en milisegundos. El bloqueo es `HERMES_TASK_BLOCKED:MISSING_SCRIPT_REQUEST_CONTEXT`, nunca `HERMES_CAPABILITY_BLOCKED`, que queda reservado para falta real de capacidad. Un especialista fallido no produce guion: no existe camino de candidato parcial.

## Qué está implementado

Selección con scores y exclusión de familias recientes/IDs consumidos/arcos repetidos; carga explícita de canon y minería; preparación de petición; protocolo stdin/stdout para escritor y crítico; validación técnica; estimación temporal; rechazo de planos largos sin dirección adicional; gates creativos con hash y evidencia; hasta 3 revisiones; exportación de guion, storyboard, paquete JSON y QC.

La narrativa libre la ejecuta Hermes o un proveedor de agentes: el módulo no contiene un modelo de lenguaje local ni una API narrativa configurada. Sin proveedor no inventa historias. Banco y scores de semillas son provisionales y no sustituyen QA del guion.

## Módulos

| Archivo | Responsabilidad |
|---|---|
| src/seed_selector.py | Selección desde semilla obligatoria |
| src/request_builder.py | Contexto, canon, minería e historial |
| prompts/writer.md | Estrategia, hooks, narrativa, dirección visual/vocal y montaje |
| **src/multiagent.py** | **Paquete autocontenido, fan-out paralelo, síntesis, precheck determinista, gatillo condicional y selección de repair** |
| src/contract_validator.py | Integridad y restricciones deterministas |
| src/timing_planner.py | Estimaciones y cobertura de planos |
| src/provider.py | Adaptador de comandos sin shell; rechaza payload stub antes de gastar sesión |
| prompts/critic.md + src/creative_qc.py | Evaluación separada y gates |
| src/scorecard.py | Ponderación local; mínimo 1 revisión, máximo 2 |
| src/orchestrator.py | Paralelo → síntesis → validación → crítico → repair → segundo condicional |
| src/exporter.py | Entrega de artefactos |
| config/ | Configuración intercambiable |
| schemas/ | Contratos publicados; el validador Python aplica controles propios |
| knowledge/ | Snapshot del canon y minería entregados |
| data/ | Banco revisado de 1.000 candidatas |

Los módulos intercambian objetos JSON. No llaman al motor de imagen, voz o render. No comparten su estado ni sus imports. La fuente viva del canon puede sustituir el snapshot mediante rutas configuradas.

## Estados

REQUEST_READY → NEEDS_SCRIPT_REVISION / AWAITING_CREATIVE_QC → SCRIPT_APPROVED.

Aprobación técnica no equivale a calidad creativa. Los tiempos siempre quedan ESTIMATED_NOT_AUDIO_ALIGNED hasta intervención del motor de voz. SCRIPT_APPROVED tampoco aprueba imágenes, audio o video inexistentes.

## Restricciones y límites

Planos 3s salvo primero; máximo 45s estimado; música y SFX desactivados. Ajustables por configuración. Estos límites operativos no se presentan como conclusiones causales de minería. Los planes de transición deben resolverse con audio real en render.

Historial se suministra explícitamente como lista JSON. Este módulo no reserva semillas ni marca consumo: el orquestador superior debe manejar reserva atómica y registrar entrega. Evitar ejecuciones concurrentes en la misma carpeta. No usar el mismo output para episodios distintos.

La inspección semántica de coherencia, canon y novedad recae en el crítico. El validador no puede demostrar que un personaje respeta identidad visual leyendo una frase. Sin evidencia suficiente el crítico debe rechazar.
