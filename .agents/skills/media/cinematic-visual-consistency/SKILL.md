---
name: cinematic-visual-consistency
description: "Use to keep all reel frames in one visual universe."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Cinematic Visual Consistency Engine

## Principio

> **No generes imágenes individuales. Genera fotogramas de una película que no existe.**

Todas las imágenes del reel deben parecer fotogramas de la misma producción. No debe existir
diferencia entre el thumbnail y los beats. El espectador debe sentir "esto pertenece al mismo mundo".

**El error típico:** thumbnail a nivel película + frames internos a nivel ilustración IA genérica.
Se siente como collage. Y el thumbnail **no debe tener mejor calidad que el video** — igual o
ligeramente superior (105% vs 100%), nunca 100% vs 70%.

## MASTER STYLE BLOCK — antes de generar el primer frame

Este bloque se copia **idéntico** en todos los prompts. No cambia.

```
MASTER VISUAL STYLE:
Premium cinematic anime drama.
Dark blue cold color palette.
High contrast low-key lighting.
Realistic cinematic rendering.
Film grain.
Volumetric fog.
Shallow depth of field.
Soft rim lighting.
Emotional storytelling.
Ultra detailed hair strands.
Realistic fabric texture.
Movie frame quality.
```

## CHARACTER CONSISTENCY BLOCK — también fijo

```
CHARACTER CONSISTENCY:
Same character:
same hairstyle, same facial structure, same proportions,
same dark formal suit, white shirt, dark tie,
same emotional register.
```

## BLOQUE CINEMATOGRÁFICO FIJO

**Cámara** (no variar al azar): `cinematic lens, 35mm film look, shallow depth of field, anamorphic composition`
**Color**: `dark teal and blue cinematic grading, cold shadows, soft highlights`
**Luz**: `dramatic side lighting, rim light, deep shadows, soft atmospheric haze`

**Calidad** — nunca "beautiful image". Usar:
`cinematic movie frame, high-end production quality, film still, professional cinematography, realistic textures, premium visual storytelling`

## Dos capas por frame

- **Capa fija:** la identidad visual (master + character + cine)
- **Capa variable:** la historia del beat

El MASTER no se toca. Solo la capa variable cambia por beat.

## Control de continuidad antes de aprobar

| Check | Pregunta |
|---|---|
| Personaje | ¿Es la misma persona? |
| Mundo | ¿Parece la misma película? |
| Luz | ¿Mantiene la misma atmósfera? |
| Color | ¿Mantiene la misma paleta? |
| Calidad | ¿Tiene el mismo nivel cinematográfico? |

## Q7 — Visual Consistency (gate)

> ¿Todos los frames parecen pertenecer a la misma película?

Si **NO** → volver a generación. No es un matiz estético: es la diferencia entre una
producción y un collage.

## Emotional Bible — se crea junto a la Visual Bible

La Visual Bible dice **cómo se ve**. La Emotional Bible dice **qué duele**. Las dos son
obligatorias antes de generar el primer frame.

| | Contenido |
|---|---|
| **Visual Bible** | colores, camara, iluminacion, lente, estilo, master block |
| **Emotional Bible** | que dolor representa, que contradiccion existe, que debe sentir el espectador |

Ejemplo (MILO002):
- Dolor: "estar bien por fuera mientras por dentro se lucha"
- Contradiccion: "sonrie / esta roto"
- Debe sentir: "yo conozco esa sensacion" — no "mira que personaje tan inquietante"

## Jerarquia de prompts: empezar por el Nivel 1

| Nivel | Pregunta | Ejemplos |
|---|---|---|
| **1 — Estado humano** | ¿Que siente? | culpa, perdida, soledad, esperanza, cansancio, miedo |
| **2 — Accion narrativa** | ¿Que esta ocurriendo? | ignora una llamada, mira una foto, espera una respuesta |
| **3 — Elementos visuales** | ¿Como se ve? | cabello, ropa, color, ambiente |

**La mayoria de IA empieza por el Nivel 3.** Describe "cabello negro, ojos brillantes, traje,
niebla, iluminacion cinematografica" y produce **personajes**. Empezar por el Nivel 1 produce
**historias**.

Prompt debil → Personaje:
```
Dark character, black hair, glowing eyes, blue lighting, cinematic atmosphere.
```

Prompt correcto → Historia:
```
A person who appears strong but is emotionally exhausted, someone hiding internal pain,
trying to maintain a normal expression while struggling privately.
```

## Test antes de aprobar cada frame

> **"Si elimino el texto, ¿la imagen todavia cuenta la emocion?"**

Si no: la imagen depende demasiado del copy, y el copy tiene que arreglarlo. Eso es un frame
de escaleras, no un frame de pelicula.

## No generar "escenas". Generar "momentos humanos"

El telefono con **MISSED CALL — MAMÁ** funciona porque no es un objeto: es ausencia, culpa,
distancia y una relacion importante. Eso es un estado humano. Un cubo de datos flotando es un
elemento visual: no dice nada por si solo.

## Regla de multiplicacion (aplica a todos los frames)

**Efectividad = Calidad Visual × Precisión Narrativa.** No es una suma.

10/10 visual + 3/10 narrativa = **fallo**.
7/10 visual + 10/10 narrativa = **funciona mejor**.

## La acción narrativa tiene tres partes

Una acción que cuenta historia no es "un hombre triste sentado en una habitación oscura".
Debe contener:

1. **Una decisión** — algo que elige (guardar el teléfono, no devolver la llamada, limpiarse la lágrima antes de entrar)
2. **Una relación** — alguien que importa (su madre, la persona que ama, quien lo espera)
3. **Una consecuencia emocional** — lo que cuesta esa decisión

| ❌ Débil | ✅ Fuerte |
|---|---|
| "mujer llorando mirando la ventana" | "mujer limpia una lágrima antes de entrar a la habitación donde todos creen que está bien" |
| "hombre triste sentado en una habitación oscura" | "hombre guarda el teléfono después de ver una llamada perdida de su madre y decide no devolverla" |

Ejemplo completo (el "antes" produce un hombre genérico, el "después" ya tiene historia):

- ❌ "Hombre de 40 años con traje elegante, cabello oscuro, oficina moderna, iluminación cinematográfica."
- ✅ "Un hombre de 40 años que acaba de recibir una noticia que no puede contarle a nadie. Sonríe durante una reunión mientras oculta la pantalla del teléfono donde aparece un mensaje de alguien importante. Lleva traje elegante, oficina moderna, luz fría de mañana, plano cercano cinematográfico mostrando la tensión en sus manos."

## Fórmula de prompt narrativo

**Estado emocional + Acción significativa + Relación + Contexto visual + Cámara**

Prioridad: 1 ¿qué siente? → 2 ¿qué hace que demuestra eso? → 3 ¿cómo lo vemos? — **nunca al revés**.

## La regla que resume todo

> **Una imagen no debe explicar una emoción. Debe contener una situación donde la emoción sea inevitable.**

Aplica a reels emocionales, documentales, historias de superación: ahí la retención
viene de la identificación, no de la estética.

## Emotional Bible v2 — cinco campos

No basta dolor/contradiccion/sensacion. La Emotional Bible tiene cinco:

| Campo | Pregunta | MILO002 |
|---|---|---|
| **Herida** | ¿que esta sufriendo? | la presion de aparentar estar bien mientras pierde la batalla |
| **Mascara** | ¿que muestra al mundo? | sonrisa, normalidad, traje impecable |
| **Necesidad** | ¿que realmente necesita? | dejar de sostener la mascara |
| **Decision critica** | ¿que hace cuando nadie mira? | guarda el telefono en vez de devolver la llamada |
| **Precio emocional** | ¿que pierde por esa decision? | su madre sigue esperando |

Los cinco campos son la entrada del prompt. La mascara es lo que el mundo ve; la decision
critica es lo que la imagen tiene que hacer visible.

## Aprobacion: 3 preguntas antes de aceptar un frame

| Pregunta | Si no |
|---|---|
| 1. ¿Existe una **decision**? | parece una foto |
| 2. ¿Existe una **relacion**? | no hay conexion emocional |
| 3. ¿Existe una **consecuencia**? | no hay tension narrativa |

Las tres, o el frame no se aprueba.

## La formula final de prompt narrativo

**Estado emocional + Acción con decisión + Relación + Consecuencia implícita + Contexto visual + Cámara**

El contexto visual y la cámara van **al final**, nunca al principio. Escribirlos primero es lo
que produce "un hombre generico".

Prompt debil → una persona triste:
> Hombre mayor triste sentado en una habitacion oscura, cinematografico.

Prompt narrativo → la imagen cuenta algo sin texto:
> Hombre mayor que intenta mantener la fortaleza despues de perder a alguien importante. Esta
> sentado en la cocina antes del amanecer, sostiene un telefono con una llamada perdida de su
> hija y decide no devolverla porque no quiere preocuparla. La taza de cafe permanece intacta
> frente a el mientras mira la pantalla apagada. Luz natural fria entrando por la ventana, plano
> cercano de sus manos y expresion contenida, estilo documental cinematografico.

Detalle que hace el trabajo: **la taza intacta** y **la pantalla apagada**. No son decoracion —
son la consecuencia hecha objeto. El mismo mecanismo que hizo funcionar el beat 4: el modelo
subio "una llamada perdida" a "tres llamadas, de la madre, 22:14, declined" sin que se le pidiera.

## Lección medida (2026-09-28, MILO002)

La consistencia se rompió por una causa concreta: los sets (`15_Escritorio_Set_Lluvia`,
`19_Habitacion_Panoramica_Lluvia`) son **realistas pintados** y el personaje es
**cel-shaded**. Sin la regla híbrida explícita, esa mezcla produce dos estilos en el mismo
frame. La regla que funciona:

```
Preserve Milo's original stylized cel-shaded character design while integrating him into
the cinematic environment naturally. Do not merge the character into photorealism.
Do not make the environment anime. Maintain a deliberate hybrid cinematic style.
```

**No usar** `Do not change the anime cel-shaded illustration style` — le dice a Meta "todo anime"
y aplana los sets realistas.

## Referencias

- `references/milo002-calibration.md` — **paquete consolidado, leer primero**: los 7 pasos, Emotional Bible completa, test de 4 preguntas
- `cinematic-thumbnail` — la portada hereda este mismo estándar
- `meta-ai-worker/references/milo-prompt-rules.md` — bloques exactos que funcionaron
