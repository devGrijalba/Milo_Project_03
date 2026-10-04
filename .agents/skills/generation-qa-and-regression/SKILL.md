---
name: generation-qa-and-regression
description: 'Audit generated images so QA can actually fail.'
version: 1.0.0
author: Hermes Agent
license: MIT
---

# QA de imagen generable y regresion de fallos

Clase de tarea: auditar una imagen generada por un modelo, y convertir cada fallo de
produccion diagnosticado en un test que impida repetirlo.

Aplica a cualquier generador de imagen. No es "mirar si salio bien": es disenar el
QA para que pueda fallar, y no perder una generacion por una ambiguedad que se podia
ver antes de gastar.

## When to Use

- Hay una imagen generada y hay que decidir si pasa o se rechaza.
- Se va a construir el prompt de una escena con dos o mas referencias.
- Un fallo de produccion ya tiene causa medida y hay que evitar repetirlo.
- Antes de generar una escena con varios personajes, planos u objetos en contacto.

## 1. Disena el QA para que pueda FALLAR

Un QA cuyas preguntas estan elegidas para obtener "si" es confirmacion con herramienta.

Medido: una generacion con **2 campanas en vez de 1**, plato desproporcionado e identidad
de personaje perdida paso **7/7** porque las 7 preguntas eran "¿cabeza blanca?", "¿hay
texto?", "¿se ve el plato?" — y la imagen **si** tenia todo eso. Preguntar por presencia
de rasgos sueltos no mide identidad.

- **Antes de mirar, nombra un fallo posible.** "¿Que podria interpretar mal el modelo?"
  Si no sabes nombrar uno, no has hecho QA: empezaste por "¿se ve bien?".
- **Pregunta cerrada por atributo** (si/no, uno a uno), y **por comparacion contra el
  master**, no por descripcion. Si dos lecturas discrepan, la acotada gana.
- **Filtro de lo no pedido:** si tu lectura menciona algo que el brief **no** pidio, es un
  FAIL hasta que se demuestre lo contrario.
- **El filtro de confirmacion es el fallo.** En el caso medido, el mismo analisis escribio
  "hay otro plato tapado junto al padre" sobre un prompt que pedia UN plato, y lo registro
  como caracteristica. El texto que revelaba el fallo estaba ahi y no se eligio como
  veredicto. **Regla: cada frase de tu lectura que describa algo no pedido es la evidencia
  mas valiosa del informe — nunca un detalle.**
- **Un score alto es compatible con ambiguedad mortal.** El scoring que presencea campos
  y penaliza keywords mide escritura, no interpretabilidad. Ningun score compensa un
  hard fail.

## 2. Referencia >1 sin slots asignados es HARD FAIL

`image 1..N` es contrato semantico, no adjunto. Adjuntar no es asignar.

- Sin *Reference Role Assignment* explicito (`Dad is the character from image 1`), el
  generador no sabe que imagen es quien. "preserve identity from references" no lo dice.
- **Slots asignados con la MISMA etiqueta no son asignacion.** `image 1 is the scene
  reference; image 2 is the scene reference` deja al modelo sin distinguir personaje de lugar.
  El check es que ningun par de slots comparta etiqueta.
- **Valida la lista de referencias, no solo los archivos.** Una referencia puede estar
  presente y con hash correcto y aun asi ser la equivocada para el plano: la identidad del
  personaje que queda en cuadro puede faltar mientras el gate que solo comprueba existencia
  da `PASS`. Checks sobre la lista: sin duplicados, con la identidad del focal exactamente
  una vez, y con el secundario distinto del focal.
- **La autoridad entre referencias se escribe en el prompt.** Un canon puede declarar que el
  master de entorno manda sobre arquitectura y el de detalle solo sobre el objeto, y si eso no
  esta en el prompt no protege nada: el modelo no lee el brief. Sin el matiz, una referencia de
  detalle rediseña la habitacion y rompe la continuidad entre encuadres — fallo invisible en
  el artefacto, porque cada imagen sale bien suelta.
- El paquete lleva mapa por slot (`image_N -> asset_id, role, prompt_name`) y el ejecutor
  **no reordena**. Prompt y adjuntos se validan juntos.
- **La imagen gobierna identidad; el texto refuerza atributos criticos.**
- El **escenario tambien tiene identidad**: un master de lugar no significa "una cocina",
  significa que ese espacio es el canonico.
- **Declara la cardinalidad de todo objeto narrativo unico** ("exactly ONE"): pedir la
  accion *y* la presencia del objeto deja la cardinalidad abierta, y el modelo genera dos.
- **Separa BODY SCALE de PERSPECTIVE SCALE.** "character small" se lee como cuerpo mas
  pequeno. **Visual prominence != physical gigantism**: "large in foreground" produce un
  objeto gigante; di tamanho normal + posicion + % de frame.
- Estilo: **una frase** de refuerzo, no seis tokens (las referencias ya lo llevan). Y un
  nombre de universo ("Milo universe") **no es instruccion de control**.

## 3. Decide el MODO de generacion antes del prompt

Puntua la complejidad de la escena **antes** de escribir. Si sale ALTA, el motor devuelve
`DECOMPOSE_SCENE`, no `READY_FOR_PROMPT`.

| Modo | Cuando | Quien compone |
|---|---|---|
| `FULL_SCENE` | 1 personaje, interaccion baja | el generador |
| `DECOMPOSED_SHOTS` | 2+ personajes, planos, contactos | shots simples + montaje |
| `COMPOSITE` | continuidad de escenario prioritaria | parcial + composicion en script |
| `EDIT` | el candidato ya esta casi bien | Edit con PRESERVE+CHANGE |

Factores de riesgo: n de personajes (1 bajo / 2 medio / 3+ alto), planos de profundidad
con sujetos criticos, **contacto fisico** (la cadena mano↔asa↔objeto↔superficie es la zona
mas visible), escenario canonico, objeto focal, dependencia de perspectiva, y el contraste
de densidad visual entre personaje simple y entorno detallado — eso obliga al modelo a
elegir cual simplificar y suele cambiar los dos.

- Estilo **por referencia**, no global: "preserve the design language of the supplied
  character reference; preserve the environment identity of the supplied environment
  reference". Pedir "transforma todo en watercolor" invita a reinterpretar ambas.
- T1 identidad/personajes/escenario/accion/cantidad/anatomia · T2 composicion · T3
  atmosfera · T4 editorial. **Si T4 sube el riesgo de T1, eliminalo.**
- **No obligues al generador a resolver en un frame lo que el editor cuenta mejor en
  tres.** Simplificar la generacion suele mejorar el video: revelacion progresiva por corte
  retiene mas que un frame que lo cuenta todo.

## 4. Un fallo diagnosticado es un test de regresion

Un fallo de produccion con causa medida deja de ser desperdicio.

- Guarda artefacto original, prompt, **reference map de lo que debia declararse**, image,
  analisis y `lessons.json`.
- **El test tiene contraprueba**: si el prompt corregido tampoco lo supera, no distingues
  "correcto" de "roto". Un gate que rechaza todo tambien "pasa".
- **Regla no evaluable ⇒ FAIL, no `ok`.** "sin brief: no evaluable" es indistinguible de
  cumplida desde fuera.
- **Preserva el input fallido con nombre explicito** (`*_ORIGINAL_failed.json`) y el
  corregido aparte (`*_v02_candidate.json`). Sobrescribir el brief que produjo el fallo
  destruye la evidencia.
- El prompt corregido es un **CANDIDATO**, no una verdad: su primer experimento cambia UNA
  variable (el prompt) y se registra como tal.

## 5. Qué NO afirmar

- No afirmes que el generador "es malo": no hay evidencia suficiente.
- No afirmes que el prompt corregido "es el bueno".
- Lo que si se demuestra es acotado: **el prompt usado contenia ambiguedades capaces de
  explicar por si mismas una parte importante de los fallos observados.**

## Referencias

- `references/image-qa-regression-recipe.md` — recipe con script worked y tabla de
  ambiguedades que peor pagan.

Skills relacionadas: `generation-pipeline-control` (verificacion de artefacto y reintentos
que cambian algo), `generation-canon-gates` (gate antes de gastar cuota), `flow-image-generation`
(QA de prompt e imagen en Flow), `media-asset-intake` (registro y medicion de assets).