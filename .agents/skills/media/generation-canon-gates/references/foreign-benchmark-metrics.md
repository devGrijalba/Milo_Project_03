# Importar metricas de un benchmark ajeno

Un dataset externo (nicho, canal, competidor) llega como numero de referencia y suele_traer dos
defectos que no se ven leyendo el analisis: **una metrica clave que nunca se publico** y **una
suposicion sobre el formato que no se verifico**. Importarlos sin comprobarlos convierte un
prior de diseno en una regla falsa.

## 1. Recalcula lo que el dataset no publico

Los analisis suelen publicar vistas, duracion y palabras, y cruzar dos de esas columnas es trivial
— y es justo el cruce que falta. El ritmo implicito (`palabras / duracion` en WPM) es el mas
frecuente porque casi todos los motores de locucion tienen un umbral de ritmo y el nicho no lo dice.

```python
wpm = palabras / (duracion_s / 60)
```

Si el dataset ya publica el ritmo, usa el suyo. Si no, el calculado es una **cifra nueva**: marcala
como tal y explica de donde salio, porque no la encontro el autor y cualquiera que la cite como
"el dato del estudio" esta atribuyendo una autoridad que el dato no tiene.

## 2. Verifica que el material contiene lo que las metricas asumen

Antes de tratar una cifra como "rango del nicho", comprueba que el nicho **produce** la magnitud
que la cifra mide. Una columna de ritmo solo significa algo si hay voz detras.

Extraccion y reparto de energia por banda:

```bash
ffmpeg -v error -i video.mp4 -map 0:a:0 -ac 1 -ar 16000 -y out.wav
```

Despues, con numpy sobre el WAV en bloques de 1024: energia en `0-120`, `120-400`, `400-1000`,
`1000-3400`, `3400-8000`, `8000-Nyquist`, y silencios `>= 0.5 s` por ventanas de 50 ms.

| Lectura | Conclusion |
|---|---|
| energia >50 % en 400-3400 Hz, silencio abundante | hay locucion; el ritmo es comparable |
| energia >60 % por debajo de 400 Hz, ~0 s de silencio | musica continua; **el ritmo medido era texto LEIDO, no voz OIDA** |

El segundo caso es el que importa, y es facil de errar porque el audio **si existe** y el archivo
**si tiene duracion**: `ffprobe` responde con un stream de audio valido y todo parece correcto. Lo
que delata la musica continua es la energia de graves junto a la ausencia total de silencios — una
locucion, por rapida que sea, respira.

Cuando el ritmo no es comparable, dilo como un hecho del formato, no como una opinion: "este
corpus es texto sobre musica; su ritmo es el del lector". Un ritmo de lectura y uno de audicion
comparten columna y son incompatibles. **El umbral propio de tu motor no se revisa por esto**: tu
rango de locucion lo define tu locucion, no lo que hace el vecino.

## 3. Una correlacion que sobrevive al recalculo no es permiso para comparar

Si reproduces las correlaciones del estudio y coinciden, eso es un indice de que tu parseo es
correcto — no de que los dos materiales sean intercambiables. Verificar el calculo y verificar la
transferibilidad son preguntas distintas, y responder solo la primera es el error tipico.

## 4. Registra los conflictos; no los resuelvas por la via del guion

Cada choque entre el benchmark y tu canon es un **registro con numero**, no una reescritura:

```
conflicto: PALABRAS
  benchmark: mediana 26 (rango 15-43), n=10
  pieza:     108  (4.2x)
  lectura:   el patron de un solo concepto es el mas fuerte del corpus; la pieza lo triplica
  accion:    REGISTRAR. Es el ajuste mas probable si la pieza no retiene.
```

Si la pieza ya fue aprobada por una direccion humana, **no la reescribas por el score**. El
scorer informa; la decision editorial es de quien dirigio. Y si el score bajo es lo unico que
ofrece el trabajo, no lo ofrezcas como recomendacion: di que mide alineacion estructural con un
prior de otro canal, y que no mide retencion ni viralidad.

## 5. El rol informativo se prueba por aislamiento

Un score que "solo informa" es el tipo de gate mas peligroso, porque todos asumen que la exclusion
ya esta hecha y nadie la vuelve a comprobar. Verifica con aislamiento: fija todas las entradas
salvo la que debe ser inerte, lleva esa entrada a sus extremos (0 y 100) y comprueba que el
veredicto agregado y el conjunto de fallos son identicos. Excluir una clave de una comprehension
no es exclusion — el evaluador puede releer la lista de roles del config, recalcular sobre todos
los roles, o exigir un resultado por rol declarado. Ver `rulebook-gated-consistency` para el
diseno del rol sin peso.