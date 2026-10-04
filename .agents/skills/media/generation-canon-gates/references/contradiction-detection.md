# Contradicción prompt/negativo: concepto + polaridad

Un detector de "el prompt exige lo que el negativo prohíbe" pasa por **tres** generaciones de
defecto, y cada una tiene que estar resuelta antes de que el detector sirva para algo.

## 1. Cadena literal — no ve nada

El negativo dice `hard directional light`. El prompt decía `one hard overhead light`. Son cadenas
distintas y la **misma idea**. Un gate que busca la frase exacta pasa un lock limpio sobre el que
tiene el fallo puesto a propósito.

Un detector así no falla: no ve nada, que es peor, porque su salida parece un aprobado.

## 2. Concepto sin polaridad — marca lo correcto

Corregido lo anterior, `no direct source in frame` dispara la misma alarma que `direct light`: el
núcleo está y el modificador está, pero el texto **niega** justo lo que el negativo veta. Medido
sobre un lock limpio: 16 falsos positivos, y entre ellos un encuadre cuyo texto dice literalmente
que no hay fuente directa.

Un gate que marca como malo lo que está bien acaba siendo ignorado, y entonces no protege nada.

## 3. Concepto + modificadores + polaridad

Un concepto se acepta solo si:

- contiene un **núcleo** del concepto (`light`, `lamp`, `spotlight`, `shadow`);
- contiene un **modificador** del concepto (`hard`, `direct`, `harsh`, `moody`, `dramatic`);
- y **no está bajo polaridad negativa**.

```js
const CONCEPTOS = [
  { concepto: 'hard directional light',
    modificadores: new Set(['hard','direct','directional','harsh','sharp','abrupt']),
    nucleo:        new Set(['light','lighting','lamp','spotlight','sunlight','glow','beam']) },
  { concepto: 'moody darkness',
    modificadores: new Set(['moody','gloomy','somber','sombre','heavy']),
    nucleo:        new Set(['darkness','dark','gloom','shadow','shadows']) },
];
```

Los sinónimos van en el conjunto, no en el código: `harsh` y `abrupt` activan lo mismo que
`hard`, y esa es la razón por la que la comparación por cadena fallaba.

## La polaridad necesita ventana y barrera

La negación cuenta solo si aparece **cerca** de la palabra, y **sin otro sustantivo en medio**:

```js
function estaNegada(ws, i, ventana = 3) {
  for (let k = Math.max(0, i - ventana); k < i; k += 1) {
    if (NEGADORES.has(ws[k])) {
      const entre = ws.slice(k + 1, i);
      if (entre.length <= 2) return true;   // no hay sustantivo de por medio
    }
  }
  return false;
}
```

Por qué las dos condiciones hacen falta:

| Texto | Veredicto | Razón |
|---|---|---|
| `no direct source in frame` | pasa | negación a distancia 1 de `direct` |
| `nothing directional` | pasa | negación a distancia 1 |
| `sin fuente directa` | pasa | negadores en español en el mismo conjunto |
| `nothing in the room, a hard overhead light` | **falla** | la negación está lejos y separa otra cláusula |

El último caso es el que separa un detector útil de uno desactivable: sin ventana, un `"nothing"`
en cualquier parte del prompt apagaría la alarma del resto de la frase. **Un gate que se puede
desactivar escribiendo una palabra no es un gate.**

Incluye los negadores del idioma en el que esté el lock, o la comprobación solo funciona en
inglés.

## Matriz de prueba obligatoria

Un detector se prueba contra casos conocidos, no contra el estado actual. Mínimo:

| Caso | Para qué |
|---|---|
| el fallo real que existía | demuestra que detecta |
| un caso legítimo equivalente | demuestra que no marca de más |
| el caso límite de polaridad | demuestra el criterio del margen |

```js
const CASOS = [
  { texto: 'one hard overhead light, black around',        esperado: ['hard directional light'] },
  { texto: 'cold blue ambient night light, no direct source', esperado: [] },
  { texto: 'nothing in the room, a hard overhead light',    esperado: ['hard directional light'] },
  { texto: 'cold blue window light',                        esperado: [] },  // espacio validado
];
```

Incluye siempre un caso tomado de un prompt **que ya se generó y pasó**. Es el ancla que impide
que "arreglar" el detector rompa algo que funcionaba.

## Cuando un caso falla

Verifica **qué** falló antes de tocar nada. Un caso mal escrito produce un fallo igual de real que
un detector mal escrito, y "arreglar" el detector para que pase una expectativa equivocada
introduce un defecto invisible.

En la sesión que originó esto: un caso esperaba que `dramatic shadows` activara también `moody
darkness`. El detector tenía razón — `dramatic` no es modificador de `moody darkness` — y el
error estaba en la expectativa. Se corrigió el caso y se añadió otro de múltiples conceptos.

## Orden: terminar el detector antes de tocar el canon

Mientras el detector pueda dar falsos positivos, corregir el lock es **cambiar el destino para que
el mapa parezca bien**. Secuencia: matriz en verde → corregir el canon → recién entonces conectar el
validador como bloqueador de producción.
