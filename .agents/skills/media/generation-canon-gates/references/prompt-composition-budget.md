# Aritmética del presupuesto de prompt

Un mapper con gate de palabras falla cuando el texto no cabe. El fallo llega tarde y como error de
estructura, no como "el entorno es demasiado largo". Merece la pena calcular **antes** de escribir.

## Cuenta primero, escribe después

```
total = ACCION + ESPACIO + LUZ + RENDER_FIJO
```

Separa lo que **nunca** cambia de lo que sí:

| Parte | Cambia | Típico |
|---|---|---|
| acción | sí, por toma | 5 |
| espacio | sí, por encuadre | 5-13 |
| luz | sí, por encuadre | 3-7 |
| `RENDER` | **no** | 13 |

`RENDER` fijo son palabras de formato (plano, profundidad, iluminación, "no text"). Con acción +
render, el presupuesto para **describir dónde está el personaje** cae a ~12 palabras. Por eso
`"dark night study"` (6) y `"dark library"` (5) caben y `"inner theatre of the mind"` no.

Antes de recortar texto, imprime el desglose con el recuento por parte. Un total 31 con un techo
de 30 se arregla recortando una palabra; se pierde media tarde si se descubre por el error.

## Orden de compresión

Cuando no cabe, comprime en este orden y **no más allá**:

```
environment_identity  >  light_detail  >  render_fixed
```

1. **Identidad del entorno** — es lo que la prueba mide. Recortarla destruye el objetivo.
2. **Detalle de luz** — es lo más barato: la placa ya transmite la luz, el texto solo la nombra.
3. **`RENDER` fijo** — es global. Tocarlo cambia todos los prompts y rompe la comparabilidad con
   lo ya producido. Solo con una decisión explícita de migrar todo.

Si después de los tres sigue sin caber, el espacio es conceptual y necesita **override por
encuadre** (`references/lock-field-provenance.md`), no una mutilación.

## `compact` frente a `full`

- `full` puede **ampliar**.
- `compact` puede **omitir**.
- `compact` no puede **contradir** ni **sustituir**.

El fallo real: `full` decía `"an inner theatre of the mind"` y `compact` decía `"a dark void"`.
Los dos son oscuros, pero no son lo mismo, y el mapper elige `compact` en modo corto — así que
el prompt describía un vacío y el criterio de la prueba quedaba sin poder evaluarse.

**Al escribir el `compact`, comprueba que comparte identidad con el `full`**, no solo que sea corto.

## `compact` no puede contradecir al negativo

Si el negativo veta `"hard directional light"`, un `compact` con `"hard"` y luz se está pidiendo y
prohibiendo lo mismo. Además `compact` significa **una** idea: si declara dos fuentes de luz, no
es compacto por definición.

Detección automática en `references/contradiction-detection.md`.

## Verifica el alcance del recorte

Recortar un `compact` debe **no mover los prompts ya validados**. Mídelo:

```bash
for E in espacio_antes espacio_despues; do node tools/generate.js; done
```

Si el prompt de otro encuadre cambia de palabras, el recorte se coló en un campo compartido. Es el
síntoma de haber editado el base space en vez de la variante del encuadre.
