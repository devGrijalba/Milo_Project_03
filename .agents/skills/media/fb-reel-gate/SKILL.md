---
name: fb-reel-gate
description: "Use as a hard gate before any image generation."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# GATE — brief obligatorio antes de generar

**Regla absoluta: no generar ninguna imagen hasta completar el brief y asignar una función
narrativa a cada frame.**

**Anclas obligatorias (MILO, 2026-09-28): todo reel emocional usa el set humano 50-55
(rostro legible, sin halo). El set de sombra (11/13/14/20) está PROHIBIDO para reels
emocionales — veto medido, no preferencia: v4-v7 devolvieron "entidad que vigila" en QC
ciego. El brief debe declarar el ancla por beat; un job con ancla de sombra se rechaza
antes de generar.**

No es una recomendación. Si el brief no está completo, el trabajo no empieza. En MILO002 se
generaron 5 imágenes antes de definir qué función tenía cada una: el reel salió plano por más
que las imágenes fueran buenas. Este gate existe para bloquear exactamente eso.

## FASE 0 — BRIEF ESTRATÉGICO (no se genera nada)

### 1. Objetivo del reel
Uno: conseguir compartidos · generar comentarios · provocar identificación · crear seguidores.

### 2. Emoción dominante
Una sola: tristeza · nostalgia · curiosidad · miedo · inspiración · rabia · esperanza · sorpresa.
No existe reel sin emoción definida.

### 3. Insight humano
La pregunta: **"¿Qué verdad humana estoy contando?"**

> Tema: persona fría
> Insight: "Las personas que parecen más fuertes muchas veces aprendieron a sobrevivir solas."

### 4. Hook (0-3s)
La frase exacta. Por qué alguien dejaría de deslizar.

## FASE 1 — MAPA DE IMÁGENES

Cada frame con función, no con descripción.

**NO:** imagen 1 persona caminando / imagen 2 persona mirando / imagen 3 persona sentada
→ produce estética sin narrativa.

**SÍ:**

| Beat | Tiempo | Función | Pregunta que responde | Imagen | Movimiento | Sonido |
|---|---|---|---|---|---|---|
| 1 | 0-3s | HOOK | ¿por qué alguien dejaría de deslizar? | primer plano emocional | zoom lento al elemento clave | impacto inicial |
| 2 | 3-7s | IDENTIFICACIÓN | ¿el espectador se ve reflejado? | problema humano visible | avance | ambiente entra |
| 3 | 7-12s | PROFUNDIZAR CONFLICTO | ¿qué se está escondiendo? | **metáfora visual** | paneo lateral | pulso bajo |
| 4 | 12-20s | CAMBIO EMOCIONAL | ¿qué cambió? | oscuridad→luz, soledad→aceptación | contraste | subida |
| 5 | final | MEMORIA + COMPARTIR | ¿puede ser portada? | cierre con carga emocional | pull-back | caída |

**Metáfora, no acción.** "Persona caminando" no dice nada. "Persona frente a una puerta cerrada
mientras escucha una conversación detrás" sí.

**El beat 5 debe poder ser thumbnail.** Si no funciona como portada, el reel no está terminado.

## FASE 2 — GENERACIÓN

Cada prompt con cuatro bloques:

- **Identidad** — quién es, edad, personalidad
- **Estado emocional** — no "triste", sino "contiene lágrimas pero intenta mantener una fortaleza"
- **Función narrativa** — "esta imagen representa el momento donde acepta que debe dejar atrás su pasado"
- **Referencia visual** — set, cámara, iluminación

En Hermes la función narrativa se traduce a la **cámara**: si el beat debe mostrar proporción adulta, el encuadre
no puede permitir que el modelo lo esconda. Ver `../milo-reel-editing` (la cámara gana al texto).

## FASE 3 — EDICIÓN

- **Movimiento**: nunca imagen estática. Acercar, alejar, lateral, profundidad falsa, desenfoque progresivo.
- **Ritmo**: cada 2-4s algo ocurre — visual, texto, sonido o emoción.

## Emotional Bible — obligatoria junto al brief

La Visual Bible (colores, camara, luz) no basta. Antes de generar el primer frame:

| | Contenido |
|---|---|
| **Dolor** | ¿que duele en este reel? |
| **Contradiccion** | ¿cual es la contradiccion humana? |
| **Debe sentir** | ¿que debe sentir el espectador al final? |

MILO002: dolor = "estar bien por fuera mientras por dentro se lucha"; contradiccion =
"sonrie / esta roto"; debe sentir = "yo conozco esa sensacion".

**Efectividad = Calidad Visual × Precisión Narrativa.** No es una suma: 10/10 visual con
3/10 narrativa falla. Ver `cinematic-visual-consistency` para la jerarquia de prompts
(estado humano → acción narrativa → elementos visuales).

## Gate de veracidad del veredicto

**El veredicto del gate lo contesta una persona, no el script.** `publish-gate.mjs` registra;
no juzga. Escribir "si x6" sin mirar produce PUBLICABLE sobre un reel que no identifica —
medido 2026-09-28: se marcaron 6 "si" y el QC ciego posterior dio 3 No.

**Regla:** el QC ciego (vision sin contexto del brief) va ANTES de responder el gate.
Si el evaluador independiente no dice "eso me pasa", Q2 es No aunque el frame sea hermoso.

## FASE 4 — GATE DE PUBLICACIÓN (6 preguntas)

Seis preguntas, respuesta sí/no. Ejecutable: `publish-gate.mjs` (escribe `metrics/publish_gate.json`).

1. ¿La primera imagen detiene el scroll?
2. ¿El espectador se siente identificado?
3. Si quito la música, ¿la historia sigue funcionando?
4. ¿La última frase genera comentario?
5. **Thumbnail** — ¿la portada vende una emoción incompleta? (no evalúa diseño, evalúa curiosidad)
6. **Rewatch** — ¿existe una razón para verlo otra vez?

**Umbral escalonado:** 0-1 NO = publicable · 2 NO = revisión obligatoria · 3+ NO = vuelve a estrategia.
Sin respuestas = bloqueado (no se publica con feedback abierto).

## Overlays: decoración vs función

Ningún overlay decorativo. Cada uno representa algo:

- **Lluvia** → aislamiento
- **Glow de ojos** → poder, transformación o misterio

Si no se puede decir qué representa, no va.

## Referencias

- `references/AUTONOMOUS_DECISION_ENGINE.md` — **motor de decisiones**: politica, frontera reversible/escalamiento, caso medido de agotamiento
- `references/CORE_NARRATIVE_ENGINE.md` — **constitución permanente**: identidad, esquema de beat de 8 campos, sistema de rechazo, QA universal. Leer primero.

- `fb-reel-strategy` — estructura, copy, método de pruebas
- `milo-reel-editing` — edición y movimiento por beat
- `meta-ai-worker` — generación y fallos medidos
