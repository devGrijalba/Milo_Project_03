# MILO_Project_03 — Bitácora del pipeline

Registro paso a paso de lo que se ha hecho. Empieza desde la instrucción a DeepSeek
de leer las 1000 semillas. **Un paso = una sección**, en orden.

Estado actual: **Completado hasta "Semilla leída y verificada". El pipeline en sí no ha
generado nada todavía.**

---

## Paso 0 — El banco canónico queda en un solo lugar ✅

El repositorio público quedó con **un solo archivo**:

| Archivo | Tamaño |
|---|---|
| `Motor_guiones/data/seeds.json` | 1.898.317 bytes |

**Por qué importa:** antes había dos representaciones del mismo banco —10 archivos
`30_0X_*.md` (~59 MB), el compacto Markdown, y ahora el JSON de producción— y todos
eran públicos en el historial de Git. `MIGRATION_AUDIT.md` del propio motor criticaba
exactamente eso: *"Dos bancos de semillas coexistían"*. Ahora hay una sola fuente, y es
la que el motor consume en runtime y la que DeepSeek puede leer completa.

**Formato:** `2.1.0-compact` / `production-compact`, 1000 semillas, contrato declarado
en `selection_contract` (`required_seed_fields`: `seed_id`, `family_id`, `territorio`,
`semilla`, `revision`).

SHA256 verificado idéntico en ambas copias del motor:
`20587d8c5f75bdf5ab0ce7473f3b11ddac532245b6bc03160f657ec2ac7e6a62`

**Por qué JSON y no Markdown:** el `.md` de 1,9 MB~(420k tokens) sí cabía en la
ventana de 1M del modelo, pero DeepSeek **no lo recorría**: el gate midió solo los
registros 1–17 y reportó un total de 17 sobre 1000
(`GITHUB_SEED_ACCESS = FAIL`). El JSON plano se lee completo.

---

## Paso 1 — Se le indica a DeepSeek que lea el banco ✅

**Cómo:** el archivo se **adjunta** a la conversación vía CDP (Chrome con perfil limpio,
puertos 9222). Herramienta: `tools/ds_upload.py`.

Se descartó la lectura por URL pública: el Markdown de 1,9 MB cabía de sobra en la
ventana de 1M del modelo, pero DeepSeek solo recorría los primeros registros
(`GITHUB_SEED_ACCESS = FAIL`, registros 1–17). Adjuntar el archivo es además el camino
que la propia web soporta: su `input[type=file]` declara `.json` en `accept`.

**Prompt enviado** (el que lee y confirma):

```
Lee el archivo JSON que te adjunté.

Responde SOLO con un objeto JSON válido, sin texto antes ni después, sin bloques de código markdown.

Formato exacto:

{"records_count": <número de objetos>,
 "seed_ids": ["...", "...", "..."],
 ...}

No infieras nada. Cada valor debe salir del archivo adjunto. Si no puedes leer un campo, devuelve null.
```

**Respuesta de DeepSeek:**

- **1000 semillas** ✅
- **Campos por semilla:** `seed_id`, `family_id`, `territorio`, `angulo`, `titulo`,
  `semilla`, `conflicto`, `accion_visible`, `objeto_emocional`, `giro_posible`,
  `desarrollo_requerido`, `personajes_requeridos`, `motor_editorial`, `fuentes_tematicas`.
  En variantes: `replaces_seed_id`, `cambio_causal`, `giro_base_descartado`,
  `narrative_cluster_id`. Para selección: `calidad`, `afinidad`, `novedad`, `compuesto`,
  `nivel`, `elegible`.
- **Títulos 0001–0003:**
  1. *Plato tapado: la primera vez*
  2. *Plato tapado: la copia que no funcionó*
  3. *Plato tapado: el favor convertido en deuda*

**Verificación de que leyó de verdad:** los títulos 0002 y 0003 son **variantes degradadas
del mismo motivo** que la 0001 —el "plato tapado" degradado: la copia que no funcionó, el
favor convertido en deuda. Esa progresión temática solo existe dentro del documento; no se
deduce del nombre del repo ni de una suposición razonable.

**Limitación registrada:** el `.md` **no lleva `seed_hash`**, así que la confirmación es de
contenido, no criptográfica. No hay forma de verificar integridad por hash desde el
exterior del `.jsonl`.

---

## Paso 2 — Motor_guiones implementado ✅

Motor 8.0.0-AGENT extraído del ZIP, con el wrapper `MILO_AGENT_ROOT/` eliminado para que
los archivos cuelguen directo de la carpeta.

**Gate de regresión: 25/25 PASS** (`Motor_guiones/tests/gate_v2.py`).

Incluye 10 negativas deliberadas que la documentación *decía* cubrir pero el código no
comprobaba, y 25 comprobaciones que sí ejecutan:

| Verificación | Resultado |
|---|---|
| `select_seed.py` recupera la semilla pedida | ✅ |
| `seed_hash` preservado, nunca recalculado | ✅ |
| Duración PASS (48–53 palabras) | ✅ 49 palabras / 24,5 s |
| Zona de reparación (54–64) | ✅ `REPAIR_REQUIRED` |
| Fuera de rango | ✅ `FAIL` |
| Hash alterado → `SEED_HASH_MISMATCH` | ✅ |
| Snapshot reescrito → `SEED_SNAPSHOT_MISMATCH` | ✅ |
| 8 validaciones mecánicas más de enum/hook/versión | ✅ |

**Banco auditado:** 1000 registros, 1000 IDs únicos, rango 0001–1000 sin huecos, 1000/1000
`seed_hash` de 64 hex preservados, 50 overrides `milo_role: niño` y 928 con metadatos
causales —ambos coinciden con `MIGRATION_AUDIT.md`.

---

## Paso 3 — El pipeline de generación ⏸ PENDIENTE

Los pasos 1 y 2 ya ocurrieron: **DeepSeek leyó el banco** y **el motor está verificado**, pero
nunca se ha corrido la generación de un episodio.

### El problema estructural

**DeepSeek es un chat: no puede correr `select_seed.py`.** Solo lee texto. Por eso la
selección no puede delegarse entera en él — hay que verificarla contra el Python local
antes de construir el guion.

### El pipeline, según `Motor_guiones/AGENTS.md`

| # | Etapa | Quién | Mecánico |
|---|---|---|---|
| 1 | Selección de semilla | Código (`select_seed.py`) | Filtros y orden |
| 2 | Construcción narrativa | **El agente** | Cadena de 7 beats |
| 3 | Validación mecánica | Código (`validate_package.py`) | Hash, hooks, duración, enums |
| 4 | Reparación | El agente | Máx 3 ciclos |
| 5 | Salida | Código + agente | `SCRIPT_PACKAGE` + `ELEVENLABS_V3_TEXT` |

**Criterios de selección (step 1):** `elegible == true` · compuesto ≥ 85 · calidad ≥ 80 ·
afinidad ≥ 85 · excluir usadas · evitar última familia si hay alternativa · ordenar por
compuesto desc + `seed_id` asc · tomar la primera.

**Regla de oro:** si el usuario da `seed_id`, recuperar exactamente esa.

### Estado de la continuidad

`state/series_state.json` está en:
```json
{"last_approved_episode": null, "used_seed_ids": [], "last_family_id": null,
 "approved_episode_count": 0}
```

Serie limpia. El siguiente episodio sería **`EP0001`** (`EP` + 4 dígitos, no deriva de la
semilla). **El estado solo se actualiza tras aprobación explícita del usuario.**

---

## Bloqueos conocidos — requieren decisión del proyecto

### 1. La duración no cuadra

| Dato | Valor |
|---|---|
| Cadena obligatoria | 7 beats |
| Banda PASS | 48–53 palabras → **6,9–7,6 palabras por beat** |
| A 2 palabras/s | **24,0–26,5 s** — no 35 s |

Para ~35 s harían falta ~70 palabras. Hay que mover `pass_words_min`/`pass_words_max` y
`repair_words_*` en `config/engine.json`. `MIGRATION_AUDIT.md` ya lo marcó como
*"DECISIÓN PENDIENTE IMPORTANTE"* y no lo cambió por decisión propia.

**No resuelto.** Es una decisión creativa, no técnica.

### 2. `AGENTS.md` §2 pide algo imposible

```
sha256(data/seeds.jsonl)  = 78096b3fb7771974d644caaa823eacc014657398685f330fac80263352c6b019
seed_hash de MILO-S0001  = 113739653e9bcae9dac5a65e3a8a091062ce065d4835511ecc46e8ec6e43927f
iguales: False
```

`AGENTS.md` §2 exige que `root.seed_hash` sea el hash del **archivo** `seeds.jsonl`;
`validate_package.py` lo compara contra `seed.seed_hash`, que es el hash **por semilla**.
Ningún paquete puede satisfacer ambas reglas.

**Propuesta:** el código ejecutable manda; corregir el texto de §2 para que diga "el hash
de la semilla seleccionada, tal como aparece en el banco, sin recalcular".

### 3. No existe carpeta de salida

El motor entrega el `SCRIPT_PACKAGE` como JSON para imprimir, pero no hay `episodes/`
donde se guarden los paquetes generados. Los estados de salida posibles son `SCRIPT_PACKAGE`
+ `ELEVENLABS_V3_TEXT`, `OUTPUT_BLOCKED` (script inválido tras reparación), o
`VOICE_TEXT_BLOCKED` (script válido, voz falló).

---

## Comandos de esta bitácora

```bash
# Gates
python Motor_guiones/tests/gate_v2.py               # 25/25 PASS
python Motor_guiones/tools/select_seed.py           # mejor semilla disponible
python Motor_guiones/tools/validate_package.py <pkg>.json
python .agents/skills/sync_skills.py                # 41 skills del proyecto

# Inyección a DeepSeek
python tools/ds_inject.py --probe                   # descubrir selectores
python tools/ds_inject.py --text "..."              # enviar prompt
```