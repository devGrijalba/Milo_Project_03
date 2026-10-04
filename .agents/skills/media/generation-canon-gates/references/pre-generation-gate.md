# Pre-generation gate: convertir reglas en ejecución

Un contrato, un hash o un presupuesto escritos en un documento **no protegen nada**. Un gate es un
comando que corre antes de gastar cuota y cuyo código de salida significa algo.

## Los siete puntos y su orden

El orden importa: para en el primero que falla, y el último suele ser el que más duele descubrir
tarde. Los cinco primeros preguntan **por el asset**; los dos últimos, **por lo que el prompt dice
de los assets**.

| # | Punto | Atrapa |
|---|---|---|
| 1 | el índice/canon existe | generar sin saber con qué |
| 2 | hashes del canon intactos | un asset modificado que se sigue enviando en silencio |
| 3 | contratos de atributo cumplidos | la referencia mal etiquetada |
| 4 | el asset/placa de esta escena es generable | la placa vetada, con su razón visible |
| 5 | nada *superseded* en la ruta generativa | el asset histórico que reintroduce el fallo corregido |
| 6 | **semantica de la lista** de referencias | la referencia duplicada, la identidad del focal ausente, el secundario igual al focal |
| 7 | **asignacion de slots en el prompt** con etiquetas distintas | N slots con la misma etiqueta: indistinguibles para el modelo |

Los puntos 6 y 7 se separan porque fallan por motivos distintos y uno no sustituye al otro: el 6
comprueba la **lista de archivos**, el 7 el **texto que se escribe sobre ella**. Un gate con
solo el 6 deja pasar un prompt donde las tres referencias se llaman `scene reference`. Ambos
son necesarios, y ninguno se deduce de "los archivos existen con su hash correcto".

Para el punto 7 el check no es "hay una frase de asignacion": es que **ningun par de slots
comparte etiqueta**. Deriva las etiquetas de la misma lista que el builder arma, en ese orden
(focal → secundario → entorno → detalle), y no de un campo opcional del brief: un campo de
roles vacio cae al fallback y reintroduce el fallo en cuanto el texto se reescribe.

Detalle de orden que importa en el punto 6: una referencia de detalle solo puede entrar si el
canon la declara con `role: detail_reference`. Aceptarla por nombre de archivo reintroduce
exactamente el problema que el rol acota.

## Tres reglas que hacen que sea un gate y no un informe

**Proceso aparte, no importado.**

```js
const gate = spawnSync(process.execPath, [join(ROOT, 'tools', 'pre-generation-gate.js')], { cwd: ROOT });
if (gate.status !== 0) { /* abortar */ process.exit(1); }
```

Si el generador **importa** el validador, una excepción al cargar el módulo se cuela como "el
gate no dijo nada, continúo". Con proceso aparte el fallo es visible y el abort es inequívoco.

**Si el gate falla, se aborta.** No debe existir ruta por la que una generación llegue al servicio
sin pasar los puntos. Un gate consultable que no bloquea es documentación con pasos extra.

**Prueba el bloqueo, no solo el aprobado.** Pasa una escena prohibida por el camino real y comprueba
dos cosas: que se aborta **y que no se gastó cuota** — cuenta los archivos de descarga antes y
después. Un gate que solo se ha visto pasar no tiene probada la mitad que importa.

En una sesión, el ensayo con una placa de texto quemado abortó con el motivo exacto y dejó el
contador de descargas intacto. Eso es lo que prueba el punto 4.

## Salida legible, no solo código

Cada paso imprime su veredicto **con el motivo**. Un gate que dice `FALLA` sin decir qué objeto ni
por qué obliga a una segunda ronda de investigación:

```
FALLA 4. milo/ciudad_acera: placa MILO_CITY_NIGHT.png es
       "environment_inspiration" y NO es generable.
       Razon: burned_text_detected.
```

## Conecta un validador nuevo al final, no al principio

Un detector recién escrito se queda **independiente** hasta que su matriz de casos conocidos esté
en verde. Conectarlo antes bloquea encuadres que funcionan, y una regresión en producción causada
por una herramienta nueva cuesta más que la deuda que querías medir.

Secuencia: matriz en verde → corregir el canon → recién entonces hacerlo bloqueante.

## Verificación tras cualquier cambio

Después de tocar el canon, comprueba en este orden: integridad (hashes sin cambios), validadores
(uno a uno), y que un dry run de un encuadre **no afectado** siga produciendo el mismo prompt. Un
cambio que mueve un prompt ya validado significa que se editó un campo compartido por error.

## El gate verde no dice que el prompt sirva — leelo

Los siete puntos pueden pasar y el prompt seguir siendo inservible, porque todos preguntan sobre
archivos, hashes y estructura: ninguno lee lo que el prompt **afirma**. Un paquete puede pasar
las tres capas (builder, QA, gate) y llevar dos referencias del mismo personaje porque la lista
tenia un duplicado y el resto estaba bien.

Asi que despues de las capas automaticas, **lee el prompt completo una vez, como lo leeria el
modelo**, y pregunta:

- ¿cada `image N` dice algo distinto de los demas?
- ¿los sustantivos del objeto narrativo son nombres, no frases? (`plate tapado` sale como
  `make the plate tapado a clear narrative focal point`)
- ¿hay oraciones en otro idioma, o notas de edicion dirigidas a quien corta?

Este read es gratuito y es el unico que pregunta por el prompt en vez de preguntar por sus
insumos. Sin el, el gate es una garantia de integridad, no de correccion.
