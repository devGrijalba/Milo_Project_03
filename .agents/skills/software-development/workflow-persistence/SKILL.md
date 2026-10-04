---
name: workflow-persistence
description: Use when work spans sessions or long tool chains.
---

# Workflow persistence

Un proyecto largo se pierde por acumulación, no por falta de trabajo. El
síntoma es siempre el mismo: alguien —o algo— vuelve dos horas después y
re-descubre lo que ya se sabía.

## Checkpoint después de cada hito grande

No al final. Hito = fase cerrada y verificada.

```
voz lista        → commit
imágenes 16/16    → commit
motion render     → commit
master armado     → commit
```

Acumular sin checkpoint tiene un coste concreto: cuando algo falla, no se
sabe qué cambió desde la última versión buena.

## `git add -A` no es un checkpoint

En un proyecto con assets pesados, `git add -A` se lleva 22 MB de PNG de
anclas y todos los audios. Añade explícito lo que es código y documentación:

```bash
git add ruta/al/codigo.py ruta/al/plan.json README.md STATE.md
```

Las salidas generadas (`salidas/`, `out/`, renders) van en `.gitignore`: son
artefactos, no fuente. Versiona el *plan* que produce el render, no el render.

## Tres documentos que no se negocian

| documento | qué guarda |
|---|---|
| `STATE.md` | dónde está el proyecto, con números medidos |
| `DECISION_LOG.md` | qué se decidió y **qué se descartó y por qué** |
| `CHECKLIST` | qué falta, marcado con lo verificado |

El log de decisiones es el que más se agradece: sin él se repite la
hipótesis que ya se probó y falló. Registra también los descartes, con motivo.

## Declara la hipótesis antes de probarla

"Prueba 0.6 → 0.35 de stability para ver si mejora el timeline." Si falla,
el resultado es dato: la variable no era la causa. Sin hipótesis escrita, un
fallo se interpreta como "aún no funciona" y se vuelve a probar lo mismo.

## Reporta lo que falló, con su mensaje literal

Un error con su texto exacto vale más que un "hubo un problema". Distingue el
fallo propio del ajeno — decir "el motor no lo soporta" cuando era un
argumento en el orden equivocado cuesta una fase entera.

## Una ruta puede parecer perdida y no estarlo

En Windows, una ruta construida a mano puede dar `exists() == False` mientras
el archivo está y se lista bien. Antes de declarar algo perdido, resuélvelo
por listado:

```python
d = next(x for x in padre.iterdir() if patron in x.name)
```

Cuesta una línea y evita reportar "el audio no existe" con el audio ahí.

## Verifica antes de afirmar

Medir, no suponer. "33.6s sin desviación" era falso: los segmentos sumaban
33.567s y solo se había verificado que el plan lo declarara. La corrección
fue 33ms, invisible — pero caía sobre el CTA, que es donde no importa que sea
invisible.
