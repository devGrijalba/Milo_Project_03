# Contratos de atributo por asset

Una referencia que se manda al generador lleva un propósito declarado. El contrato es lo que
impide que una referencia contamine otra, y el fallo que justifica este archivo es el más caro de
la clase: **una referencia mal etiquetada produce una imagen con la identidad equivocada, y
ningún ajuste de prompt lo arregla.**

## El contrato

```json
{
  "purpose": "clothing_reference",
  "allowed_attributes": ["wardrobe", "signature_object", "body_shape"],
  "forbidden_attributes": ["face", "eyes", "mouth", "expression"]
}
```

`forbidden_attributes` presente es **bloqueante**, no un aviso.

## Se valida contra lo MEDIDO, no contra el nombre

El campo de evidencia (`verified`) es lo que se compara. `purpose` declara intención y no verifica
nada: usarlo para "dar por cumplido" un contrato es exactamente el defecto que el contrato existe
para evitar.

```json
"verified": { "contiene_cara": "NO", "contiene_cabeza": "NO", "arrastra_ropa": false }
```

Cada atributo prohibido necesita su forma de comprobarse, porque "no hay cara" se mide distinto
que "no hay boca":

| Atributo prohibido | Cómo se comprueba |
|---|---|
| `face` | `contiene_cara === 'NO'` |
| `mouth` | sin cara no hay boca; en ref de cara, que no haya boca es lo esperado, no violación |
| `head` | `contiene_cabeza === 'NO'` — una cabeza completa en una ref de ropa es la contaminación clásica |
| `wardrobe` | `arrastra_ropa === false` medido, no inferido de `purpose` |
| `environment` | aplica si el propósito no lo sirve; si no, no se afirma nada |

## Tres estados, y solo uno bloquea

| Estado | Significado | Acción |
|---|---|---|
| medido y ausente | contrato cumplido | PASS |
| medido y presente | contrato violado | **FAIL, bloquea** |
| no medido | no hay evidencia | AVISO, con el recuento visible |

Tratar "no medido" como violación produce un gate que bloquea por no haber medido una combinación
improbable — y un gate que siempre falla acaba siendo ignorado.

**Excepción: campo de evidencia ausente bloquea.** Si no hay `verified`, no hay contra qué
comparar, y aprobar por omisión hace decorativa la comprobación. Es distinto de un rasgo no
medible: aquí falta el campo que el gate debe mirar.

## Un contrato por asset, un atributo de identidad por asset

Dos referencias de identidad compitiendo son la causa del defecto de rostro humano. Una sola
referencia de identidad, y todo lo demás declara `face` prohibido.

## Gates: ejecutable, no documentado

Un contrato escrito que nadie ejecuta es documentación. El validador debe ser un comando que se
puede correr y cuyo código de salida signifique algo:

```bash
node tools/validate-attributes.js    # 0 = PASS, 1 = FAIL
```

Y el generador debe llamarlo **antes de enviar nada**, como proceso aparte. Detalle en
`references/` de la skill principal.

## Referencia por ruta y hash, no copiada

El paquete que declara el canon no copia las imágenes: las referencia por ruta relativa al proyecto
y por `sha256`. Copiar crea dos canónicos que divergen, que es la misma clase de fallo que un
nombre de archivo que miente. Un hash distinto convierte una modificación accidental en un evento
detectable, en vez de una referencia que apunta en silencio a algo viejo.

Verifica los hashes tras **cualquier** cambio de canon antes de declarar cerrado el trabajo.
