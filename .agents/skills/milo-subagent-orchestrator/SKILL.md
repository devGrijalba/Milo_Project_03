---
name: milo-subagent-orchestrator
description: "Use when MILO work must fan out inside one chat: dispatch N subagents, orchestrate depth-2 trees, and verify artifacts before claiming done."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [MILO, multiagent, delegation, orchestration]
    category: autonomous-ai-agents
---

# Orquestador de subagentes MILO (dentro del mismo chat)

> **Copia local del proyecto.** Esta skill vive dentro de
> `D:\02_\MILO_HERMES_PRODUCTION_1.8.0\skills\` para que el paquete sea
> autocontenido. La copia que Hermes carga en sesión está en
> `%LOCALAPPDATA%/hermes/skills/milo-subagent-orchestrator/`. Tras editarla
> aquí, replicar con
> `python scripts/install_skills.py "%LOCALAPPDATA%/hermes/skills" --update`.
> Si divergen, **gana este archivo**.

Fan-out con `delegate_task` para trabajo MILO. Los subagentes corren **en threads del
proceso padre** (`tools/delegate_tool_child_run.py:841`), no como procesos
separados — memoria barata, pero el cuello de botella es el **provider**, no la RAM.

## Techos verificados en esta maquina (2026-10-03)

| Recurso | Medido | Implicacion |
|---|---|---|
| RAM | 15.3 GB total, **3.7 GB disponibles**, 75% carga | 27 subagentes en threads es viable; 27 **procesos** `hermes chat` no lo seria |
| RAM por especialista MILO | ~270 MB (proceso `hermes chat` separado) | El motor MILO y el fan-out de Hermes son sistemas distintos |
| `max_concurrent_children` | 27 | 27 x 3 x 3 con depth 3 es el techo teorico |
| `child_timeout_seconds` | 0 (sin tope) | El detector de heartbeat (450s idle / 1200s in-tool) sigue activo |
| `oneshot_max_children` | 2 (default, no tocar) | Los roles MILO son one-shot: cada uno paga un system prompt frio |

## La trampa que ya costo un episodio

`agente/config.json` traia `timeout_s: 1080` (18 min). EP0003 lanzo 5
especialistas en paralelo y **4 de 5 morreu con `TIMEOUT_NO_AUTO_RETRY`**. El
padre reporto `Provider failed with exit code 3` — sintoma de hijo perdido, no de
proveedor caido. Sube `timeout_s` a **2700** antes de escalar agentes; mas
agentes sobre un timeout corto solo multiplica la caida.

## Cuando delegar SIEMPRE

- N archivos de un mismo motor que auditar (contratos, adapters, canon).
- N hipotesis independientes sobre por que una etapa fallo.
- N imagenes reales a revisar (1 hijo por imagen, con proxy ya preparado).

## Cuando NO delegar

- Etapas que tocan medios, locks o APIs pagadas: `produce`, `run_voice`,
  `run_images`, `run_render`. Esas son **series** por diseno.
- Una sola llamada a herramienta. El overhead de crear el hijo supera el trabajo.
- Decisiones editoriales (que imagen, que criterio de aprobacion).
- Tareas que necesitan `clarify`: los hijos no pueden preguntar al usuario.

## Reglas de seguridad de este proyecto

1. Un subagente NUNCA llama `run_production`, `run_voice`, `run_images`,
   `run_subtitles` ni `run_render`. Esos adapters solo se invocan desde el padre.
2. Un subagente con `MILO_HERMES_WORKER=1` cumple `agente/WORKER.md`: resuelve
   el payload y escribe `RESPONSE_FILE`. Nada mas.
3. Nunca borrar `production.lock`. Nunca reintentar una generacion ambigua.
4. Nunca imprimir credenciales. Verificar presencia de claves, no su valor.
5. El veredicto es del padre. El resumen de un hijo es auto-informe.

## Procedimiento

1. **Antes de despachar:** `action='list'` para no duplicar trabajo ya en curso.
2. **Un hijo por unidad.** 13 imagenes = 13 hijos, no 1 hijo con 13 tareas.
3. **Pasa TODO el contexto.** El hijo no conoce esta conversacion: rutas
   absolutas, criterio de exito, formato exacto de salida.
4. **El resultado viaja por archivo.** Si la salida importa (JSON, tabla,
   medida), el hijo escribe un archivo y devuelve solo la ruta. Un resumen de
   300 lineas de un hijo es tan inutil como no tener respuesta.
5. **Usa `output_schema`** cuando el padre va a leer campos concretos: valida
   y devuelve `schema_valid` / `schema_errors`.
6. **`role="orchestrator"`** solo si necesitas anidamiento, y solo con
   `max_spawn_depth >= 2`. Un orquestador espera a sus hijos en el turno actual.
7. **Verifica antes de reportar.** Hash, tamano, fecha, o ejecucion real.
   Si es codigo: ejecutar, no leer.

## Arboles recomendados

```
Padre (este chat)
├── 3 hijos leaf: auditar motores / canon / adapters        (fan-out plano)
└── 1 hijo orchestrator (depth 2)
    ├── 3 nietos leaf: un motor cada uno
    └── 3 nietos leaf: una hipotesis de fallo cada una
```

Con depth 3 el techo es 27 concurrentes y el coste se multiplica por nivel.
Usalo solo con motivo: cada nivel paga un system prompt frio completo.

## Anti-patrones

| Anti-patron | Por que falla |
|---|---|
| Delegar una sola tarea | El overhead supera el trabajo |
| Delegar y creer el resumen | Es auto-informe; puede mentir |
| N tareas a 1 hijo | Se serializa dentro del hijo |
| Delegar la decision editorial | El hijo no conoce al usuario ni el canon |
| Escalar agentes sin revisar `timeout_s` | 4 de 5 mueren y el padre reporta error de proveedor |
| Devolver la salida completa en el resumen | Inunda el contexto del padre |