# Audio Decision Engine

Hermes no aprende "pasos mojados". Aprende **relaciones** entre decisión y evidencia sonora.
La biblioteca se consulta por DECISIÓN, no por emoción.

## El motor: 5 pasos antes de generar audio

### Paso 1 — Descomponer el beat
```
BEAT n
Estado:    (que siente / que evita mostrar)
Accion:    (que hace o deja de hacer)
Relacion:  (con quien)
Consecuencia: (que queda)
```

### Paso 2 — Buscar la "decisión física"
> ¿Qué movimiento, objeto o ausencia demuestra esta decisión?

| Acción | Evidencia sonora |
|---|---|
| no responde una llamada | vibración de teléfono |
| se va | pasos alejándose |
| se queda | silla / crujido / silencio |
| abre una carta | papel |
| recuerda a alguien | fotos, papel, caja |
| miente | voz que se corta, puerta |

### Paso 3 — Crear el FOLEY_REQUIRED (campo obligatorio)
```yaml
FOLEY_REQUIRED:
  evento:           llamada ignorada
  sonido:           phone vibration
  momento:          segundo 12.30
  duracion:         0.85 segundos
  razon_narrativa:  existe una oportunidad de conexión que el personaje rechaza
```
El campo `razon_narrativa` es el que obliga a pensar. Sin él, el foley se vuelve decoración.

### Paso 4 — Gate automático
```
¿Este beat tiene una decisión?                    → si no, bloqueado
¿La imagen la muestra completamente?              → si no, sigue
¿Existe un sonido que revele la parte invisible?  → si no, PENDIENTE
```

### Paso 5 — Consultar la biblioteca de patrones

## Biblioteca de patrones

Consultar por DECISIÓN. El objeto es consecuencia de la decisión, no al revés.

**La columna EVIDENCIA puede ser sonido O silencio.** Si la decisión es "no hacer nada", la
evidencia es la ausencia — ver `SILENCE AS FOLEY` en SKILL.md.

| # | DECISIÓN | OBJETO | EVIDENCIA | TIPO | EMOCIÓN |
|---|---|---|---|---|---|
| 01 | ignorar contacto | teléfono | vibración + **1.2s de silencio** | sonido + silencio | evitación, culpa |
| 02 | alejarse | cuerpo en movimiento | pasos + eco de pasillo | foley de acción | aceptación, pérdida |
| 03 | permanecer | silla / habitación | crujido + ambiente vacío | consecuencia | resignación, calma |
| 04 | detenerse y no actuar | silla | roce + golpe + respiración | cambio de estado | interioridad |
| 05 | ocultar emoción | respiración / manos | respiración profunda contenida | foley de decisión | miedo, vergüenza |
| 06 | abrir algo que duele | carta / puerta | papel, bisagra | foley de acción | vulnerabilidad |
| 07 | esperar a alguien | ventana / reloj | reloj, lluvia, **nada** | silencio + ambiente | ansiedad |
| 08 | decir la verdad | voz | **silencio antes de hablar** + inhalación | silencio + foley | liberación, terror |
| 09 | romper algo | objeto | golpe, cristal | foley de acción | rabia, renuncia |
| 10 | **no hacer nada** | — | **silencio total controlado** | **silencio narrativo** | parálisis, aceptación |
| 11 | cargar con algo | espalda, hombros | respiración cargada, pasos cortos | foley de acción | peso |
| 12 | despedirse | puerta / mano | bisagra, paso que se aleja | foley de decisión | pérdida |
| 13 | empezar a llorar | garganta / manos | inhalación rota, sin sollozo | foley de decisión | release |
| 14 | aguantar | todo el cuerpo | respiración contenida larga | foley de decisión | fortaleza, agotamiento |

### Los tres módulos

| Módulo | Qué es | Ejemplos |
|---|---|---|
| **1 Foley de acción** | el cuerpo en movimiento | pasos, objetos, roces, ropa |
| **2 Foley de decisión** | la elección y su rechazo | llamada ignorada, puerta cerrada, carta guardada |
| **3 Silencio narrativo** | la consecuencia de no hacer nada | espera, pérdida, aceptación, negación |

**El 3 es el más diferencial:** la mayoría de los sistemas intenta agregar; este aprende cuándo **NO** agregar.

### Notas de diseño

- **Patrón 10** es un patrón válido, no una ausencia. Si el beat consiste en no actuar, el silencio
  ES el sonido y hay que declararlo explícitamente en el FOLEY_REQUIRED.
- **Patrón 04 vs 03**: 04 es el momento de sentarse (movimiento), 03 es quedarse quieto después
  (quietud). No usar el mismo sonido para los dos.
- Los sonidos diegéticos (de dentro de la historia) ganan a los no diegéticos siempre que
  emparejen la acción. La vibración del teléfono es diegética; un latido de corazón sobre un
  personaje que no tiene uno visible, no.

## De "qué música queda bien" a "qué información falta"

El cambio real: Hermes deja de preguntar

> "¿Qué música queda bien aquí?"

y empieza a preguntar

> **"¿Qué información narrativa falta que solo el sonido puede entregar?"**

Si la respuesta es "ninguna", no hay música que poner.

## Estructura completa

```
HISTORIA → EMOTIONAL BIBLE → BEATS → ACCIÓN NARRATIVA → DECISIÓN
→ EVIDENCIA VISUAL → EVIDENCIA SONORA → FOLEY → MÚSICA → QA/QC
```
