---
name: generation-canon-gates
description: "Use when a data lock feeds a prompt builder."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# Canon de generación y gates

Clase de tarea: un **lock estructurado** (JSON) alimenta un **mapper** que compone el prompt
de una generación, y hay que mantener la traducción lock → prompt fiel, con gates que bloqueen
**antes de gastar cuota**.

Aplica a cualquier pipeline de assembly de texto a partir de datos: imagen, vídeo, locución con
shot list. No es "redactar un prompt": es que lo que el código lee de verdad y lo que el modelo
recibe digan lo mismo.

## Orden de trabajo

Este orden es la regla. Invertirlo produce datos corregidos a ciegas.

```
1. Gate primero (que NO se pueda saltar)
2. Detector probado contra casos conocidos (matriz)
3. Solo entonces, el canon
```

Corregir el canon mientras el detector puede dar falsos positivos es **cambiar el destino para
que el mapa parezca bien**: si el gate marca como malo algo correcto, el ajuste del canon no
persigue el defecto real, lo esconde.

1. **Abre el lock y el resolver.** Localiza qué campo lee el código de verdad — no el que parece
   obvio por el nombre. Ver `references/lock-field-provenance.md`.
2. **Cuenta el presupuesto antes de escribir el texto.** Partes fijas primero, espacio para lo
   variable después. Ver `references/prompt-composition-budget.md`.
3. **Declara el contrato de cada asset** (propósito + atributos permitidos/prohibidos) y valídalo
   contra lo **medido**, no contra el nombre. Ver `references/attribute-contracts.md`.
4. **Prueba el gate con casos conocidos** antes de confiar en él: al menos un fallo real, un caso
   que debe pasar, y el caso límite. Ver `references/contradiction-detection.md`.
5. **Conecta el gate al generador como proceso aparte.** Ver abajo.
6. **Mide sobre todos los encuadres disponibles**, no solo sobre el que vas a usar.
7. **Clasifica por evidencia.** `not_evaluable` es un resultado de primera clase.

## La cadena de verificacion se EJECUTA antes de presentar

Un artefacto se presenta **despues** de correr toda la cadena de consumidores que lo
tocaran. Cada eslabon por debajo existe, es determinista y es gratis: lo caro es
presentar y luego descubrir que el consumidor final no podia usar el output.

```
1. validador de forma (campos, rangos, oraciones)      gratis
2. los objetos que pide existen en el lock              gratis
3. EL BUILDER DE PROMPTS con la escena real            gratis
4. el motor que consumira el artefacto lo genera       gratis
5. ffprobe sobre el audio real, si hay duracion        0 o cuota de voz
6. gate del compositor final (ritmo, hook, ratio)      gratis
```

**El paso 3 es el que se salta y el que mas cuesta.** Un guion puede pasar el
validador, tener cada objeto en el lock, y aun asi ser **inproducible**: el
builder tiene una tabla de anclas y devuelve `INCOMPATIBLE` para lo que no
conoce. La validacion de forma y la de produccion son capas distintas, y pasar
la primera no dice nada de la segunda.

Regla de umbral: **si un paso falla, no se presenta** — se corrige y se repite
desde ese paso. Una presentacion sin cadena verificada es una hipotesis, no un
artefacto.

El sesgo que produce el salto: los pasos que ya corrieron **PASAN**, y "no fallo
lo que probe" se lee como "no hay mas que probe". La cadena no se termina cuando
algo pasa, se termina cuando todos los consumidores han dicho que pueden.

**Costo de saltarla:** un guion aprobado y un plan visual aprobado que nadie paso
por el compositor. El plan era narrativamente correcto (6 escenas, una por beat,
funcion editorial por entorno) y **invalido como edicion** — con 38 s de audio,
6 planos son 6,3 s cada uno y el gate de ritmo (ningun corte > 3 s) exige
`ceil(audio_s / 3.0)` = 13. El plan narrativo y el plan de cortes son dos
artefactos distintos; el motor produce el primero y el compositor necesita el
segundo.

Los cortes son de **edicion**, no de generacion: si varios cortes comparten
imagen, las imagenes de produccion siguen siendo las mismas. Reparte por peso de
cada beat en palabras, divide entre los cortes de ese beat, y pasa el gate real
antes de pedir autorizacion de generacion — la prueba cuesta cero cuota.

## Vision: pregunta por el rasgo que define la identidad, no por el cuerpo entero

Una lectura abierta de un frame devuelve el cuerpo (vestuario, postura) y con eso se
concluye mal sobre un personaje cuya identidad esta en una parte concreta. Medido: un
frame de un personaje de esfera lisa dio "hombre con traje y corbata, piel oscura" en
la primera lectura; la segunda, con la pregunta acotada **solo al rasgo definitorio**
(preguntas si/no: pelo, piel, nariz, boca, barbilla), confirmo la identidad correcta.

**Regla:** para verificar identidad con vision, no preguntes "¿quien es?". Pregunta por
rasgos, uno a uno, con respuesta si/no, y compara el rasgo definitorio contra su ancla. Si dos
lecturas discrepan, **la acotada gana**: la pregunta abierta invita a describir, la acotada exige
comprobar. Un frame que "se ve bien" no es un gate; el luma medido por `ffmpeg` sobre la banda de
texto contra el control sin texto, si.

## Una rama de check inalcanzable no la detecta la prueba de mutacion

La prueba de mutacion por check (un artefacto alterado por check, cada uno cae
en su etiqueta) verifica que un check **pueda** fallar. No verifica que pueda
fallar sobre **cada rama**.

Un gate con dos ramas —comparar contra un dato medido, o contra un rango
declarado— tiene la rama medida muerta si la etapa que produce el dato corre
**despues** del gate en el pipeline. Medido: plan de 30,50 s contra audio real de
11,84 s, **desvio de 158 % con PASS**. El codigo cumple la regla del SPEC
("audio medido manda"); el **orden** del pipeline la hace inalcanzable. El check
dispara, cae en la etiqueta correcta, sobre la clase de input equivocada.

Audita alcanzabilidad por rama: para cada rama, nombrar la etapa que le entrega
el input, y si esa etapa corre despues, la rama no existe en el flujo. Es
distinto del eclipse (un check tapa a otro) — aqui no hay dos checks, hay uno bien
escrito que nadie puede ejecutar.

## Un valor de config no es una politica del servicio

Antes de reportar un limite como si lo impusiera el servicio externo, trazalo
hasta su unico lector: quien lo escribe, quien lo lee, que lo arma, y si algo
alguna vez lo disparo.

Medido: un `cooldownMinutes: 60` en el config del proyecto. Solo lo leian dos
modulos del guard, y solo se armaba desde un estado de error concreto
(`UNUSUAL_ACTIVITY`); el ritmo entre generaciones venia de otro campo, puesto a
`null` a proposito. La evidencia de 14 ejecuciones reales mostraba mediana de
12,9 min entre envios, **cero intervalos entre 55 y 65 min**, y cuatro envios
consecutivos con 0,0 min de separacion.

El error no fue leer mal el numero: fue **reportar un tope declarado como si fuera
un ritmo observado**, y usar esa cifra para justificar una decision de coste. Si
el dato no tiene registro de por cuando se disparo, es un techo para un estado
de error, no una espera entre operaciones. No se anota como deuda ni se planifica
sobre el hasta tener la respuesta.

## Reglas permanentes

- **`asset_name ≠ asset_truth`.** Un asset se registra por lo que se midió que contiene. Un
  archivo llamado "torso" que es un cuerpo entero con la cara dentro es la causa clásica de
  contaminación de identidad: el modelo mezcla la referencia que no debía y devuelve un rostro
  ajeno. El nombre del archivo no es evidencia.
- **Nunca reescribas una validación para poder importarla: extráela verbatim.** Al mover lógica a
  una función importable, copiarla "corriéndola" produce una segunda implementación con nombres de
  campo distintos que divergen en silencio y devuelve veredictos falsos. Mueve el código; la capa
  de presentación es lo único que se escribe de nuevo.
- **Un gate que siempre falla acaba siendo ignorado, y eso es peor que no tenerlo.** Distingue
  tres estados: `PASS`, `FAIL` (medido y presente) y `NO MEDIDO` (ausencia de evidencia). Solo
  `FAIL` bloquea. `NO MEDIDO` avisa con el recuento a la vista. Un campo de evidencia ausente es
  distinto de un rasgo no medible: ausente **bloquea**, porque no hay contra qué comparar y
  aprobar por omisión hace decorativa la comprobación.
- **El gate corre como proceso aparte (`spawnSync`), no importado.** Si se importa, una excepción
  al cargar el módulo se cuela como "el gate no dijo nada, continúo". Y si el gate falla, se
  aborta: no debe existir ruta por la que una generación llegue al servicio sin pasar los puntos.
- **Antes de preguntar por un rasgo, localiza la zona.** Un recorte mal situado da falso
  negativo con total confianza, y eso es peor que una respuesta incierta porque elimina el motivo
  para volver a mirar.
- **Recortar y reescalar destruye texto pequeño.** Para leer algo, usa el frame completo a alta
  resolución; el recorte conserva píxeles pero cada reescalado posterior vuelve a promediar los
  glifos. Recorta para aislar rasgos grandes, no para leer.
- **`not_evaluable` honesto vale más que un `PASS` inventado.** Si la resolución no resuelve el
  rasgo, dilo y nombra el límite. No declares PASS por defecto ni FAIL por ausencia de lectura:
  son afirmaciones que la evidencia no sostiene.
- **Partir un check que mezcla medir y declarar.** Un solo check que dice "paleta nocturna y sin
  texto" es dos mitades de especies distintas, y suele acabar siendo solo declarativo — o sea,
  un gate que dice verificar algo que no verifica. Sepáralos: la mitad medible **se mide** (una
  luma por frame con ffmpeg, sin visión), la que exige mirar la imagen **se declara** y su OK
  lleva escrito que no es un OK de medición. En el informe y en el veredicto, separa lo medido de
  lo declarado; un `midio: [...]` / `declaro: [...]` explícito evita que alguien lea un OK como
  evidencia.
- **Un umbral que no has medido no es un umbral: es una opinión con comparador.** Calibra los
  topes contra casos reales de tu propio material y el caso negativo que debe caer. Medido:
  producción 18–27 de luma contra un fixture de día en 191 —separación de 10×— deja el tope en 60
  sin ambigüedad. Puesto a ojo, el mismo número no significa nada y no se puede defender. Y
  **mide el peor elemento, no el promedio**: cuatro piezas nocturnas y una de día son una pieza
  de día.
- **Un gate necesita un fixture del caso contrario.** Sin una imagen de día contra la que
  comparar, "se midió la paleta" no distingue nada. Genera el fixture sintético (`color=c=…`) y
  mételo en la matriz negativa.
- **Mide el alcance del fallo antes de decidir el arreglo.** Un dry run que falla por palabras y
  otro que falla por contradicción de manifiesto son deuda de catálogo distinta; mezclarlas
  convierte una tarea de datos en una espiral de código.
- **La elipsis es puente, no frontera.** Un regex que busca la estructura narrativa tipica
  (`no es X, es Y`) usando `[^.!?…]{0,80}?` como puente tiene la elipsis en la clase **excluida**,
  asi que no puede cerrarse sobre el patron mas comun de esa estructura: el texto que si lleva el
  giro marca FALLA. Cuando la elipsis significa pausa dramatica —que es exactamente su funcion—
  DJ excluyela del juego de caracteres. Y valida el detector contra el texto real que se sabe que
  tiene la estructura, no contra un caso sintetico sin puntuacion.
- **Revisa a mano los textos largos tras escribir JSON.** El espanol tecleado a mano, una letra
  latina o un glifo de otro idioma se cuela sin que el parser proteste: `excusas` por `excusa`,
  `giro rapidoScore`, y una palabra china donde iba `el detalle`. Un gate de encoding detecta
  mojibake, no una palabra casi correcta que se lee bien. Pasa un detector de caracteres fuera del
  rango latino sobre los campos de prosa de todo JSON nuevo antes de darlo por bueno.

## Un analisis externo se acepta con evidencia, no con cortesia

Una auditoria, un informe o un documento de arquitectura llega como afirmacion. Su trabajo
es **verificar las afirmaciones medibles antes de aceptarlas**, y|reportar cual caia. Medido
en una sesion de piloto: de cuatro cifras de un informe externo, **una era correcta, dos
eran falsas como regla general, y una no era medible con el insumo disponible**.

- **Comprueba cada numero, no el conjunto.** Una afirmacion que sobrevive es credito para
  es credito para las demas solo si se verificó una por una. Saludo lo que se confirma, corrige lo
    que cae, y nombra lo que no se puede comprobar **sin inventar**: "no es medible con este metadata"
    es una respuesta distinta de "es falso", y ambas se dicen de forma distinta.
  - **Un ritmo ajeno no se corrige, se evita.** Si una metrica documental te pide repetir y el motor
    no puede, la metrica esta describiendo a alguien mas. No "compensa" con relleno ni se relaja el
    guion para perseguirla: se registra la desviacion y se sigue. Ver
    `references/foreign-benchmark-metrics.md` para el procedimiento completo: recalcular la metrica
    que el dataset no publico, verificar si el material contiene la voz que las metricas asumen, y
    separar lo que entra como canonicamente de lo que solo informa.
  - **Separa lo que el dato SOSTIENE de lo que el dato SUGIERE.** Una proporcion de un
  subconjunto no describe el conjunto: un canal de 400 piezas tiene mas ocasiones de
  tener un viral que uno de 10, y un tema que aparece en 2 de 13 canales no es el tema
  del nicho. Cuando el genero de un documento contradicts el dato, el genero es lo que
  se corrige.
- **Una mediana no es una distribucion.** Si un informe afirma un rango ("23-33
  segundos") a partir de una mediana que cae dentro, comprueba que proporcion del corpus
  esta realmente ahi. Medido: la mediana era 30,7 s pero solo el 22,9 % de las piezas
  caian en el rango afirmado, y el p10 real estaba en 12,2 s. El rango correcto salia
  de las piezas que **funcionaron**, no del promedio de todas.
- **Un documento que propone construir algo ya existente: dilo y nombra donde esta.** La
  conclusion frecuente ("hay que crear una base de datos de transcripciones") es
  informacion sobre el estado real: se cruza el directorio y la cobertura esta al 93,5 %.
  Verificar el inventario ANTES de proponer construccion evita un duplicado entero, y
  la verificacion es gratuita.
- **Cuando una afirmacion propia resultare falsa, corrigela en el sitio y nombra el
  error.** No anexes una nota "en realidad..." debajo: edita la frase que engaño y deja
  la correccion visible en el registro de commits.

## Un umbral que no separa, no es un umbral

Antes de adoptar una cifra como criterio, exige que **distinga** lo que debe de lo que
no debe. Medido: se propuso una ventana de medicion de 0,5 s para una segunda metrica
y, al medirla, la linea base estatica dio **mas** que la pieza cinematica — la ventana
ya cruzaba cortes. El umbral no fallaba en los casos que importan: fallaba en el
contraste.

Antes de fijar cualquier numero de corte:

1. Mide la poblacion real (el peor caso legitimo) y el contraejemplo (lo que debe caer).
2. Coloca el umbral **entre** los dos, no donde parezca Round.
3. Guarda **los dos medidos** junto al umbral, para que el siguiente lector pueda
   re-derivarlo sin repetir el trabajo.
4. Si la cifra propuesta no separa, **cambiala y explica por que** — no la llames
   "mas completa" ni la aceptes por defecto. Una metrica que no discrimina es un numero.

## Una herramienta hermana que ignora el mismo flag es un fallo de clase

Corregir "la herramienta ignora `--manifest`" **no cierra el bug**: el mismo error de cableado
esta copiado en el directorio hermano. Busca el flag en todos los scripts y comprueba que cada
uno lo parsea. Los tres fallos que vienen siempre juntos — flag ignorado, default hardcodeado y
artefacto de salida compartido — y las tres defences (fail closed, comparar lo pedido contra lo
leido, nombrar la salida por entrada) estan en `references/sibling-tool-audit.md`.

## Un contrato para direccion separa MEDIDO de DECIDIDO

Cuando el trabajo acaba en un documento que otra persona va a discutir en una
reunion, la tabla mas util del documento no es la de reglas: es la que dice que
afirmacion es hallazgo medido y cual es decision de mercado. Sin esa separacion
se discute lo que no se puede discutir y se filtra como criterio lo que alguien
eligio.

Ver `references/director-contract-delivery.md` para el procedimiento completo y
el ejemplo de verificacion de cifras contra la fuente.

## Nunca asustes donde vive un campo

Nunca asumas dónde vive un campo. Antes de escribirlo, **grep el resolver**:

```bash
grep -rn "prompt_en\|framing_prompt_en\|light_en" src/flow/
```

Si el campo que inventaste no aparece en el `require`, el edit se acepta y **no hace nada** — un
cambio silencioso que parece un arreglo. Y si el tipo no coincide (el resolver exige array y
escribes string), falla con un error de manifiesto que habla de estructura y no del campo.

Costó tres iteraciones en una sesión: un campo con nombre inventado, un array escrito como
string, y un override puesto en el nivel equivocado del árbol.

Ver `references/lock-field-provenance.md` para el procedimiento y el patrón de override por
encuadre.

## Matriz de prueba de un detector

Un gate no se prueba por lo que dice sobre el estado actual, sino por lo que detecta ante casos
conocidos. La matriz mínima:

| Tipo de caso | Para qué |
|---|---|
| el fallo real que existía | demuestra que detecta |
| un caso legítimo equivalente | demuestra que no marca de más |
| el caso límite | demuestra el criterio del margen |

Escribe la **expectativa** de cada caso antes de ejecutar. Si un caso falla, verifica si falla el
detector o el caso: un caso mal escrito se corrige, un detector mal escrito se corrige, y
confundir los dos hace que "arregles" el detector para que pase una expectativa equivocada.

## Reglas de compresión del prompt

Cuando un entorno no cabe en el presupuesto de palabras, comprime en este orden, y nunca más
allá:

```
environment_identity  >  light_detail  >  render_fixed
```

`render_fixed` es global: tocarlo cambia todos los prompts y destruye la comparabilidad con lo ya
producido. El último recurso es el **override por encuadre**, que aplica solo a esa toma y deja
intacto el canon del espacio.

Además: `compact` puede **omitir**, nunca **contradecir** ni **sustituir** a `full`. Y `compact`
no puede usar palabras que el negativo veta — el prompt se estaría exigiendo y prohibiendo lo
mismo.

Ver `references/prompt-composition-budget.md`.

## Un gate sobre archivos no ve lo que el prompt dice de esos archivos

La clase de fallo mas cara: **todos los checks pasan y el prompt es inservible.** Un gate que
valida que las referencias **existan** con su sha256 intacto no puede detectar que la lista no
dice lo que el plano queria.

Medido: una escena de dos personajes dio `FATHER_MASTER.png` en dos slots y
`MILO_ADULT_MASTER.png` ausente — la identidad del personaje que quedaba en cuadro no estaba.
Las dos referencias existen, con hash correcto: el gate dio `PASS` en las tres capas. El
modelo recibio al mismo hombre dos veces y a nadie mas.

**Sobre una lista de referencias, el gate tiene que comprobar la LISTA, no los archivos:**

| Check | Que atrapa |
|---|---|
| `REFERENCE_DUPLICATE` | la misma referencia canonica en dos slots |
| `FOCAL_REFERENCE_MISSING` | la identidad del personaje focal no esta exactamente una vez |
| `SECONDARY_IS_FOCAL` | el secundario es el mismo que el focal: dos cuerpos, una identidad |
| `DETAIL_REFERENCE_PRESENT` | el master de detalle no puede entrar sin `role: detail_reference` en el canon |

Y una regla que ninguna de las anteriores sustituye: **dos slots con la MISMA etiqueta son
indistinguibles para el modelo.** Asignar slots sin distinguir quien es quien no es asignar:
`image 1 is the scene reference; image 2 is the scene reference` deja al modelo sin saber cual
imagen es el personaje y cual el lugar. El check es **sobre el texto del prompt**, no sobre la
lista: `len(set(labels)) == len(labels)`.

Los roles se derivan de la **misma lista que el builder ya arma**, en ese orden, no de un campo
opcional del brief. Un campo de roles que nadie rellena cae al fallback y produce N etiquetas
identicas — el fallo se reintroduce solo en cuanto el texto se reescribe por otra razon (por
 ejemplo, al condensarlo por presupuesto).

Medido dos veces en la misma sesion, con dos mechanisms distintos: primero la lista con
duplicados, despues las etiquetas identicas al condensar el bloque de autoridad. **El segundo
duplico al primero porque el check vivia en el lugar equivocado** — sobre `refs`, no sobre lo
que se escribe.

## La autoridad entre referencias vive en el prompt, no en un campo del brief

Un canon puede declarar que una referencia gobierna una dimension y otra otra, y el prompt no
lo dice: **el modelo solo lee el prompt.** Un campo `reference_authority` en el brief protege
nada porque nadie lo lee ahi.

Texto normativo minimo dentro del prompt, cuando hay master de entorno y master de detalle:

```
image 2 governs the room: architecture, layout, furniture, light, continuity.
image 3 governs ONLY the plate, food and tabletop detail; it must not redesign the kitchen.
```

Sin esto, una referencia de detalle toma autoridad sobre la habitacion entera y **rompe la
continuidad arquitectonica entre encuadres** — que es justo lo que el maestro del mundo debe
garantizar. Y el fallo es invisible en el artefacto: cada imagen sale individual mente bien.

## Cuando una clausula normativa desborda el presupuesto, se condensa la clausula

Anadir una regla al prompt compite por el mismo presupuesto que la composicion. Medido: una
autoridad entre referencias escrita al detalle eran 55 palabras y mando dos encuadres a
`BLOCKED` sobre el tope duro de palabras.

**No subas el presupuesto para que quepa la clausula.** El tope existe porque el relleno compite
con la identidad, y subirlo deja entrar relleno en todos los prompts siguientes. Condensa la
norma a su contenido —arquitectura, layout, furniture, luz, continuidad / solo el objeto, sin
rediseñar— y el mismo limite sigue valiendo.

## El idioma del prompt y el idioma de la entrega son campos distintos

La prosa que consumes (VO, texto de pantalla, notas de encuadre) va en el idioma del espectador.
**Los campos que el builder convierte en prompt van en el idioma del modelo.** Poner la accion
en la lengua editorial produce un prompt que empieza en otra lengua y diluye las dos: el modelo
no entiende la instruccion y el lector tampoco la ejecuta.

El sintoma es reconocible: el prompt arranca con texto que no es instruccion, y los sustantivos
del objeto salen como frase rota cuando el builder concatena (`make the plato tapado a clear
narrative focal point`). Un nombre de objeto con guion baja a frase; un nombre de objeto con
palabras no es un nombre de objeto.

Y al revés: una nota de edicion dentro del prompt (`identical framing to the opening shot`) es
una instruccion para el editor de corte, no para el modelo. El encuadre repetido se logra
repitiendo el encuadre, no describiendo que se repite.

## Un check que miente es peor que no tenerlo

Una comprobación que da un veredicto falso entrena al usuario a desconfiar de **todas** las
comprobaciones. Medido: un autopregóstico de salud informaba "sin puente" con el puente
perfectamente vivo, porque su propia salida se truncaba a 444 B a mitad de un array y el parser
nunca veía el cierre.

- **Consulta la fuente directamente**, no a través de una imprimidora que pueda truncar. El
  autopregóstico pasó a abrir el WebSocket directamente en vez de parsear la salida de un script
  auxiliar.
- **Un diagnóstico con solo rama de PASS no verifica nada.** Ejercita cada rama de fallo: mata el
  proceso de verdad, inyecta el estado malo, confirma el código de salida 1.
- **Aísla una prueba rota de verdad.** Copiar un directorio no aísla nada cuando el JSON de dentro
  sigue apuntando a las rutas **originales**: la prueba mutaba la copia mientras el código leía el
  original y devolvía un PASS falso.
- **Parsea argv marcando qué índices son valores de flag** antes de escanear. "El primer argumento
  que no empieza por `--`" también coincide con el valor de `--request`.

## Un check que no puede fallar no es un check

El fallo más caro de un gate no es que mienta: es que **nunca tenga ocasión de hacerlo**. Un check
canónicamente antes de otro queda eclipsado —el primero siempre cae primero— así que el segundo
solo puede dar la razón cuando el primero ya aprobó. Pasa aunque los dos midan cosas distintas y
ambos sean correctos por separado.

Medido: un gate de vídeo con 7 checks tenía el 5 (ningún plano > 3 s) y el 6 (primer plano ≤ 3 s).
Un primer plano largo hacía fallar el 5, y el 6 no se podía ejecutar nunca. Se descubrió
escribiendo planes negativos y viendo que **uno no caía**; el código estaba bien y el gate pasaba
todo. Tres eclipses más aparecieron al exigir cobertura: un check de "lista no vacía" que el
anterior ya había tragido por exigir *truthy* (`[]` es *falsy*), y dos checks etiquetados igual
que se contaban como uno solo.

**Reglas:**

- **Cada check necesita un caso negativo que lo tumbe por su cuenta.** No basta con que la matriz
  tenga fallos: tiene que haber un plan donde **ese** check sea el único que falla.
- **Comprueba la cobertura leyendo la etiqueta del fallo**, no contando casos. Si el verificador
  emite `[5] ritmo` y `[6] hook`, extrae el número y comprueba que cada check tenga al menos uno.
  Si un check nunca es el primero en fallar, no sabes si funciona o si está eclipsado.
- **Cuando dos checks miden lo mismo sobre el mismo elemento, reparte el dominio.** El primero
  excluye el caso que le toca al segundo.
- **Un check no puede exigir una propiedad más fuerte de la que comprueba el anterior.** Si el 1
  exige "`planos` es truthy", el 2 (que valida que no esté vacía) es inalcanzable: exige solo que
  la **clave exista**.

**El indicador es el comportamiento, no el nombre del check.** Un check que solo aprueba, o que
nunca puede fallar, está apagado por mucho que suene bien y salga con `exit 0`. Y esto es
estructural, no un bug de codigo: por eso el doctor debe **comprobar la cobertura** y no limitarse
a contar que los casos negativos se rechazan.

## No mezcles capas al ofrecer opciones

Un proyecto con muchas capas abiertas invita a que las **opciones que ofreces** mezclen capas
distintas: presentar "definir el umbral de exito", "integrar el canon narrativo" y "generar los
encuadres no generables" como alternativas del mismo paso. No lo son, y la pregunta "cual elijo"
no tiene respuesta util, porque la respuesta es "todas, en orden".

**Antes de ofrecer opciones, clasifica cada una por capa** y nombra a que capa pertenece. Si solo
una es de la capa actual, esa es la opcion; las demas se mencionan como "esto es V3.0" o "esto es
deuda de la capa de imagen", no como alternativas. Señal de que te equivocaste: el usuario dice
"estoy desviando el foco" o "eso es otra capa". Esa corrección significa que **la pregunta estaba
mal**, no que faltara una opción más.

**Cada capa se cierra antes de abrir la siguiente.** Cuando el alcance queda fijado ("cerrar V2.0
con 7a medido, 7b declarativo"), el trabajo es ese: no abrir la siguiente, no tocar los gates que
ya pasan. Cerrar la capa es el trabajo; ofrecer trabajo posterior es ruido, por bien fundado que
esté — y sobre todo en pipelines de gates, donde una capa abierta pronto se convierte en un gate
más que alguien tiene que mantener.

## Regla en un gate > regla en memoria
Cuando se dice que una regla no cabe en la memoria por falta de presupuesto, comprueba si ya
existe un gate que la haga cumplir. Si el check existe y dispara, la regla **ya se está
ejecutando**: el agente no necesita recordarla. Lo que la memoria necesita es el puntero al gate,
una línea. La regla completa no.

## Delegar es otra clase de gate

Delegar imágenes a subagentes falla de una forma muy concreta: el padre pasa el **original**. Un
PNG de 1,4 MB tarda ~40 s en cargarse, el hijo lo recorta y reintenta por su cuenta, y 6 llamadas
después está adjudicando dos lecturas de un texto que no ve.

- El padre prepara el **proxy** (300–400 px clasificar, ~900 px OCR); el hijo solo lee.
- **Pasa el proxy como imagen adjunta, pero no asumas que basta.** Medido: texto grande (un
  letrero) se lee nativo, 0 llamadas; texto pequeño (lomos) con el **mismo** proxy de 900 px
  consumió 2 llamadas de `vision_analyze` para recortes. La variable es el **tamaño del texto**,
  no el proxy ni el motor. Cuando el texto es pequeño, **el padre recorta con `ffmpeg`**: dejar
  que el hijo lo descubra consumiendo su presupuesto cuesta más que el recorte.
- **Todo encargo lleva tipo de respuesta y presupuesto de llamadas declarados**, y `ilegible`
  tiene que ser una respuesta **válida**: un encargo que solo acepta una lectura correcta fuerza al
  hijo a inventar, y de ahí nacen las espirales de reintento.

Ver `references/delegation-gate.md`.

## Referencias

- `references/lock-field-provenance.md` — localizar el campo real, override por encuadre
- `references/attribute-contracts.md` — contrato de atributos y validación contra lo medido
- `references/prompt-composition-budget.md` — aritmética de presupuesto, compact/full, priority
- `references/contradiction-detection.md` — concepto + polaridad, y la matriz de prueba
- `references/delegation-gate.md` — encargo como contrato, checks de forma vs intención
- `references/foreign-benchmark-metrics.md` — recalcular la metrica no publicada, verificar que el material tiene la voz que las metricas asumen, registrar conflictos sin reescribir la pieza

Skills relacionadas: `generation-pipeline-control` (ejecución secuencial y verificación de
artefacto), `media-asset-intake` (registro e inspección de assets), `flow-image-generation`
(QA de prompt y de imagen).
