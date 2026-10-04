# Contrato para direccion — lo medido y lo decidido

Cuando el trabajo medido en el corpus se entrega como documento que otra persona
va a discutir en una reunion, la seccion mas util no es la de reglas: es la que
separa **hallazgo** de **decision**.

## Por que la separacion es la seccion principal

Una regla sin estatus invita a discutirla. "Los virales duran ~25 s" y "este canal
es el nicho" tienen el mismo tono en un documento y pesos epistemicos opuestos: la
primera se midio en 22 piezas, la segunda la eligio alguien. Presentadas juntas,
la reunion gasta su tiempo re-litigando la medicion.

## Verifica cada cifra contra su fuente, por script

Un numero transcrito a mano es un numero sin verificar, y un documento de
direccion se cita sin volver a mirar el origen. La comprobacion es barata y
automatizable: carga el JSON fuente, extrae los numeros del `.md`, compara, y
reporta los que no aparecen.

```python
import json, pathlib
src = json.load(open('registry/viral_dna.json', encoding='utf-8'))
doc = pathlib.Path('CONTRATO.md').read_text(encoding='utf-8')
for txt, val in [('30,7s', src['duracion']['todos']['mediana_s']),
                 ('25,3s', src['duracion']['viral_1M']['mediana_s'])]:
    print(txt, 'en doc:', txt in doc, '| real:', val)
```

Ojo con el separador de miles: si el documento escribe `1.669` y la busqueda
compara `1669`, el verificador dice "falta" sobre una cifra que si esta. Formatea
igual en ambos lados o compara los dos formatos.

## El limite del dato va pegado a la cifra

Si una medicion tiene un sesgo conocido, el aviso va **en la tabla donde se usa**,
no en un anexo: escrito lejos, se cita como ley. Igual la cobertura parcial
("solo el 77 % de los casos tiene el campo observable") pegada al patron que ese
campo sostiene, y el minimo de fuentes que hace falta para que algo sea patron y
no anecdota.

## Una especificacion que contradice lo ya medido

Si una instruccion pegada propone un campo, un enum o una regla mas estrecha que
la que el sistema real usa, no la apliques en silencio:

1. **Comprueba el sistema real** — el schema, el lock, el enum vivo.
2. **Di que cedio**: o se traduce el vocabulario ajeno al del sistema, o se declara
   la excepcion con su motivo.
3. **Un enum nuevo en un sistema con enum congelado es deuda**, no una mejora: cada
   valor anadido es una rama mas que ningun gate ha medido.

Lo mismo con una regla que el codigo ya cumple de otra forma: no la dupliques,
enlaza el gate existente.

## Verificacion final antes de entregar

- Todas las cifras del documento contrastadas contra su fuente.
- Encoding limpio (acentos y simbolos correctos; los CJK son un fallo real).
- Cada seccion limitante pegada a la cifra que limita.
- La tabla de estatuto presente: medido / decision / no-medible.
- Las decisiones del usuario marcadas como suyas, con la nota de que el corpus
  no las respalda — para que la distincion sobreviva al traspaso del documento.