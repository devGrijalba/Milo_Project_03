# Auditar las herramientas hermanas tras corregir un flag

Cuando una herramienta ignora un flag y usa siempre un default hardcodeado, **el mismo error esta
copiado en el directorio hermano**. Corregir solo una deja el pipeline entero expuesto.

Medido: corregido el CLI que generaba, el dry-run siguiente leia igualmente el manifiesto legacy y
resolvia el **universo equivocado** (el lock de otro personaje), escribiendolo en un `plan.json`
compartido. El dry-run era la unica via segura para iterar sin cuota y reportaba como correcto el
plan de otro mundo: el sintoma es que el gate de palabras pasaba, el trace era valido, y ninguna
senal delataba el cruce de universos.

## Los tres fallos que aparecen juntos

1. **El flag se ignora** y se lee un archivo fijo.
2. **El default esta hardcodeado** — el fallback al archivo equivocado.
3. **La salida es compartida** — un unico `plan.json` que el ultimo dry-run pisa.

Cuando aparecen dos de tres, busca el tercero.

## Procedimiento

```bash
# 1. quien declara el flag
grep -rn "\-\-manifest\|process.argv" tools/ scripts/ | grep -v node_modules
```

Un script que **no aparece** en el grep de `process.argv` es un script que ignora todos los flags.

```bash
# 2. quien escribe en el mismo fichero de salida
grep -rn "writeFile\|OUT/" tools/ scripts/ | grep -v node_modules
```

Dos scripts escribiendo el mismo `OUT/plan.json` es el tercer fallo confirmado.

## Las tres defences

### Fail closed, no fallback silencioso

Sin `--manifest`, **avisa en voz alta** y nombra el archivo que va a usar. El fallback al legacy es
precisamente lo que produce un dry-run del archivo equivocado sin que nadie lo note.

### Compara lo pedido contra lo leido

El plan resuelto declara su procedencia. Si el mundo resuelto no contiene el `character` que el
manifesto pide, **no se escribe el plan** y se sale con error:

```js
const pedido = manifest.character;
const leido = plan.scene?.provenance?.world_lock ?? '';
if (pedido && leido && !leido.includes(pedido)) {
  console.error(`universo incorrecto: pide ${pedido}, leyo ${leido}`);
  process.exit(1);
}
```

Sin esta comparacion, un resolver que lee el lock equivocado pasa el dry-run con un plan valido de
**otro** personaje — porque el plan es coherente, solo que de otro mundo.

### Nombra el artefacto de salida por entrada

Un fichero de salida compartido hace que el ultimo dry-run pise el anterior y no se sabe a que toma
pertenece. Dos tomas se confunden en un fichero que ambas dicen haber escrito:

```js
const sufijo = rutaManifest.replace(/[^\w]+/g, '_').replace(/^_|_$/g, '');
const rutaPlan = `${OUT}/plan-${sufijo}.json`;
```

## El companion: el resolver puede rechazar tus campos nuevos

Anadir campos de contrato a un manifiesto puede romper el dry-run si el resolver **rechaza lo que no
conoce** — y ese es el comportamiento correcto, no un bug que sortear: un campo mal escrito que se
ignora produce una escena mas pobre de lo que el manifiesto pedia.

Cuando eso ocurre, declara el campo en la lista de campos opcionales del resolver **documentando
quien lo lee**:

```js
// Estos campos no los usa el resolver: los leen los gates para comprobar
// que cada propiedad tiene un dueno ANTES de gastar cuota. Se declaran
// aqui porque el resolver rechaza lo que no conoce, y un campo de
// contrato rechazado seria un contrato que nadie puede usar.
```

La consecuencia de alcance: **si el gate nuevo necesita campos que el manifiesto no transportaba,
el contrato hay que extenderlo en el resolver tambien**, o el gate es inaplicable.