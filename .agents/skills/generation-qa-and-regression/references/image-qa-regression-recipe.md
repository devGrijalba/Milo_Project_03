# Recipe: QA de imagen que puede fallar, y regresion de un Golden Failure

Procedimiento completo con el caso medido que lo motiva.

## 1. El fallo de confirmation bias, tal como se presento

Generacion con 3 referencias (personaje A, personaje B, entorno canonico) y prompt de 97
palabras. Paso 7/7 checks:

| Check | Pregunta | Respuesta |
|---|---|---|
| identidad | ¿cabeza redonda blanca? | si |
| secundario | ¿nino con sudadera amarilla? | si |
| objeto | ¿plato en primer plano? | si |
| estilo | ¿calido de libro ilustrado? | si |
| texto | ¿sin texto ni logos? | si |
| anatomia | ¿manos bien? | si |
| editorial | ¿espacio arriba-izquierda? | si |

Y aun asi la imagen tenia:

- **DOS campanas metalicas** (el prompt pedia una)
- la de primer plano **desproporcionada** respecto a encimera y padre
- el padre descrito con "barba corta" y chaleco azul — ya no era el master
- proporciones del nino alteradas
- el entorno reditado, en otro tratamientо visual

Lo critico no es que los checks fueran erroneos: es que **el mismo analisis habia escrito
"hay otro plato tapado junto al padre"** y lo registro como caracteristica de la escena.
El prompt pedia un plato; la imagen tenia dos. El texto que revelaba el fallo estaba
escrito y no se eligio como veredicto.

**Regla:** cuando tu propia lectura contenga algo que el brief no pidio, ese fragmento es
la evidencia mas valiosa del informe. Tratarlo como detalle lo entierra.

**Segunda regla:** "cabeza blanca" no es identidad. Identidad es la combinacion de forma
de cabeza + proporciones + vestuario comparada contra el master. Un check pasable con
rasgos sueltos mide lo que no es.

## 2. Las ambiguedades que peor pagan

| Frase del prompt | Lo que el modelo puede hacer | Correccion |
|---|---|---|
| `preserve identity from references` | no saber que imagen es quien | `... from image 1` |
| `character small in doorway background` | reducirle el cuerpo | `appears smaller only because of perspective` |
| `plate large in foreground` | plato gigante | `normal-sized ... occupying roughly the lower 20% of the frame` |
| accion sobre un objeto + objeto en primer plano | generar dos | `There is exactly ONE ...` |
| nombre del entorno, sin autoridad | rediseño libre | `Image 3 is the canonical kitchen environment` |
| 6 tokens de estilo | compiten con identidad | una frase de refuerzo |
| nombre de universo | el generador no lo sabe | fuera del prompt |

Las dos primeras reglas se、市場an asi: **BODY SCALE != PERSPECTIVE SCALE** y
**VISUAL PROMINENCE != PHYSICAL GIGANTISM**.

## 3. Test de regresion: script worked

```python
import re, json
from pathlib import Path

GF = Path('.../milo_failures/GF001_multireference_kitchen')
ASSIGN    = re.compile(r'image\s*([1-9])\b', re.I)
ASSIGNED  = re.compile(r"(?:is|are)\s+the\s+[\w\s]{0,30}?from\s+image\s*([1-9])", re.I)
PERSP_OK  = re.compile(r'(because of perspective|due to perspective|farther|further|far from)', re.I)
SIZE_OK   = re.compile(r'(normal[- ]sized|physically realistic|occupies roughly)', re.I)
UNIQUE    = re.compile(r'exactly\s+(one|1)|only\s+one', re.I)

HARD_FAILS = []
def fail(rule, triggered, msg): HARD_FAILS.append((rule, triggered, msg))

def analyse(prompt, reference_map, brief):
    n = len(reference_map['slots_enviados'])
    slots = set(ASSIGN.findall(prompt))
    faltan = {str(i) for i in range(1, n + 1)} - slots
    fail('R1_reference_role_assignment', n > 1 and faltan,
         f'slots sin mencionar: {faltan}')

    maps = reference_map['contrato_que_falto']
   Slots = {f'image_{i}' for i in range(1, n + 1)}
    fail('R2_reference_map_inmutable',
         bool(Slots - set(maps)) or
         [s for s in Slots & set(maps)
          if not all(maps[s].get(k) for k in ('asset_id','role','prompt_name'))],
         'reference_map incompleto')

    vago = re.search(r'preserve\s+(?:exact\s+)?\w*\s*identity\s+from\s+references',
                     prompt, re.I)
    fail('R3_identity_generica', bool(vago), 'sin indicar que imagen es quien')

    hay_small = SMALL.search(prompt)
    fail('R4a_escala_cuerpo', bool(hay_small) and not PERSP_OK.search(prompt),
         '"small" sin aclarar perspectiva')

    hay_large = LARGE.search(prompt)
    fail('R4b_escala_fisica', bool(hay_large) and not SIZE_OK.search(prompt),
         '"large" sin tamanho normal')

    obj = re.search(r'(covered plate|food cover|dome|cloche)', prompt, re.I)
    fail('R5_cardinalidad', bool(obj) and not UNIQUE.search(prompt),
         'objeto unico sin "exactly ONE"')

    # Regla no evaluable => FAIL, no ok
    if brief is None:
        fail('R6_complejidad_sin_modo', True, 'sin brief: no evaluable')
    else:
        cs = brief.get('scene_complexity', {})
        modo = brief.get('generation_mode')
        fail('R6_complejidad_sin_modo',
             cs.get('risk') == 'HIGH' and not modo,
             'complejidad HIGH sin modo declarado')

    uni = re.search(r'\b<Nombre de universo>\b', prompt, re.I)
    fail('R7_universo_como_control', bool(uni), 'nombre de universo como instruccion')

    return {'hard_fails': [m for _, t, m in HARD_FAILS if t]}


def main():
    res = analyse((GF/'prompt_original.txt').read_text(),
                  json.loads((GF/'reference_map.json').read_text()),
                  json.loads((GF/'scene_brief_ORIGINAL_failed.json').read_text()))
    if not res['hard_fails']:
        print('PASS — ESTO ES UNA REGRESION'); return 1
    print(f'REJECTED — {len(res["hard_fails"])} hard fails (correcto)')
    return 0 if check_corrected() else 1


def check_corrected():
    """Contraprueba: sin esto, un gate que rechaza todo tambien 'pasa'."""
    HARD_FAILS.clear()
    analyse((GF/'corrected_prompt.txt').read_text(),
            json.loads((GF/'reference_map.json').read_text()),
            json.loads((GF/'scene_brief_v02_candidate.json').read_text()))
    fallos = [m for _, t, m in HARD_FAILS if t]
    if fallos:
        print(f'CONTRAPRUEBA FALLA: {len(fallos)} hard fails'); return False
    print('CONTRAPRUEBA OK'); return True
```

Salida medida del caso: `REJECTED — 7/8 hard fails` sobre el original, y
`CONTRAPRUEBA OK` sobre el corregido. Los dos sentidos importan.

## 4. Trampas del propio test

- **`all(...)` sobre un dict no vacio devuelve `True` aunque falten claves.** Para
  comprobar cobertura de slots, resta conjuntos: `slots_esperados - slots_declarados`.
- **"no evaluable" marcado como `ok` es un gate que no puede fallar.** Si falta el
  brief, es FAIL — la ausencia de evidencia no es cumplimiento.
- **No sobrescribas el brief que produjo el fallo.** Renombralo a `*_ORIGINAL_failed.json`
  y pon el corregido aparte; el original es la evidencia del test.
- **El primer versionado de un prompt corregido suele fallar el propio gate**, y eso
  tambien es informacion: encontro una regla que tu primer arreglo no cubria.

## 5. Bucle de aprendizaje

```
GENERAR → MEDIR → DIAGNOSTICAR → FORMULAR HIPOTESIS
        → CAMBIAR UNA VARIABLE → GENERAR → COMPARAR → REGISTRAR
```

El primer experimento tras un fallo cambia **una** variable (el prompt), manteniendo
referencias, modelo y ratio. Si falla, se aisla por pasos:

- A: solo personaje + entorno
- B: solo secundario + entorno
- C: ambos + entorno (control)

Eso separa si el drift viene del prompt, del segundo personaje, de la acumulacion de
referencias, del entorno, o de la interaccion entre factores. Sin ese aislamiento, un
segundo fallo no te dice nada nuevo.