# Gate de encargo: delegar con un artefacto, no con una instrucción

Una regla sobre delegación escrita en un `.md` no es una regla: no se ejecuta. La forma que sí
se impone es un **artefacto obligatorio** más un **gate que falla si falta** — igual que el
manifiesto es el input del gate de generación, el encargo es el input del gate de delegación.

## El fallo que motivó esto

Un padre declaró `task_type: classify` con un proxy de 300 px para una pregunta de OCR. El gate lo
aceptó porque el tamaño del proxy **sí** correspondía a `classify`. Lo que no correspondía era la
**intención de la pregunta**.

El hijo recibió una tarea imposible y, sin salida honesta, gastó 6 llamadas de visión y 2 timeouts
de 120 s adjudicando dos lecturas de un texto que no se leía. Escribió 0 archivos.

La cadena falló completa: el padre declaró mal, el gate no lo detectó, el hijo intentó cumplir.
**El hijo no falló — el encargo no le dio opción de triunfar.**

## Los checks que faltan en un gate de solo-forma

Un gate que valida tamaño contra tipo tiene el inverso sin cubrir:

| Check | Atrapa |
|---|---|
| proxy **no menor** que lo que el tipo necesita | tipo `ocr` con proxy de 300 px |
| proxy **no mayor** que lo que el tipo necesita | `classify` con proxy de 900 px = OCR disfrazado |
| `expected_answer_kind` obligatorio | el padre nunca declara qué respuesta espera |
| `max_calls` obligatorio (por defecto 3, tope 10) | reintentos hasta agotar el timeout del padre |
| `ilegible` como respuesta **válida** | el hijo no tiene salida honesta y adivina |

Los dos últimos son los que rompen la espiral. Un gate que solo acepta una lectura correcta
**fuerza al hijo a inventar**.

## Límite que hay que declarar, no esconder

El gate valida **forma**, no **intención**. No puede saber que el padre declaró el tipo
honestamente. Un padre que declara `text` con un proxy de 300 px sigue pasando los checks.

Lo que sí cambia el resultado: `ilegible` pasa a ser una salida declarada y válida, y el reintento
infinito queda limitado por un presupuesto visible.

Igual que `verified` en V1.0: el gate no puede verificar que alguien mire.

## Proxy: el tamaño decide primero; la herramienta depende del tamaño del texto

Medido sobre texto **grande** (un letrero quemado) — un solo caso:

| | proxy | llamadas | resultado |
|---|---|---|---|
| OCR a 300 px | 41 KB | 6, con 2 timeouts | 0 archivos, 510 s |
| OCR a 900 px | 412 KB | 0 | transcripción correcta, 18 s |

Ahí el hijo leyó la imagen **adjunta**, sin `vision_analyze`.

Pero eso **no generaliza**, y se comprobó con un caso más: mismo tipo de encargo y mismo proxy de
900 px, sobre **lomos de libros** (texto pequeño), consumed **2 llamadas** de `vision_analyze`
para recortes, con el presupuesto justo agotado y la lectura correcta. La variable no era el motor
ni el tamaño del proxy: era **el tamaño del texto**.

| texto | proxy 900 px | llamadas | resultado |
|---|---|---|---|
| grande (letrero) | 412 KB | 0 | correcto, barato |
| pequeño (lomos) | 412 KB | 2 | correcto, presupuesto justo |

**Regla:** el padre recorta con `ffmpeg` cuando el texto es pequeño. Dejar que el hijo descubra
que el texto es pequeño consumiendo su presupuesto cuesta más que el recorte. Pasa el proxy como
imagen adjunta **y** declara si el texto es grande o pequeño, para que el hijo sepa si esperar a
leerlo nativo o recortar.

Con `ocr` a 300 px el resultado sigue siendo fracaso en ambos casos de texto: el proxy pequeño es
el problema cuando el detalle no cabe, y ninguna herramienta lo arregla.

## El camino correcto debe ser el fácil

Un helper que genera proxy al tamaño correcto, calcula hashes y emite el encargo completo reduce
la fricción hasta que delegar bien cuesta menos que delegar mal. Si no existe, el gate se
incumple por omisión: nadie lo salta, simplemente nadie lo usa.

Es la misma lección del validador de composición: correcto y sin uso es código muerto con
apariencia de protección.

## Other limits worth declaring in the artifact

- El padre puede saltarse la herramienta: el gate hace el bypass **visible** en la bitácora, no lo
  bloquea.
- El hijo tiene terminal propia: `forbidden: outside_project_read` es instrucción, no sandbox. El
  check impide que el **padre** apunte fuera; no impide que el hijo lea fuera por su cuenta.
- Jerarquía de un nivel: el hijo no puede delegar.

## Casos de regresión que hay que guardar

Guarda el encargo fallido como caso, con su expectativa (`FAIL`) y el motivo. Sin eso, en tres
semanas alguien reconstruye el gate sin el check y el fallo vuelve.

El ancla más útil: *el tamaño del texto, no el tamaño del proxy, decide si hace falta
`vision_analyze`*. Rotula el mecanismo, no el incidente.

## Ningún ancla se escribe desde un solo caso

Este archivo es la prueba de su propia regla. El ancla anterior —*el hijo leyó la imagen adjunta
sin `vision_analyze`*— salió de **una** medición, se escribió en la bitácora del proyecto **y en
este reference como si fuera la regla**, y un caso posterior la refutó. Pasó un rato hasta que
alguien lo detectó comparando datos, no leyendo la afirmación.

**Regla:** toda afirmación con forma de regla declara **en cuántos casos se basa**. Con n=1 se
escribe como hipótesis, con su condicional —*funciona cuando el texto es grande*—, nunca como
regla general. Y cuando el caso que la refuta llegue, **corrige la frase que engañó**: no
añadas un «UPDATE» debajo. Un ancla sin número de casos se lee como ley dentro de tres meses.

Corolario útil: «0 llamadas» y «2 llamadas» con el mismo encargo es **información, no ruido**.
Significa que hay una variable sin medir. La pregunta que sirve no es «cuánto costó» sino «qué
caso lo hace barato».
