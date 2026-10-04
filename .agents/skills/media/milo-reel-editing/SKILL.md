---
name: milo-reel-editing
description: "Use when editing MILO stills into a cinematic reel."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# MILO Reel — stills a reel cinematográfico

## Principio

Una imagen fija no entrega transformación. Facebook premia **evento → emoción → transformación**, y un still
solo entrega evento. La transformación se construye en edición: movimiento falso de cámara, sonido, ritmo,
texto en pulsos, overlays y transiciones. Pedirle al modelo que "actúe" es la vía equivocada cuando no hay video.

## Orden de los bloques de prompt (personaje híbrido)

1. CHARACTER IDENTITY LOCK
2. CHARACTER MORPHOLOGY LOCK
3. ENVIRONMENT LOCK (`EXACT LOCATION REFERENCE` + prohibición de reemplazo)
4. CAMERA
5. ACTION
6. STRICT NEGATIVE

`preserve atmosphere` solo = el modelo inventa otro lugar con la misma sensación. Anclar por nombre.

## Vocabulario que dispara arquetipos

- ❌ `spiky hair` → adolescente, cabeza inflada
- ✅ `abundant messy black hair with irregular natural strands`, `mature messy hairstyle`
- ❌ `Do not change the anime cel-shaded style` → le dice "todo anime" y aplana sets realistas
- ✅ `Preserve Milo's cel-shaded design while integrating into the cinematic environment. Do not make the environment anime.`

## Morphology: la cámara gana al texto

Con el MISMO bloque de identidad:
- `Full body, head to shoes` → **adulto**
- `Medium shot sitting` → **adolescente**

Principio: no digas "Milo es adulto"; elige el encuadre donde no pueda no serlo. En plano abierto añadir
restricción geométrica (`shoulders wider than his head`, `do not shrink his legs`) porque la referencia
es pequeña en el frame. En close-up la edad no es medible: mirar cráneo, masa de pelo y cuello.

## QC de personaje — por visión, nunca por píxeles

Comparar contra el ancla: silueta, proporción cabeza/cuerpo relativa, extremidades, hombros, postura, pelo, vestuario.
Un `head_ratio` absoluto por segmentación NO sirve: el pelo, las sombras y el estilo gráfico lo rompen
(medido: marcó como "niño" un ancla que era un adulto). Un gate de texto tampoco: 11 gates pasaron un batch
entero con el personaje infantil.

## Audio: 4 capas, cada una con función

> El sonido no acompaña la imagen. **El sonido revela informacion que la imagen no muestra.**

Prioridad: Narrativa > Emocion > Sonido > Estetica.

| Capa | Que construye | Ejemplos |
|---|---|---|
| **1 Ambiente** | el mundo donde ocurre | habitacion vacia, lluvia, ciudad nocturna |
| **2 Foley narrativo** | **la accion** | telefono vibrando, pasos, puerta cerrandose, papel doblandose |
| **3 Musica emocional** | la energia interna | tension, introspeccion, esperanza |
| **4 Impacto** | solo en momentos clave | revelacion, cambio, decision |

**El foley es la capa que mas se olvida y la que mas anade.** Un beat de "una llamada perdida
deferida" sin el telefono vibrando es una foto con texto. Con la vibracion en el momento exacto
de la decision, el espectador oye lo que la imagen no puede mostrar: que el telefono **sono**, y
que el personaje **lo dejo sonar**.

### Antes de seleccionar audio responder

1. ¿Que siente el personaje?
2. ¿Que accion ocurre?
3. **¿Que informacion falta en la imagen?**
4. ¿Que sonido puede revelarla?

Nunca: musica triste generica sobre tristeza · saturar todas las escenas · efectos sin intencion.
Siempre: dejar espacio al silencio · sonidos pequenos con significado · priorizar diegeticos.

## Matriz emocion → audio

| Emocion | Ambiente | Foley | Musica |
|---|---|---|---|
| Soledad | habitacion vacia | reloj, respiracion, telefono | piano minimalista |
| Tension | drone bajo | latidos, pasos | suspense lento |
| Esperanza | manana, naturaleza | acciones cotidianas | cuerdas calidas |
| **Autodesnudo** (MILO002) | lluvia + room tone | **telefono vibrando una vez** | pad menor muy bajo |
| Verguenza / ocultamiento | habitacion ocupada a distancia | respiracion contenida | sin musica |

Regla de musica: **no usarla para decir "esto es triste"**. Usarla para crear tension,
introspeccion o esperanza.

## Referencias

- `references/audio-decision-engine.md` — **motor de 5 pasos + biblioteca de 12 patrones** (consultar por DECISIÓN, no por emoción)
- `cinematic-visual-consistency` — jerarquía de prompts y Emotional Bible
- `generation-pipeline-control` — un proceso a la vez, artifact gate

## Foley narrativo = acción invisible

> **Todo beat importante debe tener al menos un sonido que represente una decisión.**
> Si no existe, la escena puede estar visualmente correcta pero narrativamente incompleta.

Un objeto visual no siempre cuenta su historia. "Hombre mirando un teléfono" dice: hay un
teléfono, hay un hombre, parece preocupado. **No dice si sonó, si alguien intentó contactarlo,
ni si tomó una decisión.** El foley completa eso.

La acción real de un beat no es "mirar el teléfono" — es *"alguien intentó acercarse y él decidió
no abrir esa puerta"*.

### Qué responde cada capa

| Capa | Pregunta |
|---|---|
| Ambiente | ¿donde estamos? |
| Musica | ¿que debemos sentir? |
| **Foley** | **¿que acaba de ocurrir?** |
| **Impacto** | **¿que acaba de cambiar?** |
| **Silencio** | **¿que NO ocurrio?** (la consecuencia) |

### Estructura de un beat con foley

```
12.30s  vibracion del telefono
   ↓
0.85s   la vibracion suena
   ↓
1.2s    SILENCIO
   ↓
el personaje no responde
```

## SILENCE AS FOLEY — el silencio es una decisión, no una ausencia

> **Una decisión no siempre produce un sonido. A veces produce un silencio diseñado.**

Regla que corrige el error mas comun: intentar llenar todos los espacios con audio.

La asociacion antigua era `accion = sonido`. La correcta es:

> **accion = evidencia perceptible**

Y la evidencia perceptible puede ser: **sonido · ausencia de sonido · pausa · respiración · espacio vacío**.

### Silencio vacío vs silencio narrativo

| | Qué es | |
|---|---|---|
| **Silencio vacío** | no pasa nada | ❌ |
| **Silencio narrativo** | pasó algo y ahora esperamos la consecuencia | ✅ |

MILO002: telefono vibra → no responde → **silencio**. Ese segundo no es ausencia de audio, es
*"la oportunidad existio y fue rechazada"*.

### Test de silencio (4º test de audio)

> **Si elimino este silencio, ¿la decision pierde peso?**

Si si → mantener. Si no → eliminar.

Un silencio que no se puede sentir al quitarlo no es narrativo: es un hueco en la mezcla.

### YAML de silencio narrativo

```yaml
silencio_narrativo:
  existe: true
  cuando:
    - el personaje decide no actuar
    - el personaje oculta algo
    - la consecuencia pesa mas que la accion
  validacion:
    pregunta: "El silencio comunica una decision?"
```

### La regla accion = evidencia perceptible

Cuando la accion de un beat es "quedarse quieto" o "no contestar", **no hay sonido que fabricar**.
La evidencia es la ausencia. Fabricar un sonido ahi seria mentir sobre la accion.

## Los tres modulos permanentes

| Modulo | Qué es | Ejemplos |
|---|---|---|
| **1 Foley de accion** | el cuerpo en movimiento | pasos, objetos, roces, ropa |
| **2 Foley de decision** | la eleccion y su rechazo | llamada ignorada, puerta cerrada, carta guardada |
| **3 Silencio narrativo** | la consecuencia de no hacer nada | espera, perdida, aceptacion, negacion |

**El 3 es el mas diferencial:** la mayoria de los sistemas intenta agregar; este aprende cuando NO agregar.

## Conclusion medida (MILO002)

El beat 4 no funcionaba porque tuviera un telefono. Funcionaba porque tenia una **accion
irreversible pequena**: "alguien llama y el decide no contestar". El sonido solo hizo visible
la decision.

## Beat Validation Gate — 6 preguntas + gate de evidencia

Cada beat debe responder las 6. Si falta una, el beat está incompleto.

1. ¿Existe estado humano? (¿qué siente?)
2. ¿Existe conflicto? (¿qué está en juego?)
3. ¿Existe decisión? (¿qué hace o evita hacer?)
4. ¿Existe relación? (¿a quién afecta?)
5. ¿Existe consecuencia? (¿qué cambia?)
6. ¿Existe identificación? (¿el espectador puede pensar "eso podría ser yo"?)

**Gate adicional — evidencia:** ¿la decisión tiene evidencia visual O sonora?
Si no: el beat no está terminado. Una decisión sin evidencia es una intención invisible.

```
Impacto = Imagen × Acción × Sonido × Silencio
```

## Corrección de episodio existente — auditar antes de modificar

No asumir que los assets actuales son correctos. El objetivo no es conservar
producción previa: es maximizar narrativa.

FASE 1 — Analizar cada beat existente contra el gate (6Q + evidencia).
FASE 2 — Detectar fallos: personaje sin acción · emoción explicada por texto ·
ausencia de relación · ausencia de consecuencia · audio decorativo.
FASE 3 — Regenerar beats débiles. FASE 4 — Aplicar audio narrativo.
FASE 5 — QA/QC final (5 tests).

**Regenerar cuando:** la imagen necesita texto para funcionar · el personaje solo posa ·
la emoción es genérica · no existe acción · no hay relación humana.

**Mantener cuando:** la imagen cuenta una situación · existe decisión visible ·
el espectador puede identificarse.

No conservar una escena solo porque sea visualmente bonita.
Si una imagen no cuenta una historia, se regenera.

## QA/QC — 5 tests (el 5º es nuevo)

| Test | Pregunta | Falla si |
|---|---|---|
| **1 — Sin texto** | si elimino el texto, ¿la imagen sigue contando algo? | fallo narrativo |
| **2 — Sin voz** | ¿imagen + sonido sostienen la emoción? | solo queda estética bonita |
| **3 — Solo audio** | ¿puedo imaginar una escena? | audio decorativo |
| **4 — Decisión** | ¿tiene decisión audible o silencio narrativo? | beat incompleto |
| **5 — Identificación** | ¿el espectador puede verse reflejado? | "qué personaje tan interesante" en vez de "eso me pasó" |

## Tests de audio (4, obligatorios antes de aprobar)

| Test | Pregunta | Falla si |
|---|---|---|
| **1 — Imagen sola** | si elimino audio y texto, ¿la situacion tiene sentido? | no hay historia base |
| **2 — Imagen + audio sin voz** | ¿el sonido agrega informacion nueva? | solo aumenta tristeza |
| **3 — Audio solo** | ¿puedo imaginar una escena? | no completa "algo paso" |
| **4 — Silencio** | si elimino este silencio, ¿la decision pierde peso? | el silencio no es narrativo |

Test 2 es el que separa el foley de la decoracion: si quito el audio y solo se pierde "tristeza",
sobra. Si quito el audio y se pierde **una decision**, funciona.

## Metrica de impacto

```
Impacto = Imagen × Accion × Sonido × Silencio
```

No es una suma: falta cualquiera de los cuatro y el producto cae. Muchas emociones fuertes viven
precisamente en lo que **no** ocurre — la llamada no contestada es mas poderosa que una
disputa; la puerta que no se abre es mas poderosa que alguien diciendo "vete".

## Reglas de edicion

- **Musica entra 2-5s ANTES del momento emocional.** Sostener, nunca competir con la voz.
- **Foley en el momento exacto de la accion**, no durante toda la escena. Telefono en imagen →
  una vibracion cuando ocurre la decision, no un bucle de 5 segundos.
- **El silencio es un recurso narrativo.** Usarlo despues de: una llamada perdida · una noticia ·
  una decision dificil. Cortar la musica 1-2s es mas fuerte que subirla.

## QA/QC de audio

| Tipo | Pregunta | Si falla |
|---|---|---|
| **Narrativo** | ¿el sonido agrega informacion? | eliminar |
| **Emocional** | ¿provoca "entiendo esa sensacion" o "escucho un efecto triste"? | re-elegir |
| **Tecnico** | sin clipping · niveles consistentes · voz entendible · musica debajo de narrativa · sin efectos innecesarios | re-mezclar |
| **Beat** | estado humano + accion + relacion + consecuencia + audio asociado | falta una capa |

**QC final — 3 pruebas:**

1. Ver el video SIN texto → ¿cuenta la historia?
2. Ver el video SIN voz → ¿la imagen + el audio sostienen la emocion?
3. Escuchar SOLO el audio → ¿sostiene la emocion a ojos cerrados?

> **Si elimino el audio, ¿pierdo informacion emocional o narrativa?**
> Si la respuesta es no, ese audio sobra.

## Movimiento por beat (no repetir el mismo zoom)

| Beat | Función | Movimiento | Escala |
|---|---|---|---|
| 1 | HOOK | push-in lento | 100 → 108% |
| 2 | DESPLAZAMIENTO | avance digital | 100 → 112% |
| 3 | INTERIORIDAD | paneo lateral mínimo + overlay lluvia | 100 → 108% |
| 4 | REVELACIÓN | zoom casi estático + glow | 100 → 106% |
| 5 | CIERRE | **pull-back** | 106 → 100% |

Entrada → avance → cercanía → revelación → distancia.

## Efectos que suman

- Glow/pulso de ojos en beats 1 y 4 (solo opacidad, no animación total)
- Overlay de lluvia sutil en 3 y 5
- Grano fino uniforme: unifica estilos y quita el aire de "IA estática"
- Viñeta muy leve

## Transiciones

Solo: crossfade corto, blur dissolve, dip to black breve, flash azul muy sutil.
Evitar giros, rebotes, barridos y transiciones de plantilla.

## Copy: identificación > consejo

- ❌ "No necesitamos cargar más. Necesitamos mirar adentro." → instrucción
- ✅ "A veces no estamos cansados de vivir… estamos cansados de ocultar." → identificación

La identificación es la que abre comentarios. Máximo 2 líneas por bloque, respiradas.
Todo bloque de reflexión necesita una pregunta al final: sin CTA se pierde el potencial de comentarios.

## Checklist antes de publicar

- [ ] Identidad estable, no cambia edad aparente, silueta adulta
- [ ] Ubicación respetada, no inventa escenarios
- [ ] Hook en los primeros segundos
- [ ] Texto arriba (regla MILO), 2 lineas máximo por bloque
- [ ] Movimiento varied por beat
- [ ] Audio con progresión y **cada capa con funcion narrativa** (ambiente/foley/musica/impacto)
- [ ] Cierre que genere comentario

### Historia e imagen (del pack de calibración)

- [ ] Existe una emoción clara
- [ ] Existe una decisión, una relación, una consecuencia
- [ ] La imagen cuenta algo **sin texto**
- [ ] Precisión narrativa > belleza visual

## Principio final

Si el problema es de edición, no busques más imágenes. Primero narrativa, ritmo y montaje.

## Referencias

- `../meta-ai-worker/references/milo-prompt-rules.md` — bloques exactos que funcionaron
