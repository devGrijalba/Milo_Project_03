# Localizar el campo real antes de escribirlo

Un lock estructurado alimenta un resolver que compone el prompt. El error más barato de este
pipeline es escribir el campo correcto en el objeto equivocado: el edit se acepta, el JSON sigue
válido, y el efecto es **cero**. Pasa por un arreglo y no arregla nada.

## Procedimiento

Antes de escribir cualquier campo nuevo, lee de dónde lo lee el código:

```bash
grep -rn "campo_que_quieres\|variante_hermana" src/flow/
```

El resultado que importa es la línea del **resolver** que construye la escena, no la del mapper
que la consume. Resolver → campo intermedio → mapper es la cadena real.

Comprueba tres cosas antes de escribir:

1. **La ruta exacta**, incluido el nivel del árbol. Un override de encuadre puede vivir dentro de
   la variante del encuadre (`framing_variants.<id>.<campo>`) y no en el base space, aunque el
   nombre del campo sea idéntico en ambos niveles.
2. **El tipo esperado.** El resolver exige array y escribe `light_en.compact` como lista de
   cadenas; un string pasa la validación del JSON y revienta después con un error de manifiesto que
   habla de estructura, no del campo.
3. **La prioridad.** Si dos campos compiten por el mismo valor, gana el más específico; saber cuál
   gana explica por qué el prompt no cambia aunque hayas escrito algo razonable.

## Override por encuadre

Cuando un valor concreto no sirve para todos los encuadres del mismo espacio, la salida no es
duplicar el espacio base sino declarar el override en la variante que lo necesita:

```json
{
  "framing_variants": {
    "mente_medio": { "prompt_en": "…", "_nota": "por qué existe y por qué aquí" },
    "mente_detalle": { "prompt_en": "…" }
  }
}
```

Ventajas que hay que saber articulate al decidir:

- aplica **solo** a ese encuadre, así que los prompts ya validados no se mueven;
- no cambia el canon del espacio, que sigue siendo el mismo para el resto;
- es reversible quitando una clave, sin editar el resto del lock.

**Siempre verifica el alcance después de escribirlo.** Cuenta cuántos encuadres tienen el override
y confirma que son los que querías:

```bash
python -c "
import json; wl=json.load(open('knowledge/visual/world_lock.json',encoding='utf-8'))
for b in wl['space_architecture']['base_spaces']:
    for k,v in b['framing_variants'].items():
        if 'prompt_en' in v: print(k)"
```

## Un gate que busca en el nivel equivocado bloquea sobre datos que SI existen

Un gate nuevo que recorre un lock para validar sus entradas **no se equivoca de conclusion: se equivoca de ruta**, y en la salida ambos errores parecen lo mismo. Medido: un gate de contrato narrativo reporto "sin luz declarada" y despues "placa inexistente" sobre cuatro escenas que si tenian luz correcta. El lock era correcto; el gate leia `location_materials[espacio][encuadre]` cuando el indice era **plano, por nombre de encuadre** (`location_materials["biblioteca_medio"]`), y antes habia intentado `space_architecture.base_spaces[].framing_variants`, que solo contiene encuadre y camara, no luz.

El sintoma es silencioso y peligroso: **un bloqueo falso entrena a ignorar el gate**. Un gate que solo dice OK no sirve, pero uno que bloquea sobre datos sanos es peor, porque la proxima vez se le da la razon sin mirar.

Protocolo, en orden:

1. **Localiza el indice real antes de escribir el gate**, no cuando ya fallo. El propio lock suele
   decirlo: busca una clave `note`, `purpose` o `reference_rule` en el nodo y leela. Aquella
   declaraba literalmente *"Indexado por NOMBRE DE ENCUADRE, no de espacio base"*.
2. **Verifica el tipo del campo, no solo su nombre.** Un valor que esperas como string puede ser
   lista de cadenas, y una lista de frases se cuenta como `len(' '.join(lista).split())`, nunca como
   `len(lista[0].split())` — asi se cuenta lo que ira al prompt, no la primera frase.
3. **El nombre del campo de complejidad varia:** `complexity` frente a `lighting_complexity`.
   Asumir el corto produce el valor por defecto y salta silenciosamente la rama que valida.
4. **Prueba el gate con un caso que SI tiene el dato antes de crearlo.** Si todos los casos
   bloquean, el diagnostico mas probable es la ruta, no los datos.

Cierra con una comprobacion negativa explicita: **un gate de datos debe poder responder "todo
bien"**. Si su primer uso real bloquea en masa, depura la ruta antes de tocar datos que ya eran
correctos.

## Consistencia dentro del mismo concepto

Si un valor tiene dos representaciones (`compact` y `full`), corregir una y dejar la otra es la
peor de las dos situaciones: el sistema queda con dos verdades incompatibles del mismo concepto, y
la ruta que no se corrigió sigue produciendo el defecto sin señal.

Antes de dar por cerrado un arreglo, busca **el mismo defecto en el nivel hermano**:

```bash
grep -n "el_termino_que_corregiste" knowledge/visual/*.json
```

Un arreglo a medias se detecta con un grep, no con un dry run del encuadre que ya funcionaba.
