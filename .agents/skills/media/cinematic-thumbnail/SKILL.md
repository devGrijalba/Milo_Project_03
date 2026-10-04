---
name: cinematic-thumbnail
description: "Use when building a reel thumbnail for CTR."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Cinematic Thumbnail Engine

## Principio

El thumbnail **no resume** el video. **Vende una emoción incompleta** que obliga a descubrir la historia.

> Antes: "haz un thumbnail del personaje"
> Después: "diseña una portada que venda una contradicción emocional"

No es una captura con texto encima: es una composición estratégica nueva basada en la emoción principal.

## Antes de escribir el prompt, responder

**1. ¿Qué emoción vende?** tristeza oculta · miedo · nostalgia · sorpresa · esperanza · misterio.
Nunca "bonito".

**2. ¿Cuál es la contradicción humana?** — el mejor thumbnail tiene contraste:
- "Sonríe pero está roto"
- "Es fuerte pero está solo"
- "Parece feliz pero oculta dolor"

**3. ¿Qué pregunta mental genera?** Texto "Sonreía por fuera..." → pregunta "¿qué estaba pasando realmente?"

## Estructura del prompt (6 bloques)

1. **IDENTIDAD** — personaje, edad, vestuario, rasgos únicos
2. **EMOCIÓN** — el bloque más importante. Nunca "sad character" (genérico). Usar:
   `subtle emotional exhaustion, someone trying to hide internal pain, quiet suffering, vulnerability without showing weakness`
3. **COMPOSICIÓN** — close-up, sujeto dominante, punto focal claro, espacio para texto
4. **ILUMINACIÓN** — nunca "good lighting": `low key cinematic lighting, dramatic rim light, deep shadows, soft volumetric fog, film color grading, subtle bloom`
5. **ATMÓSFERA** — `cold blue atmosphere, night mood, shallow depth of field, cinematic drama`
6. **DIRECCIÓN ARTÍSTICA** — película / documental / thriller / drama emocional / misterio

## Texto

- **Nunca pedir al modelo que lo genere.** Generar imagen limpia, texto en edición.
- 3-5 palabras máximo. Abre una pregunta, no resume.
- Bueno: "Sonreía por fuera..." · "No dijo nada..." · "Nadie lo vio..."
- Malo: "Una persona que parecía tener todo bajo control pero estaba sufriendo internamente"

**Posición:** zona superior en Facebook/Reels — el texto abajo compite con la descripción,
los botones y la interfaz de la app.

**Tipografía:** validar fuente disponible, medir tamaño real, comprobar contraste.
Si PIL cae a `load_default` el texto queda a ~11px e ilegible. Medir el ancho en píxeles
y ajustar hasta ~62% del ancho del frame; avisar si baja de 50px de alto.

## Fórmula

**Imagen 80% · Texto 20%.** El texto completa la imagen, no cuenta la historia.

## Variantes obligatorias (mínimo 3)

| | Tipo |
|---|---|
| A | frame adaptado |
| B | nueva composición cinematográfica |
| C | más emocional/humana |

No elegir la más bonita. Elegir: **"¿cuál crea más curiosidad en menos de un segundo?"**

## Formatos

- **4:5** (1080×1350) — feed de Facebook, escritorio y móvil
- **9:16** (1080×1920) — portada de Reel, perfil y Explore

Generar la imagen **una vez** y recortar ambos. Dos generaciones = dos imágenes distintas
= el packaging deja de contar la misma historia en los dos sitios.

## Dos capas de evaluacion (Q5.1)

Separar siempre ambas. Una imagen puede pasar una y fallar la otra.

**Capa 1 — Impacto visual** → ¿detiene el scroll? Evalúa: contraste, composicion, calidad, color, foco.

**Capa 2 — Interpretación narrativa** → ¿la persona entiende la emoción correcta? Evalúa: conflicto, vulnerabilidad, intencion, promesa emocional.

**Regla de bloqueo:** si la imagen comunica A pero el reel cuenta B, Q5.1 falla. No se negocia con la calidad.

## Proceso de validacion en 3 pasos (obligatorio)

| Paso | Pregunta | Respuesta obligatoria |
|---|---|---|
| 1 | Sin conocer el contexto, ¿qué pensaría un usuario? | "Esta imagen parece una historia sobre ______." |
| 2 | ¿Qué historia queremos contar? | "Este reel trata sobre ______." |
| 3 | ¿Son iguales? | Sí → continúa. **No → regenerar.** |

El paso 1 se hace **a ciegas**: no se le dice al evaluador qué quiere el reel. Si se le dice, la
respuesta se ancla al brief y el gate no mide nada.

## Criterio de multiplicacion

**Visual Quality × Narrative Accuracy.** No basta 9/10 visual si la interpretacion narrativa es
incorrecta: el resultado final es fallo. Un 6/10 visual con interpretacion correcta gana a un
9/10 visual con interpretacion equivocada.

## Describir estados humanos, no elementos visuales

Describir solo "cabello oscuro, ojos brillantes, traje, niebla" produce **personajes**.
Describir "alguien que oculta dolor, alguien que aparenta estar bien, alguien que perdio algo,
alguien que intenta resistir" produce **historias humanas**.

| Prompt | Resultado |
|---|---|
| "Dark mysterious anime character, glowing eyes, cinematic lighting." | Personaje interesante |
| "A cinematic portrait of someone who appears strong but is emotionally exhausted, hiding a personal struggle nobody sees." | Historia humana |

## Criterio Q5 (emotion gap)

> ¿El thumbnail crea una emoción incompleta que obliga a descubrir la historia?

- "personaje interesante" → **no pasa**
- "quiero saber qué le ocurrió" → **pasa**

## Q5.1 — Primera interpretación (gate de contradiction)

> ¿Un usuario que nunca vio el reel entiende la emoción correcta en menos de un segundo?

Comparar siempre dos cosas:

| | |
|---|---|
| **Lectura visual inmediata** | ¿qué piensa alguien en 1 segundo? |
| **Promesa narrativa del reel** | ¿qué historia realmente contamos? |

Si no coinciden → regenerar. Ejemplo medido (MILO002):
- Lectura inmediata: "villano / personaje poderoso / misterio"
- Historia real: "persona ocultando dolor mientras parece fuerte"
- → el thumbnail contaba una historia distinta. Corregido con ancla 40 (cabeza baja, ojos rendija, cara negra).

**No aprobar si falla esta comparación**, por muy cinematográfica que sea la imagen.

## Validación final (5 preguntas, en orden)

1. ¿Qué emoción vende la imagen?
2. ¿Qué historia interpreta un desconocido?
3. ¿Coincide con la historia real del reel? ← **si falla, NO APROBAR**
4. ¿Genera una pregunta?
5. ¿Invita a descubrir la respuesta?

## Regla de contradicción emocional

**Superficie** (lo que todos ven) + **Verdad oculta** (lo que queremos descubrir).

- Superficie: "persona seria en oscuridad"
- Verdad: "está sufriendo y nadie lo sabe"

## Dirección de personaje cuando el concepto es emocional

Evitar: mirada desafiante · postura dominante · iluminación de antagonista · composición heroica.
Buscar: hombros bajos · cabeza inclinada · mirada cansada · manos visibles cuando sea posible · espacios vacíos · sensación de aislamiento.

## Plantilla de prompt emocional

```
Create a cinematic thumbnail that communicates a hidden human struggle.
The character should not look powerful or threatening.
The emotion should be:
someone trying to hide pain, emotional exhaustion, silent suffering,
vulnerability behind a strong appearance.
Avoid: villain feeling, aggressive expression, dominant posture.
Prioritize: human connection, curiosity, emotional contradiction.
```

Continuidad: el thumbnail es **105% de calidad visual pero 100% de coherencia emocional**.
No puede ser "thriller oscuro" si el video es "reflexión humana".

## Lección medida (2026-09-28, MILO002)

Con 6 instrucciones explícitas de vulnerabilidad (ojos tenues, hombros caídos, cuerpo
contraído) sobre el ancla de rostro, el modelo devolvió "entidad que observa desde las
sombras", ojos brillantes y corbata al centro. **El ancla pesa más que el texto.** Si la
vulnerabilidad no se consigue con el ancla de rostro, usar un frame donde el personaje ya
salga vulnerable, o **la imagen que entrega el director** — esa fue la corrección que funcionó.

**Error grave que la regla previene:** usar un frame del reel como ancla del thumbnail cuando
el director ya dio la referencia correcta. El beat 4 produjo un hombre con jersey gris y cara
visible; la imagen del director (ancla 40) tenía los ojos rendija, la cara negra y el traje.
**Si el director entrega una imagen, esa es el ancla — no un frame propio.**

## Referencias

- `cinematic-visual-consistency` — mantener el universo entre frames
- `fb-reel-gate` — brief antes de generar
